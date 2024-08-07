"""Decorators that handle input errors are collected here."""

def add_input_error(func):
    """handles a missing argument error for add_contact()

    Args:
        func (callable): add_contact()
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Arguments are required. Print 'add username 123456', \
where username is contact's name, and 12345 is contacts phone number."
    return inner

def change_input_error(func):
    """handles a missing argument error for change_contact()

    Args:
        func (callable): change_contact()
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Arguments are required. Print 'change username 123456', \
where username is contact's name, and 12345 is contacts phone number."
    return inner

def show_input_error(func):
    """handles a missing argument error for show_phone()

    Args:
        func (callable): show_phone()
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Argument is required. Print 'phone username', \
where username is contact's name."
    return inner

def del_input_error(func):
    """handles a missing argument error for delete_contact()

    Args:
        func (callable): delete_contact()
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Argument is required. Print 'delete all', or 'delete username'."
    return inner

def empty_contact_list(func):
    """handles an empty contact list error

    Args:
        func (callable): any function that depends on the fullness of the contact list
    """
    def inner(*args, **kwargs):
        if len(args) <= 1:
            if len(args[0]) == 0:
                return "The contacts list is empty. \
Print 'add username 123456' to add your first contact."
        elif len(args) > 1:
            if len(args[1]) == 0:
                return "The contacts list is empty. \
Print 'add username 123456' to add your first contact."
        return func(*args, **kwargs)
    return inner
