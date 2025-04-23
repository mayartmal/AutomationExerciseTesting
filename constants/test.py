from http import HTTPStatus

from api_services.brand_service import BrandService
from api_services.product_service import ProductService
from models.common import Credentials, User, Email


class Common:
    NEW_COMPANY = ["company", "new_work"]
    BAD_PASSWORD = "bad_password"


class UserRelated:
    TEST_MAIL_DOMAIN = "@test.tt"
    TEST_USER_BASE_NAME = "user"


class BrandRelated:
    WRONG_METHODS_FOR_GET_ALL_BRANDS = [
        {"service_class": BrandService, "method": "POST"},
        {"service_class": BrandService, "method": "PUT"},
        {"service_class": BrandService, "method": "DELETE"}
    ]


class ProductRelated:
    WRONG_METHODS_FOR_GET_ALL_PRODUCTS = [
        {"service_class": ProductService, "method": "POST"},
        {"service_class": ProductService, "method": "PUT"},
        {"service_class": ProductService, "method": "DELETE"}
    ]
    TSHIRT_STRINGS_IN_DIFFERENT_CASES = [
        "tshirt",
        "Tshirt",
        "TSHIRT",
        "TsHiRt"
    ]


class ExpectedCodes:
    CREATED = HTTPStatus.CREATED
    OK = HTTPStatus.OK
    NOT_FOUND = HTTPStatus.NOT_FOUND
    BAD_REQUEST = HTTPStatus.BAD_REQUEST
    UNSUPPORTED_METHOD = HTTPStatus.METHOD_NOT_ALLOWED


class ExpectedMessages:
    USER_CREATED = "User created!"
    USER_EXIST = "User exists!"
    USER_NOT_FOUND = "User not found!"
    BAD_VERIFY_REQUEST = "Bad request, email or password parameter is missing in POST request."
    UNSUPPORTED_METHOD = "This request method is not supported."
    MISSING_SEARCH_PARAMETER = "Bad request, search_product parameter is missing in POST request."


class Payloads:
    USER_VITUS_BERING = User(name="vitus_bering",
                             email="vitus_bering@kostava43.ge",
                             password="PassWord1@",
                             title="Mr",
                             birth_date="12",
                             birth_month="8",
                             birth_year="1981",
                             firstname="Vitus",
                             lastname="Bering",
                             company="UCS",
                             address1="owl st. 11",
                             address2="far st. 27",
                             country="India",
                             zipcode="0111",
                             state="ND",
                             city="ND",
                             mobile_number="555 111 333")

    VALID_VITUS_BERING_CREDENTIALS = Credentials(email="vitus_bering@kostava43.ge",
                                                 password="PassWord1@")

    WRONG_PASSWORD_VITUS_BERING_CREDENTIALS = Credentials(email="vitus_bering@kostava43.ge",
                                                          password="wrong_password")

    EMAIL_VITUS_BERING = Email(email="vitus_bering@kostava43.ge")

# region obsolete

# SESSION_ID_COOKIE = {
#         'domain': 'www.automationexercise.com',
#         'expiry': 1744704757,
#         'httpOnly': True,
#         'name': 'sessionid',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': False,
#         'value': 'c2hjz6zydhvs0mj06rlmpe63u39iomch'
# }
# ALL_SAVED_COOKIES = [
#     {
#         'domain': '.automationexercise.com',
#         'expiry': 1775031159,
#         'httpOnly': False,
#         'name': 'FCNEC',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': False,
#         'value': '%5B%5B%22AKsRol_TS2ASVYN6TVW5X_WoeaWmKuT6S0OBfwLyYG-lJxElPP48HhNrBv46DIvIai1hbqEuBuNXxO3Lz4uYL_nnCrykP6TqCvVsLxKyDajQ0U62_FyNDatXVnnPBg8gDbCBkyGonyJo2TbnuGItYj80nhqOyhukwg%3D%3D%22%5D%5D'
#     },
#     {
#         'domain': 'www.automationexercise.com',
#         'expiry': 1744704757,
#         'httpOnly': True,
#         'name': 'sessionid',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': False,
#         'value': 'c2hjz6zydhvs0mj06rlmpe63u39iomch'
#     },
#     {
#         'domain': '.automationexercise.com',
#         'expiry': 1777191148,
#         'httpOnly': False,
#         'name': '__gads',
#         'path': '/',
#         'sameSite': 'None',
#         'secure': True,
#         'value': 'ID=55f59fa186ad4e01:T=1743495148:RT=1743495148:S=ALNI_MZzkfojAYuaTQ-3pRQo3ngqlen_fQ'
#     },
#     {
#         'domain': '.automationexercise.com',
#         'expiry': 1759047148,
#         'httpOnly': False,
#         'name': '__eoi',
#         'path': '/',
#         'sameSite': 'None',
#         'secure': True,
#         'value': 'ID=14cee8b3e0a2527a:T=1743495148:RT=1743495148:S=AA-AfjZJGbfvsL-DDWnhX2k7tiJT'
#     },
#     {
#         'domain': '.automationexercise.com',
#         'expiry': 1777191148,
#         'httpOnly': False,
#         'name': '__gpi',
#         'path': '/',
#         'sameSite': 'None',
#         'secure': True,
#         'value': 'UID=00001078311175ad:T=1743495148:RT=1743495148:S=ALNI_Mb_RHgLpN9DMX-yLa35-mxfT_hitw'
#     },
#     {
#         'domain': 'www.automationexercise.com',
#         'expiry': 1774944757,
#         'httpOnly': False,
#         'name': 'csrftoken',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': False,
#         'value': 'wRZhkm4DcgBm8a2Fb7IWnwqNVYHRoz9JqXCcOXdRSlkIMLzWf0sTt8RCdejMHj9l'
#     }
# ]
# endregion
