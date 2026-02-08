import sys
import traceback

print("Testing imports...")

try:
    print("Importing openai...")
    import openai
    print(f"OpenAI version: {openai.__version__}")
except Exception as e:
    print(f"Failed to import openai: {e}")
    traceback.print_exc()

try:
    print("Importing pandas...")
    import pandas as pd
    print(f"Pandas version: {pd.__version__}")
except Exception as e:
    print(f"Failed to import pandas: {e}")
    traceback.print_exc()

try:
    print("Importing chatbot service...")
    from project.services import chatbot
    print("Chatbot service imported successfully.")
except Exception as e:
    print(f"Failed to import chatbot service: {e}")
    traceback.print_exc()

print("Import test complete.")
