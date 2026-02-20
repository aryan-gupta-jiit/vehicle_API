from fastapi import FastAPI, HTTPException
import json
from services.bs_service import detect_bs_norm
from utils.helpers import generate_request_id, current_timestamp

app = FastAPI(title="Mock VAHAN RC API")

# Load mock data
with open("data/mock_vehicles.json") as f:
    vehicles = json.load(f)

@app.get("/vehicle/{reg_no}")
def get_vehicle_details(reg_no: str):

    vehicle = next(
        (v for v in vehicles if v["registration_number"].upper() == reg_no.upper()),
        None
    )

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    bs_norm = detect_bs_norm(vehicle["manufacturing_date"])

    response = {
        "status": "success",
        "request_id": generate_request_id(),
        "timestamp": current_timestamp(),
        "data_source": "MOCK_VAHAN_SANDBOX",
        "data": {
            **vehicle,
            "emission_norms": bs_norm
        }
    }

    return response