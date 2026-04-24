from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import Annotated,Literal
from pydantic import BaseModel, Field,computed_field
import json
app = FastAPI()
class Patient(BaseModel):
    id: Annotated[str,Field(..., description="Unique identifier for the patient", example="12345")]
    name: Annotated[str,Field(..., description="Full name of the patient", example="John Doe")]
    city: Annotated[str,Field(..., description="City where the patient resides", example="New York")]
    age: Annotated[int,Field(...,gt=0,lt=150, description="Age of the patient", example=30)]
    gender:Annotated[Literal['Male','Female','Other'],Field(..., description="Gender of the patient", example="Male")]
    height: Annotated[float,Field(...,gt=0, description="Height of the patient in centimeters", example=175.5)]
    weight: Annotated[float,Field(...,gt=0, description="Weight of the patient in kilograms", example=70.2)]

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"



def insert_patient_data(p: Patient):
    print(f"Patient{p.name} (ID: {p.id}) from {p.city}, age {p.age}, gender{p.gender}, height {p.height} cm, weight {p.weight} kg inserted into the database. BMI: {p.bmi} ({p.verdict})")

patient_info={"id":"P001","name":"John Doe","city":"New York","age":100,"gender":"Male","height":175.5,"weight":70.5}
patient1=Patient(**patient_info)
insert_patient_data(patient1)

@app.post("/create")
def create_patient(patient: Patient):
    try:
        insert_patient_data(patient)
        return {"message": f"Patient {patient.name} created successfully.", "bmi": patient.bmi, "verdict": patient.verdict}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully."})
