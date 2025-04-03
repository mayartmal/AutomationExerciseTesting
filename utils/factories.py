from dataclasses import dataclass
from utils.data_generator import generate_current_datetime_string


@dataclass
class User:
    name: str
    email: str
    password: str = "12345678"
    title: str = "Mr"
    birth_date: str = "3"
    birth_month: str = "2"
    birth_year: str = "1990"
    firstname: str = "John"
    lastname: str = "Smitty"
    company: str = "APEX"
    address1: str = "owl st. 11"
    address2: str = "far st. 27"
    country: str = "India"
    zipcode: str = "0111"
    state: str = "ND"
    city: str = "ND"
    mobile_number: str = "555 111 333"

    @staticmethod
    def generate():
        user = "user" + generate_current_datetime_string()
        email = user + "@testhost.tt"
        return User(name=user, email=email)

    def credentials(self):
        return {
            "email": self.email,
            "password": self.password,
        }

    def mail(self):
        return {
            "email": self.email,
            "password": self.password,
        }

@dataclass
class UniversalResponseData:
    user: User
    message: str
    code: int
    raw_response: dict

    @staticmethod
    def build(user, response):
        message = response.json().get("message")
        code = response.json().get("responseCode")
        raw_response = response.json()
        return UniversalResponseData(user=user, message=message, code=code, raw_response=raw_response)


