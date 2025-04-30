import os

from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class LongText(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(data: LongText):
    response = client.responses.create(
        model="gpt-4o",
        instructions="Tu es un assistant qui résume les textes.",
        input=f"Résume ce texte en quelques lignes : {data.text}"
    )
    summary = response.output_text
    return {"summary": summary}
