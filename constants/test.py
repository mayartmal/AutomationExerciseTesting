from http import HTTPStatus


class UserRelated:
    TEST_MAIL_DOMAIN = "@test.tt"
    TEST_USER_BASE_NAME = "user"

class ExpectedCodes:
    CREATED = HTTPStatus.CREATED
    OK = HTTPStatus.OK
    NOT_FOUND = HTTPStatus.NOT_FOUND


class ExpectedMessages:
    USER_CREATED = "User created!"
    USER_EXIST = "User exists!"


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