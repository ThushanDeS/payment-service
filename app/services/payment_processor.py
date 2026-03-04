class PaymentProcessor:
    def __init__(self):
        pass

    def process_payment(self, payment_data: dict):
        """Process a payment"""
        return {
            "status": "success",
            "transaction_id": "TXN123456"
        }

    def validate_payment(self, payment_data: dict) -> bool:
        """Validate payment data"""
        return True
