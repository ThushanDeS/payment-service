# Payment Service 💳

## Student C - Payment Microservice

This microservice handles payments and fare calculations for the flight management system.

## Technologies
- Python 3.11
- FastAPI
- PostgreSQL
- Docker
- GitHub Actions
- Azure Container Apps

## Features
- Process credit card payments
- Calculate flight fares with taxes and fees
- Multiple fare classes (economy, business, first)
- Payment history and tracking
- Integration with Flight and Booking services

## API Endpoints

### Health & Info
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/` | Service information |

### Payments
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/payments/` | Process a new payment |
| GET | `/api/payments/{payment_id}` | Get payment by ID |
| GET | `/api/payments/booking/{booking_ref}` | Get all payments for a booking |
| GET | `/api/payments/user/{user_id}` | Get all payments for a user |

### Fares
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/fares/` | Get all fares (with optional filtering) |
| GET | `/api/fares/{flight_id}` | Calculate fare for a specific flight |
| POST | `/api/fares/calculate` | Calculate fare using request body |

## Integration Points

### This service is called by:
- **Booking Service (Student B)**: 
  - `POST /api/payments` - To process payments
  - `GET /api/fares/{flight_id}` - To calculate fares

### This service calls:
- **Flight Service (Student A)**:
  - `GET /api/flights/{flight_id}` - To get flight details for fare calculation

## Setup Instructions

### Prerequisites
- Python 3.11+
- PostgreSQL
- Docker (optional)

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/payment-service.git
cd payment-service