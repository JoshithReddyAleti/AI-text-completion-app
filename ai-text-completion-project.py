import os
import sys
from huggingface_hub import InferenceApi

# Try to load .env if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not available; continue, but ensure HF_TOKEN is set in the environment
    pass

print("Starting text-completion app...")

# Retrieve Hugging Face API token from environment
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    print(
        "HF_TOKEN not found.\n"
        "   • Either install python-dotenv and add HF_TOKEN to a .env file, or\n"
        "   • Set HF_TOKEN as an environment variable (e.g. `set HF_TOKEN=hf_...`).",
        file=sys.stderr
    )
    sys.exit(1)

# Model selection
MODEL_ID = "gpt2"

# Initialize the Inference API client
inference = InferenceApi(repo_id=MODEL_ID, token=HF_TOKEN)

def generate_text(prompt: str, max_new_tokens: int = 50, temperature: float = 1.0) -> str:
    try:
        output = inference(
            inputs=prompt,
            parameters={
                "max_new_tokens": max_new_tokens,
                "temperature": temperature,
            },
        )
        # Handle different return formats
        if isinstance(output, list) and output and isinstance(output[0], dict):
            return output[0].get("generated_text", str(output))
        if isinstance(output, dict) and "generated_text" in output:
            return output["generated_text"]
        return str(output)
    except Exception as e:
        return f"[Error] {e}"

def main():
    print(f"Text completion with {MODEL_ID}. Type 'exit' to quit.\n")
    while True:
        prompt = input("Prompt: ").strip()
        if prompt.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        if not prompt:
            print("Please enter a non-empty prompt.")
            continue

        # Get parameters from user
        try:
            temp_input = input("  – temperature (0.0–2.0) [1.0]: ").strip()
            temperature = float(temp_input) if temp_input else 1.0
        except ValueError:
            print("Invalid temperature; using default 1.0.")
            temperature = 1.0

        try:
            len_input = input("  – max_new_tokens [50]: ").strip()
            max_new_tokens = int(len_input) if len_input else 50
        except ValueError:
            print("Invalid length; using default 50.")
            max_new_tokens = 65

        print("\n Generating...\n")
        result = generate_text(prompt, max_new_tokens=max_new_tokens, temperature=temperature)
        print("Response:\n" + result + "\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()
