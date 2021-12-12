class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://opensource-demo.orangehrmlive.com/"

    def find_element(self, by, text):
        return self.driver.find_element(by, text)


    def open_site(self):
        return self.driver.get(self.base_url)