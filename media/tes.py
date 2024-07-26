import requests

# Define the endpoint URL
url = 'https://cbweb.onrender.com/api/dronedata/'

# Define the payload and headers if needed
payload = {
    'droneid': 'dfs',
    'time': '2024-12-12'
}

# Define the path to the file you want to upload
file_path = 'about.jpeg'

# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Create a dictionary for the files parameter
    files = {
        'FileField': file
    }

    # Make the POST request
    response = requests.post(url, data=payload, files=files)

# Print the response
print(response.status_code)
print(response.text)
