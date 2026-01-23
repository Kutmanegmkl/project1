class ClientOperationsIterator:
    def __init__(self, operations):
        self.operations = operations
        self.index = 0
    
    def __next__(self):
        if self.index < len(self.operations):
            operation = self.operations[self.index]
            self.index += 1
            return operation
        else:
            raise StopIteration


class ClientOperations:
    def __init__(self, operations):
        self.operations = operations
    
    def __iter__(self):
        return ClientOperationsIterator(self.operations)


# Пример использования
operations = [
    {"type": "deposit", "amount": 1000},
    {"type": "withdraw", "amount": 200},
    {"type": "deposit", "amount": 500},
    {"type": "withdraw", "amount": 100}
]

client_ops = ClientOperations(operations)

# Подсчёт баланса
balance = 0
for operation in client_ops:
    if operation["type"] == "deposit":
        balance += operation["amount"]
    elif operation["type"] == "withdraw":
        balance -= operation["amount"]
    print(f"{operation['type']}: {operation['amount']}, баланс: {balance}")

print(f"\nИтоговый баланс: {balance}")