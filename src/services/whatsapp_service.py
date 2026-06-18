import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WhatsAppService:

    def __init__(self):
        self.instance_id = os.getenv("ZAPI_INSTANCE_ID")
        self.token = os.getenv("ZAPI_TOKEN")
        self.client_token = os.getenv("ZAPI_CLIENT_TOKEN")

        self.url = (
            f"https://api.z-api.io/"
            f"instances/{self.instance_id}/"
            f"token/{self.token}/send-text"
        )

    def send_message(self, phone: str, name: str):
        headers = {
            "Content-Type": "application/json",
            "Client-Token": self.client_token
        }

        payload = {
            "phone": phone,
            "message": f"Olá, {name} tudo bem com você?"
        }

        response = requests.post(
            self.url,
            json=payload,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            print(f"🚨 ERRO Z-API: {response.text}")

        response.raise_for_status()
        return response.json()
