from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
import enum
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Administrador(db.Model):
    id_administrador = db.Column(db.Intpeger, primarpiy_key=True)
    nombre_administrador = db.Column(db.String(128))
    contraseña = db.Column(db.String(128))
    email = db.Column(db.String(128))
    telefono = db.Column(db.String(20))

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    contraseña = db.Column(db.String(128))
    tipo = db.Column(db.String(20))
    albumes = db.relationship('Album', cascade='all, delete, delete-orphan')

class Empleado(db.Model):
    id_empleado = db.Column(db.Integer, primary_key=True)
    nombre_empleado = db.Column(db.String(128))
    contraseña = db.Column(db.String(128))
    email = db.Column(db.String(128))
    direccion = db.Column(db.String(256))
    telefono = db.Column(db.String(20))

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    contraseña = db.Column(db.String(128))
    direccion = db.Column(db.String(256))
    email = db.Column(db.String(128))

class CarritoCompras(db.Model):
    id_carrito = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    cantidad = db.Column(db.Integer)

class Factura(db.Model):
    id_factura = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    nombre_cliente = db.Column(db.String(128))
    subtotal = db.Column(db.Integer)
    total = db.Column(db.Integer)

class Calzado(db.Model):
    id_calzado = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(128))
    talla = db.Column(db.String(10))
    tipo = db.Column(db.String(50))
    color = db.Column(db.String(50))
    precio = db.Column(db.String(20))
    composicion = db.Column(db.String(256))
    detalles_producto = db.Column(db.String(512))
    disponibilidad = db.Column(db.String(50))

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3

albumes_canciones = db.Table('album_cancion',
    db.Column('album_id', db.Integer, db.ForeignKey('album.id_album'), primary_key=True),
    db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id_cancion'), primary_key=True)
)

class Cancion(db.Model):
    id_cancion = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    albumes = db.relationship('Album', secondary='album_cancion', back_populates='canciones')

class Album(db.Model):
    id_album = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.String(512))
    medio = db.Column(db.Enum(Medio), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    canciones = db.relationship('Cancion', secondary='album_cancion', back_populates='albumes')
    usuario = db.relationship('Usuario', back_populates='albumes')
    __table_args__ = (db.UniqueConstraint('usuario_id', 'titulo', name='titulo_unico_album'),)


