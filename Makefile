.PHONY: setup dev test lint format typecheck clean
setup:
	python -m venv .venv
	.venv/bin/pip install -r requirements-dev.txt
	.venv/bin/playwright install chromium
dev:
	cd backend && ../.venv/bin/uvicorn api.main:app --reload --port 8000
frontend-dev:
	cd frontend && npm run dev
test:
	.venv/bin/pytest tests/ -v --asyncio-mode=auto
lint:
	.venv/bin/ruff check backend/ tests/
format:
	.venv/bin/ruff format backend/ tests/
typecheck:
	.venv/bin/mypy backend/ --ignore-missing-imports
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .mypy_cache .ruff_cache
