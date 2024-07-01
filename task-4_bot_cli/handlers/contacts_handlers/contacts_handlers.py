from ..decorators.decorators import add_input_error, change_input_error, show_input_error, del_input_error, empty_contact_list

@add_input_error
def add_contact(args, contacts): # приймає два аргументи: args, який є списком і містить ім'я та телефонний номер, та contacts, який є словником, де зберігаються контакти
    name, phone = args # два елементи зі списку args розпаковуються в змінні name та phone
    if name in contacts:
        return f"Contact {name} already exists"
    contacts[name] = phone # додає пару "ключ: значення" до словника контактів, використовуючи ім'я як ключ і телефонний номер як значення contacts[name] = phone.
    return f"Contact added: {name} {phone}"

@change_input_error
@empty_contact_list
def change_contact(args, contacts): # Змінити контакт 
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"{name}'s phone changed."
    return f"The {name} is not found"

@show_input_error
@empty_contact_list
def show_phone(args, contacts): # Показати номер
    name = args[0]
    if name in contacts:
        number = contacts[name]
        return f"The {name}'s phone is: {number}"
    return f"The {name} is not found"

@empty_contact_list
def show_all(contacts): # показати всі контакти в списку
    return f"All phone numbers: {contacts}"

@empty_contact_list
@del_input_error
def delete_contact(args, contacts): # видалити контакт
    name = args[0]
    if name in contacts:
        del contacts[name]
        return f"The {name} has been deleted"
    elif name == "all": # видалити всі контакти
        contacts.clear()
        return "All contacts have been deleted"
    return f"The {name} is not found"
