from faker import Faker

fake = Faker()


def generate_user():
    return {
        "id": fake.random_int(min=1000, max=9999),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "country": fake.country()
    }


if __name__ == "__main__":
    print(generate_user())