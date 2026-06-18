import os
import sys

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print(
        "Erro: variáveis SUPABASE_URL e SUPABASE_KEY "
        "não encontradas no .env"
    )
    sys.exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
