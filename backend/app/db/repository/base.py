# for use with session.py
from typing import TypeVar, Type, Optional, Generic

from sqlalchemy import select, update, delete

from pydantic import BaseModel

from db.session import Base, session

ModelType = TypeVar("ModelType", bound=Base)

class SynchronizeSessionEnum(BaseModel):
    FETCH = "fetch"
    EVALUATE = "evaluate"
    FALSE = False

class BaseRepo(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

# make the following method static if wanted!
    async def get_all(self):
        query = select(self.model)
        return await session.execute(query).scalars().all()

    async def get_by_id(self, model_id: int) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == model_id)
        # return await session.execute(query).scalars().first()
        return await session.execute(query).scalar_one_or_none()

    async def update_by_id(
        self,
        model_id: int,
        params: dict,
        synchronize_session: SynchronizeSessionEnum = False,
        **kwargs # replace params if error occurs
    ) -> None:
        query = (
            update(self.model)
            .where(self.model.id == model_id)
            .values(**params)
            .execution_options(synchronize_session=synchronize_session) # synchronize_session="fetch"
        )
        await session.execute(query)
        # add an await session rollback

    async def delete(self, model: ModelType) -> None:
        await session.delete(model)

    async def delete_by_id(
        self,
        model_id: int,
        synchronize_session: SynchronizeSessionEnum = False,
    ) -> None:
        query = (
            delete(self.model)
            .where(self.model.id == model_id)
            .execution_options(synchronize_session=synchronize_session)
        )
        await session.execute(query)
        # add an await session rollback

    async def save(self, model: ModelType) -> ModelType:  # also create
        saved = await session.add(model)
        return saved
