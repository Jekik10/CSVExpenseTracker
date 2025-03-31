class NewEntry:
    def __init__(self, date, beneficiary, currency, amount_eur):
        self.date = date
        self.beneficiary = beneficiary
        self.currency = currency
        self.amount_eur = amount_eur
        self.category = ""
        self.subcategory = ""