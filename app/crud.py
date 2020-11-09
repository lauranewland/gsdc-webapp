from sqlalchemy.orm import Session
import model
import schemas


# Queries a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(model.Users).filter(model.Users.email == email).first()


# Creates a user
def create_user(db: Session, user: schemas.UserCreate):

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

