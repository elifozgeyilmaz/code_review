# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

""" 
def count_valid_emails(emails):
    count = 0

    for email in emails:
        if "@" in email:
            count += 1

    return count


"""
import re

def count_valid_emails(emails):
    count = 0

    if not emails or not isinstance(emails, list):
        return 0

    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
    

    for email in emails:
        if not isinstance(email, str):
            continue
        text = email.strip()
        if not text:
            continue
        if text.count("@") != 1:
            continue
        local, domain = text.split("@")
        if not local or not domain:
            continue
        if "." not in domain:
            continue

        if domain.startswith(".") or domain.endswith("."):
            continue
        if re.match(email_pattern, text):
            count += 1
      

    return count