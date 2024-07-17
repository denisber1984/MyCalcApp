from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    total = request.form['total']
    tip_percentage = request.form['tip']
    num_people = request.form['people']

    if not all([total, tip_percentage, num_people]):
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        response = requests.post(
            'http://calc-app:5000/calculate',
            json={'total': total, 'tip': tip_percentage, 'people': num_people}
        )
        result = response.json()
        return render_template('result.html', result=result['result'])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
