from pydantic import BaseModel , EmailStr

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email :EmailStr
    addresses :list[Address]

user_data = {
    "id": 2 ,
    "name": "Faizan",
    "email": "faizan@example.com",
    "addresses":[
        {"street": "123 Main st", "city" : "New York", "zip_code": "10001"},
            {"street": "145 Main st", "city": "Los Angeles" , "zip_code":"10002" }   
              ],
}

user = UserWithAddress.model_validate(user_data)
print(user.model_dump())