__author__ = 'waldo'
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.orm.exc import FlushError
class ObjetoBase(object):
    def __init__(self):
        self.baja = False

    def getBaja(self):
        return self.baja

    def setBaja(self, baja):
        self.baja = baja

    # ----- Guarda el objeto en la base
    def guardar(self, sesion):
        try:
            sesion.add(self)
            sesion.commit()
            return True
        except IntegrityError:
            sesion.rollback()
            return False
        except FlushError:
            sesion.rollback()
            return False
        except InvalidRequestError:
            sesion.rollback()
            sesion.add(self)
            sesion.commit()
            return True

    # ----- Baja logica del objeto en la base
    def borrar(self, sesion):
        self.setBaja(True)
        sesion.commit()

    # ----- Modifica los datos en la base
    def modificar(self, sesion):
        sesion.commit()

    # ----- Alta del objeto que fue dado de baja
    def alta(self, sesion):
        self.setBaja(False)
        sesion.commit()

    @classmethod
    def buscarLike(cls, campo, sesion, varBusq):
        return sesion.query(cls).filter(campo.like('%'+varBusq+'%'), cls.baja == False).order_by(campo)

    @classmethod
    def buscarAlta(cls, campo, sesion, varBusq):
        return sesion.query(cls).filter(campo == varBusq, cls.baja == False)

    #Busca todos los objetos que no esten dados de baja
    @classmethod
    def buscarTodos(cls, campo, sesion):
        if hasattr(cls, 'baja'):
            return sesion.query(cls).filter(cls.baja == False).order_by(campo)
        else:
            return sesion.query(cls).order_by(campo)

    #Busca el objeto en la base este o no dado de baja
    @classmethod
    def buscar(cls, campo, sesion, varBusq):
        return sesion.query(cls).filter(campo == varBusq)