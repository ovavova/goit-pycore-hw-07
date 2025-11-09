from collections import UserDict
from datetime import datetime
import re
         

class Field:                     # Базовий клас для полів запису
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
class Birthday(Field):                                        # Step 1 - adding Birthday Classes
    def __init__(self, value):
        pattern = r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b'
        if not re.match(pattern, value):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        try:
            date_value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(date_value)


class Name(Field):               # Клас для зберігання імені контакту. Обов'язкове поле.
    def __init__(self, name:str):
         if not name:            # Обов'язкове поле. Перевірка
              raise ValueError("Поле імʼя не може бути порожнім")
         super().__init__(name)

class Phone(Field):              # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, phone_number: str):
         ph = str(phone_number).strip()               # приводимо до єдиного формату
         if len(ph) != 10 or not ph.isdigit():        # check fot 10 and for digits
              raise ValueError("Номер має бути у форматі 10 цифр")
         else:
             super().__init__(ph)
         
    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value     # To be able to compare two phone obj in Record dd change remove phone

# Adding birthday to record with None as defult
class Record:                    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    def __str__(self):
        return f"Name: {self.name} Phone: {self.phones} Birthday: {self.birthday}"   
    
    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            print(f"Такий номер вже є")
         
    def remove_phone(self, phone: Phone):
        self.phones = [p for p in self.phones if p != phone]  # New list withou phone to delete
        print(f"Видалено номер {phone}")

    def edit_phone(self, old_phone:Phone, new_phone:Phone):
        for p in range(len(self.phones)):
            if self.phones[p] == old_phone:
                self.phones[p] = new_phone
                print(f"{old_phone} замінено на {new_phone}")
                break        # заміна першого знайденого
            else:
                print(f"{old_phone} не знайдено")

    def find_phone(self, phone: str):
        phone_obj = Phone(phone)
        for p in self.phones:
            if p == phone_obj:
                return p.value
        return None
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):     # Клас для зберігання та управління записами.

    def add_record(self, record: Record):
          self.data[record.name.value] = record

    def find(self, name_to_find: str):
        return self.data.get(name_to_find)    # To get the record by name
    
    def find_phone(self, phone_to_find: str):  # To find a record by a phone number
        for rec in self:
            if phone in rec.phones:
                return rec
            else:
                return None
               
    def delete(self, name: str):
        record = self.data.pop(name, None)    # Deleting or returning a message of not found
        if record:
            print(f"Запис {name} видалено")
        else:
            print(f"Запис {name} не знайдено")  

def parse_input(user_input):
    """
    Parsing input to a command and arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give a name and a phone please"
        except KeyError:
            return "No such contact"
        except IndexError:
            return "Please provide a name"
    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record.find_phone(old_phone):
        record.edit_phone(old_phone, new_phone)
    else:
        return f"Contact {name} phone {old_phone} - not found"


@input_error
def phone (args, book: AddressBook):    # Returns a contact by Name
    name, *_ = args
    record = book.find(name)
    return record.phones            # returns a list of persons phone numbers


    
    
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Godd bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        elif command in ["help", "?"]:
            print("Place for ReadMe")
        
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))     # Add record

        elif command == "change":
            print(change(args, book))    # Add contact also changes number for a given name
            # реалізація

        elif command == "phone":
            print(phone(args, book))           # Returns a Phone info by name
            # реалізація

        elif command == "all":
            # реалізація
            pass

        elif command == "add-birthday":
            # реалізація
            pass

        elif command == "show-birthday":
            # реалізація
            pass

        elif command == "birthdays":
            # реалізація
            pass

        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()