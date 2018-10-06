from selenium import webdriver
import unittest
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class HomeNewVisitorTest(StaticLiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("Taskbuster", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        header = self.browser.find_element_by_id("header")
        self.assertEqual(header.value_of_css_property("background-color"),"rgba(0, 0, 0, 1)")
