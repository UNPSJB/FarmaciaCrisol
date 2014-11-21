__author__ = 'waldo'
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from gui import MyMdi


class ObjetoBase(object):
    # ----- Guarda el objeto en la base

    def guardar(self, sesion):
        try:
            sesion.add(self)
            sesion.commit()
            return True
        except IntegrityError:
            sesion.rollback()
            return False
        except InvalidRequestError:
            sesion.rollback()
            sesion.add(self)
            sesion.commit()
            return True

    # ----- Borra el objeto en la base
    def borrar(self, sesion):
        sesion.delete(self)
        sesion.commit()

    # ----- Modifica los datos en la base
    def modificar(self, sesion):
        sesion.commit()

    @classmethod
    def buscarLike(cls, campo, sesion, varBusq):
        return sesion.query(cls).filter(campo.like('%'+varBusq+'%')).order_by(campo)

    @classmethod
    def buscar(cls, campo, sesion, varBusq):
        return sesion.query(cls).filter(campo == varBusq)

    @classmethod
    def buscarTodos(cls, order, sesion):
        return sesion.query(cls).order_by(order)