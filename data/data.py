from dataclasses import dataclass
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


@dataclass
class Person:
    full_name: str = faker_ru.first_name(),
    email: str = faker_ru.email(),
    current_address: str = faker_ru.address(),
    permanent_address: str = faker_ru.address()
