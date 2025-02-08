from fastapi import APIRouter, HTTPException
from supabase import create_client, Client
import os
import uuid
from models import RoomRequestModel, RoomResponseModel

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.post("/create-room", response_model=RoomResponseModel)
async def create_room(req: RoomRequestModel):
    room_id = str(uuid.uuid4())
    response = supabase.table("rooms").insert({
        "room_id": room_id,
        "repo_id": req.repo_id,
        "path": req.path
    }).execute()
    if response.error:
        raise HTTPException(status_code=500, detail="Failed to create room")
    return {"error": False, "room_id": room_id, "message": "Room created successfully"}
