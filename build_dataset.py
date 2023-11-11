from datasets import load_dataset

dataset = load_dataset('communityai/apt-openchat-micro-dataset-llm-v2-714k')
print(dataset)

dataset['train'].to_json('./dataset/dataset.jsonl', orient='records', lines=True)