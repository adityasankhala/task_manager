import enum
from sqlalchemy import Column, Integer, String, Boolean,DateTime,Enum
from datetime import datetime,timezone
from fastapi_taskmanager.database import Base
class RoleEnum(str,enum.Enum):
    admin="admin"
    user="user"
class User(Base):
    __tablename__= "users"
    id=Column(Integer, primary_key=True)
    email=Column(String, unique=True)
    hashed_password=Column(String,nullable=False)
    full_name=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
    role=Column(Enum(RoleEnum),default=RoleEnum.user)


    created_at=Column(DateTime,default=lambda:
    datetime.now(timezone.utc))
    

