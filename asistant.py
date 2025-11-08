from collections import UserDict
import re

# Step 1 - adding Birthday Classes
class Birthday(value):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних DD.MM.YYYY
            pattern = r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b'
            self.birthday = datetime.strptime(d, "%d.%m.%Y")  # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    


# Adding birthday to record with None as defult
class Record:                    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

class Field:                     # Базовий клас для полів запису
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

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
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):     # Клас для зберігання та управління записами.

    def add_record(self, record: Record):
          self.data[record.name.value] = record

    def find(self, name_to_find: str):
        return self.data.get(name_to_find)    # To get the record by name
               
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
            print("Place for ReadMe"
        
                elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # реалізація

        elif command == "change":
            # реалізація

        elif command == "phone":
            # реалізація

        elif command == "all":
            # реалізація

        elif command == "add-birthday":
            # реалізація

        elif command == "show-birthday":
            # реалізація

        elif command == "birthdays":
            # реалізація

        else:
            print("Invalid command.")
        

if __name__ = "__main__":
    main()