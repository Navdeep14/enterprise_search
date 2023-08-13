from flask import Flask,request
from flask_http_response import success, result, error

app = Flask(__name__)

notion_data=[]

@app.route("/addnotion")
def add_data_notion():
    request_body_json = request.json
    print(request_body_json)
    notion_data.append(request_body_json['author'])
    notion_data.append(request_body_json['subject'])
    notion_data.append(request_body_json['data'])
    print(notion_data)
    return success.return_response(message='Data Successfully stored in notion ', status=200)


@app.route("/notionsearch",methods=['GET', 'POST'])
def search_notion():
    request_body_json = request.json
    data=request_body_json['data']
    if data in notion_data:
        return success.return_response(message="data found in notion",status=200)
    else:
        return error.return_response(message="data not found in notion try somewhere else", status=403)
    


if __name__ == '__main__':
    app.run(debug=True, port=5003)