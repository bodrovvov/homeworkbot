from sqlalchemy import Column, Integer, String

from dataclasses import dataclass

from database.main_db.database import  Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    telegram_id = Column(Integer, nullable=True, unique=True)


    def __repr__(self):
        return f'Teacher [ID: {self.id}, ФИО: {self.full_name}, TgID: {self.telegram_id}]'

@dataclass
class TeacherRaw:
    full_name: str
    telegram_id: int
    is_admin: bool