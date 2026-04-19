from pydantic import BaseModel, field_validator
from datetime import datetime

class ScheduleCreate(BaseModel):
    title: str
    start_time: str
    end_time: str

    @field_validator("start_time", "end_time")
    @classmethod
    def validate_time_format(cls, v):
        try:
            datetime.strptime(v, "%H:%M")
        except ValueError:
            raise ValueError("time must be in HH:MM format")
        return v

    @field_validator("end_time")
    @classmethod
    def validate_time_order(cls, end_time, info):
        start_time = info.data.get("start_time")
        if start_time:
            start = datetime.strptime(start_time, "%H:%M")
            end = datetime.strptime(end_time, "%H:%M")
            if end <= start:
                raise ValueError("end_time must be after start_time")
        return end_time


class ScheduleOut(BaseModel):
    id: int
    title: str
    start_time: str
    end_time: str

    class Config:
        from_attributes = True

