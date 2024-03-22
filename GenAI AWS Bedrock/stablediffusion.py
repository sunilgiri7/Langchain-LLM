import base64
import os
import boto3
import json

prompt_data = """
    Provide me 4k hd image of a a man chilling on beach, also use blue sky rainy season and cinematic diplay  
"""

prompt_template = [{"text": prompt_data, "weight": 1}]

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "text_prompts":prompt_template,
    "cfg_scale": 10,
    "seed": 0,
    "steps": 50,
    "weidth": 1024,
    "height": 1024
}

body = json.dumps(payload)

model_id = "stability.stable-diffusion-xl-v1"

response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept= "application/json",
    contentType="application/json"
)

response_body = json.loads(response.get('body').read())
print(response_body)
artifact = response_body('artifacts')[0]
image_encoded = artifact.get("base64").encode("utf-8")
image_bytes = base64.b64decode(image_encoded)

#save
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
file_name = f"{output_dir}/generated-img.png"
with open(file_name, 'wb') as f:
    f.write(image_bytes)