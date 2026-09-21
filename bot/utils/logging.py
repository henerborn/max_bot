import logging
from bot.config import settings

logger = logging.getLogger(__name__)


def configure_logging(level=logging.INFO) -> None:        
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)14s:%(lineno)-5d %(levelname)-5s - %(message)s"
    )

    logger.info("Logger was configured")