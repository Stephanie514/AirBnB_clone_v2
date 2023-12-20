#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import pep8
import unittest

HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation and code style of the console"""

    @staticmethod
    def check_pep8_conformance(files):
        """Check PEP8 compliance for a list of files"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(files)
        return result.total_errors

    def test_pep8_conformance(self):
        """Test PEP8 compliance for console.py and test_console.py"""
        console_file = ['console.py']
        test_console_file = ['tests/test_console.py']

        console_errors = self.check_pep8_conformance(console_file)
        test_console_errors = self.check_pep8_conformance(test_console_file)

        error_msg_console = "Found code style errors in console.py"
        error_msg_test_console = "Found code style errors in test_console.py"

        self.assertEqual(console_errors, 0, error_msg_console)
        self.assertEqual(test_console_errors, 0, error_msg_test_console)

    def test_module_docstring(self):
        """Test module-level docstrings"""
        modules_to_test = [console, HBNBCommand]

        for module in modules_to_test:
            module_name = module.__name__
            msg_doc_missing = f"{module_name} needs a docstring"
            self.assertIsNot(module.__doc__, None, msg_doc_missing)
            self.assertTrue(len(module.__doc__) >= 1, msg_doc_missing)
