from decimal import Decimal

from src.vacation_payment import zachs_algorithm, Person

if __name__ == '__main__':
    zachs_algorithm([Person('Alex', Decimal(9)), Person('Justin', Decimal(2)), Person('Caleb', Decimal(1))])

