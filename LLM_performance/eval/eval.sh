run_name='a'
prediction_dir=/home/tp030/medical_hallucination/LLM_performance/medgemma/results
prediction_file=/home/ptthang/medical_hallucination/testing_space/LLM_performance/prediction.jsonl
prediction_file=/home/tp030/medical_hallucination/LLM_performance/medgemma/updated_prediction.jsonl
python run.py ${prediction_file} --run_name ${run_name} --output_dir ${prediction_dir}