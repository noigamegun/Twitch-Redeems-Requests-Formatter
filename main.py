from pathlib import Path
import random
import string
import json
import re

welcome_message = """Welcome to Twitch-Redeems-Requests-Formatter!
This program will format your Twitch Redeems Requests in a way that you can easily copy and paste them into DevTools console for spamming.
You can use this program to spam your favorite streamer with your favorite redeems!
Instructions:
    1. Open the network tab in DevTools and filter by "gql.twitch" to find the request.
    2. Clear the Network tab.
    3. Redeem the redeem you want to spam.
    4. Copy the request as fetch.
    5. Paste the request in input-fetch.txt.
    6. Run this program.
    7. The formatted request will be in output-fetch.txt.
    8. Copy the formatted request and paste it in the DevTools console.
    9. Spam the request by pressing Up,Enter multiple times."""

print(welcome_message)
print()
input("Press Enter to continue...")

print()
while True:
    try:
        input = Path("input-fetch.txt")
        if input.exists():
            print("File found successfully!")
            break
        else:
            quit(1)
    except Exception as e:
        print()
        print("ERROR : Failed to open file")
        print("Make sure you have a file named input-fetch.txt in the same directory as this program")
        print(str(e))
        print()
        input("Press Enter to retry...")

print("Reading file and formating (Step 1)...")

while True:
    try:
        name = str(random.randint(1,999999999))+'.txt'
        with open('input-fetch.txt', 'r') as file:
            lines = file.readlines()
        with open(name, 'w') as file:
            for line in lines:
                if '"credentials": "include"' not in line:
                    file.write(line)
            break
    except Exception as e:
        print()
        print('ERROR : Failed to format file ("credentials": "include")')
        print(str(e))
        print()
        print("Stopping program now to prevent any further damages to your system.")
        exit(1)

print("File step 1 formmatted successfully!")
print("Reading file and formating (Step 2)...")
while True:
    try:
        # Generate a random string of 31 alphanumeric characters
        new_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=31))

        with open(name, 'r') as file:
            input_string = file.read()

        # Replace the transactionID
        input_string = re.sub(r'\\\"transactionID\\\":\\\".*?\\\"', '\\\"transactionID\\\":\\\"' + new_id + '\\\"', input_string)

        with open('output-fetch.txt', 'w') as file:
            file.write(input_string)
        break
    except Exception as e:
        print()
        print('ERROR : Failed to format file (Step 2)')
        print(str(e))
        print()
        print("Stopping program now to prevent any further damages to your system.")
        quit(1)

print("Deleting temporary file...")
while True:
    try:
        Path(name).unlink()
        break
    except Exception as e:
        print()
        print('ERROR : Failed to delete temporary file')
        print(str(e))
        print()
        print("You can delete the file manually.")
        break

print("\n")
print("File formatted successfully!")
print("Formatted request is in output-fetch.txt")
print("You can now copy the request and paste it in the DevTools console.")


