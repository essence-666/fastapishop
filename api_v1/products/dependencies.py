from typing import Annotated
from fastapi import Depends, HTTPException, Path, status
from api_v1.products import crud
from core.models import db_helper, Product
from sqlalchemy.ext.asyncio import AsyncSession


async def product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    product = await crud.get_product(session=session, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product
