from fastapi import APIRouter, HTTPException
from supabase import create_client, Client
import os
import uuid
from models import AccessRequestModel, AccessResponseModel

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.post("/set-access", response_model=AccessResponseModel)
async def set_access(req: AccessRequestModel):
    response = supabase.table("access").insert({
        "userid": req.userid,
        "repo_id": req.repo_id,
        "access": req.access
    }).execute()
    if response.error:
        raise HTTPException(status_code=500, detail="Failed to set access")
    return {"error": False, "access": req.access, "message": "Access set successfully"}
