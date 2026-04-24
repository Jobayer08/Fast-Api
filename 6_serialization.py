from pydantic import BaseModel,EmailStr
from typing import List,Dict

class address(BaseModel):
    city: str
    state: str
    zip_code: int

class patient(BaseModel):
    name: str
    email: EmailStr
    age: int =22
    weight: float
    height: float
    alergies: List[str]
    contacts: Dict[str, str]
    Address: address

address_info={"city":"New York","state":"NY","zip_code":10001}
address1=address(**address_info)

patient_info={"email":'abc@hdfc.com',"name":"John Doe","weight":70.5,"height":170,
              "alergies":["pollen","nuts"],"contacts":{"doctor":"987-654-3210"},"Address":address1}

patient1=patient(**patient_info)

temp=patient1.model_dump()
print(temp)
print(type(temp))

temp1=patient1.model_dump_json()
print(temp1)
print(type(temp1))

temp2=patient1.model_dump(include={'name','Address'})
print(temp2)
print(type(temp2))

temp3=patient1.model_dump(exclude={'Address':['zip_code'],"alergies",'contacts'})
print(temp3)
print(type(temp3))

temp4=patient1.model_dump()
print(temp4)
print(type(temp4))

temp5=patient1.model_dump(exclude_unset=True)
print(temp5)