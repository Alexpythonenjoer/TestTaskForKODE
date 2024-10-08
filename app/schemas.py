from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    user: str
