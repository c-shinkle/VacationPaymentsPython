from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from re import sub


@dataclass
class Person:
    name: str
    amount: Decimal


TWOPLACES = Decimal(10) ** -2


def cli_caleb():
    people = calebs_algorithm(handle_input())
    for p in people:
        print("{} owes {}".format(p.name, "$" + str(p.amount) if p.amount > 0 else 'nothing'))


def cli_zach():
    zachs_algorithm(handle_input())


def handle_input() -> [Person]:
    print("Enter name of person and amount they paid (separated by space)")
    print("Enter '#' when finished")
    people = []
    user_input = input()
    while '#' not in user_input:
        tokens = user_input.split()
        people.append(Person(tokens[0], Decimal(sub(r'[^\d.]', '', tokens[1])).quantize(TWOPLACES, ROUND_HALF_UP)))
        user_input = input()
    return people


def calebs_algorithm(people: [Person]) -> [Person]:
    per_person = sum(p.amount for p in people) / len(people)
    return [
        Person(p.name, max((per_person - p.amount).quantize(TWOPLACES, ROUND_HALF_UP), Decimal('0.00')))
        for p in people
    ]


def zachs_algorithm(people: [Person]):
    spent_per_person: dict[str, Decimal] = {}
    for person in people:
        spent_per_person[person.name] = person.amount / len(people)
    debt_dict: dict[tuple[str, str], Decimal] = {}
    for earner in people:
        for payee in people:
            debt_dict[(earner.name, payee.name)] = spent_per_person[earner.name] if earner is not payee else Decimal(0)
    pay_dict: dict[tuple[str, str], Decimal] = {}
    for earner in people:
        for payee in people:
            amount = debt_dict[earner.name, payee.name] - debt_dict[payee.name, earner.name]
            pay_dict[(earner.name, payee.name)] = max(amount, Decimal(0))
    for person in people:
        total_to_pay = Decimal(0)
        for payee in people:
            total_to_pay += pay_dict[(payee.name, person.name)]
        total_to_receive = Decimal(0)
        for earner in people:
            total_to_receive += pay_dict[(person.name, earner.name)]
        amount = (total_to_pay - total_to_receive).quantize(TWOPLACES, ROUND_HALF_UP)
        print("{} owes {}".format(person.name, "$" + str(amount) if amount > Decimal(0) else 'nothing'))
