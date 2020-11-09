from pydantic import BaseModel
from typing import Optional, List


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
    # interests: List[Interest] = []

    # orm_mode tells Pydantic model to read the data even if its not a dict
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    """Creates a User
        UserCreate inherits the attributes from the UserBase Class
        + password
    """
    password: str


class InterestBase(BaseModel):
    """This class contains all common interest attributes"""
    obedience: bool = False
    rally: bool = False
    conformation: bool = False
    agility: bool = False
    herding: bool = False
    scentwork: bool = False
    fun_match: bool = False
    shep_o_gram: bool = False
    training: bool = False
    hospitality: bool = False
    fundraising: bool = False
    gsd_fun_day: bool = False
    demo_mn_fair: bool = False
    annual_banquet: bool = False
    breeding: bool = False
    other: Optional[str] = None


class Interest(InterestBase):
    """Interest inherits all attributes from the InterestBase class
        + interest_id & user_id
    """
    interest_id: int
    user_id: int

    class Config:
        """orm_mode tells Pydantic model to read the data even if its not a dict"""
        orm_mode = True


class CreateInterest(InterestBase):
    """Creates an Interest"""
    pass
