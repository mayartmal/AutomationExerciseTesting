from pickle import FALSE

import pytest
from selenium import webdriver

from api_services.user_service import UserService
from constants.applications import AUTOMATION_EXERCISE
from page_objects.browser_wrapper import BrowserWrapper
from page_objects.common_page import CommonPage
# from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage
# from page_objects.item_page import ItemPage





@pytest.fixture
def user_service():
    return UserService()




# @pytest.fixture(scope="session", autouse=True)
@pytest.fixture(scope="function", autouse=False)
def init(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
    driver.get(AUTOMATION_EXERCISE)
    driver.delete_all_cookies()
    BrowserWrapper.driver = driver
    yield
    driver.quit()

@pytest.fixture
def abstract_page():
    return CommonPage()


@pytest.fixture
def home_page():
    return HomePage()

# @pytest.fixture
# def cart_page():
#     return CartPage()
#
# @pytest.fixture
# def item_page():
#     return ItemPage()


@pytest.fixture
def prepare_home_page(home_page):
    home_page.clear_browser()
    home_page.close_cookie_dialog()


@pytest.fixture
def add_books_to_cart(request, prepare_home_page, home_page, cart_page):
    home_page.add_books_to_cart(book_adder=request.param)
    return request.param


@pytest.fixture
def switch_to_cart(request, home_page):
    if request.param == "new tab":
        home_page.go_to_cart_in_a_new_tab()
    elif request.param == "current tab":
        home_page.go_to_cart()
    else:
        home_page.go_to_cart()
