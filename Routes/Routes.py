from Controllers.CityController import GeoPy, CitiesApi, CityApi


def initialize_routes(api):
    api.add_resource(GeoPy, '/')
    api.add_resource(CitiesApi, '/api/cities')
    api.add_resource(CityApi, '/api/cities/<id>')
