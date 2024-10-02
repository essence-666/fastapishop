"""
CRUD operations for products
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from api_v1.products.schemas import ProductCreate, ProductUpdate, ProductUpdatePartial
from core.models import Product
from sqlalchemy import select


async def get_products(session: AsyncSession) -> list[Product]:
    statement = select(Product).order_by(Product.id)
    result: Result = await session.execute(statement)
    return list(result.scalars().all())


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, productCreate: ProductCreate):
    product = Product(**productCreate.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product


async def update_product(
    session: AsyncSession,
    product: Product,
    productUpdate: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    for key, value in productUpdate.model_dump(exclude_unset=partial).items():
        setattr(product, key, value)
    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> dict:
    try:
        await session.delete(product)
        await session.commit()
    except:
        return {"message": "the product was not found"}
    return {"message": "the product was succsessfully deleted"}
