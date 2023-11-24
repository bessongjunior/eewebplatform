from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base # replace session with database in case of errors

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(128))
    lastname = Column(String(128))
    email = Column(String(128))
    phone_number = Column(String(20))
    address = Column(String)
    city = Column(String(256))
    sex = Column(String(20))
    profile: str = Column(String(256))
