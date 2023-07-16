import time

from page_objects.RegisterPage import RegisterPage
from faker import Faker


def fake_user() -> list:
    fake_list = [Faker().name().split()[0], Faker().name().split()[1], Faker().email(), fake_phone_number(Faker()),
                 Faker().password(length=10)]
    return fake_list


def fake_phone_number(fake: Faker) -> str:
    return f'+91{fake.msisdn()[3:]}'


def test_register_user(browser):
    RegisterPage(browser).alert_accept()
    time.sleep(1)
    RegisterPage(browser).register(*fake_user())
    assert RegisterPage(browser).validate_register()
