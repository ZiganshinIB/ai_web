from typing import Annotated

from fastapi import APIRouter, Body, Path

from core.schema import CreateSiteRequest, GeneratedSitesResponse, SiteGenerationRequest, SiteResponse

router = APIRouter()


# TODO: Mock роутер потом переделать
@router.post(
    path="/create",
    summary="Создать сайт",
    response_model=SiteResponse,
)
async def create_site(site: Annotated[CreateSiteRequest, Body()]) -> None:
    return


@router.post(
    path="/{site_id:int}/generate",
    summary="Сгенерировать HTML код сайта.",
)
async def generate_site(
    site_id: Annotated[int, Path(gt=0)],
    site: Annotated[SiteGenerationRequest | None, Body()],
) -> str:
    """Код сайта будет транслироваться стримом по мере генерации."""
    return "Test"


@router.get(
    path="/{site_id:int}",
    summary="Получить список сайтов",
    response_model=SiteResponse,
)
async def get_site(site_id: int) -> None:
    return None


@router.get(
    path="/my",
    summary="Получить список сгенерированных сайтов текущего пользователя",
    response_model=GeneratedSitesResponse,
)
async def get_my_sites() -> None:
    return
