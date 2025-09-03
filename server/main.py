# server/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from .tools.substitutions import find_substitutions

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

class ChatIn(BaseModel):
    message: str

@app.post("/chat")
def chat(inp: ChatIn):
    msg = inp.message.lower()
    # ultra-simple intent: if message contains "substitute"/"swap", treat last word as ingredient
    if any(k in msg for k in ["substitute", "swap", "replace"]):
        candidate = msg.split()[-1].strip("?!.,")
        subs = find_substitutions(candidate)
        return {"type": "subs", "ingredient": candidate, "results": subs}
    # fallback for now
    return {"type": "info", "message": "Ask for a substitution, e.g., 'substitute egg in pancakes'."}
