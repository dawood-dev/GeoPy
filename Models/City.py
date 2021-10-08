from utils.db import db


class City(db.Document):

    datasetid  = db.StringField(required=False)
    recordid = db.StringField(required=False)
    fields = db.DynamicField(required=False)
    address = db.StringField(required=False)
    category1 = db.StringField(required=False)
    category2 = db.StringField(required=False)
    name = db.StringField(required=False)
    url = db.URLField(required=False)
    url2 = db.URLField(required=False)
    url3 = db.URLField(required=False)
    mapid = db.StringField(required=False)
    geom = db.PointField(required=False)
    type = db.StringField(required=False)
    coordinates = db.PointField(required=False)
    short_description = db.StringField(required=False)
    geo_local_area = db.StringField(required=False)
    record_timestamp = db.DateTimeField(required=False)

