import logging
from typing import Generic, List, Optional, Type, TypeVar

import database
from entity.basic_entity import BasicEntity

E = TypeVar('E', bound=BasicEntity)


class BasicRepository(Generic[E]):
    def __init__(self, entity: Type[E]):
        self.entity = entity

    def get_one_by_id(self, find_id: int) -> Optional[E]:
        db_session = next(database.get_db_session())
        find_entity = db_session.query(self.entity).filter(self.entity.id == find_id).first()
        if find_entity is None:
            logging.error(f"{self.entity}'s id {find_id} is not found")
        return find_entity

    def get_by_id_list(self, id_list: List[int]) -> List[E]:
        """ Get entity list by id list. (must every id in id list)"""
        db_session = next(database.get_db_session())
        find_entity_list = db_session.query(self.entity).filter(self.entity.id.in_(id_list)).all()  # type: ignore

        return find_entity_list

    def get_all(self) -> List[E]:
        db_session = next(database.get_db_session())
        return db_session.query(self.entity).all()

    def save_all(self, entity_list: List[E]) -> None:
        db_session = next(database.get_db_session())
        if len(entity_list) < 10:
            db_session.add_all(entity_list)
        else:
            db_session.bulk_save_objects(entity_list)

    def save_one(self, entity: E) -> E:
        db_session = next(database.get_db_session())
        db_session.add(entity)
        db_session.flush()
        return entity

    def delete_by_id(self, find_id: int) -> None:
        db_session = next(database.get_db_session())
        db_session.query(self.entity).filter(self.entity.id == find_id).delete()
