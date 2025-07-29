4b có 34 hidden layers. 
attention shape mình đang có là 50x34x..... 50 là số predicted tokens, 34 là số hidden layers.
Trong đó token đầu sẽ attention nhiều, các token sau sẽ attention ít hơn. Check shape sẽ thấy dễ hiểu hơn. 
Lý do: chưa rõ. assume là technical advantage để save memory. Khi chạy nó sẽ lưu past key value, và khi attention thì nó sẽ lấy past key value đó ra để tính attention.
Cứ mỗi lần predict xong, thì lưu sẽ chỉ feed vào 1 token. Ví dụ ở đây: 
```
    def _cache_dependant_input_preparation(
        self,
        input_ids: torch.LongTensor,
        inputs_embeds: Optional[torch.FloatTensor],
        cache_position: Optional[torch.LongTensor],
    ) -> tuple[torch.FloatTensor, torch.LongTensor]:
        """
        Generic cache-dependent input preparation
        The code is put in a separate function to allow granular unit testing
        as it needs a different implementation to be exportable.

        If we have cache: let's slice `input_ids` through `cache_position`, to keep only the unprocessed tokens
        - Exception 1: when passing input_embeds, input_ids may be missing entries
        - Exception 2: some generation methods do special slicing of input_ids, so we don't need to do it here
        - Exception 3: with synced GPUs cache_position may go out of bounds, but we only want dummy token in that case.
        - Exception 4: If input_embeds are passed then slice it through `cache_position`, to keep only the unprocessed tokens and
          generate the first token for each sequence. Later use the generated Input ids for continuation.

        The current implementation does not rely on ``self`` and could be
        a class method. It is left as a standard method to be easily rewritten.
        """
        if is_torchdynamo_exporting():
            return self._cache_dependant_input_preparation_exporting(input_ids, inputs_embeds, cache_position)
        if inputs_embeds is not None and input_ids.shape[1] == 0:  # Exception 4
            inputs_embeds = inputs_embeds[:, -cache_position.shape[0] :]
        elif (
            inputs_embeds is not None  # Exception 1
            or (cache_position[-1] >= input_ids.shape[1])  # Exception 3
        ):
            input_ids = input_ids[:, -cache_position.shape[0] :]
        elif input_ids.shape[1] != cache_position.shape[0]:  # Default case (the "else", a no op, is Exception 2)
            input_ids = input_ids[:, cache_position]
        return inputs_embeds, input_ids
```
Hàm này đi cắt input id từ `cache_position`, để chỉ lấy những token chưa được xử lý.



This is the function that they take attention score out of: 
```python
/home/ptthang/miniforge3/envs/medgemma/lib/python3.10/site-packages/transformers/models/gemma3/modeling_gemma3.py:240 
def eager_attention_forward(
    module: nn.Module,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attention_mask: Optional[torch.Tensor],
    dropout: float = 0.0,
    scaling: Optional[float] = None,
    softcap: Optional[float] = None,
    **kwargs,
) -> tuple[torch.Tensor, torch.Tensor]:
    if scaling is None:
        scaling = module.head_dim**-0.5

    key_states = repeat_kv(key, module.num_key_value_groups)
    value_states = repeat_kv(value, module.num_key_value_groups)

    attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling

    if softcap is not None:
        attn_weights = attn_weights / softcap
        attn_weights = torch.tanh(attn_weights)
        attn_weights = attn_weights * softcap
    if attention_mask is not None:  # no matter the length, we just slice it
        causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]
        attn_weights = attn_weights + causal_mask

    # upcast attention to fp32
    attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query.dtype)
    attn_weights = nn.functional.dropout(attn_weights, p=dropout, training=module.training)
    attn_output = torch.matmul(attn_weights, value_states)
    attn_output = attn_output.transpose(1, 2).contiguous()
    return attn_output, attn_weights
```


Trace of attention shape 
The function of interest 
hidden_states, self_attn_weights = self.self_attn(
            hidden_states=hidden_states,
            position_embeddings=position_embeddings,
            attention_mask=attention_mask,
            position_ids=position_ids,
            past_key_value=past_key_value,
            output_attentions=output_attentions,
            use_cache=use_cache,
            cache_position=cache_position,
            **kwargs,
        )

First catch: 
    inputs_embeds.shape
        torch.Size([1, 293, 2560])
    self_attn_weights.shape
        torch.Size([1, 8, 293, 293])
    hidden_states.shape
        torch.Size([1, 293, 2560])
    attention_mask.shape
        torch.Size([1, 1, 293, 293])
    position_ids.shape
        torch.Size([1, 293])


Some particular catch when attn_weights.shape == torch.Size([1, 8, 1, 303])
    self_attn_weights.shape
        torch.Size([1, 8, 1, 303])
    hidden_states.shape
        torch.Size([1, 1, 2560])
    attention_mask.shape
        torch.Size([1, 1, 1, 303])
    position_ids.shape
        torch.Size([1, 1])
    query_states.shape
        torch.Size([1, 8, 1, 256])
    key_states.shape
        torch.Size([1, 4, 303, 256]) # they will repeat it into [1, 8, 303, 256]. 
        Repeat:
            key[0,:,0,0]
                tensor([ 0.0265,  0.0053, -0.0208, -0.0280])
            key_states[0,:,0,0]
                tensor([ 0.0265,  0.0265,  0.0053,  0.0053, -0.0208, -0.0208, -0.0280, -0.0280])
    value_states.shape
        torch.Size([1, 4, 303, 256])
    attention_mask.shape
    torch.Size([1, 1, 1, 303])
    attention_mask
    tensor([[[[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0.]]]])


Anyway, in summary, mình sẽ có 2 loại attention scores:
1. Attention scores của các token đã được xử lý, sẽ có shape là `[1, 8, 293, 293]` (1 là batch size, 8 là số attention heads, 293 là token all ban đầu).
2. Attention scores của các token chưa được xử lý, sẽ có shape là `[1, 8, 1, prev token length]` (1 là batch size, 8 là số attention heads, 1 là token vừa được predict, tức chưa được embed, prev token length là số token trong input).

đại loại là ban đầu chưa embed state -> vào attention để embed state, tiện calculate attn weight luôn, còn query thì sẽ là token vừa predict, key value sẽ là các token đã được embed trước đó. -> self_attn_weights -> loop 

