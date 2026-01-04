import asyncio
from pathlib import Path as OSPath
from typing import Annotated

import aiofiles
from fastapi import APIRouter, Body, Path
from fastapi.exceptions import HTTPException
from fastapi.responses import StreamingResponse

from .mocks import MOCK_SITE_RESPONSE
from .schemas import CreateSiteRequest, GeneratedSitesResponse, SiteGenerationRequest, SiteResponse

router = APIRouter()

MEDIA_DIR = OSPath(__file__).parent.parent.parent.parent / "media"


async def generate_text_chunks(relative_path: str):
    relative_path = relative_path.lstrip("/").lstrip("media").lstrip("/")
    file_path = (MEDIA_DIR / relative_path).resolve()

    if not file_path.is_file() or MEDIA_DIR not in file_path.parents:
        raise HTTPException(status_code=400, detail="Invalid file path")
    async with aiofiles.open(file_path, encoding="utf-8") as file:
        async for line in file:
            yield line
            await asyncio.sleep(0.05)


# TODO: Mock роутер потом переделать
@router.post(
    path="/create",
    summary="Создать сайт",
    response_model=SiteResponse,
)
async def create_site(site: Annotated[CreateSiteRequest, Body()]) -> SiteResponse:
    local_mock = MOCK_SITE_RESPONSE.copy()
    local_mock["prompt"] = site.prompt
    local_mock["title"] = site.title if site.title else local_mock["title"]
    return SiteResponse.model_validate(local_mock)


@router.post(
    path="/{site_id:int}/generate",
    summary="Сгенерировать HTML код сайта.",
)
async def generate_site(
    site_id: Annotated[int, Path(gt=0)],
    site: SiteGenerationRequest | None = Body(default=None, title="SiteGenerationRequest"),
) -> StreamingResponse:
    """Код сайта будет транслироваться стримом по мере генерации."""
    uri_path = "/media/index.html"
    return StreamingResponse(
        content=generate_text_chunks(uri_path),
        media_type="text/plain; charset=utf-8",
    )


@router.get(
    path="/{site_id:int}",
    summary="Получить список сайтов",
    response_model=SiteResponse,
)
async def get_site(site_id: int) -> SiteResponse:
    return SiteResponse.model_validate(MOCK_SITE_RESPONSE)


@router.get(
    path="/my",
    summary="Получить список сгенерированных сайтов текущего пользователя",
    response_model=GeneratedSitesResponse,
)
async def get_my_sites() -> GeneratedSitesResponse:
    return GeneratedSitesResponse(sites=[SiteResponse.model_validate(MOCK_SITE_RESPONSE)])
