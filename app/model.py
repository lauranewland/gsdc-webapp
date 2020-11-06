from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import relationship


from database import Base


class Users(Base):
    """Data Model for a User"""

    # Creates a table of users
    __tablename__ = 'users'

    # Defines the Schema for the users table
    user_id = Column(Integer, primary_key=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    zip_code = Column(String(10), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
    app_date = Column(Date)
    co_app_fname = Column(String(50))
    co_app_lname = Column(String(50))
    co_app_email = Column(String(100))
    pref_communication = Column(String(50), nullable=False)
    print_permissions = Column(Boolean, nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    member_type = Column(String(100), nullable=False)
    member_standing = Column(String(25), nullable=False)
    other_orgs = Column(Text)
    num_of_gsd = Column(Integer)
    num_breedings = Column(Integer)

    # Add Relationship to Interest Table
    interest = relationship('Interest', backref='user')

    def __repr__(self):
        return f'<user_id={self.user_id}, fname={self.fname}, lname={self.lname}>'


class Interest(Base):
    """Data Model for User Interest"""

    # Creates a table of user interests
    __tablename__ = 'interest'

    # Defines the Schema for the users interest table
    interest_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    obedience = Column(Boolean)
    rally = Column(Boolean)
    conformation = Column(Boolean)
    agility = Column(Boolean)
    herding = Column(Boolean)
    scentwork = Column(Boolean)
    fun_match = Column(Boolean)
    shep_o_gram = Column(Boolean)
    training = Column(Boolean)
    hospitality = Column(Boolean)
    fundraising = Column(Boolean)
    gsd_fun_day = Column(Boolean)
    demo_mn_fair = Column(Boolean)
    annual_banquet = Column(Boolean)
    breeding = Column(Boolean)
    other = Column(String(100))

    user = relationship('User', backref='interest')

    def __repr__(self):
        return f'<interest_id={self.interest_id}, obedience={self.obedience}, training={self.training}>'
