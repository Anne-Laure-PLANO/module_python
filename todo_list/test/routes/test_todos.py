import pytest
from fastapi.testclient import TestClient
from main import app
from todo import Todo
from database import todos, users
from user import User

client = TestClient(app)

@pytest.fixture
def sample_todos():
    todos.clear()
    users.clear()
    users.append(User(name="Test"))
    users.append(User(name="User"))
    todos.append(Todo(id = 1 , user_id = 1, title="Faire ses courses"))
    yield
    todos.clear()
    users.clear()


def test_get_empty()->None:
    todos.clear()
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []
    todos.clear()


def test_get_todos(sample_todos)->None:
    response = client.get("/todos")
    assert response.status_code == 200

def test_get_error(sample_todos)->None:
    response = client.get("/todo")
    assert response.status_code == 404

def test_get_todos_content(sample_todos)->None:
    response = client.get("/todos")
    assert response.json() == [{
        "id": 1,
        "user_id": 1,
        "title": "Faire ses courses",
        "completed": False
    }]


def test_post_todos(sample_todos)->None:
    response = client.post("/todos", json={"user_id" : 1 ,"title": "Ma tâche"})
    assert response.status_code == 200

def test_post_empty(sample_todos)->None:
    response = client.post("/todos")
    assert response.status_code == 422

def test_post_error(sample_todos)->None:
    response = client.post("/todos", json={"1" : "Faire ses courses"})
    assert response.status_code == 422