class Entry:
    def __init__(self, booking_date, value_date, beneficiary, account_number, transaction_type, payment_reference, account_name, amount_eur, amount_other, currency, exchange_rate):
        self.booking_date = booking_date
        self.value_date = value_date
        self.beneficiary = beneficiary
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.payment_reference = payment_reference
        self.account_name = account_name
        self.amount_eur = amount_eur
        self.amount_other = amount_other
        self.currency = currency
        self.exchange_rate = exchange_rate
                
class NewEntry:
    def __init__(self, value_date, beneficiary, currency, amount_eur):
        self.date = value_date
        self.beneficiary = beneficiary
        self.currency = currency
        self.amount_eur = amount_eur
        self.category = ""
        self.subcategory = ""