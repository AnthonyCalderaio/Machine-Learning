import io
import os
import sys
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS


from misc.utils import save_to_csv, add_module_directories_to_os, get_files_from_folder
add_module_directories_to_os()

from models.fake_or_not.run  import predictComment, process_csv
from env_secrets import config

home_dir = str(config['models_path'])

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to Anthony\'s Machine Learning API'

@app.route('/version', methods=['GET'])
def version():
    return jsonify({'version':'1.0.0'})


# Define a route for your API endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/getCurrentDir', methods=['GET'])
def currDir():
    dir = str(os.listdir(sys.path[0]))
    print(dir)
    return dir

# Stock predictor route
    # TODO: 
    # 1) Make this route only send the plot.
    # 2) Move the model creation to outside the API(See fake_or_not)
    # 3) The API should only serve data. Models are deployed and fetched in other folders.
# @app.route('/nvidia_prediction', methods=['GET'])
# def nvidia_predictor():
#     # Pass the JSON data to a function in another file
    
#     image = get_todays_nvidia_prediction()
#     # Return the response in JSON format
#     return send_file(image, as_attachment=True)

# Fake or not review route
@app.route('/fake_or_not', methods=['POST'])
def fake_or_not():
    input_json = request.get_json(force=True) 
    return str(predictComment(input_json['review']))

@app.route('/fake_or_not_bulk', methods=['POST'])
def fake_or_not_bulk():
    return process_csv(file = request.files['file'])


@app.route('/credit_card_fraud', methods=['GET'])
def credit_card_fraud():
    files_to_send = get_files_from_folder('./models/credit_card_fraud')
    return jsonify(files_to_send)

@app.route('/download_csv', method=['GET'])
def download_csv():
    # Convert DataFrame to CSV
    csv_buffer = io.StringIO()

    dataframe = '../LeagueChamp'
    csv_buffer.seek(0)

    # Send CSV file
    response = make_response(csv_buffer.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.mimetype = 'text/csv'
    return response

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
    
