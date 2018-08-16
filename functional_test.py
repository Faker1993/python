from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('TO-DO',self.driver.title)
        self.fail('Finish the test!')

if __name__ == "__main__":
    unittest.main(warnings='ignore')