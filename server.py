from flask import Flask, jsonify, request

app = Flask(__name__)

# Список для хранения объявлений
ads = []
ad_id_counter = 1

@app.route('/ads', methods=['POST'])
def create_ad():
    global ad_id_counter
    data = request.json
    ad = {
        'id': ad_id_counter,
        'title': data['title'],
        'description': data['description'],
        'created_at': data['created_at'],
        'owner': data['owner']
    }
    ads.append(ad)
    ad_id_counter += 1
    return jsonify(ad), 201

@app.route('/ads', methods=['GET'])
def get_ads():
    return jsonify(ads), 200

@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    global ads
    ads = [ad for ad in ads if ad['id'] != ad_id]
    return jsonify({'message': 'Ad deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)