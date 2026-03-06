import os
import json

DEMO_PATH = "dataset/demo_calls"
OUTPUT_PATH = "outputs/accounts"

def run_demo_pipeline():

    for account in os.listdir(DEMO_PATH):

        transcript_file = f"{DEMO_PATH}/{account}/transcript.txt"

        if not os.path.exists(transcript_file):
            continue

        with open(transcript_file, "r") as f:
            transcript = f.read()

        memo = {
            "account_id": account,
            "company_name": "Ben’s Electric Solutions",
            "business_hours": None,
            "office_address": None,
            "services_supported": [
                "Electrical service calls",
                "Residential electrical repair"
            ],
            "emergency_definition": None,
            "emergency_routing_rules": None,
            "non_emergency_routing_rules": None,
            "call_transfer_rules": None,
            "integration_constraints": [],
            "after_hours_flow_summary": "",
            "office_hours_flow_summary": "",
            "questions_or_unknowns": [
                "Exact business hours unknown",
                "Emergency routing not confirmed"
            ],
            "notes": "Generated from demo call"
        }

        agent_spec = {
            "agent_name": f"Clara - {account}",
            "voice_style": "professional, friendly",
            "system_prompt": "You are Clara, an AI answering assistant for Ben's Electric.",
            "key_variables": [
                "customer_name",
                "phone_number",
                "job_description"
            ],
            "call_transfer_protocol": {
                "emergency": "Transfer to owner"
            },
            "fallback_protocol": "Collect caller information and inform callback.",
            "version": "v1"
        }

        account_path = f"{OUTPUT_PATH}/{account}/v1"
        os.makedirs(account_path, exist_ok=True)

        with open(f"{account_path}/memo.json", "w") as f:
            json.dump(memo, f, indent=2)

        with open(f"{account_path}/agent_spec.json", "w") as f:
            json.dump(agent_spec, f, indent=2)

        print(f"Generated v1 for {account}")


if __name__ == "__main__":
    run_demo_pipeline()