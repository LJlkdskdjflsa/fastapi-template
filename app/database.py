import logging
from contextvars import ContextVar
from functools import wraps
from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

from app.core.config import SystemConfig

# engine = create_engine(
#     f'{SystemConfig.DB_URL}?charset=utf8mb4', pool_pre_ping=True, echo='debug', encoding='utf8',
#     convert_unicode=True, pool_size=10, max_overflow=20, pool_recycle=3600,
# )
engine = create_engine(f'{SystemConfig.DB_URL}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


db_session_context: ContextVar[Optional[Session]] = ContextVar('db_session', default=None)


def get_db_session() -> Generator[Session, None, None]:
    db_session = db_session_context.get()
    if db_session is None:
        db_session = SessionLocal()
    try:
        yield db_session
    except Exception:
        db_session.rollback()
        raise
    finally:
        if db_session_context.get() is not None:
            # it will be committed by transactional decorator
            pass
        else:
            db_session.commit()
            db_session.close()


def transactional(*exceptions):
    # if not set exceptions, set Exception
    if not exceptions:
        exceptions = (Exception,)

    def decorator(func):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            db_session = db_session_context.get()
            # If we already have a session in context
            # than it means that this method is called
            # from already a transactional method which
            # will handle rollback so we won't need
            # to worry about it
            if db_session is not None:
                return func(*args, **kwargs)
            # If we don't have a session in
            # context yet, we have to create it
            db_session = SessionLocal()
            db_session_context.set(db_session)
            # Once we have a session in our context
            # we can call the wrapped function and
            # commit after it's finished
            try:
                result = func(*args, **kwargs)
                db_session.commit()
            # If an exception occurs during the method
            # execution it won't be committed but will
            # be rolled back instead but we still need
            # to raise the exception cause it's not
            # ours to handle
            except exceptions as e:
                logging.error(f'db error: {e}')
                logging.error('db rollback')
                db_session.rollback()
                raise
            # In the end we should close the session
            # and empty the context
            finally:
                db_session.close()
                db_session_context.set(None)
            return result

        return wrap_func

    return decorator


def transactional_async(*exceptions):
    # if not set exceptions, set Exception
    if not exceptions:
        exceptions = (Exception,)

    def decorator(func):
        @wraps(func)
        async def wrap_func(*args, **kwargs):
            db_session = db_session_context.get()
            # If we already have a session in context
            # than it means that this method is called
            # from already a transactional method which
            # will handle rollback so we won't need
            # to worry about it
            if db_session is not None:
                return await func(*args, **kwargs)
            # If we don't have a session in
            # context yet, we have to create it
            db_session = SessionLocal()
            db_session_context.set(db_session)
            # Once we have a session in our context
            # we can call the wrapped function and
            # commit after it's finished
            try:
                result = await func(*args, **kwargs)
                db_session.commit()
            # If an exception occurs during the method
            # execution it won't be committed but will
            # be rolled back instead but we still need
            # to raise the exception cause it's not
            # ours to handle
            except exceptions as e:
                logging.error(f'db error: {e}')
                logging.error('db rollback')
                db_session.rollback()
                raise
            # In the end we should close the session
            # and empty the context
            finally:
                db_session.close()
                db_session_context.set(None)
            return result

        return wrap_func

    return decorator
