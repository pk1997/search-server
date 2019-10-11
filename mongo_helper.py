from pymongo import MongoClient

class MongoHelper():
    #connect to mongodb
    def __init__(self, *args, **kwargs):
        self.client = MongoClient()
        self.db = self.client['yolo_data']
        self.mycol = self.db['video_info_times']
        
    #get all data
    def all_data(self):
        data = []
        cursor = self.mycol.find({}).sort('timestamp', -1)
        for document in cursor:
            data.append(document)
        return data

    def data_by_item(self,item):
        data = []
        cursor = self.mycol.find({'item': item})
        for document in cursor:
            data.append(document)
        return data
        
