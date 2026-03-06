import os
import subprocess

DATASET_PATH = "dataset/onboarding_calls"

def transcribe_audio():
    for account in os.listdir(DATASET_PATH):

        account_path = os.path.join(DATASET_PATH, account)
        audio_file = os.path.join(account_path, "audio.m4a")

        if os.path.exists(audio_file):

            print(f"Transcribing {account}")

            subprocess.run([
                "python",
                "-m",
                "whisper",
                audio_file,
                "--model",
                "base",
                "--output_format",
                "txt",
                "--output_dir",
                account_path
            ])

if __name__ == "__main__":
    transcribe_audio()