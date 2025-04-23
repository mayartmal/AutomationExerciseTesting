# from constants.test import HOME_PAGE_TITLE, ALL_SAVED_COOKIES, SESSION_ID_COOKIE
# from selenium import webdriver
#
# def test_home_page_can_be_opened(home_page):
#     assert home_page.get_opened_page_tab_name() == HOME_PAGE_TITLE
#
#
# def test_get_cookies(home_page):
#     import time
#     time.sleep(30)
#     cookies = home_page.driver.get_cookies()
#     print(cookies)
#
# def test_add_cookies(home_page):
#     # for cookie in ALL_SAVED_COOKIES:
#     #     home_page.driver.add_cookie(cookie)
#
#     # with requests
#     # response = requests.get(url, cookies=cookies)
#
#     # move to base page
#     home_page.driver.add_cookie(SESSION_ID_COOKIE)
#     home_page.driver.refresh()
#     import time
#     time.sleep(30)
#
