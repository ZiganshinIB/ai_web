from pydantic import AliasGenerator, BaseModel, ConfigDict, Field, HttpUrl
from pydantic.alias_generators import to_camel

from core.common import IsoDateTime


class SiteGenerationRequest(BaseModel):

    prompt: str
    """Описание сайта"""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        json_schema_extra={
            "examples": [
                {
                    "prompt": "Сайт любителей играть в домино",
                },
            ],
        },
        use_attribute_docstrings=True,
    )


class CreateSiteRequest(SiteGenerationRequest):

    title: str | None = None
    """Название сайта"""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "title": "Фан клуб игры в домино",
                    "prompt": "Сайт любителей играть в домино",
                },
            ],
        },
    )


class SiteResponse(BaseModel):
    pk: int = Field(..., gt=0, alias="id")
    """ID сайта"""
    title: str | None
    """Название сайта"""
    html_code_download_url: HttpUrl
    """Ссылка на скачивание HTML кода сайта"""
    html_code_url: HttpUrl
    """Ссылка на HTML код сайта"""
    screenshot_url: HttpUrl
    """Ссылка на скриншот сайта"""
    prompt: str
    """Описание сайта"""
    created_at: IsoDateTime
    """Дата создания сайта"""
    updated_at: IsoDateTime
    """Дата обновления сайта"""

    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            serialization_alias=to_camel,
        ),
        populate_by_name=True,
        json_schema_extra={
            "examples": [
                {
                    "createdAt": "2025-06-15T18:29:56+00:00",
                    "htmlCodeDownloadUrl": "http://example.com/media/index.html?response-content-disposition=attachment",
                    "htmlCodeUrl": "http://example.com/media/index.html",
                    "id": 1,
                    "prompt": "Сайт любителей играть в домино",
                    "screenshotUrl": "http://example.com/media/index.png",
                    "title": "Фан клуб Домино",
                    "updatedAt": "2025-06-15T18:29:56+00:00",
                },
            ],
        },
        use_attribute_docstrings=True,
    )


class GeneratedSitesResponse(BaseModel):
    sites: list[SiteResponse]
    """Список сайтов"""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        json_schema_extra={
            "examples": [
                {
                    "sites": [
                        {
                            "createdAt": "2025-06-15T18:29:56+00:00",
                            "htmlCodeDownloadUrl": "http://example.com/media/index.html?response-content-disposition=attachment",
                            "htmlCodeUrl": "http://example.com/media/index.html",
                            "id": 1,
                            "prompt": "Сайт любителей играть в домино",
                            "screenshotUrl": "http://example.com/media/index.png",
                            "title": "Фан клуб Домино",
                            "updatedAt": "2025-06-15T18:29:56+00:00",
                        },
                    ],
                },
            ],
        },
        use_attribute_docstrings=True,
    )
