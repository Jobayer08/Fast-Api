from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    
    alergies: List[str]
    contacts: Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, v):
        valid_domain=['hdfc.com','icici.com']
        domain=v.split('@')[-1]
        if domain not in valid_domain:
            raise ValueError(f'Email domain must be one of {valid_domain}')
        
        return v
    @field_validator('name')
    @classmethod
    def transform_name(cls, v):
        return v.upper()
    
    
def insert_patient_data(p: Patient):
    print(f"Patient {p.name} of age {p.age} inserted into the database.weight:{p.weight} email:{p.email}")    
    

patient_info={"email":'abc@hdfc.com',"name":"John Doe","age":100,"weight":70.5,
              "alergies":["pollen","nuts"],"contacts":{"emergency":"123-456-7890","doctor":"987-654-3210"}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)

