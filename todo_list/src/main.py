from routes.users import router as users_router
from routes.todos import router as todos_router
from database import todos, users
from fastapi import FastAPI
app = FastAPI()
app.include_router(users_router, prefix="/users",  tags=["users"])
app.include_router(todos_router, prefix = "/todos",   tags=["todos"])





def main():
    print("Hello from todo-list!")


if __name__ == "__main__":
    main()
