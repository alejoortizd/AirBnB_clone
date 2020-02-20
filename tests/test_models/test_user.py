#!/usr/bin/python3
"""
Tests for module of User class
"""
import os
import unittest
import datetime
import models
import models.user
from models.user import User


class TestUser(unittest.TestCase):
    """
    Testing the class.
    """
    def test_instance_no_arg(self):
        msj = "Bad id for User without args"
        my_model1 = User()
        self.assertIsNotNone(my_model1.id, msj)

    def test_instance_arg(self):
        msj = "Bad id for User with args"
        my_model_json = {'id': 'd2f054ed-7125-4417-8416-aea973791d04',
                         'my_number': 89, 'name': 'Holberton',
                         'created_at': datetime.datetime(2020, 2, 19, 19,
                                                         14, 55, 659675),
                         'updated_at': datetime.datetime(2020, 2, 19, 19,
                                                         14, 55, 659675)}
        my_model1 = User(**my_model_json)
        self.assertIsNotNone(my_model1.id, msj)

    def test_no_arg_random(self):
        msj = "Id User no random for created User"
        my_model1 = User()
        my_model2 = User()
        self.assertNotEqual(my_model1.id, my_model2.id, msj)

    def test_no_arg_timestamp(self):
        msj = "Date User bad timestamp"
        my_model1 = User()
        self.assertEqual(my_model1.created_at, my_model1.updated_at, msj)

    def test_id_public(self):
        msj = "Id isn't public"
        my_model1 = User()
        my_model1.id = "HELLO"
        self.assertEqual(my_model1.id, "HELLO")

    def test_name_public(self):
        msj = "Name isn't public"
        my_model1 = User()
        my_model1.name = "Holberton"
        self.assertEqual(my_model1.name, "Holberton")

    def test_my_number_public(self):
        msj = "My_number isn't public"
        my_model1 = User()
        my_model1.my_number = 89
        self.assertEqual(my_model1.my_number, 89)

    def test_first_name_public(self):
        msj = "First_name isn't public"
        my_model1 = User()
        my_model1.first_name = "Betty"
        self.assertEqual(my_model1.first_name, "Betty")

    def test_last_name_public(self):
        msj = "Last_name isn't public"
        my_model1 = User()
        my_model1.last_name = "Holberton"
        self.assertEqual(my_model1.last_name, "Holberton")

    def test_email_public(self):
        msj = "Last_name isn't public"
        my_model1 = User()
        my_model1.email = "airbnb@holbertonshool.com"
        self.assertEqual(my_model1.email, "airbnb@holbertonshool.com")

    def test_password_public(self):
        msj = "Password isn't public"
        my_model1 = User()
        my_model1.password = "root"
        self.assertEqual(my_model1.password, "root")

    def test_id(self):
        '''test if the id of two instances are different'''
        my_model = User()
        my_model1 = User()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''check if my_model is an instance of User'''
        my_model = User()
        self.assertIsInstance(my_model, User)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_model4 = User()
        _dict = my_model4.__dict__
        string1 = "[User] ({}) {}".format(my_model4.id, _dict)
        string2 = str(my_model4)
        self.assertEqual(string1, string2)

    def test_save(self):
        '''check if the attribute updated_at (date) is updated for
        the same object with the current date'''
        my_model2 = User()
        first_updated = my_model2.updated_at
        my_model2.save()
        second_updated = my_model2.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_model3 = User()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'User':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


class TestBase_Model_documentation(unittest.TestCase):
    """
    Testing the documentation
    """
    def test_module_docstring(self):
        """
        Test if modules have docstring
        """
        obj = models.user.__doc__
        msj = "Module does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_class_docstring(self):
        """
        Test if class have docstring
        """
        obj = models.user.User.__doc__
        msj = "Class does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_init_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.user.User.__init__.__doc__
        msj = "Method __init__ does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_str_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.user.User.__str__.__doc__
        msj = "Method __str__ does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_save_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.user.User.save.__doc__
        msj = "Method save does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_to_dict_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.user.User.to_dict.__doc__
        msj = "Method to_dict does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

if __name__ == "__main__":
    unittest.main()
