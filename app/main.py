import json
import os
from .bedrock_client import generate_pipeline_yaml

TEMPLATE_TYPE = os.getenv("DEFAULT_TEMPLATE_TYPE", "github")


def build_prompt(config: dict, template_type: str) -> str:
    return f"""
Generate a {template_type} CI/CD pipeline.

Requirements (JSON):
{json.dumps(config, indent=2)}

Return ONLY the YAML for the pipeline. No explanations.
"""


def cli():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to JSON config file")
    parser.add_argument("--type", default=TEMPLATE_TYPE, choices=["github", "terraform", "kubernetes"])
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)

    prompt = build_prompt(cfg, args.type)
    yaml = generate_pipeline_yaml(prompt)
    print(yaml)


def lambda_handler(event, context):
    """
    HTTP API: POST { templateType, config }
    """
    body = {}
    if "body" in event and event["body"]:
        body = json.loads(event["body"])

    template_type = body.get("templateType", TEMPLATE_TYPE)
    config = body.get("config")
    if not config:
        return {"statusCode": 400, "body": json.dumps({"error": "Missing 'config' in request body"})}

    prompt = build_prompt(config, template_type)
    yaml = generate_pipeline_yaml(prompt)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/x-yaml"},
        "body": yaml,
    }


if __name__ == "__main__":
    cli()
