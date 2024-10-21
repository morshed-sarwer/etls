from sqlalchemy import Column, DateTime, String
from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

#-
Base = declarative_base()
class DimCustomer(Base):
    __tablename__ = 'dim_customers'
    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    registration_date = Column(DateTime)
    picture_url = Column(String)
    gender = Column(String)