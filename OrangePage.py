from BaseApp import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
class OrangeTesting(BasePage):

    def login(self, login, password):
        self.find_element(By.NAME, "txtUsername").send_keys(login)
        field = self.find_element(By.NAME, "txtPassword")
        field.send_keys(password)
        field.send_keys(Keys.RETURN)

    def add_user(self, role, empl, username, password):
        self.find_element(By.ID, "menu_admin_viewAdminModule").click()
        self.find_element(By.ID, "btnAdd").click()
        Select(self.find_element(By.ID, "systemUser_userType")).select_by_visible_text(role)
        self.find_element(By.ID, "systemUser_employeeName_empName").send_keys(empl)
        self.find_element(By.ID, "systemUser_userName").send_keys(username)
        self.find_element(By.ID, "systemUser_password").send_keys(password)
        self.find_element(By.ID, "systemUser_confirmPassword").send_keys(password)
        time.sleep(5)
        self.find_element(By.ID, "btnSave").click()


    def check_user(self, username):
        return username in self.driver.page_source

    def check_del_user(self, username):
        return username not in self.driver.page_source

    def find_user(self, username):
        self.find_element(By.NAME, "searchSystemUser[userName]").send_keys(username)
        self.find_element(By.ID, "searchBtn").click()

    def reset(self):
        self.find_element(By.ID, "resetBtn").click()

    def delete_user(self, username):
        href = self.find_element(By.LINK_TEXT, username).get_attribute('href')
        value = ''.join(list(filter(str.isdigit, href)))
        self.find_user(username)
        self.find_element(By.ID, "ohrmList_chkSelectRecord_" + value).click()
        self.find_element(By.ID, "btnDelete").click()
        self.find_element(By.ID, "dialogDeleteBtn").click()