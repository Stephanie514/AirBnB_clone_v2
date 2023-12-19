# test_console.py
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        # Testing create command with valid input
        valid_input = "create User email='test@test.com' password='pass' " \
                      "first_name='John' last_name='Doe'"
        self.console.onecmd(valid_input)
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)

        # Testing create command with invalid class name
        self.console.onecmd("create InvalidClass")
        output = mock_stdout.getvalue().strip()
        self.assertIn("** class doesn't exist **", output)

        # Testing create command with missing class name
        self.console.onecmd("create")
        output = mock_stdout.getvalue().strip()
        self.assertIn("** class name missing **", output)

        # Testing create command with missing parameters
        self.console.onecmd("create User")
        output = mock_stdout.getvalue().strip()
        self.assertIn("** parameters missing **", output)

        # Testing create command with invalid parameters
        invalid_param_input = "create User invalid_param"
        self.console.onecmd(invalid_param_input)
        output = mock_stdout.getvalue().strip()
        self.assertIn("Skipping invalid parameter", output)
