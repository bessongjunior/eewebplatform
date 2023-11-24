from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base # replace session with database in case of errors



# rdv booking



# email notifications
class EmailNotif(Base):
    __tablename__ = 'emailnotifs'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), nullable=True)



# others