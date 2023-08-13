from flask import Flask,request
from flask_http_response import success, result, error

app = Flask(__name__)

gmail_data=[]

@app.route("/addgmail")
def add_data_gmail():
    request_body_json = request.json
    print(request_body_json)
    gmail_data.append(request_body_json['name'])
    gmail_data.append(request_body_json['email'])
    gmail_data.append(request_body_json['subject'])
    print(gmail_data)
    return success.return_response(message='Data Successfully stored in gmail ', status=200)


@app.route("/gmailsearch",methods=['GET', 'POST'])
def search_gmail():
    request_body_json = request.json
    data=request_body_json['data']
    if data in gmail_data:
        return success.return_response(message="data found in gmail",status=200)
    else:
        return error.return_response(message="data not found in gmail try somewhere else", status=403)
    

    

if __name__ == '__main__':
    app.run(debug=True, port=5002)