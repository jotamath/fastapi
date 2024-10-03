run: 
	@uvicorn workout_api.main:app --reload

create-migrations:
	alembic revision --autogenerate -m $(d)

run-migrations:
	alembic upgrade head

dkr:
	@docker-compose up