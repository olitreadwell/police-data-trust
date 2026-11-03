from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


class RegisterUserDTO(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    first_name: Optional[str] = Field(None, alias="firstname")
    last_name: Optional[str] = Field(None, alias="lastname")
    phone_number: Optional[str]
