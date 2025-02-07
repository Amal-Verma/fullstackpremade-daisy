from fastapi import APIRouter
from models import userReqMod,userResMod
from database import db_dependancy
from schema import Peoples
from database import Base,engine
from auth import hashed_pass,verify_hash_pass,jwt_encode,jwt_decode
router=APIRouter()
Base.metadata.create_all(bind=engine)

@router.post("/login",response_model=userResMod)
async def login(req:userReqMod,db:db_dependancy):
    user=db.query(Peoples)
    findUser=user.filter(Peoples.email==req.email).first()
    if findUser:
        if verify_hash_pass(req.password,findUser.password):
            token=jwt_encode(findUser.id)
            return {"error":False,"token":token}
        else:
            return {"error":True,"token":""}
    else:
        return {"error":True,"token":""}

Base.metadata.create_all(bind=engine)
@router.post("/register",response_model=userResMod)
async def register(req:userReqMod,db:db_dependancy):
    user=db.query(Peoples)
    findUser=user.filter(Peoples.email==req.email).first()
    if findUser:
        return {"error":True,"token":""}
    hash_pass=hashed_pass(req.password)
    user=Peoples(email=req.email,password=hash_pass)
    db.add(user)
    db.commit()
    db.refresh(user)
    token=jwt_encode(user.id)
    return {"error":False,"token":token}
