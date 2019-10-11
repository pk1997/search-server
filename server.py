import cherrypy
import mongo_helper
import json
import timeago, datetime


class MongoServer(object):
    @cherrypy.expose
    def index(self):
        obj = mongo_helper.MongoHelper()
        data = obj.all_data()
        now = datetime.datetime.now()
        for item in data:
            item['timestamp'] = datetime.datetime.utcfromtimestamp(item['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        data = data
        return(json.dumps(data, default=str))        

    @cherrypy.expose
    def item(self, item = "none"):
        obj = mongo_helper.MongoHelper()
        return(json.dumps(obj.data_by_item(item),default=str))


cherrypy.quickstart(HelloWorld())

