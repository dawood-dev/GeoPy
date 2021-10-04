from flask import Flask
from flask_restful import Api
from utils.db import initialize_db
from Routes.Routes import initialize_routes

app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/geopy'
}

initialize_db(app)
initialize_routes(api)


app.run()
