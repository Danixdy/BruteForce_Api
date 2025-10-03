from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()

class UserLogin(SQLModel):
    username: str
    password: str
    
class User(SQLModel):
    id: int | None = None
    username: str
    password: str
    is_active: bool = True

users_db = {
    "admin": User(id=1, username="admin", password="1234", is_active=True),
    "user": User(id=2, username="user", password="abcd", is_active=True),
}
next_id = 3

@app.post("/users")
def create_user(user: User):
    if user.username in users_db:
        return {"message": "Usuario ya existe."}
    
    global next_id
    user.id = next_id
    next_id += 1
    users_db[user.username] = user
    return {"message": "Usuario creado exitosamente.", "user_id": user.id}

@app.get("/users")
def get_All_Users():
    return list(users_db.values())

@app.get("/users/{id}")
def get_user(id: int):
    for user in users_db.values():
        if user.id == id:
            return user
    return {"message": "Usuario no encontrado."}

@app.put("/users/{id}")
def update_user(id: int, user: User):
    for username, db_user in users_db.items():
        if db_user.id == id:
            new_username = user.username or db_user.username
            if new_username != db_user.username and new_username in users_db:
                return {"message": "Username ya existe."}
            
            db_user.username = new_username
            db_user.email = user.email or db_user.email
            db_user.is_active = user.is_active if user.is_active is not None else db_user.is_active
            
            if new_username != username:
                del users_db[username]
                users_db[new_username] = db_user
            
            return {"message": "Usuario actualizado exitosamente."}
    
    return {"message": "Usuario no encontrado."}

@app.delete("/users/{id}")
def delete_user(id: int):
    for username, user in list(users_db.items()):
        if user.id == id:
            del users_db[username]
            return {"message": "Usuario eliminado exitosamente."}
    
    return {"message": "Usuario no encontrado."}

@app.post("/login")
def login(user: UserLogin):
    for username, db_user in users_db.items():
        if db_user.username == user.username and db_user.password == user.password and db_user.is_active:
            return {"message": "Login successful"}
    
    return {"message": "usuario y/o contraseña incorrectos."}
