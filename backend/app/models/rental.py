from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base # replace session with database in case of errors

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    cartype_id = Column(Integer, ForeignKey('cartypes.id'))
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    color = Column(String)
    price_per_day = Column(Integer)
    status = Column(String)
    image_main: str = Column(String(256))
    image_1: str = Column(String(256))
    image_2: str = Column(String(256))
    image_3: str = Column(String(256))
    image_4: str = Column(String(256))
    poster_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    poster = relationship("User", back_populates="carposts")


class Rental(Base):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    start_data = Column(String)
    end_data = Column(String)
    total_price = Column(Integer)
    location = Column(String(256))


class CarType(Base):
    __tablename__ = 'cartypes'

    id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String)
    description = Column(String)


