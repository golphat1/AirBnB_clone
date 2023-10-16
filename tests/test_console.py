#!/usr/bin/python3
"""Describe unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.test_stdout = StringIO()

# Define a tearDown method that runs after each test case
def tearDown(self):
    # Destroy the console object and close the test stdout object
    self.console = None
    self.test_stdout.close()

# Define a test method for testing an empty line input
@patch('sys.stdout', new_callable=StringIO)
def test_emptyline(self, mock_stdout):
    self.console.onecmd("\n")
    self.assertEqual(mock_stdout.getvalue(), "")

# Define a test method for testing the quit command
@patch('sys.stdout', new_callable=StringIO)
def test_do_quit(self, mock_stdout):
    self.assertTrue(self.console.onecmd("quit"))
    self.assertEqual(mock_stdout.getvalue(), "")

# Define a test method for testing the EOF command
@patch('sys.stdout', new_callable=StringIO)
def test_do_EOF(self, mock_stdout):
    self.assertTrue(self.console.onecmd("EOF"))
    self.assertEqual(mock_stdout.getvalue(), "\n")

# Define a test method for testing the create command with a valid class name
@patch('sys.stdout', new_callable=StringIO)
def test_do_create(self, mock_stdout):
    # Mock the parse function from the console module to return a list with "BaseModel"
    with patch('console.parse', return_value=["BaseModel"]):
        # Pass the create command with "BaseModel" as an argument to the console command method
        self.console.onecmd("create BaseModel")
        obj_dict = storage.all()
        self.assertIn("BaseModel.{}".format(mock_stdout.getvalue().strip()), obj_dict)

# Define a test method for testing the create command with no class name argument
@patch('sys.stdout', new_callable=StringIO)
def test_do_create_missing_class_name(self, mock_stdout):
    # Pass the create command with no argument to the console command method
    self.console.onecmd("create")
    expected_output = "** class name missing **\n"
    self.assertEqual(mock_stdout.getvalue(), expected_output)

# Define a test method for testing the create command with an invalid class name argument
@patch('sys.stdout', new_callable=StringIO)
def test_do_create_invalid_class_name(self, mock_stdout):
    # Pass the create command with "InvalidClass" as an argument to the console command method
    self.console.onecmd("create InvalidClass")
    expected_output = "** class doesn't exist **\n"
    self.assertEqual(mock_stdout.getvalue(), expected_output)

# Define a test method for testing the show command with valid arguments
@patch('sys.stdout', new_callable=StringIO)
def test_do_show(self, mock_stdout):
    # Create an object key as "BaseModel.1234"
    obj = "BaseModel.1234"
    storage.all()[obj] = "test"
    with patch('console.parse', return_value=["BaseModel", "1234"]):
        self.console.onecmd("show BaseModel 1234")
        self.assertEqual(mock_stdout.getvalue(), "test\n")

# Define a test method for testing the show command with no class name argument
@patch('sys.stdout', new_callable=StringIO)
def test_do_show_missing_class_name(self, mock_stdout):
    self.console.onecmd("show")
    expected_output = "** class name missing **\n"
    self.assertEqual(mock_stdout.getvalue(), expected_output)

# Define a test method for testing the show command with an invalid class name argument
@patch('sys.stdout', new_callable=StringIO)
def test_do_show_invalid_class_name(self, mock_stdout):
    # Pass the show command with "InvalidClass" and "1234" as arguments to the console command method
    self.console.onecmd("show InvalidClass 1234")
    expected_output = "** class doesn't exist **\n"
    self.assertEqual(mock_stdout.getvalue(), expected_output)

# Define a test method for testing the show command with no instance id argument
@patch('sys.stdout', new_callable=StringIO)
def test_do_show_missing_instance_id(self, mock_stdout):
    self.console.onecmd("show BaseModel")
    expected_output = "** instance id missing **\n"
    
    self.assertEqual(mock_stdout.getvalue(), expected_output)

# Define a test method for testing the show command with an instance id that does not match any object
@patch('sys.stdout', new_callable=StringIO)
def test_do_show_instance_not_found(self, mock_stdout):
    self.console.onecmd("show BaseModel 1234")
    # Define the expected output as an error message indicating that no instance was found
    expected_output = "** no instance found **\n"
    self.assertEqual(mock_stdout.getvalue(), expected_output)

# Define a test method for testing the destroy command with valid arguments
@patch('sys.stdout', new_callable=StringIO)
def test_do_destroy(self, mock_stdout):
    # Create an object key as "BaseModel.1234"
    obj = "BaseModel.1234"
    storage.all()[obj] = "test"
    with patch('console.parse', return_value=["BaseModel", "1234"]):
        self.console.onecmd("destroy BaseModel 1234")
        obj_dict = storage.all()
        self.assertNotIn("BaseModel.1234", obj_dict)

# Define a test method for testing the destroy command with no class name argument
@patch('sys.stdout', new_callable=StringIO)
def test_do_destroy_missing_class_name(self, mock_stdout):
    self.console.onecmd("destroy")
    expected_output = "** class name missing **\n"
    self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_invalid_class_name(self, mock_stdout):
        self.console.onecmd("destroy InvalidClass 1234")
        expected_output = "** class doesn't exist **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_missing_instance_id(self, mock_stdout):
        self.console.onecmd("destroy BaseModel")
        expected_output = "** instance id missing **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_instance_not_found(self, mock_stdout):
        self.console.onecmd("destroy BaseModel 1234")
        expected_output = "** no instance found **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        obj = "BaseModel.1234"
        storage.all()[obj] = "test"
        with patch('console.parse', return_value=[]):
            self.console.onecmd("all")
            self.assertIn("test", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_with_valid_class(self, mock_stdout):
        obj1 = "BaseModel.1234"
        obj2 = "User.5678"
        storage.all()[obj1] = "test1"
        storage.all()[obj2] = "test2"
        with patch('console.parse', return_value=["BaseModel"]):
            self.console.onecmd("all BaseModel")
            self.assertIn("test1", mock_stdout.getvalue())
            self.assertNotIn("test2", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_missing_class(self, mock_stdout):
        self.console.onecmd("all InvalidClass")
        expected_output = "** class doesn't exist **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        obj1 = "BaseModel.1234"
        obj2 = "User.5678"
        storage.all()[obj1] = "test1"
        storage.all()[obj2] = "test2"
        with patch('console.parse', return_value=["BaseModel"]):
            self.console.onecmd("count BaseModel")
            self.assertEqual(mock_stdout.getvalue(), "1\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count_with_missing_class(self, mock_stdout):
        self.console.onecmd("count InvalidClass")
        expected_output = "** class doesn't exist **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        obj = "BaseModel.1234"
        storage.all()[obj] = "test"
        with patch('console.parse', return_value=["BaseModel", "1234", "name", "John"]):
            self.console.onecmd("update BaseModel 1234 name 'John'")
            updated_obj = storage.all()[obj]
            self.assertIn("name", updated_obj.__dict__)
            self.assertEqual(updated_obj.__dict__["name"], "John")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_class_name(self, mock_stdout):
        self.console.onecmd("update")
        expected_output = "** class name missing **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_invalid_class_name(self, mock_stdout):
        self.console.onecmd("update InvalidClass 1234")
        expected_output = "** class doesn't exist **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_instance_id(self, mock_stdout):
        self.console.onecmd("update BaseModel")
        expected_output = "** instance id missing **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_instance_not_found(self, mock_stdout):
        self.console.onecmd("update BaseModel 1234")
        expected_output = "** no instance found **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_attribute_name(self, mock_stdout):
        obj = "BaseModel.1234"
        storage.all()[obj] = "test"
        self.console.onecmd("update BaseModel 1234")
        expected_output = "** attribute name missing **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_value(self, mock_stdout):
        obj = "BaseModel.1234"
        storage.all()[obj] = "test"
        with patch('console.parse', return_value=["BaseModel", "1234", "name"]):
            self.console.onecmd("update BaseModel 1234 name")
            expected_output = "** value missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_attribute_with_non_dict_value(self, mock_stdout):
        obj = "BaseModel.1234"
        storage.all()[obj] = BaseModel()
        with patch('console.parse', return_value=["BaseModel", "1234", "name", "John"]):
            self.console.onecmd("update BaseModel 1234 name 'John'")
            updated_obj = storage.all()[obj]
            self.assertIn("name", updated_obj.__dict__)
            self.assertEqual(updated_obj.__dict__["name"], "John")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_attribute_with_dict_value(self, mock_stdout):
        obj = "BaseModel.1234"
        storage.all()[obj] = BaseModel()
        with patch('console.parse', return_value=["BaseModel", "1234", "name", "{'first_name': 'John'}"]):
            self.console.onecmd("update BaseModel 1234 name {'first_name': 'John'}")
            updated_obj = storage.all()[obj]
            self.assertIn("name", updated_obj.__dict__)
            self.assertEqual(updated_obj.__dict__["name"], {'first_name': 'John'})

if __name__ == '__main__':
    unittest.main()
