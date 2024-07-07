# Task 1: Define SQLAlchemy ORM Models for Claim and Policy Data Structures
# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Policy(Base):
    __tablename__ = 'policies'
    id = Column(Integer, primary_key=True)
    policy_number = Column(String(100), unique=True, nullable=False)
    policyholder = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)
    claims = relationship('Claim', backref='policy')

class Claim(Base):
    __tablename__ = 'claims'
    id = Column(Integer, primary_key=True)
    policy_id = Column(Integer, ForeignKey('policies.id'))
    claim_description = Column(String(200), nullable=False)
    claim_date = Column(DateTime, nullable=False)
    status = Column(String(100), nullable=False)
