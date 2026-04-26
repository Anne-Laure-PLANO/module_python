from fastapi import APIRouter
from todo import TodoCreate, TodoResponse
from database import todos, users
from fastapi import HTTPException
router = APIRouter()


@router.get("/", response_model=list[TodoResponse])
def get_todos() -> list[TodoResponse]:
    return todos

@router.post("/", response_model= TodoResponse)
def post_todo(newTask : TodoCreate) -> TodoResponse:
    for user in users :
        if newTask.user_id == user.id :
            newId = max((todo.id for todo in todos), default =0) + 1
            newTodo : TodoResponse = TodoResponse(id = newId,**newTask.dict())
            todos.append(newTodo)
            return newTodo
    raise HTTPException (status_code=404, detail="Utilisateur introuvable.")
@router.get("/{todo_id}", response_model= TodoResponse)
def get_todo_id(todo_id : int) ->TodoResponse :
    for item in todos:
        if item.id == todo_id :
            return item
    raise HTTPException(status_code=404, detail="Tâche introuvable")

@router.put("/{todo_id}", response_model= TodoResponse)
def put_todo_id (todo_id : int, task : TodoCreate) -> TodoResponse:
    for user in users :
        if user.id == task.user_id :
            newTodo = TodoResponse(id = todo_id,**task.dict())
            todos[todo_id] = newTodo
            return newTodo
    raise HTTPException(status_code=404, detail = "Tâche introuvable")

@router.delete("/{todo_id}", response_model= TodoResponse)
def delete_todo_id (todo_id: int) -> TodoResponse:
    for index, item in enumerate(todos):
        if todo_id == item.id :
            todos.pop(index)
            return item
    raise HTTPException(status_code = 404, detail = "Tâche introuvable")


