from fastapi import APIRouter
from database import users, todos
from fastapi import HTTPException

from todo import TodoResponse
from user import UserCreate, UserResponse

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
def get_users() -> list[UserResponse]:
    return users

@router.post("/", response_model=UserResponse)
def post_users(newUser: UserCreate)-> UserResponse:
    id : int = max(user.id for user in users)+1

    addUser : UserResponse = UserResponse(id = id, name = newUser.name)
    users.append(addUser)
    return addUser

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int)-> UserResponse:
    if users :
        for user in users:
            if user.id == user_id:
                return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=UserResponse)
def put_user(user_id: int, newUser: UserCreate)-> UserResponse:
    for index, user in enumerate(users) :
        if user.id == user_id :
            updateUser = UserResponse(id = user.id, name = newUser.name)
            users[index] = updateUser
            return updateUser
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}", response_model=UserResponse)
def del_user(user_id: int)-> UserResponse:
    for index, user in enumerate(users) :
        if user.id == user_id:
            users.pop(index)
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/{user_id}/todos", response_model=list[TodoResponse])
def get_user_todos(user_id: int)-> list[TodoResponse]:
    userConcerned : UserResponse|None = None
    result: list[TodoResponse] = []

    if users :
        for user in users:
            if user.id == user_id:
                userConcerned = user
                break

        if userConcerned :
            for index, task in enumerate(todos) :
                if task.user_id == userConcerned.id:
                    result.append(task)
            if result != [] :
                return result
            else:
                return []
        else :
            raise HTTPException(status_code=404, detail="User doesn't exist")
    raise HTTPException(status_code=404, detail="no users created")