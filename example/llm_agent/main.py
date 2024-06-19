import os
import openai
import json
from dotenv import load_dotenv
from pygard.data_model_loader import DataModelLoader
from pygard.data_model_validator import DataValidator

load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up PyGard policies
REPO_URL = "https://github.com/your-username/your-repo.git"
CACHE_DIR = os.path.expanduser("~/.pygard/cache/policies")
CUSTOM_MODEL_PATHS = [r"local/path/to/custom/data_models"]
CUSTOM_VALIDATOR_PATHS = ["custom_validators"]

# Load data models
model_loader = DataModelLoader(CACHE_DIR, CUSTOM_MODEL_PATHS)

# Set up data validator
validator = DataValidator(model_loader)

def get_llm_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    prompt = "Provide information about the population in CA state in USA, the CA size in miles, and popular landscapes in CA. Respond in JSON format with keys 'population', 'size', and 'landscapes'."

    # Validate the input prompt
    prompt_data = {
        "PromptModel": {
            "task": prompt,
            "state": "CA",
            "country": "USA"
        }
    }
    prompt_validation = validator.validate_data(prompt_data)
    print(f"prompt_validation:{prompt_validation}")
    if not all(result['valid'] for result in prompt_validation.values()):
        print(f"Prompt validation failed: {prompt_validation}")
        return

    # Get response from OpenAI LLM
    llm_response = get_llm_response(prompt)
    print(f"LLM Response: {llm_response}")

    try:
        response_data = json.loads(llm_response)
        # print(response_data)
    except json.JSONDecodeError:
        print("LLM response is not in valid JSON format.")
        return

    # Validate the LLM response
    # response_data = {
    #     "ResponseModel": {
    #         "population": "39.14 million",
    #         "size": "163,696 square miles",
    #         "landscapes": ["Yosemite National Park", "Death Valley", "Big Sur"]
    #     }
    # }
    response_validation = validator.validate_data({"ResponseModel":{**response_data}})
    print(f"response_validation:{response_validation}")
    if not all(result['valid'] for result in response_validation.values()):
        print(f"Response validation failed: {response_validation}")
        # Here, you would send feedback to the LLM for correction
        return

    print("Validation successful. LLM response is valid.")

if __name__ == "__main__":
    main()
