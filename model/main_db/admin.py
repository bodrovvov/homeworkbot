from sqlalchemy import Column, Integer, Boolean

from database.main_db.database import  Base

class Admin(Base):
    __tablename__ = 'admin'

    telegram_id = Column(Integer, primaty_key=True)
    teacher_mode = Column(Boolean, default=False)

    def __repr__(self):
        return f'Admin [ID: {self.telegram_id}, mode: {self.teacher_mode}]'

