#Siempre vas a importar
from flask_restful import Resource # esto siempre se importa
from db import db #esto siempre se importa
from flask import request #esto siempre se importa
from schemas import CategorySchema #importamos el schema de la categoria
from pydantic import ValidationError #importamos la libreria de validacion de datos
from models import CategoryModel #importamos el modelo de la categoria


# Para crear tu resource(controlador)
class CategoryResource(Resource):
    def post(self):
        try:
            #Obtener los datos del request y validarlos con el schema
            data = request.get_json()
            validated_data = CategorySchema(name=data["name"])
            new_category = CategoryModel(name=validated_data.name)

            # Guardar la nueva categoría en la base de datos
            db.session.add(new_category)
            db.session.commit()

            return {"message": "Categoria creada exitosamente"}, 201

        except ValidationError as e:
            return {"error": e.errors()}, 400
        except Exception:
            db.session.rollback()
            return {"error": "Ha ocurrido un error en la categoria"}, 500

    def get(self):
        try:
            categories = CategoryModel.query.filter_by(is_active=True)
            result = []
            for category in categories:
                result.append(category.to_json())
            return {
                "msg": "Respuesta exitosa",
                "data": result
            }
        except Exception:
            return{
                "msg": "Hubo un error en el servidor"
            }, 500

