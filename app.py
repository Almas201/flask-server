from flask import Flask, request, jsonify
from check_credentials import check_credentials
from prepocess import preprocess
import json

app = Flask(__name__)

@app.route('/check-credentials', methods=['POST'])
def handle_login():
    # Get the username and password from the request
    username = request.form['username']
    password = request.form['password']
    print('username = {}\npassword = {}'.format(username, password))
    # Check the credentials using Selenium WebDriver
    result, content = check_credentials(username, password)
    content = preprocess(content)
    # Return the result as a JSON object
    if result == False:
        # print("False")
        # return json({"result": "False"})
        return json.dumps({"result": "False"}) 
    else:
        # print(content)
        # return json({"result": content})
        return json.dumps({"result" : content}, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
