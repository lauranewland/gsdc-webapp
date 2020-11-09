from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    """This class contains all common attributes every user will have"""
    fname: str
    lname: str
    address: str
    city: str
    zip_code: str
    phone: str
    email: str
    app_date: Optional[str] = None
    # co_app_fname: Optional[str] = None
    # co_app_lname: Optional[str] = None
    # co_app_email: Optional[str] = None
    pref_communication: str
    print_permissions: bool
    member_type: str
    member_standing: str
    other_orgs: Optional[str] = None
    num_of_gsd: Optional[int] = None
    num_breedings: Optional[int] = None


class UserGet(UserBase):
    """ UserGet inherits the attributes from the UserBase Class + user_id
        Password is not included in the UserGet
        class so it will not be sent through the API
    """
    user_id: int

    # orm_mode tells Pydantic model to read the data even if its not a dict
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    """UserCreate inherits the attributes from the UserBase Class + password"""
    password: str

