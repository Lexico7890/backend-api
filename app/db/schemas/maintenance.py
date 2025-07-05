from pydantic import BaseModel, Field
from typing import Optional

class MaintenanceBase(BaseModel):
    service_date: str = Field(..., description="Date when the service was performed", regex=r"^\d{4}-\d{2}-\d{2}$")
    service_type: str = Field(..., description="Type of service performed (e.g., oil change, tire rotation)")
    cost: float = Field(..., description="Cost of the service performed", ge=0.0)
    notes: Optional[str] = Field(None, description="Additional notes about the service", min_length=3, max_length=500)

class MaintenanceCreate(MaintenanceBase):
    pass

class MaintenanceOutput(MaintenanceBase):
    id: int = Field(..., description="Unique identifier for the maintenance record")
    car_id: int = Field(..., description="ID of the car associated with this maintenance record")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "car_id": 101,
                "service_date": "2023-10-01",
                "service_type": "Oil Change",
                "cost": 29.99,
                "notes": "Changed oil and filter"
            }
        }