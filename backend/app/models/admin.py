from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base # replace session with database in case of errors

class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String)
    sex = Column(String)
    email = Column(String)
    contact = Column(String)
    address = Column(String)
    