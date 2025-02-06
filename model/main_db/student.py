from enum import unique

from sqlalchemy import Column, Integer, String, ForeignKey

from dataclasses import dataclass

from database.main_db.database import  Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    group = Column(Integer, ForeignKey('groups.id'), nullable=False)
    telegram_id = Column(Integer, nullable=True, unique=True)


    def __repr__(self):
        return f'Student [ID: {self.id}, ФИО: {self.full_name}, grID: {self.group}, TgID: {self.telegram_id}]'

@dataclass
class StudentRaw:
    full_name: str