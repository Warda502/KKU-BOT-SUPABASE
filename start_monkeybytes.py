"""Startup script — runs bot and API on the same asyncio event loop."""
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
    from bot.main import post_init, error_handler, register_handlers
    from bot.config import BOT_TOKEN
    from telegram.ext import ApplicationBuilder

    # Build and initialize bot
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    register_handlers(application)
    await application.initialize()
    await application.start()

    # Start polling (non-blocking, returns immediately)
    await application.updater.start_polling(drop_pending_updates=True)

    # Start uvicorn (blocks forever — keeps the process alive)
    config = uvicorn.Config(
        app, host="0.0.0.0",
        port=int(os.getenv("PORT", 3000)),
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    logger.info("Starting KKU Bot + API server...")
    asyncio.run(run())
