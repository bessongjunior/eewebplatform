

from fastapi import HTTPException
import logging
import re
from typing import TypeVar, Optional

from pydantic import BaseModel, validator, EmailStr
from sqlalchemy import false, Enum



T = TypeVar('T')

# get root logger
logger = logging.getLogger(__name__)

class Sex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class CustomerRegisterSchema(BaseModel):

    username: str
    email: EmailStr
    name: str
    password: str
    phone_number: str
    birth: str
    sex: Sex
    # profile: str = "base64"

    # phone number validation

    @validator("phone_number")
    def phone_validation(cls, v):
        logger.debug(f"phone in 2 validatior: {v}")

        # regex phone number
        regex = r"^[\+]?[(]?[0-9]{4}[)]?[-\s\.]?[0-9]{4}[-\s\.]?[0-9]{4,6}$"
        if v and not re.search(regex, v, re.I):
            raise HTTPException(status_code=400, detail="Invalid input phone number!")
        return v

    # Sex validation
    @validator("sex")
    def sex_validation(cls, v):
        if hasattr(Sex, v) is False:
            raise HTTPException(status_code=400, detail="Invalid input sex")
        return v


class CustomerLoginSchema(BaseModel):
    email: EmailStr
    password: str


class ForgotPasswordSchema(BaseModel):
    email: EmailStr
    new_password: str

class ForgotPasswordRequestSchema(BaseModel):
    email: EmailStr




class CarTypeSchema(BaseModel):
    id: int
    type_name: str
    description: str

    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    # profile: Optional[str] = None  

    class Config:
        orm_mode = True

class CarSchema(BaseModel):
    id: Optional[int] = None
    cartype: CarTypeSchema
    make: str
    model: str
    year: int
    color: str
    price_per_day: int
    status: str
    image_main: Optional[str] = None  # This will store the path to the image file
    image_1: Optional[str] = None  # This will store the path to the image file
    image_2: Optional[str] = None  # This will store the path to the image file
    image_3: Optional[str] = None  # This will store the path to the image file
    image_4: Optional[str] = None  # This will store the path to the image file
    poster: Optional[UserSchema] = None

    class Config:
        orm_mode = True  


class CustomerSchema(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    phone_number: str
    address: str
    city: str
    sex: str
    profile: str


    class Config:
        orm_mode = True

    



# image: Optional[str] = None  # This will store the path to the image file

# class DetailSchema(BaseModel):
#     status: str
#     message: str
#     result: Optional[T] = None


# class ResponseSchema(BaseModel):
#     detail: str
#     result: Optional[T] = None
