from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional
class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int=Field(gt=0,lt=150)
    weight: float
    married: Optional[bool] = None
    alergies: List[str]
    contacts: Dict[str, str]
def insert_patient_data(p: Patient):
    print(f"Patient {p.name} of age {p.age} inserted into the database.{p.married}")

patient_info={"email":'abc@gmail.com',"name":"John Doe","age":300,"weight":70.5,
              "alergies":["pollen","nuts"],"contacts":{"emergency":"123-456-7890","doctor":"987-654-3210"}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)
