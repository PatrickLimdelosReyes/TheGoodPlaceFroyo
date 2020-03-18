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
	
	def test_can_display_ingredients_detail(self):
		self.browser.get('http://localhost:8000/froyo/ingredients_detail/')
		correct_value = 'Ingredients - Detail'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_ingredients_create_form(self):	
		self.browser.get('http://localhost:8000/froyo/ingredients_create_form/')
		correct_value = 'Ingredients - Create'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_ingredients_update_form(self):	
		self.browser.get('http://localhost:8000/froyo/ingredients_update_form/')
		correct_value = 'Ingredients - Update'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_orders_list(self):	
		self.browser.get('http://localhost:8000/froyo/orders_list/')
		correct_value = 'Orders - List'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_orders_detail(self):		
		self.browser.get('http://localhost:8000/froyo/orders_detail/')
		correct_value = 'Orders - Detail'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_orders_create_form(self):		
		self.browser.get('http://localhost:8000/froyo/orders_create_form/')
		correct_value = 'Orders - Create'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_orders_update_form(self):		
		self.browser.get('http://localhost:8000/froyo/orders_update_form/')
		correct_value = 'Orders - Update'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_recipes_list(self):		
		self.browser.get('http://localhost:8000/froyo/recipes_list/')
		correct_value = 'Recipes - List'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_recipes_detail(self):		
		self.browser.get('http://localhost:8000/froyo/recipes_detail/')
		correct_value = 'Recipes - Detail'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_recipes_create_form(self):		
		self.browser.get('http://localhost:8000/froyo/recipes_create_form/')
		correct_value = 'Recipes - Create'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

	def test_can_display_recipes_update_form(self):		
		self.browser.get('http://localhost:8000/froyo/recipes_update_form/')
		correct_value = 'Recipes - Update'
		self.assertIn(correct_value, self.browser.title)
		detail = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(detail.get_attribute('innerHTML'), correct_value)

		
	def test_can_display_all_froyo_pages(self):
		self.fail('Finished the test! Test Successful!')		
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')		
