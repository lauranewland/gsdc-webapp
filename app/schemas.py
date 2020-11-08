from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    fname: str
    lname: str
    address: str
    city: str
    zip_code: str
    phone: str
    email: str
    app_date: Optional[str] = None
    co_app_fname: Optional[str] = None
    co_app_lname: Optional[str] = None
    co_app_email: Optional[str] = None
    pref_communication: str
    print_permissions: bool
    member_type: str
    member_standing: str
    other_orgs: Optional[str] = None
    num_of_gsd: Optional[int] = None
    num_breedings: Optional[int] = None


class UserGet(UserBase):
    user_id: int

    class Config:
        orm_mode = True


# UserCreate class represents all of Userbase and password
class UserCreate(UserBase):
    password: str

