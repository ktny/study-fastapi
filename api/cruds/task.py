from typing import Optional, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.task as task_schema
from api.models.task import Done, Task


async def create_task(db: AsyncSession, task_create: task_schema.TaskCreate) -> Task:
    task = Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_task_with_done(db: AsyncSession) -> list[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                Task.id,
                Task.title,
                Done.id.isnot(None).label("done"),
            ).outerjoin(Done)
        )
    )
    return result.all()


async def get_task(db: AsyncSession, task_id: int) -> Optional[Task]:
    result: Result = await db.execute(select(Task).filter(Task.id == task_id))
    task: Optional[Tuple[Task]] = result.first()
    return task[0] if task is not None else None


async def update_task(db: AsyncSession, task_create: task_schema.TaskCreate, original: Task) -> Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_task(db: AsyncSession, original: Task) -> None:
    await db.delete(original)
    await db.commit()
