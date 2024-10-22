from fastapi import APIRouter, Body, status
from workout_api.categories.schemas import CategoriaOut, CategoriaIn
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/',
    summary='Criar nova categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_session: DatabaseDependency,
    atleta_in: CategoriaIn = Body(...)
):
    pass
