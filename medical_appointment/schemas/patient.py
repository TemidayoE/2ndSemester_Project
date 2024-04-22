from pydantic import BaseModel



class PatientDetail(BaseModel):
    username: str
    first_name: str
    last_name: str
    age: int
    sex: str
    weight: float
    height: float
    phone_number: str


class PatientCreate(PatientDetail):
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "king123",
                "first_name": "King",
                "last_name": "Mastermind", 
                "age": 20,
                "sex": "male",
                "weight": 50,
                "height": 1.85,
                "phone_number": "+1234567890",
                "password": "megalomaniac"
            }
        }

class Patient(PatientCreate):
    id: int



patients: list[Patient] = []
