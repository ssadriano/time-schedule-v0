from pydantic import BaseModel

class ScheduleCreate(BaseModel):
    title: str
    start_time: str
    end_time: str

class ScheduleOut(BaseModel):
    id: int
    title: str
    start_time: str
    end_time: str

    class Config:
        from_attributes = True

