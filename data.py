class TransactionError(Exception):
    pass

class KeyValueDatabase:
    def __init__(self):
        self.main_data = {}
        self.transaction_data = None
        self.in_transaction = False

    def begin_transaction(self):
        if self.in_transaction:
            raise TransactionError("A transaction is already in progress.")
        self.transaction_data = {}
        self.in_transaction = True

    def put(self, key, value):
        if not self.in_transaction:
            raise TransactionError("No transaction in progress.")
        self.transaction_data[key] = value

    def get(self, key):
        if self.in_transaction and key in self.transaction_data:
            return self.transaction_data[key]
        return self.main_data.get(key, None)

    def commit(self):
        if not self.in_transaction:
            raise TransactionError("No transaction in progress.")
        for key, value in self.transaction_data.items():
            self.main_data[key] = value
        self.transaction_data = None
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise TransactionError("No transaction in progress.")
        self.transaction_data = None
        self.in_transaction = False
