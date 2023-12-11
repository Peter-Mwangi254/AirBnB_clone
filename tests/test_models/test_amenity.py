#!/usr/bin/python3
""" Unittest for Amenity class """
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.amenity1 = Amenity()
        self.amenity1.name = " "

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.amenity1, Amenity)

    def test_attributes(self):
        """Test to check attributes"""
        self.amenity1.save()
        amenity1_json = self.amenity1.to_dict()
        my_new_amenity = Amenity(**amenity1_json)
        self.assertEqual(my_new_amenity.id, self.amenity1.id)
        self.assertEqual(my_new_amenity.created_at, self.amenity1.created_at)
        self.assertEqual(my_new_amenity.updated_at, self.amenity1.updated_at)
        self.assertIsNot(self.amenity1, my_new_amenity)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method"""
        variable_update = self.amenity1.updated_at
        self.amenity1.save()
        self.assertNotEqual(variable_update, self.amenity1.updated_at)
