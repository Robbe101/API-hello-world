from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#Make class inherited from Resource 
class Algorithm(Resource):
    def get(self):
            return {"Data" : "Hello World"}

    def post(self):
            return {"Data" : "Data postes"}
    
    
#Add resource to our API
api.add_resource(Algorithm, "/")

if __name__ == "__main__":
    app.run(debug=True)
