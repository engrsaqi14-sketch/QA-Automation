from fastapi import FastAPI

app = FastAPI()

notes = []

@app.get("/")
def home():
    return {"message": "Notes API running"}

@app.post("/notes")
def create_note(note: dict):
    notes.append(note)
    return {"message": "Note created", "data": note}

@app.get("/notes")
def get_notes():
    return notes
