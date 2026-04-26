from todo import TodoResponse
from user import UserResponse

#  stockage en mémoire

todos : list[TodoResponse] = [
    TodoResponse(id=0, user_id = 1, title = "Range tes chaussettes", description="Le panier à linge est dans la buanderie, vise bien !"),
    TodoResponse(id = 1, user_id = 2, title = "Fais le ménage", description="L'aspirateur ne mord pas."),
    TodoResponse (id = 2, user_id=1, title = "prends une douche", description="Le savon n'est pas là pour servir de décoration."),
    TodoResponse (id = 3, user_id = 2, title = "Range ta chambre", description="Planquer les affaires sous le lit n'est pas ranger."),
    TodoResponse(id=4, user_id=1, title="Fais à manger", description="Ne te contente pas d'ouvrir le paquet de céréales."),

]

users : list[UserResponse] = [
    UserResponse(id=0, name="Gabriel"),
    UserResponse(id =1, name ="Alain"),
    UserResponse(id =2, name ="Georges")
]