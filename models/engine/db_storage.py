from sqlalchemy import create_engine, exc, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.sign_in import SignIn
from models.sign_up import SignUp

Base = declarative_base()

DATABASE_URL = 'mysql://debian-sys-maint:77Bh2wFNVVwZruXr@localhost:3306/models'

Base = declarative_base()

def create_database(engine_url):
    """Creates a database"""
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def populate_database(engine_url):
    """Populates a database"""
    engine = create_engine(engine_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    sign_in_data = [
        {id='1', username='user1', password='pass1'},
        {id='2', username='user2', password='pass2'},
    ]

    sign_up_data = [
        {id='1', username='user1', password='pass1', email='user1@example.com'},
        {id='2', username='user2', password='pass2', email='user2@example.com'},
    ]

    try:
        for data in sign_in_data:
            session.add(SignIn(**data))

        for data in sign_up_data:
            session.add(SignUp(**data))

        session.commit()
        print('Test database populated successfully.')

    except exc.IntegrityError as e:
        session.rollback()
        print('Error: Duplicate entry or integrity violation.')

    finally:
        session.close()

if __name__ == '__main__':
    create_database(DATABASE_URL)
    populate_database(DATABASE_URL)
