import requests
from openai import OpenAI

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


class LLM_OpenAI:
    def __init__(self, openai_key):
        self.openai_key = openai_key
 

    def get_completion(self, context, prompt):
        client = OpenAI(api_key=self.openai_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
            ]
        )

        completion = response.choices[0].message.content

        return completion