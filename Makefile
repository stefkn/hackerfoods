.PHONY: ruff

ruff:
	poetry run ruff check
	poetry run ruff format
