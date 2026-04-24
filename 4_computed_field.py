from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    alergies: List[str]
    contacts: Dict[str, str]

    @computed_field
    @property
    def bmi_(self) -> float:
        bmi=self.weight / ((self.height / 100) ** 2)
        return round(bmi,2)

    

def insert_patient_data(p: Patient):
    print(f"Patient {p.name} of age {p.age} inserted into the database.weight:{p.weight} email:{p.email} bmi:{p.bmi_}")    
    

patient_info={"email":'abc@hdfc.com',"name":"John Doe","age":'40',"weight":70.5,"height":170,
              "alergies":["pollen","nuts"],"contacts":{"doctor":"987-654-3210"}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)    