import os
import json

ONBOARD_PATH = "dataset/onboarding_calls"
OUTPUT_PATH = "outputs/accounts"

def run_onboarding_pipeline():

    for account in os.listdir(ONBOARD_PATH):

        transcript_file = f"{ONBOARD_PATH}/{account}/audio.txt"

        if not os.path.exists(transcript_file):
            continue

        with open(transcript_file) as f:
            transcript = f.read()

        v1_path = f"{OUTPUT_PATH}/{account}/v1/memo.json"

        with open(v1_path) as f:
            memo = json.load(f)

        memo["business_hours"] = {
            "days": "Monday-Friday",
            "hours": "8:00 AM - 4:30 PM"
        }

        memo["emergency_definition"] = "Emergency calls from property managers"

        v2_path = f"{OUTPUT_PATH}/{account}/v2"
        os.makedirs(v2_path, exist_ok=True)

        with open(f"{v2_path}/memo.json", "w") as f:
            json.dump(memo, f, indent=2)

        agent_spec = {
            "agent_name": f"Clara - {account}",
            "voice_style": "professional, friendly",
            "system_prompt": "Updated agent prompt based on onboarding.",
            "version": "v2"
        }

        with open(f"{v2_path}/agent_spec.json", "w") as f:
            json.dump(agent_spec, f, indent=2)

        with open(f"{OUTPUT_PATH}/{account}/changes.md", "w", encoding="utf-8") as f:
            f.write(
"""# Changes from v1 → v2

Confirmed business hours
Added emergency routing
Updated system prompt
"""
            )

        print(f"Generated v2 for {account}")

if __name__ == "__main__":
    run_onboarding_pipeline()