import requests

parameters = {      # if we want only 10 questions and only True/False type, we have to specify so in parameters
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)   # use parameters here
response.raise_for_status()     # raise exception if request not successful
question_data = response.json()["results"]  # have to tap into "results" key to get the data with questions same as list above
