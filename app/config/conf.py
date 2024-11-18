import os 
from dotenv import load_dotenv
load_dotenv()
FALKOR_HOST = os.getenv("FALKOR_HOST_URL")
PORTS = os.getenv("PORTS")
FALKOR_USERNAME = os.getenv("FALKOR_USERNAME")
FALKOR_PASSWORD = os.getenv("FALKOR_PASSWORD")
LLM_MODEL = "gemini-1.5-flash-latest"