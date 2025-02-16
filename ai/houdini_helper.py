# Run with
# PS C:\Francois\repos\demos> python .\ai\houdini_helper.py

import openai
from my_secrets import api_key
openai.api_key = api_key

def get_api_call(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
		# max_tokens=200,
        messages=[
			{"role": "system", "content": "You are an AI that converts natural language commands into function names. You must ONLY return code that can get executed right away. You are only a helper inside of the software Houdini. Your job is to help the user by writing code that will create node in the node network, connect nodes, fill in parameters on nodes, and so on. Don't add ``` around the code snippet. Also include all imports you would need in the code."},
            {"role": "user", "content": user_input},
		]
    )
    return response["choices"][0]["message"]["content"]

# Example Usage

# Had an error in the script creation
# command = get_api_call("Build met a node network that explains how to use a for loop")

# It's really battling to do this
# command = get_api_call("Read my current scene. Please create a cube node. And connect it in between the camera and light nodes in the scene. Don't search for specific light or camera node names. You need to dynamically look for the nodes.")


# Had an error in the script creation
command = get_api_call("Build a node network that explains to me how to import something from the obj level to the stage level")


# Open a file in write mode
with open("output.txt", "w") as file:
    file.write(command)
