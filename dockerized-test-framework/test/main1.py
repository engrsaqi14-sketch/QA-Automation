from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# fake database (single note storage)
note = None


class Note(BaseModel):
    title: str
    content: str


@app.get("/")
def home():
    return {"message": "Notes API running"}


# CREATE (only one note allowed)
@app.post("/note")
def create_note(n: Note):
    global note

    note = {
        "title": n.title,
        "content": n.content
    }

    return {"message": "Note created", "data": note}


# GET
@app.get("/note")
def get_note():
    if note is None:
        raise HTTPException(status_code=404, detail="No note found")

    return note


# UPDATE
@app.put("/note")
def update_note(n: Note):
    global note

    if note is None:
        raise HTTPException(status_code=404, detail="No note to update")

    note["title"] = n.title
    note["content"] = n.content

    return {"message": "Note updated", "data": note}


# DELETE
@app.delete("/note")
def delete_note():
    global note

    if note is None:
        raise HTTPException(status_code=404, detail="No note to delete")

    deleted = note
    note = None

    return {"message": "Note deleted", "data": deleted}
