from openai import OpenAI
from helpers import get_config

def send_chat_to_openai(context, prompt):
    config = get_config()

    client = OpenAI(
        organization=config['openai']['organization'],
        api_key=config['openai']['api_key']
    )


    response = client.chat.completions.create(
        model=config['openai']['model'],
        messages=[
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=config['openai']['temperature'],
        max_tokens=config['openai']['max_tokens'],
    )

    return response.choices[0].message.content
