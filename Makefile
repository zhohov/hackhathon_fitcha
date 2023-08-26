run_server:
	uvicorn src.backend.main:app --reload

generate:
	alembic revision --m="$(NAME)" --autogenerate

migrate:
	alembic upgrade head