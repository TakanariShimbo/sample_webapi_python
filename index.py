from flask import Flask, request, jsonify


app = Flask(__name__)


def post_action(req):
    # get data from request
    data_get = req.get_json()
    value1 = data_get['value1']
    value2 = data_get['value2']

    # return result as json
    data_send = {
        'value1': value1,
        'value2': value2
    }
    return jsonify(data_send)


@app.route('/')
def get_index():
    return 'Hello world'


@app.route('/api/', methods=['POST'])
def post_api():
    return post_action(request)


# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=8888, debug=True)
