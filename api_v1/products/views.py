from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.products.schemas import (
    ProductCreate,
    Product,
    ProductUpdate,
    ProductUpdatePartial,
)
from core.models import db_helper
from . import crud
from .dependencies import product_by_id


router = APIRouter(tags=["products"])


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product=Depends(product_by_id),
):
    return product


@router.post("/", response_model=Product)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, productCreate=product)


@router.put("/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(
        product=product,
        session=session,
        productUpdate=product_update,
    )


@router.patch("/{product_id}/")
async def update_product(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(
        product=product,
        session=session,
        productUpdate=product_update,
        partial=True,
    )


@router.delete("/deleteitem/{product_id}/")
async def delete_item(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.delete_product(product=product, session=session)
