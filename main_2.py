from fastapi import FastAPI, HTTPException, Query
from typing import Annotated,Literal
from pydantic import BaseModel, Field
import json
app = FastAPI()
class patient(BaseModel):
    id: Annotated[str,Field(..., description="Unique identifier for the patient", example="12345")]
    name: Annotated[str,Field(..., description="Full name of the patient", example="John Doe")]
    city: Annotated[str,Field(..., description="City where the patient resides", example="New York")]

