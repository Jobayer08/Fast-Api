from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    
    alergies: List[str]
    contacts: Dict[str, str]

    @model_validator(mode='after')
    @classmethod
    def validate_patient(cls, values):
        if values.age >60 and 'emergency' not in values.contacts:
            raise ValueError('Emergency contact required for patients over 60')
        return values

def insert_patient_data(p: Patient):
    print(f"Patient {p.name} of age {p.age} inserted into the database.weight:{p.weight} email:{p.email}")    
    

patient_info={"email":'abc@hdfc.com',"name":"John Doe","age":'40',"weight":70.5,
              "alergies":["pollen","nuts"],"contacts":{"doctor":"987-654-3210"}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)    