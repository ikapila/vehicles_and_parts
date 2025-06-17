from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    transactions = relationship("Transaction", back_populates="user")

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    model = Column(String, nullable=False)
    stock = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    transactions = relationship("Transaction", back_populates="vehicle")

class Part(Base):
    __tablename__ = "parts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    stock = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    transactions = relationship("Transaction", back_populates="part")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=True)
    part_id = Column(Integer, ForeignKey("parts.id"), nullable=True)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="transactions")
    vehicle = relationship("Vehicle", back_populates="transactions")
    part = relationship("Part", back_populates="transactions")
