"""
main.py - catalogue summarizer is used to call an OpenAI agent who is going to summarize a text.
"""
import os

from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class LongText(BaseModel):
    """
    Reprénsente le texte en entrée
    """
    text: str

@app.post("/summarize")
def summarize_text(data: LongText):
    """
    Call an OpenAI agent to summarize a text.
    :param data: The text to be summarized.
    :return: The summarized text.
    """
    response = client.responses.create(
        model="gpt-4o",
        instructions="Tu es un assistant qui résume les textes.",
        input=f"Résume ce texte en quelques lignes : {data.text}"
    )
    summary = response.output_text
    return {"summary": summary}
