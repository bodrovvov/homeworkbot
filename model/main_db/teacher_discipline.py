from sqlalchemy import Column, Integer, ForeignKey

from database.main_db.database import  Base

class TeacherDiscipline(Base):
    __tablename__ = 'teacher_disciplines'

    id = Column(Integer, primary_key=True, autoincrement=False)
    discipline_id = Column(Integer, ForeignKey('disciplines.id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)

    def __repr__(self):
        return f'Discipline [grID: {self.discipline_id}, tId: {self.teacher_id}]'

