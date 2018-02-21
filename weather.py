
from flask import Flask, jsonify

app = Flask(__name__)

weathers = [
    {
        'id': 110000,
        'city': 'BeiJing',
        'description': 'rainy',
        'high_template': '15',
        'low_template': '3',
    },
    {
        'id': 310000,
        'city': 'ShangHai',
        'description': 'sunny',
        'high_template': '20',
        'low_template': '6',
    },
    {
        'id': 440100,
        'city': 'GuangZhou',
        'description': 'cloudy',
        'high_template': '25',
        'low_template': '8',
    }
]

@app.route('/')
def index():
    return 'Hello,welcome to query the weathers!'


@app.route('/weather/api/weathers', methods=['GET'])
def get_weathers():
    return jsonify({'weathers': weathers})


from flask import abort

@app.route('/weather/api/weathers/<int:city_id>', methods=['GET'])
def get_city_weather_id(city_id):
    city = list(filter(lambda t: t['id'] == city_id, weathers))
    if len(city) == 0:
        abort(404)
    return jsonify({'weather': city[0]})

@app.route('/weather/api/weathers/<string:city_list>', methods=['GET'])
def get_city_weather(city_list):
    city = list(filter(lambda t: t['city'] == city_list, weathers))
    if len(city) == 0:
        abort(404)
    return jsonify({'weather': city[0]})

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

from flask import request
#执行用 curl -i -H "Content-Type: application/json" -X POST -d
# '{"id":"440100","city":"ShenZhen","description":"runny","high_template":"22","low_template":"10"}'
#  http://localhost:5000/weather/api/weathers
@app.route('/weather/api/weathers', methods=['POST'])
def create_task():
    if not request.json or not 'id' in request.json:
        abort(400)
    weather = {
        'id': request.json['id'],
        'city': request.json['city'],
        'description': request.json.get('description', ""),
        'high_template': request.json['high_template'],
        'low_template': request.json['low_template']
    }
    weathers.append(weather)
    return jsonify({'weather': weather}), 201

if __name__ == '__main__':
    app.run(debug=True,port=5000)

