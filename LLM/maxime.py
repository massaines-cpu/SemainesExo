from openai import OpenAI

# config
endpoint = "https://llm-res-ttt.cognitiveservices.azure.com/openai/v1/"
model_name = "gpt-4o"
deployment_name = "gpt-4o"

#! NE PAS PUSH CA SUR GIT !!
api_key = "blablabla"

client = OpenAI(
    base_url=f"{endpoint}",
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "blabla bla mon prompt",
        }
    ],
)

# la réponse de super intélligente de chat gpt
print(completion.choices[0].message)