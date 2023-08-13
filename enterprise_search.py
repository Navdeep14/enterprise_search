from flask import Flask,request
from flask_http_response import success, result, error
import requests

app = Flask(__name__)

@app.route("/search", methods=['GET', 'POST'])
def enterprise_search():
    request_body_json = request.json
    url="http://127.0.0.1:5001/gdrivesearch"
    data_object=request_body_json
    response=requests.post(url=url,json=data_object)
    dict_response=response.json()
    if dict_response['success']==True:
        return success.return_response(message="data found in gdrive",status=200)
    else:
        url="http://127.0.0.1:5002/gmailsearch"
        response=requests.post(url=url,json=data_object)
        dict_response=response.json()
        if dict_response['success']==True:
            return success.return_response(message="data found in gmail",status=200)
        else:
            url="http://127.0.0.1:5003/notionsearch"
            response=requests.post(url=url,json=data_object)
            dict_response=response.json()
            if dict_response['success']==True:
                return success.return_response(message="data found in notion",status=200)
            else:
                url="http://127.0.0.1:5004/slacksearch"
                response=requests.post(url=url,json=data_object)
                dict_response=response.json()
                if dict_response['success']==True:
                    return success.return_response(message="data found in slack",status=200)
                else:
                    return error.return_response(message='data no where found in any app', status=403)

if __name__ == '__main__':
    app.run(debug=True, port=5007)