"""
Faker package : generaters fake data for you .

"""
import csv
import time

from faker.proxy import Faker

from UserDataGenerator.User import User


fake = Faker()


def generate_user()->User:
    faker = Faker()
    user_id = faker.unique.random_int(min=1000, max=9999)
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    phone_number= faker.phone_number()
    date_of_birth = faker.date_of_birth()
    address = faker.address()
    city = faker.city()
    state = faker.state()
    country = faker.country()
    zip_code = faker.postcode()
    username = faker.user_name()
    password=faker.password()
    account_created=faker.date_time()
    is_active = faker.boolean()
    return User(user_id, first_name, last_name, email, phone_number, date_of_birth,
            address, city, state, country, zip_code, username, password, account_created, is_active)

def generate_users(count: int = 1_000_000)->list[User]:
    users: list[User] = []
    print(f"Generating {count} users...")
    for i in range(count):
        users.append(generate_user())

        if (i + 1) % 10000 == 0:
         print(f"{i + 1} users generated so far...")

    return users

def save_users_csv(users: list[User], file_name: str) -> None:
    fieldnames: list[str] = list(users[0].user_dict().keys())
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow(user.user_dict())











user_count = int(input("Enter the number of users to generate (default is 1,000,000): ") or 1_000_000)
users = generate_users(user_count)

file_name_input = input("Enter the CSV file name (default is 'users.csv'): ")
file_name = file_name_input.strip() if file_name_input.strip() else 'users.csv'
start_time = time.time()
users = generate_users(user_count)
save_users_csv(users, file_name)
end_time = time.time()

print(f"Time taken to generate and save {user_count} users to '{file_name}': {end_time - start_time:.2f} seconds")


