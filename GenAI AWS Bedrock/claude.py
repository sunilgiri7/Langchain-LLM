import boto3
import json

prompt_data = """
    Act as a Shakespeare  and write a poem on  machine learning
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "prompt":prompt_data,
    "max_gen_len":512,
    "temperature":0.8,
    "top_p":0.8
}

body = json.dumps(payload)

model_id = "anthropic.claude-v2"

response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept= "application/json",
    contentType="application/json"
)

response_body = json.loads(response.get('body'.read()))
response_text = response_body.get("completions")[0].get("data").get("text")
print(response_text)