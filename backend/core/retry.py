import logging

from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from .exceptions import LLMError, ScrapingError

logger = logging.getLogger(__name__)


# Standard LLM retry: 3 attempts, 1s → 2s → 4s backoff
llm_retry = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((LLMError, Exception)),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)

# Scraper retry: 2 attempts, longer wait to avoid rate limiting
scraper_retry = retry(
    stop=stop_after_attempt(2),
    wait=wait_exponential(multiplier=2, min=2, max=15),
    retry=retry_if_exception_type(ScrapingError),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)

