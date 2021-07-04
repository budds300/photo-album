from django.test import TestCase
from .models import Image, Location, Category
import datetime as dt

class ImageTestClass(TestCase):
    def setUp(self):
        
        self.location = Location(location='bedroom')
        self.location.save_location()

        self.category = Category(category='Real')
        self.category.save_category()

        self.coolpic = Image(id=1, image_name='image', image_description='ya fao really', location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.coolpic, Image))

    def test_save_image(self):
        self.coolpic.save_image()
        pics = Image.objects.all()
        self.assertTrue(len(pics) > 0)

    def test_delete_image(self):
        self.coolpic.delete_image()
        pics = Image.objects.all()
        self.assertTrue(len(pics) == 0)

   
class CategoryTestClass(TestCase):
    def setUp(self):
        self.fiction= Category(category='fiction')

    def test_instance(self):
        self.assertTrue(isinstance(self.fiction,Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_delete_category(self):
        self.fiction.delete_category('fiction')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

class LocationTestClass(TestCase):

    def setUp(self):
        self.africa= Location(location='africa')

    def test_instance(self):
        self.assertTrue(isinstance(self.africa,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_delete_location(self):
        self.africa.delete_location('africa')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)