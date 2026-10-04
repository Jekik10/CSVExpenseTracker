class TradeRepublicEntry:
    def __init__(self, datetime, date, account_type, category, type, asset_class, name, symbol, shares, price, 
                 amount, fee, tax, currency, original_amount, original_currency, fx_rate, description, transaction_id, 
                 counterparty_name, counterparty_iban, payment_reference, mcc_code):
        self.type = type
        self.datetime = datetime
        self.date = date
        self.account_type = account_type
        self.category = category
        self.type = type
        self.asset_class = asset_class
        self.name = name
        self.symbol = symbol
        self.shares = shares
        self.price = price
        self.amount = amount
        self.fee = fee
        self.tax = tax 
        self.currency = currency
        self.original_amount = original_amount
        self.original_currency = original_currency
        self.fx_rate = fx_rate
        self.description = description
        self.transaction_id = transaction_id
        self.counterparty_name = counterparty_name
        self.counterparty_iban = counterparty_iban
        self.payment_reference = payment_reference
        self.mcc_code = mcc_code