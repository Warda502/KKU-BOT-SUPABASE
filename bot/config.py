import os
import re
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "")

def _to_pooler_url(url: str) -> str:
    # Supabase direct: postgresql://postgres:PASS@db.REF.supabase.co:5432/postgres
    # Supabase pooler: postgresql+asyncpg://postgres.REF:PASS@aws-0-ap-south-1.pooler.supabase.com:6543/postgres
    m = re.match(r'postgres(ql)?(\+\w+)?://postgres:([^@]+)@db\.([^.]+)\.supabase\.co:5432/(.+)', url)
    if m:
        password = m.group(3)
        ref = m.group(4)
        db = m.group(5)
        return f"postgresql+asyncpg://postgres.{ref}:{password}@aws-0-ap-south-1.pooler.supabase.com:6543/{db}"
    return url

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

DATABASE_URL = _to_pooler_url(DATABASE_URL)

ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]

R2_ACCOUNT_ID = os.getenv("R2_ACCOUNT_ID", "")
R2_ACCESS_KEY_ID = os.getenv("R2_ACCESS_KEY_ID", "")
R2_SECRET_ACCESS_KEY = os.getenv("R2_SECRET_ACCESS_KEY", "")
R2_BUCKET_NAME = os.getenv("R2_BUCKET_NAME", "kku-bot")
R2_PUBLIC_URL = os.getenv("R2_PUBLIC_URL", "")
OPENCODE_API_KEY = os.getenv("OPENCODE_API_KEY", "")
OPENCODE_API_URL = os.getenv("OPENCODE_API_URL", "")
OPENCODE_AI_MODEL = os.getenv("OPENCODE_AI_MODEL", "")
