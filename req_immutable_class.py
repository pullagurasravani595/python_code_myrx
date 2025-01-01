from dataclasses import dataclass
from datetime import date
from typing import List, Any

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    pin_code: str

@dataclass(frozen=True)
class ImmutableEmployee:
    name: str
    id: str
    date_of_joining: date
    addresses: List[Address]

# Example usage
if __name__ == "__main__":
    address1 = Address(street="Ameerpet", city="Hyderabad", state="Telangana", pin_code="62701")
    address2 = Address(street="Suchitra", city="chennai", state="Tamilnadu", pin_code="62565")

    employee = ImmutableEmployee(
        name="John Doe",
        id="E12345",
        date_of_joining=date(2020, 5, 15),
        addresses=(address1, address2)
    )

    print(employee)

 

class Employee:
  
    def __init__(self, name, id, date_of_joining, street, city, state, pin_code):
       self.name = name
       self.id = id
       self.deal_price = date_of_joining
       self.street = street
       self.city = city 
       self.state = state 
       self.pin_code = pin_code
    def make_address_list(self, address):
       self.address = []
       self.address.append(self.street)
       self.address.append(self.city)
       self.address.append(self.state)
       self.address.append(self.pin_code)
       return self.address


employee_details = Employee("suchitra","1", "2020, 5, 15", "Ameerpet", "Hyderabad", "Telangana", "516360")
employee.make_address_list([])

print(employee_details)
