from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

    @field_validator("name")
    @classmethod
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least two characters long")
        return v

    @field_validator("email")
    @classmethod
    def email_must_be_company_domain(cls, v):
        if not v.endswith("@myemail.com"):
            raise ValueError("Email must be a company email")
        return v

try: 
    invalid_user = UserWithAddress(
        id=3,
        name="A",
        email="charlie@example",
        addresses=[{"street": "653 Pine Rd", "city": "chicago", "zip_code": "643224"}]
    )
except ValidationError as e:
    print(e)
