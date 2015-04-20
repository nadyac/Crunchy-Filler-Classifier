from flask import Flask
from DataModules.GetLatestEpisodes import extractData
app = Flask(__name__, static_folder = 'UI', static_url_path='/UI')

@app.route('/UI/', methods=['GET'])
def hello_world():
    return app.send_static_file("index.html")

@app.route('/UI/shows/<name>')
def python_function(name):
    extractData(name)
    
    return ''
    

if __name__ == '__main__':
    app.run(debug=True)