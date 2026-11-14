import os
import requests
from dotenv import load_dotenv

# Read my login details from the .env file
load_dotenv()
instance = os.environ["SN_INSTANCE"]
user = os.environ["SN_USER"]
password = os.environ["SN_PASSWORD"]

# The web address of my ServiceNow tickets
url = "https://" + instance + ".service-now.com/api/now/table/incident"

# What I want back: 5 tickets, only their number and description
how_many_tickets = 5
which_details = "number,short_description"

settings = {
    "sysparm_limit": how_many_tickets,
    "sysparm_fields": which_details,
}

# Ask ServiceNow for the tickets
response = requests.get(
    url,
    auth=(user, password),
    params=settings,
    headers={"Accept": "application/json"},
)

# 200 means it worked, 401 means the login was rejected
print("Status code:", response.status_code)

# Turn the reply into Python data and pull out the list of tickets
data = response.json()
tickets = data["result"]

print("Number of tickets:", len(tickets))

# Print each ticket on its own line
for ticket in tickets:
    number = ticket["number"]
    description = ticket["short_description"]
    print(number, "-", description)