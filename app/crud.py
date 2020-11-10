from sqlalchemy.orm import Session
import model
import schemas


def get_user_by_email(db: Session, email: str):
    """Queries a user by email"""
    return db.query(model.Users).filter(model.Users.email == email).first()


def get_all_users(db: Session):
    """Queries and returns all users"""
    return db.query(model.Users).all()


def get_user(db: Session, user_id: int):
    """Queries and returns a user"""
    return db.query(model.Users).filter(model.User.user_id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    """Creates a user"""

    # Creates a Fake hashed password
    hashed_password = user.password + "thisisaplaceholder"

    # Creates a user
    db_user = model.Users(
        fname=user.fname,
        lname=user.lname,
        address=user.address,
        city=user.city,
        zip_code=user.zip_code,
        phone=user.phone,
        email=user.email,
        password=hashed_password,
        app_date=user.app_date,
        # co_app_fname=user.co_app_fname,
        # co_app_lname=user.co_app_lname,
        # co_app_email=user.co_app_email,
        pref_communication=user.pref_communication,
        print_permissions=user.print_permissions,
        member_type=user.member_type,
        member_standing=user.member_standing,
        other_orgs=user.other_orgs,
        num_of_gsd=user.num_of_gsd,
        num_breedings=user.num_breedings
    )

    # Adds user to the database session
    db.add(db_user)

    # Commits user to the database
    db.commit()

    # Refreshes the database instances
    db.refresh(db_user)

    return db_user


def create_user_interest(db: Session, interest: schemas.CreateInterest, user_id: int):
    """Creates a user interest"""

    db_interest = model.Interest(**interest.dict(), user_id=user_id)

    # Adds user interest to the database session
    db.add(db_interest)

    # Commits user interest to the database
    db.commit()

    # Refreshes the database instances
    db.refresh(db_interest)

    return db_interest


def get_all_interest(db: Session):
    """Queries and returns all users interests"""

    return db.query(model.Interest).all()

