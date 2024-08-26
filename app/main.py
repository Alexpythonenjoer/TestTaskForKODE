from typing import List
from fastapi import FastAPI, Depends
from .auth import get_current_user
from .schemas import Note, NoteCreate
from .crud import create_note, get_notes

app = FastAPI()


@app.post("/notes/", response_model=Note)
async def add_note(note: NoteCreate, user: str = Depends(get_current_user)):
    return create_note(note, user)


@app.get("/notes/", response_model=List[Note])
async def list_notes(user: str = Depends(get_current_user)):
    return get_notes(user)
