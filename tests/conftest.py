import pytest
from selenium import webdriver

from api_services.base_service import BaseService
from api_services.brand_service import BrandService
from api_services.product_service import ProductService
from api_services.user_service import UserService
from constants.applications import AUTOMATION_EXERCISE
from constants.test import ExpectedCodes
from page_objects.browser_wrapper import BrowserWrapper
from page_objects.common_page import CommonPage
from page_objects.home_page import HomePage
from utils.logger_config import get_logger

# region API tests

logger = get_logger(__name__)


@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    test_name = request.node.name
    # print()
    logger.info(f"\n====================== START TEST: {test_name} ======================")
    yield
    logger.info(f"\n======================= END TEST: {test_name} =======================")


@pytest.fixture
def user_service():
    return UserService()


@pytest.fixture
def brand_service():
    return BrandService()


@pytest.fixture
def product_service():
    return ProductService()


@pytest.fixture()
def base_service():
    return BaseService()


@pytest.fixture
def create_and_clean_up_user(request, user_service):
    user = request.param if hasattr(request, "param") else None
    response, user = user_service.create_user(user=user)
    assert response.responseCode == ExpectedCodes.CREATED
    yield response, user
    print()
    user_service.delete_user(user)
    response = user_service.verify_user(user)
    logger.debug(
        f" ASSERT Actual response code: {response.responseCode} vs Expected response code: {ExpectedCodes.NOT_FOUND}")


@pytest.fixture
def run_service_with_overridden_method(request):
    service_class = request.param['service_class']
    service = service_class()
    service.override_method_to(request.param['method'])
    yield service
    service.reset_method()


@pytest.fixture
def product_searching(request, product_service):
    return product_service.search_product(request.param), request.param


@pytest.fixture()
def update_user_data(request, create_and_clean_up_user, user_service):
    _, user = create_and_clean_up_user
    response = user_service.update_user_details(user=user,
                                                field_to_update=request.param[0],
                                                field_new_value=request.param[1])
    assert response.responseCode == ExpectedCodes.OK
    return response, user


# region UI (POM) tests
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
# endregion
