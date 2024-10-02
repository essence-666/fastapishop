from users.schemas import User

def create_user(userin : User) -> dict:
    return {
        "status" : "success",
        "message" : f'user {userin.username} was succsessfully added!',
        "user" : userin.model_dump(),
    }
