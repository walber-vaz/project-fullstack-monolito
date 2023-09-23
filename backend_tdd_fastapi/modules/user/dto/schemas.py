from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserSchemaResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserSchemaDB(UserSchema):
    id: int


class UserSchemaUserList(BaseModel):
    users: list[UserSchemaResponse]


class Message(BaseModel):
    detail: str
