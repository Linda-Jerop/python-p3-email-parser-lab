import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string  # Store the string of emails
    
    def parse(self):
        # Split by commas and/or spaces using regex
        parts = re.split(r'[,\s]+', self.email_string)
        
        # Filter to keep only valid email addresses (must contain @)
        emails = [part for part in parts if '@' in part]
        
        # Return unique emails, sorted alphabetically (set removes duplicates)
        return sorted(set(emails))