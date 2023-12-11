#!/usr/bin/python3
""" Unittest for BaseModel class """
import unittest
import json
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """SetUp method"""
        self.bm_instance1 = BaseModel()
        self.bm_instance2 = BaseModel()

    def test_base_pep8(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_is_instance(self):
        """Test that instantiation is correct"""
        self.assertIsInstance(self.bm_instance1, BaseModel)
        self.assertIsInstance(self.bm_instance1.created_at, datetime)
        self.assertIsInstance(self.bm_instance1.updated_at, datetime)

    def test_id(self):
        self.assertNotEqual(self.bm_instance1.id, self.bm_instance2.id)
        self.assertTrue(hasattr(self.bm_instance1, "id"))
        self.assertEqual(type(self.bm_instance1.id), str)
        self.assertEqual(type(self.bm_instance2.id), str)

    def test_attributes(self):
        """Test that instantiation is correct"""
        self.bm_instance1.name = "Holberton"
        self.bm_instance1.my_number = 89
        self.bm_instance1.save()
        bm_instance1_json = self.bm_instance1.to_dict()
        self.bm_instance2 = BaseModel(**bm_instance1_json)
        self.assertEqual(self.bm_instance2.id, self.bm_instance1.id)
        self.assertEqual(self.bm_instance2.name, self.bm_instance1.name)
        self.assertEqual(self.bm_instance2.my_number,
                         self.bm_instance1.my_number)
        self.assertEqual(self.bm_instance2.created_at,
                         self.bm_instance1.created_at)
        self.assertEqual(self.bm_instance2.updated_at,
                         self.bm_instance1.updated_at)
        self.assertIsNot(self.bm_instance1, self.bm_instance2)

    def test_string(self):
        """check that it displays the correct string format output"""
        bm_instance1_json = self.bm_instance1.to_dict()
        bm_instance3 = BaseModel(**bm_instance1_json)
        self.assertEqual(bm_instance3.__str__(),
                         "[{}] ({}) {}".format(bm_instance3.__class__.__name__,
                                               bm_instance3.id,
                                               bm_instance3.__dict__))

    def test_save(self):
        """check if update changes"""
        bm_instance1_json = self.bm_instance1.to_dict()
        bm_instance3 = BaseModel(**bm_instance1_json)
        self.bm_instance1.save()
        self.assertEqual(bm_instance3.created_at,
                         self.bm_instance1.created_at)
        self.assertNotEqual(bm_instance3.updated_at,
                            self.bm_instance1.updated_at)

    def test_dictionary(self):
        """check if to_dict module exists in the _ic of the class."""
        self.bm_instance1.name = "to infinity and beyond"
        bm1_dic = self.bm_instance1.to_dict()
        self.assertIsInstance(bm1_dic, dict)
        self.assertEqual(bm1_dic['__class__'], "BaseModel")
        self.assertEqual(bm1_dic["id"], self.bm_instance1.id)
        update_aux = bm1_dic["updated_at"].split("T")
        self.assertEqual(" ".join(update_aux),
                         str(self.bm_instance1.updated_at))
