from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dog, Base as base


engine = create_engine("sqlite:///dogs.db")
def create_table(base):
   
    base.metadata.creat_all(engine)

def save(session, dog):
   session.add(dog)
   session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

if __name__ == "__main__":
    create_table(base)

    Session = sessionmaker(bind=engine)
    session = Session()