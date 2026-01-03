import datetime

from fastapi import APIRouter

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
    openapi_extra={
        "responses": {
            "200": {
                "description": "Учетные данные пользователя.",
                "content": {
                    "application/json": {
                        "example": {
                            "email": "user123@example.com",
                            "isActive": True,
                            "profileId": 1,
                            "registeredAt": datetime.datetime.now(datetime.UTC),
                            "updatedAt": datetime.datetime.now(datetime.UTC),
                            "username": "user123",
                        },
                    },
                },
            },
        },
    },
)
async def me() -> dict:
    print("me")
    return MOCK_USER
