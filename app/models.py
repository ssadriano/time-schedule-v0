from sqlalchemy import Column, Integer, String
from .database import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    start_time = Column(String)
    end_time = Column(String)
