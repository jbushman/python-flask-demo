import logging


class BaseDao:
    model = None
    session = None
    logger = logging.getLogger('app')

    def __init__(self, model, session):
        self.model = model

        self.session = session

    def find_all(self):
        return self.session.query(self.model).all()

    def find_by_id(self, identifier):
        return self.session.query(self.model).get(identifier)

    def save(self, obj):
        try:
            self.session.add(obj)
        except RuntimeError:
            self.logger.error(f"Failed to save record [model={type(self.model)}, identifier={obj.get_identifier()}")
            self.session.rollback()
            raise
        finally:
            self.session.commit()

        return obj

    def update(self, obj):
        try:
            _persistent_obj = self.find_by_id(obj.get_identifier())
            self.session.merge(obj)
            self.session.add(_persistent_obj)
            return obj
        except RuntimeError:
            self.logger.error(f"Failed to update record [model={type(self.model)}, identifier={obj.get_identifier()}")
            self.session.rollback()
            raise
        finally:
            self.session.commit()

    def delete(self, identifier):
        try:
            _persistent_obj = self.find_by_id(identifier)
            self.session.delete(_persistent_obj)
        except RuntimeError:
            self.logger.error(f"Failed to delete record [model={type(self.model)}, identifier={identifier}")
            self.session.rollback()
            raise
        finally:
            self.session.commit()

        return True
