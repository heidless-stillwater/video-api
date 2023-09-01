from flask import Flask, render_template
from flask_restful import Api, Resource
import datetime

app = Flask(__name__)
api = Api(app)

@app.route('/test')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

class HelloWorld(Resource):
  def get(self):
    return {"data": "Hello World"}
#    return render_template("index.html")

api.add_resource(HelloWorld, '/helloworld')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
  
  
