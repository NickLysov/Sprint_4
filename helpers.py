from faker import Faker

fake = Faker("ru_RU")


def get_name():
    name = fake.first_name()
    return name


def get_last_name():
    last_name = fake.last_name()
    return last_name


def get_address():
    address = fake.street_address()
    return address


def get_phone_number():
    phone_number = fake.numerify(text='+7%%%%%%%%%%')
    return phone_number