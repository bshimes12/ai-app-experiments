from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

assistant_id = 'asst_ugRzy1ru2Xnvk6uLD5LDJavb'
api_key = os.getenv("OPENAI_API_KEY")
#api_key = "sk-proj-n0vSHsctXCZJ2q7HiZFTT3BlbkFJU6joaeRET12F3BBbYTuG"
file_path = "/Users/bower/code/justPrompts/openai_assistant_files/f_THE_PROBLEM_gpt-3.5-turbo-0125_2024-04-16 09-18-50.txt"

def upload_file_to_existing_assistant(api_key, assistant_id, file_path):

    # Initialize OpenAI client with the API key
    client = OpenAI(api_key=api_key)
    
    # Upload a file to OpenAI
    with open(file_path, 'rb') as file:
        uploaded_file = client.files.create(file=file, purpose='assistants')

    # Add the uploaded file to the assistant
        client.beta.assistants.files.create(assistant_id=assistant_id, file_id=uploaded_file.id)

    print(f"File '{file_path}' uploaded and added to the assistant with ID: {assistant_id}")

# Example usage
upload_file_to_existing_assistant(api_key, assistant_id, file_path)