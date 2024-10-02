from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
import uvicorn
from users.views import router as users_router
from items.views import router as items_router
from core.models import Base, db_helper
from api_v1 import router as api_v1_router
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all,
        )
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users_router)
app.include_router(items_router)
app.include_router(router=api_v1_router, prefix=settings.api_v1_prefix)


async def shared_parameters(q: int, w: int) -> int:
    return q + w


@app.get("/")
def hello_man(res=Depends(shared_parameters)):
    return {"message": f"hello {res}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
