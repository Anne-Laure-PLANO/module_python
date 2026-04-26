from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str
    user_id : int



class TodoResponse(BaseModel):
    id: int
    user_id : int
    title: str
    description: str
    completed: bool = False


