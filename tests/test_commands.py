#!/usr/bin/env python3
import unittest
import tempfile
import os
from unittest.mock import patch
import sys
import uuid
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import commands_alois as commands  # noqa: E402 (Flake8 lint error)


class TestCommands(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for each test
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.temp_filename = self.temp_file.name
        self.temp_file.close()

    def tearDown(self):
        # Clean up the temporary file
        try:
            os.unlink(self.temp_filename)
        except FileNotFoundError:
            pass

    def test_get_tasks_empty_file(self):
        tasks = commands.get_tasks(self.temp_filename)
        self.assertEqual(tasks, [])

    def test_get_tasks_with_data(self):
        # Write test data
        with open(self.temp_filename, 'w') as f:
            f.write("12345678\tTest task 1\n")
            f.write("87654321\tTest task 2\n")

        tasks = commands.get_tasks(self.temp_filename)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['id'], '12345678')
        self.assertEqual(tasks[0]['description'], 'Test task 1')

    @patch('uuid.uuid4')
    def test_add_task(self, mock_uuid):
        mock_uuid.return_value = uuid.UUID('12345678-1234-5678-1234-567812345678')
        commands.add("Test task", self.temp_filename)
        # Check file contents
        with open(self.temp_filename, 'r') as f:
            content = f.read()
        self.assertIn("12345678\tTest task", content)

    def test_modify_existing_task(self):
        # Setup initial data
        with open(self.temp_filename, 'w') as f:
            f.write("12345678\tOriginal task\n")

        commands.modify("12345678", self.temp_filename, "Modified task")

        # Check modification
        tasks = commands.get_tasks(self.temp_filename)
        self.assertEqual(tasks[0]['description'], "Modified task")

    def test_modify_nonexistent_task(self):
        with open(self.temp_filename, 'w') as f:
            f.write("12345678\tTask\n")

        with self.assertRaises(ValueError):
            commands.modify("99999999", self.temp_filename, "New task")

    def test_rm_existing_task(self):
        # Setup initial data
        with open(self.temp_filename, 'w') as f:
            f.write("12345678\tTask to remove\n")
            f.write("87654321\tTask to keep\n")

        commands.rm("12345678", self.temp_filename)

        # Check task was removed
        tasks = commands.get_tasks(self.temp_filename)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['id'], "87654321")

    def test_rm_nonexistent_task(self):
        with open(self.temp_filename, 'w') as f:
            f.write("12345678\tTask\n")

        with self.assertRaises(ValueError):
            commands.rm("99999999", self.temp_filename)


if __name__ == '__main__':
    unittest.main()
