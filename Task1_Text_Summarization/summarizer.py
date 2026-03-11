from transformers import pipeline

summarizer = pipeline("summarization")

text = """
Artificial Intelligence is transforming industries such as healthcare,
education, and finance. AI systems can analyze large datasets, detect
patterns, and make intelligent decisions. As AI technology continues
to advance, it is expected to play an even greater role in our daily lives.
"""

summary = summarizer(text, max_length=40, min_length=20, do_sample=False)

print("Original Text:")
print(text)

print("\nSummary:")
print(summary[0]['summary_text'])
