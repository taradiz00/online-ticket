# Airport Reservation System API

A backend API for managing flight reservations, passengers, tickets, and authentication built with FastAPI and SQLAlchemy.

## Tech Stack

• FastAPI
• SQLAlchemy (ORM)
• Pydantic (Schemas)
• Pytest (Testing)
• Faker (Database seeding)
• Uvicorn
• SMTP Email (Password reset system)

## Overview

This project simulates a real-world airport reservation system where users can:

• Register and authenticate
• Create flight reservations
• Add passengers to reservations
• Automatically generate tickets per passenger
• Manage flight-seat assignments
• Receive email-based password reset links

## Architecture

The project follows a clean layered architecture:

Models (ORM)
↓
Schemas (Pydantic)
↓
Routers (API endpoints)
↓
Database (SQLAlchemy Session)

## Database Design

Built using SQLAlchemy ORM with relationships between:

• User
• Reservation
• Passenger
• Flight
• Ticket

## Key Relationships:

• A User has many Reservations
• A Reservation belongs to one Flight
• A Reservation can have multiple Passengers
• Each Passenger gets a Ticket
• Ticket is linked to Flight + Passenger + Reservation

## Features Implemented

Authentication

    •	User registration
    •	Login system
    •	Password hashing
    •	Password reset via email (SMTP)

Flight Management

    •	Flight data stored with pricing and schedule
    •	Linked to origin and destination cities
    •	Airline association

Reservation System

    •	Create reservation per flight
    •	Link reservation to authenticated user
    •	Retrieve reservation details with nested flight data

Passenger Management

    •	Add multiple passengers per reservation
    •	Store passport, contact, and personal info
    •	Link passengers to reservation

Ticket System

    •	Automatic ticket generation per passenger
    •	Unique ticket number generation
    •	Seat assignment logic per flight
    •	Price and class assignment

Email System

    •	Password reset via email link
    •	Token-based reset mechanism
    •	SMTP integration

Testing

    •	Basic API testing with Pytest
    •	Endpoint validation
    •	Database interaction tests

Database Seeding

    •	Faker-based script to populate database with:
    •	Users
    •	Flights
    •	Reservations
    •	Sample data for testing

API Endpoints

Authentication
• POST /register
• POST /login
• POST /forgot-password
• POST /reset-password

Reservations
• POST /reservation/init
• POST /reservation/{reservation_id}/confirm
• POST /reservation/{reservation_id}/add_passengers

Tickets
• GET /ticket/{ticket_id}

## Database Seeding

To populate database with fake data:

python qollabi_records.py
Faker-based generator script included

## Key Learnings

    • Designing relational database with ORM
    • Handling complex relationships (Reservation → Passenger → Ticket)
    • Schema validation using Pydantic
    • Building RESTful APIs with FastAPI
    • Email integration for password recovery
    • Writing basic tests with Pytest
    • Structuring scalable backend architecture

## Future Improvements

    • Payment gateway integration (Stripe)
    • Role-based access (Admin/User)
    • Deployment on cloud (Render / Railway)
    • Async email queue (Celery + Redis)
    • Better seat allocation algorithm

## Installation & Run

### 1. Clone repo

```bash
git clone https://github.com/taradiz00/ticket-online.git
cd ticket-online

2. Create virtual environment

python -m venv venv
venv/Scripts/activate

3. Install dependencies

pip install -r requirements.txt

4. Run server

uvicorn main:app --reload



Swagger UI

API documentation available at:

http://127.0.0.1:8000/docs

Author
Tara Dizaji

Built as a backend portfolio project for learning and demonstrating real-world API development skills.
```
