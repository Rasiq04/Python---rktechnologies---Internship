def email_slicer(email):
    try:
        # Split the email address into username and domain
        username, domain = email.split('@')
        
        # Remove numbers from the username
        username_without_numbers = ''.join(char for char in username if not char.isdigit())

        return f"Your username is {username_without_numbers} & domain is {domain}"
    except ValueError:
        return "Invalid email address format"

# Example usage
email_address = input("Enter an email address: ")
result = email_slicer(email_address)

# Display output
print(result)
