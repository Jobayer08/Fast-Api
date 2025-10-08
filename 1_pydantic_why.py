from pydantic import BaseModel
class Patient(BaseModel):
    name: str
    age: int
def insert_patient_data(p: Patient):
    print(f"Patient {p.name} of age {p.age} inserted into the database.")

patient_info={"name":"John Doe","age":30}
patient1=Patient(**patient_info)
insert_patient_data(patient1)
