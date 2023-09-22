from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserSchemaResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserSchemaDB(UserSchema):
    id: int


class UserSchemaUserList(BaseModel):
    users: list[UserSchemaResponse]


class Message(BaseModel):
    detail: str
