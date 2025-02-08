from pydantic import BaseModel
import uuid


class RoomRequestModel(BaseModel):
    repo_id: str
    path: str

class RoomResponseModel(BaseModel):
    error: bool
    message: str
    room_id: str