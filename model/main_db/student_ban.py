from sqlalchemy import Column, Integer, Boolean

from database.main_db.database import  Base

class StudentBan(Base):
    __tablename__ = 'student_ban'

    telegram_id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'StudentBan [ID: {self.telegram_id}]'
