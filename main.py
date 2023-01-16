# Import the search_phonenumber function from the truecallerpy library
from truecallerpy import search_phonenumber

# Assign an empty string to the id variable
# This variable will be used to store your Truecallerpy authentication ID
id = "" # enter your truecallerpy authentication id here

# Assign a phone number to the phone_number variable
phone_number = '+911234567890'

# Call the search_phonenumber function and pass in the phone number, country code and authentication ID
response = (search_phonenumber(phone_number,"IN", id))

# Extract the data from the response
data = response["data"][0]

# Print the name of the person associated with the phone number
print("Name - ",data["name"])

# Extract the phone data from the data
data2 = data["phones"][0]

# Print the carrier information of the phone number
print(data2['carrier'])
