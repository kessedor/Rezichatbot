
import requests
from bs4 import BeautifulSoup
import json
import re

# Define global variables
USER_DATA = {}
PROPERTY_LISTINGS = []

# Define helper functions
def send_message(recipient_id, message):
    """
    Sends a message to the specified recipient using the Facebook Messenger API.
    """
    # TODO: Implement Facebook Messenger API integration
    pass

def send_typing_on(recipient_id):
    """
    Sends a typing on indicator to the specified recipient using the Facebook Messenger API.
    """
    # TODO: Implement Facebook Messenger API integration
    pass

def send_typing_off(recipient_id):
    """
    Sends a typing off indicator to the specified recipient using the Facebook Messenger API.
    """
    # TODO: Implement Facebook Messenger API integration
    pass

def scrape_properties(location, budget, property_type):
    """
    Scrapes property listings from various websites and returns a list of properties that match
    the specified location, budget, and property type criteria.
    """
    # TODO: Implement web scraping functionality
    pass

def send_property_listings(recipient_id, property_listings):
    """
    Sends a list of property listings to the specified recipient using the Facebook Messenger API.
    """
    # TODO: Implement Facebook Messenger API integration
    pass

def send_contact_info(recipient_id, phone_number):
    """
    Sends contact information to the specified recipient using the Facebook Messenger API.
    """
    # TODO: Implement Facebook Messenger API integration
    pass

# Define message handlers
def handle_message(recipient_id, message_text):
    """
    Handles an incoming message from the specified recipient.
    """
    # Check if user is already in the system
    if recipient_id not in USER_DATA:
        # If not, add user to system and ask for name
        USER_DATA[recipient_id] = {'name': ''}
        send_typing_on(recipient_id)
        send_message(recipient_id, "Hello! My name is Rezi. What's your name?")
    else:
        # If user is already in the system, process their message based on conversation flow
        user_data = USER_DATA[recipient_id]
        if not user_data['name']:
            # If we don't have the user's name yet, save it and ask for their enquiry
            user_data['name'] = message_text
            send_typing_on(recipient_id)
            send_message(recipient_id, f"Nice to meet you, {user_data['name']}! Are you looking to buy or rent a property in Abuja?")
        elif 'enquiry' not in user_data:
            # If we don't have the user's enquiry yet, save it and ask for additional details
            enquiry = message_text.lower()
            if 'buy' in enquiry:
                user_data['enquiry'] = 'buy'
            elif 'rent' in enquiry:
                user_data['enquiry'] = 'rent'
            else:
                send_typing_on(recipient_id)
                send_message(recipient_id, "I'm sorry, I didn't understand. Are you looking to buy or rent a property in Abuja?")
                return
            send_typing_on(recipient_id)
            send_message(recipient_id, f"Great! What type of property are you interested in, {user_data['name']}? (e")
