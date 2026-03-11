from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Artificial Intelligence will"

result = generator(prompt, max_length=50)

print(result[0]['generated_text'])
