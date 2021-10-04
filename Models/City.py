from utils.db import db


class City(db.Document):

    datasetid  = db.StringField(required=True)
    recordid = db.StringField(required=True)
    fields = db.DynamicField(required=True)
    address = db.StringField(required=True)
    category1 = db.StringField(required=True)
    category2 = db.StringField(required=True)
    name = db.StringField(required=True)
    url = db.URLField(required=True)
    url2 = db.URLField(required=False)
    url3 = db.URLField(required=False)
    mapid = db.StringField(required=True)
    geom = db.PointField(required=True)
    url3 = db.URLField(required=True)
    short_description = db.StringField(required=True)
    geo_local_area = db.StringField(required=True)
    record_timestamp = db.DateTimeField(required=True)

