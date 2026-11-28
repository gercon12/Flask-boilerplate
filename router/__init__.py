from flask_restful import Api
from resources import UserResource, CategoryResource, RolesResource  # Importar CategoriesResource

def register_routes(api: Api):
    api.add_resource(UserResource, "/api/users")
    api.add_resource(CategoryResource, "/api/v1/category")  # Agregar la ruta para CategoriesResource
    api.add_resource(RolesResource, "/api/v1/roles")
