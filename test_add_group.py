# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.open_home_page()
        self.login()
        self.open_group_page()
        self.init_group_creation()
        self.fill_group_form()
        self.submit_group_creation()

    def submit_group_creation(self):
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.LINK_TEXT, "group page").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def fill_group_form(self):
        # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys("dfgechrthb")
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.execute_script("window.scrollTo(0,211.1999969482422)")
        self.driver.find_element(By.NAME, "group_header").send_keys("dgdmcuhrbg")
        self.driver.find_element(By.NAME, "group_footer").send_keys("dfjcjdufhgbe")

    def init_group_creation(self):
        # init group creation
        self.driver.find_element(By.NAME, "new").click()

    def open_group_page(self):
        # open group page
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self):
        self.driver.find_element(By.NAME, "user").send_keys("admin")
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys("secret")

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
