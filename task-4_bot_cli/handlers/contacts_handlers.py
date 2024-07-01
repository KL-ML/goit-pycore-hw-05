"""A module for working with a list of contacts: adding, editing, outputting, deleting."""
# pylint: disable=line-too-long
from .decorators import add_input_error, change_input_error, show_input_error, del_input_error, empty_contact_list

@add_input_error
def add_contact(args, contacts):
    """Adds a new contact to the contact list.

    Args:
        args (list): contains name and phone number
        contacts (dict): contact list

    Returns:
        str: message that the contact has been added or that it is already in the list
    """
    name, phone = args

    if name in contacts:
        return f"Contact {name} already exists"

    contacts[name] = phone

    return f"Contact added: {name} {phone}"

@change_input_error
@empty_contact_list
def change_contact(args, contacts):
    """Changes a contact's phone number to their name

    Args:
        args (list): contains name and phone number
        contacts (dict): contact list

    Returns:
        str: notification that the contact has been changed, or contact not found
    """
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return f"{name}'s phone changed."

    return f"The {name} is not found"

@show_input_error
@empty_contact_list
def show_phone(args, contacts):
    """Показує інформацію про контакт

    Args:
        args (list): contains name and phone number
        contacts (dict): contact list

    Returns:
        str: a message with information about the contact, or that the contact was not found
    """
    name = args[0]

    if name in contacts:
        number = contacts[name]
        return f"The {name}'s phone is: {number}"

    return f"The {name} is not found"

@empty_contact_list
def show_all(contacts):
    """Shows all contacts in the list

    Args:
        contacts (dict): contact list

    Returns:
        str: message with a list of contacts
    """
    return f"All phone numbers: {contacts}"

@empty_contact_list
@del_input_error
def delete_contact(args, contacts):
    """Function to delete one contact or all at once

    Args:
        args (list): contains name and phone number
        contacts (dict): contact list

    Returns:
        str: message about deleting one or all contacts
    """
    name = args[0]

    if name in contacts:
        del contacts[name]
        return f"The {name} has been deleted"

    if name == "all": # видалити всі контакти
        contacts.clear()
        return "All contacts have been deleted"

    return f"The {name} is not found"
