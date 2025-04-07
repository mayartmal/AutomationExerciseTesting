import random
from datetime import datetime


def generate_random_number(min_value: int, max_value: int):
    return random.randint(min_value, max_value)

def choose_items(list_of_items: list, number_of_items_to_choose: int):
    return random.choices(list_of_items, k=number_of_items_to_choose)

def generate_user_name_with_time_postfix(base_name: str="empty"):
    return f"{base_name}{generate_current_datetime_string()}"

def generate_current_datetime_string():
    return datetime.now().strftime("%d%m%Y%H%M%S")



