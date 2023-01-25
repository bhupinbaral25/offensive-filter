from transformers import pipeline

task='offensive'

MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

PIPELINE = pipeline('text-classification', model=MODEL)
