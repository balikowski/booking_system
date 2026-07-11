from database import engine
from sqlmodel import SQLModel, Session
import crud

SQLModel.metadata.create_all(engine) # tworzenie tabeli w bazie (jesli nie ma)
with Session(engine) as session:
    user = crud.create_user(session, "ania", "ania@test.pl","haslo123")
    print("Utworzono: ", user)
    
    found = crud.get_user_by_username(session, "ania")
    print("Znaleziono: ", found)

    not_found = crud.get_user_by_username(session, "nieistnieje")
    print("Nieistniejący :", not_found)
