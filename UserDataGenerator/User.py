
from datetime import date, datetime




class User :
    def __init__(this,user_id: int, first_name: str, last_name: str, email: str, phone_number: str,
                 date_of_birth: date, address: str, city: str, state: str, country: str, zip_code: str, username: str, password: str,
                 account_created: datetime, is_active: bool):
            this.user_id = user_id
            this.first_name = first_name
            this.last_name = last_name
            this.email = email
            this.phone_number = phone_number
            this.date_of_birth = date_of_birth
            this.address = address
            this.city = city
            this.state = state
            this.country = country
            this.zip_code = zip_code
            this.username = username
            this.password = password
            this.account_created = account_created
            this.is_active = is_active

    def __repr__(self):
        return f"""
   User Information:
     User ID: {self.user_id}
     Name: {self.first_name} {self.last_name}
     Email: {self.email}
     Phone Number: {self.phone_number}
     Date of Birth: {self.date_of_birth}
     Address:
        {self.address}
        {self.city}, {self.state} {self.zip_code}
        {self.country}
     Username: {self.username}
     Account Created: {self.account_created}
     Active: {self.is_active}
   """

    def user_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "date_of_birth": self.date_of_birth,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "zip_code": self.zip_code,
            "username": self.username,
            "password": self.password,
            "account_created": self.account_created,
            "is_active": self.is_active,
        }