from pydantic import AliasGenerator, BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel

from core.common import IsoDateTime


class UserDetailsResponse(BaseModel):

    profile_id: int = Field(..., gt=0)
    """Идентификатор профиля"""
    username: str = Field(..., max_length=254)
    """Имя пользователя"""
    email: EmailStr
    """Email пользователя"""
    registered_at: IsoDateTime
    """Дата регистрации пользователя"""
    updated_at: IsoDateTime
    """Дата последнего обновления профиля"""
    is_active: bool
    """Признак активности пользователя"""

    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            serialization_alias=to_camel,
        ),
        populate_by_name=True,
        json_schema_extra={
            "examples": [
                {
                    "profileId": 1,
                    "username": "user123",
                    "isActive": True,
                    "email": "user123@example.com",
                    "registeredAt": "2025-06-15T18:29:56+00:00",
                    "updatedAt": "2025-06-15T18:29:56+00:00",
                },
            ],
        },
        use_attribute_docstrings=True,
    )
