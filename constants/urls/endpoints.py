class Endpoints:
    #  как хранить base url? в applications или в endpoints?
    BASE_URL = "https://automationexercise.com"

    # region User
    USER_CREATE_ACCOUNT = "/api/createAccount"
    USER_VERIFY = "/api/verifyLogin"
    USER_DELETE = "/api/deleteAccount"
    USER_GET_DETAILS = "/api/getUserDetailByEmail"
    USER_UPDATE_DETAILS = "/api/updateAccount"
    # endregion

    # region Brand
    BRAND_GET_LIST = "/api/brandsList"
    # endregion

    # region Products
    PRODUCT_GET_LIST = "/api/productsList"
    PRODUCT_SEARCH = "/api/searchProduct"
    # endregion
