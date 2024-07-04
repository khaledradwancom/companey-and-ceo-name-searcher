import requests
from bs4 import BeautifulSoup
import re

def get_contacts_from_website(url):
    try:
        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all the text from the page
        text = soup.get_text()

        # Regular expressions to find email addresses and phone numbers
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
        phone_pattern = r'\+?\d[\d -]{8,}\d'

        emails = re.findall(email_pattern, text)
        phone_numbers = re.findall(phone_pattern, text)

        # Remove duplicates by converting the lists to sets
        emails = list(set(emails))
        phone_numbers = list(set(phone_numbers))

        return emails, phone_numbers

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return [], []

# Example usage
url = 'https://www.instagram.com/mohamed.radwanofficial/?hl=ar'  # Replace with the URL of the website you want to search
emails, phone_numbers = get_contacts_from_website(url)
print("Found emails:", emails)
print("Found phone numbers:", phone_numbers)
