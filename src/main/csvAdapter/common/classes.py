class NewEntry:
    def __init__(self, value_date, beneficiary, currency, amount_eur):
        self.date = value_date
        self.beneficiary = beneficiary
        self.currency = currency
        self.amount_eur = amount_eur
        self.category = ""
        self.subcategory = ""
    
    def to_row(self):
        return [
            self.date,
            self.beneficiary,
            self.currency,
            str(self.amount_eur),
            self.category,
            self.subcategory
        ]