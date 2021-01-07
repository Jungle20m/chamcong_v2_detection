from sqlalchemy import Column, String, Integer, Date, DateTime, Text, Numeric

from app.database.database import Base


class Images(Base):
    __tablename__ = "images"
    
    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String(512))
    user_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)