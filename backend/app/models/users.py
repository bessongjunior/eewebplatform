from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base # replace session with database in case of errors

class User(Base):
    __tablename__ = 'users'

    id =  Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String)
    sex = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)
    marital_status = Column(String)
    carposts = relationship(
        "Car",
        cascade="all,delete-orphan",
        back_populates="poster",
        uselist=True,
    )