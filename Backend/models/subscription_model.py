from pydantic import BaseModel, EmailStr

class EmailSubscription(BaseModel):
    email: EmailStr
