from selenium import webdriver
import unittest
 
 
class NewVisitorTest(unittest.TestCase):
 
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
        
    def tearDown(self):
        self.browser.quit()
 
    def test_it_worked(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Django Taskbuster', self.browser.title)
 
if __name__ == '__main__':
    unittest.main(warnings='ignore')