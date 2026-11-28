#Siempre vas a importar

from flask_restful import Resource
from db import db
from flask import request
from schemas import RoleSchema
from pydantic import ValidationError
from models import RoleModel


# Resource para administrar los roles
class RolesResource(Resource):

    # Crear un nuevo rol
    def post(self):
        try:
            # Obtener los datos enviados en formato JSON
            data = request.get_json()

            # Validar todos los datos utilizando Pydantic
            validated_data = RoleSchema.model_validate(data)

            # Crear una instancia del modelo RoleModel
            new_role = RoleModel(name=validated_data.name)

            # Agregar el nuevo registro a la sesión
            db.session.add(new_role)

            # Guardar los cambios en PostgreSQL
            db.session.commit()

            return {
                "message": "Rol creado exitosamente"
            }, 201

        except ValidationError as e:
            return {
                "error": e.errors()
            }, 400

        except Exception as e:
            db.session.rollback()

            return {
                "error": "Ha ocurrido un error al crear el rol"
            }, 500


    # Obtener todos los roles activos
    def get(self):
        try:
            # Consultar únicamente los roles activos
            roles = RoleModel.query.all()

            # Convertir los resultados a formato JSON
            result = []

            for role in roles:
                result.append(role.to_json())

            return {
                "msg": "Respuesta exitosa",
                "data": result
            }, 200

        except Exception as e:
            return {
                "msg": "Hubo un error en el servidor"
            }, 500

