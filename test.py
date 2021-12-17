from OrangePage import OrangeTesting
import time
from random import randint

username = "AlinkaTsaryk" + str(randint(0, 100))
def test_add_user(browser):
    orange_page = OrangeTesting(browser)
    orange_page.open_site()
    orange_page.login("Admin", "admin123")
    orange_page.add_user("ESS", "Joe Root", username, "AlinaTsaryk_26")
    time.sleep(5)
    assert orange_page.check_user(username)

def test_find_user(browser):
    orange_page = OrangeTesting(browser)
    orange_page.find_user(username)
    assert orange_page.check_user(username)
    assert orange_page.check_user("ESS")
    assert orange_page.check_user("Joe Root")
    assert orange_page.check_user("Enabled")
    orange_page.reset()
    assert orange_page.check_user(username)

def test_delete_user(browser):
    orange_page = OrangeTesting(browser)
    orange_page.delete_user(username)
    assert not orange_page.check_user(username)



