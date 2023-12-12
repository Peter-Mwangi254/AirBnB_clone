#!/usr/bin/python3
""" Unittest for FileStorage class """
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
import models
classes = {"BaseModel": BaseModel}


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """SetUp method"""
        self.bm_instance = BaseModel()
        self.storage_instance = FileStorage()
        self.user1 = User()

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        print(result.messages)
        self.assertEqual(result.total_errors, 1)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.storage_instance, FileStorage)
        self.assertEqual(type(models.storage).__name__, "FileStorage")
        self.assertEqual(type(self.storage_instance).__name__, "FileStorage")

    def test_file_storage_exist(self):
        """ Checks if methods exists """
        storage_instance = FileStorage()
        self.assertTrue(hasattr(storage_instance, "all"))
        self.assertTrue(hasattr(storage_instance, "new"))
        self.assertTrue(hasattr(storage_instance, "save"))
        self.assertTrue(hasattr(storage_instance, "reload"))

    def test_BaseModel_saveStorage(self):
        """ Checks if the save function works """
        self.bm_instance = BaseModel()
        self.bm_instance.name = "Pinocho"
        self.bm_instance.save()
        models.storage.reload()
        models.storage.all()
        self.assertIsInstance(models.storage.all(), dict)
        self.assertTrue(hasattr(self.bm_instance, 'save'))
        self.assertNotEqual(self.bm_instance.created_at,
                            self.bm_instance.updated_at)

    def test_User_saveStorage(self):
        """ Checks if the save function works """
        self.user1.first_name = "betty"
        self.user1.save()
        models.storage.reload()
        models.storage.all()
        self.assertIsInstance(models.storage.all(), dict)
        self.assertTrue(hasattr(self.user1, 'save'))
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_attributes(self):
        """ tests class attributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertIsInstance(models.storage._FileStorage__objects, dict)
        self.assertIsInstance(models.storage._FileStorage__file_path, str)

    def test_no_arguments(self):
        """ tests initialization without arguments  """
        with self.assertRaises(TypeError) as error:
            FileStorage.__init__()
            fail = "descriptor '__init__' of 'object' object needs an argument"
            self.assertEqual(str(error.exception), fail)

    def test_arguments(self):
        """ tests __init__ with many arguments"""
        with self.assertRaises(TypeError) as error:
            base = FileStorage(7, 12)
        fail = "FileStorage() takes no arguments"
        self.assertEqual(str(error.exception), fail)

    def test_all_dict_returned(self):
        """test the method all when returns dict"""
        file = FileStorage()
        dicto = file.all()
        self.assertIs(dicto, file._FileStorage__objects)
        self.assertEqual(type(dicto), dict)

    def test_new(self):
        """test the method new at the creation of new object"""
        file = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                file.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, file._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        file = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        file.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            file_content = f.read()

    def test_base_pep8_conformance_file_storage(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['/models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 1)

    def test_base_pep8_conformance_filesto_test(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            '/tests/test_models/test_engine/test_file_storageconsole.py'])
        self.assertEqual(result.total_errors, 1)
