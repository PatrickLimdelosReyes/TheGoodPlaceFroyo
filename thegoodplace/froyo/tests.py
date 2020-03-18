from django.test import TestCase
import unittest
from django.urls import resolve
from selenium import webdriver

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()