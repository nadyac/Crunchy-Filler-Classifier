#------------------------------------------------------------------------------------ 
#CFNController - Crunchy Filler Notifier Controller, serves the html pages for the 
#   CFN project on a local server and passes the selected show title to the 
#   python scripts that execute the analysis.
#
#NOTE: To run the project, run this file in terminal and go to 127.0.0.1:5000/UI
#------------------------------------------------------------------------------------
from flask import Flask
from DataModules.GetLatestEpisodes import extractData
app = Flask(__name__, static_folder = 'UI', static_url_path='/UI')

@app.route('/UI/', methods=['GET'])
def hello_world():
    return app.send_static_file("index.html")

@app.route('/UI/shows/<name>')
def python_function(name):
    extractData(name)
    
    return app.send_static_file("./shows.html")
    
if __name__ == '__main__':
    app.run(debug=True)