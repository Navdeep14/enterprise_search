from flask import Flask,request
from flask_http_response import success, result, error

app = Flask(__name__)

slack_data=[]

@app.route("/addslack")
def add_data_slack():
    request_body_json = request.json
    print(request_body_json)
    slack_data.append(request_body_json['sender'])
    slack_data.append(request_body_json['reciever'])
    slack_data.append(request_body_json['message'])
    slack_data.append(request_body_json['mobile_number'])
    print(slack_data)
    return success.return_response(message='Data Successfully stored in slack ', status=200)


@app.route("/slacksearch",methods=['GET', 'POST'])
def search_slack():
    request_body_json = request.json
    data=request_body_json['data']
    if data in slack_data:
        return success.return_response(message="data found in slack",status=200)
    else:
        return error.return_response(message="data not found in slack try somewhere else", status=403)
    

    

if __name__ == '__main__':
    app.run(debug=True, port=5004)