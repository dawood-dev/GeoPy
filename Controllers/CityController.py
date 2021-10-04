from flask import Response, request
from Models.City import City
from flask_restful import Resource


class CitiesApi(Resource):
    def get(self):
        cities = City.objects().to_json()
        return Response(cities, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        city = City(**body).save()
        id = city.id
        return {'id': str(id)}, 200


class CityApi(Resource):
    def get(self, id):
        city = City.objects.get(id=id).to_json()
        return Response(city, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        City.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        City.objects.get(id=id).delete()
        return '', 200
