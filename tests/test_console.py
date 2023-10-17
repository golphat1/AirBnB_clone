#!/usr/binpython3
import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        sel.test_stdout = StringIO()

    def tearDown(self):
        '''Destroys the console object and close the test stdout object'''
        self.console = None
        self.test_stdout.close()

    def test_do_quit(self):
        '''Define a test method for testing the quit command'''
        with patch('sys.stdout', new_callable=StringIO):
            self.assertTrue(self.console.onecmd("quit"))
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_EOF(self):
        '''Define a test method for testing the EOF command'''
        with patch('sys.stdout', new_callable=StringIO):
            self.assertTrue(self.console.onecmd("EOF"))
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_emptyline(self):
        '''Define a test method for testing an empty line input'''
        with patch('sys.stdout', new_callable=StringIO):
            self.console.emptyline()
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_create(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("create BaseModel")
            output = sys.stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_do_create_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("create")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_create_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("create InvalidClass")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


class TestHBNBCommandShow(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_show_success(self):
        with patch('sys.stdout', new_callable=StringIO):
            obj = BaseModel
            obj.save()
            obj_id = obj.id
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = sys.stdout.getvalue().strip()
            expected_output = str(obj)
            self.assertEqual(output, expected_output)

    def test_show_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("show")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("show InvalidClass 12345")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_missing_instance_id(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("show BaeModel")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_nonexistent_instance(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("show BaseModel 12345")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


class TestHBNBCommandDestroyAll(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_destroy_success(self):
        with patch('sys.stdout', new_callable=StringIO):
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "")
            self.assertIsNone(storage.get(BaseModel, obj_id))

    def test_destroy_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("destroy")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("destroy InvalidClass 12345")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_missing_instance_id(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("destroy BaseModel")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_nonexistent_instance(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("destroy BaseModel 12345")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all_success(self):
        with patch('sys.stdout', new_callable=StringIO):
            obj1 = BaseModel()
            obj2 = BaseModel()
            obj1.save()
            obj2.save()
            self.console.onecmd("all BaseModel")
            output = sys.stdout.getvalue().strip()
            self.assertIn(str(obj1), output)
            self.assertIn(str(obj2), output)

    def test_all_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("all")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_all_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("all InvalidClass")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


class TestHBNBCommandAll(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_all_success(self):
        with patch('sys.stdout', new_callable=StringIO):
            obj1 = BaseModel()
            obj2 = BaseModel()
            obj1.save()
            obj2.save()
            self.console.onecmd(f"BaseModel")
            output = sys.stdout.getvalue().strip()
            self.assertIn(str(obj1), output)
            self.assertIn(str(obj2), output)

    def test_all_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("all")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_all_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("all InvalidClass")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


class TestHBNBCommandCount(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_count_success(self):
        with patch('sys.stdout', new_callable=StringIO):
            obj1 = BaseModel()
            obj2 = BaseModel()
            obj3 = User()
            obj1.save()
            obj2.save()
            obj3.save()
            self.console.onecmd(f"count BaseModel")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "2")

    def test_count_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("count")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_count_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("count InvalidClass")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


class TestHBNBCommandUpdate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_update_success(self):
        with patch('sys.stdout', new_callable=StringIO):
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd(f"update BaseModel {obj_id} dict")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_update_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("update")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("update InvalidClass 12345 dict")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_instance_id(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("BaseModel")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_invalid_attribute_dictionary(self):
        with patch('sys.stdout', new_callable=StringIO):
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd(f"update BaseModel {obj_id} not_a_dict")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** invalid attribute dictionary **")

    def test_update_nonexistent_instance(self):
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("update BaseModel 12345 dict")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_invalid_attribute_name(self):
        with patch('sys.stdout', new_callable=StringIO):
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd(f"update BaseModel {obj_id}
                                {'{"invalid_attr": "value"}'}")
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name doesn't exist **")


if __name__ == "__main__":
    unittest.main()
