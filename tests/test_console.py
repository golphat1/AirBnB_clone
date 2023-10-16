#!/usr/bin/python3
# unittest for console

import os
import sys
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()
        self.output = StringIO()

    def tearDown(self):
        self.output.close()

    def test_quit_command(self):
        with patch('sys.stdout', self.output):
            self.assertTrue(self.cmd.onecmd("quit"))

    def test_create_command(self):
        with patch('sys.stdout', self.output):
            self.cmd.onecmd("create BaseModel")
            output = self.output.getvalue().strip()
            self.assertTrue(output)

    def test_show_command(self):
        with patch('sys.stdout', self.output):
            self.cmd.onecmd("show BaseModel")
            output = self.output.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")


if __name__ == '__main__':
    unittest.main()
