"""Startup script — runs API server only (no Telegram bot)."""
import asyncio
import os
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def run():
    from bot.api.main import app
    import uvicorn

    config = uvicorn.Config(
        app, host="0.0.0.0",
        port=int(os.getenv("PORT", 3000)),
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    logger.info("Starting KKU Bot Dashboard API server...")
    asyncio.run(run())
