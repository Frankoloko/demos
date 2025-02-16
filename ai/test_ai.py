# Run with
# PS C:\Francois\repos\demos> python .\ai\test_ai.py

import openai
from my_secrets import api_key
openai.api_key = api_key

def please_close():
  	print("Please close!!!")

def please_open():
  	print("Please open!!!")

def please_refresh():
	print("Please refresh!!!")

def get_api_call(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
		max_tokens=200,
        messages=[
			{"role": "system", "content": "You are an AI that converts natural language commands into function names. You must ONLY return the function name (e.g., 'open()', 'close()', or 'refresh()') and nothing else."},
            {"role": "user", "content": user_input},
		]
    )
    return response["choices"][0]["message"]["content"]

# Example Usage
command = get_api_call("Please open the window")

if command == "open()":
    please_open()
elif command == "close()":
    please_close()
elif command == "refresh()":
    please_refresh()