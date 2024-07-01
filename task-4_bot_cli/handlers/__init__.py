"""All working functions of the bot are collected here"""
# pylint: disable=line-too-long
from handlers.parse_input import parse_input
from handlers.contacts_handlers import add_contact, change_contact, show_all, show_phone, delete_contact


__all__ = ["parse_input",  "add_contact", "change_contact", "show_all", "show_phone", "delete_contact"]
