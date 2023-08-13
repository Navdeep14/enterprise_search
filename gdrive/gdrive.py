from flask import Flask,request
from flask_http_response import success, result, error

app = Flask(__name__)

gdrive_data=[]

@app.route("/addgdrive")
def add_data_gdrive():
    request_body_json = request.json
    print(request_body_json)
    gdrive_data.append(request_body_json['name'])
    gdrive_data.append(request_body_json['age'])
    gdrive_data.append(request_body_json['city'])
    print(gdrive_data)
    return success.return_response(message='Data Successfully stored in gdrive', status=200)


@app.route("/gdrivesearch",methods=['GET', 'POST'])
def search_gdrive():
    request_body_json = request.json
    data=request_body_json['data']
    if data in gdrive_data:
        return success.return_response(message="data found in gdrive",status=200)
    else:
        return error.return_response(message="data not found in gdrive try somewhere else", status=403)
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)