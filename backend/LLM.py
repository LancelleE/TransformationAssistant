import requests
import urllib3

class LLM_Mistral:
    def __init__(self, mistral_key):
        self.mistral_api_key = mistral_key
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': self.mistral_api_key
    }

    

    def get_completion(self, context, prompt):
        json_data = {
            'model': 'mistral-small',
            'messages': [
                {
                    'role': 'system',
                    'content': context
                }, {
                    'role': 'user',
                    'content': prompt,
                },
            ]
        }

        response = requests.post('https://api.mistral.ai/v1/chat/completions', headers=self.headers, json=json_data)
        completion = response.json()["choices"][0]["message"]["content"]
        return completion

