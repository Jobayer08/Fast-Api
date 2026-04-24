from pydantic import BaseModel,EmailStr
from typing import List,Dict

class address(BaseModel):
    city: str
    state: str
    zip_code: int

class patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    alergies: List[str]
    contacts: Dict[str, str]
    Address: address

address_info={"city":"New York","state":"NY","zip_code":10001}
address1=address(**address_info)

patient_info={"email":'abc@hdfc.com',"name":"John Doe","age":'40',"weight":70.5,"height":170,
              "alergies":["pollen","nuts"],"contacts":{"doctor":"987-654-3210"},"Address":address1}

patient1=patient(**patient_info)

print(patient1)
print(patient1.Address.city)