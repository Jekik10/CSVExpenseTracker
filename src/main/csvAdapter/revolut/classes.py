class RevolutEntry:
    def __init__(self, type, product, started_date, completed_date, description, amount, fee, currency, state, balance):
        self.type = type
        self.product = product
        self.started_date = started_date
        self.completed_date = completed_date
        self.description = description
        self.amount = amount
        self.fee = fee
        self.currency = currency
        self.state = state
        self.balance = balance