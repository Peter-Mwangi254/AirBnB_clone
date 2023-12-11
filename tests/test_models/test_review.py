#!/usr/bin/python3
""" Unittest for Review class """
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


class TestReview(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.review1 = Review()
        self.review1.place_id = ""
        self.review1.user_id = ""
        self.review1.text = ""

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Review.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.review1, Review)

    def test_attributes(self):
        """Test to check attributes"""
        self.review1.save()
        review1_json = self.review1.to_dict()
        my_new_review = Review(**review1_json)
        self.assertEqual(my_new_review.id, self.review1.id)
        self.assertEqual(my_new_review.created_at, self.review1.created_at)
        self.assertEqual(my_new_review.updated_at, self.review1.updated_at)
        self.assertIsNot(self.review1, my_new_review)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.review1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method"""
        variable_update = self.review1.updated_at
        self.review1.save()
        self.assertNotEqual(variable_update, self.review1.updated_at)
