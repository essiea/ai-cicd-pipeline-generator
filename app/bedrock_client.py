import json
import boto3
import os

MODEL_ID = os.getenv("PIPELINE_MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0")

_client = boto3.client("bedrock-runtime")


def generate_pipeline_yaml(prompt: str) -> str:
    body = {
        "messages": [
            {
                "role": "system",
                "content": [{
                    "type": "text",
                    "text": "You are a senior DevOps engineer. Generate ONLY valid YAML code with no explanations."
                }],
            },
            {"role": "user", "content": [{"type": "text", "text": prompt}]},
        ],
        "max_tokens": 800,
        "temperature": 0.2,
    }

    resp = _client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )

    payload = json.loads(resp["body"].read())
    content = payload["output"]["message"]["content"]
    text_parts = [c["text"] for c in content if c["type"] == "text"]
    return "\n".join(text_parts)
