from dataclasses import dataclass, InitVar
from http import HTTPStatus
from typing import Any


@dataclass
class RequestParameters:
    endpoint: str
    payload: Any
    expected_code: HTTPStatus
    deserialize_to: dataclass
    deserialize: bool


@dataclass
class User:
    name: str = None
    email: str = None
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


@dataclass
class Credentials:
    email: str = None
    password: str = None
    # "PassWord1@"


@dataclass
class Email:
    email: str = None


@dataclass
class CredentialsWithUpdates:
    email: str = None
    password: str = None
    dynamic_field: InitVar[tuple] = None

    def __post_init__(self, dynamic_field: tuple):
        if dynamic_field:
            setattr(self, dynamic_field[0], dynamic_field[1])


@dataclass
class GeneralResponse:
    responseCode: HTTPStatus
    message: str


@dataclass
class UserData:
    id: int
    name: str
    email: str
    title: str
    birth_day: str
    birth_month: str
    birth_year: str
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str


@dataclass
class UserDataResponse:
    responseCode: HTTPStatus
    user: UserData

    def __post_init__(self):
        self.user = UserData(**self.user)
