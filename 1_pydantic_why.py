from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name: Annotated[str,Field(max_length=100,title="Full Name of the Patient",description="This field contains the full name of the patient.",examples=["John Doe","Jane Smith"])]
    email:EmailStr
    age: int=Field(gt=0,lt=150)
    weight: Annotated[float,Field(strict=True, gt=0.0,title="Weight in kilograms",description="The weight of the patient in kilograms.",examples=[70.5,80.0])]
    married: Annotated[Optional[bool],Field(default=None,title="Marital Status",description="Indicates if the patient is married.")]
    alergies: List[str]
    contacts: Dict[str, str]
def insert_patient_data(p: Patient):
    print(f"Patient {p.name} of age {p.age} inserted into the database.{p.married} weight:{p.weight} email:{p.email}")

patient_info={"email":'abc@gmail.com',"name":"John Doe","age":100,"weight":70.5,
              "alergies":["pollen","nuts"],"contacts":{"emergency":"123-456-7890","doctor":"987-654-3210"}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)
