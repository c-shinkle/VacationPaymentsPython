from decimal import Decimal
from unittest import TestCase
from unittest.mock import patch, call

from src.vacation_payment import cli_caleb, calebs_algorithm, zachs_algorithm, Person, handle_input, cli_zach


class Test(TestCase):

    @patch('builtins.input', side_effect=['Alex $8,000.00', 'Justin $2,000.00', '#'])
    def test_given_amount_with_dollar_sign_and_period_as_input_should_parse_correctly(self, mock_input):
        actual = handle_input()

        self.assertListEqual([Person('Alex', Decimal(8000)), Person('Justin', Decimal(2000))], actual)

    @patch('builtins.print')
    def test_given_people_caleb_should_print_amounts_owed(self, mock_print):
        calebs_algorithm([Person('Alex', Decimal(6)), Person('Justin', Decimal(2)), Person('Caleb', Decimal(1))])

        calls = [call('Alex owes nothing'), call('Justin owes $1.00'), call('Caleb owes $2.00')]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    def test_given_people_zach_should_print_amounts_owed(self, mock_print):
        zachs_algorithm([Person('Alex', Decimal(6)), Person('Justin', Decimal(2)), Person('Caleb', Decimal(1))])

        calls = [call('Alex owes nothing'), call('Justin owes $1.00'), call('Caleb owes $2.00')]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    def test_given_amount_with_decimals_as_input_should_round_amounts_owed(self, mock_print):
        calebs_algorithm([Person('Alex', Decimal('1.33')), Person('Justin', Decimal('0'))])

        calls = [call('Alex owes nothing'), call('Justin owes $0.67')]
        mock_print.assert_has_calls(calls)

    @patch('builtins.input',
           side_effect=['Alex $3,136.02', 'Justin $290.64', 'Christian $680.95', 'Zach $159.71', 'Caleb $363.14', '#'])
    @patch('builtins.print')
    def test_given_a_trip_to_florida_caleb_should_print_amounts_owed(self, mock_print, mock_input):
        cli_caleb()

        calls = [call('Enter name of person and amount they paid (separated by space)'),
                 call("Enter '#' when finished"), call('Alex owes nothing'), call('Justin owes $635.45'),
                 call('Christian owes $245.14'),
                 call('Zach owes $766.38'), call('Caleb owes $562.95')]
        mock_print.assert_has_calls(calls)

    @patch('builtins.input',
           side_effect=['Alex $3,136.02', 'Justin $290.64', 'Christian $680.95', 'Zach $159.71', 'Caleb $363.14', '#'])
    @patch('builtins.print')
    def test_given_a_trip_to_florida_zach_should_print_amounts_owed(self, mock_print, mock_input):
        cli_zach()

        calls = [call('Enter name of person and amount they paid (separated by space)'),
                 call("Enter '#' when finished"), call('Alex owes nothing'), call('Justin owes $635.45'),
                 call('Christian owes $245.14'),
                 call('Zach owes $766.38'), call('Caleb owes $562.95')]
        mock_print.assert_has_calls(calls)
