from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    total = float(data.get("total"))
    tip_percentage = int(data.get("tip"))
    num_people = int(data.get("people"))

    tip_amount = total * (tip_percentage / 100)
    new_total = total + tip_amount

    per_person = new_total / num_people
    final_amount = round(per_person, 2)
    final_amount = "{:.2f}".format(per_person)

    return jsonify({"result": f"Each person should pay: {final_amount} shekels"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
