from fastapi import APIRouter

from .mocks import MOCK_USER
from .schemas import UserDetailsResponse

router = APIRouter()


# TODO: Mock роутер потом переделать
@router.get(
    path="/me",
    summary="Получить учетные данные пользователя",
    response_model=UserDetailsResponse,
)
async def me() -> UserDetailsResponse:
    return UserDetailsResponse.model_validate(MOCK_USER)
