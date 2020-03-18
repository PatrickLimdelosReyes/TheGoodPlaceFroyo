from django.test import TestCase
import unittest
from django.urls import resolve
from selenium import webdriver

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
		
    def test_can_display_ingredients_list(self):
        self.browser.get('http://localhost:8000/froyo/ingredients_list/')
        correct_value = 'Ingredients - List'
        self.assertIn(correct_value, self.browser.title)
        detail = self.browser.find_element_by_tag_name('h1')
        self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

    def test_can_display_all_froyo_pages(self):
        self.fail('Finished the test! Test Successful!')		
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')		