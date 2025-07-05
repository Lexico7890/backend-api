from sqlalchemy import Column, Integer, String, DateTime
from session import Base

class Maintenance(Base):
    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Maintenance(id={self.id}, car_id={self.car_id}, description='{self.description}', cost={self.cost}, date={self.date})>"