import datetime

from fastapi import APIRouter

from core.schema import UserDetailsResponse

router = APIRouter()

MOCK_USER = {
    "email": "user123@example.com",
    "isActive": True,
    "profileId": 1,
    "registeredAt": datetime.datetime.now(datetime.UTC),
    "updatedAt": datetime.datetime.now(datetime.UTC),
    "username": "user123",
}


# TODO: Mock роутер потом переделать
@router.get(
    path="/me",
    summary="Получить учетные данные пользователя",
    response_model=UserDetailsResponse,
)
async def me() -> UserDetailsResponse:
    return UserDetailsResponse.model_validate(MOCK_USER)
