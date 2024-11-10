import os

from datetime import datetime
from model.general import User, Publisher
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session


def setup() -> (Faker, session):
    load_dotenv()
    engine = create_engine(os.getenv('DATABASE_URI'), echo=True)
    local_session_object = sessionmaker(bind=engine)
    local_session = local_session_object()

    return Faker(), local_session


def create_publisher_data(temp_fake: Faker, local_session: session) -> Publisher:
    publisher = Publisher()
    publisher.name = temp_fake.company()
    publisher.description = temp_fake.text()
    publisher.domain = temp_fake.domain_name()
    publisher.mail = temp_fake.email()
    local_session.add(publisher)
    return local_session.commit()


def create_user_data(temp_fake: Faker, local_session: session) -> None:
    for _ in range(10):
        user = User()
        user.firstName = temp_fake.first_name()
        user.lastName = temp_fake.last_name()
        user.email = temp_fake.email()
        user.password = temp_fake.password()
        user.registrationDate = datetime.now()
        user.admin = False
        user.publisher = create_publisher_data(temp_fake, local_session)

        local_session.add(user)
    local_session.commit()

if __name__ == '__main__':
    fake, session = setup()

    # Create data
    create_user_data(fake, session)