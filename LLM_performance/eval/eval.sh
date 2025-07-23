run_name='a'
prediction_dir=/home/ptthang/medical_hallucination/testing_space/LLM_performance/results
prediction_file=/home/ptthang/medical_hallucination/testing_space/LLM_performance/prediction.jsonl
python run.py ${prediction_file} --run_name ${run_name} --output_dir ${prediction_dir}