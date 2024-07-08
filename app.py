from flask import Flask
from flask_restful import Api, Resource
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)


#Make class inherited from Resource 
class Algorithm(Resource):

    data = pd.read_excel("data.xlsx")
    dt = data.to_json()
    print(dt)
    data2 = dt.

    #Read data for server
    def get(self):
            return {"Data" : "Hello World"}
    
    #Add new data to server
    def post(self, data):
            df = data.read
            return {"Data" : "Data posted"}
    
    #Change data on server
    def put(self):
          return {"Data" : "Data put"}
    
    #Delete data from server
    def delete(self):
          return {"Data" : "Data deleted"}

#Add resource to our API
api.add_resource(Algorithm, "/")

if __name__ == "__main__":
    #put arg host = "IP" to change access IP
    app.run(debug=True)
