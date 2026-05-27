import random
from faker import Faker

fake = Faker()

def generate_user():
    return {
        "id": random.randint(1000, 9999),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email()
    }