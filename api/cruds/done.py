from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.task import Done


async def get_done(db: AsyncSession, task_id: int) -> Optional[Done]:
    result: Result = await db.execute(
        select(Done).filter(Done.id == task_id)
    )
    done: Optional[Tuple[Done]] = result.first()
    return done[0] if done is not None else None


async def create_done(db: AsyncSession, task_id: int) -> Done:
    done = Done(id=task_id)
    db.add(done)
    await db.commit()
    await db.refresh(done)
    return done


async def delete_done(db: AsyncSession, original: Done) -> None:
    await db.delete(original)
    await db.commit()
