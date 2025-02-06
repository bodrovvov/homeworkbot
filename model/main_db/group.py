from sqlalchemy import Column, Integer, String

from database.main_db.database import  Base

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primaty_key=True)
    group_name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'Group [ID: {self.id}, mode: {self.group_name}]'

