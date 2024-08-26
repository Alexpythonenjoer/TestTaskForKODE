import json
from .schemas import Note, NoteCreate


def load_notes():
    with open("data/notes.json", "r") as file:
        return json.load(file)


def save_notes(notes):
    with open("data/notes.json", "w") as file:
        json.dump(notes, file)


def create_note(note: NoteCreate, user: str):
    notes = load_notes()
    new_note = {"id": len(notes) + 1, "user": user, **note.dict()}
    notes.append(new_note)
    save_notes(notes)
    return new_note


def get_notes(user: str):
    notes = load_notes()
    return [note for note in notes if note["user"] == user]
