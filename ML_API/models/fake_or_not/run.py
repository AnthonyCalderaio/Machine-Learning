import pickle
import os
import io
import pandas as pd
from flask import send_file

from pathlib import Path
from io import BytesIO


parent_folder =  '.' if os.environ.get("AWS_EXECUTION_ENV") is not None else 'models/fake_or_not'

# load the deployed model
with open(parent_folder+'/fake_or_not.pkl', 'rb') as f:
    model = pickle.load(f)

with open(parent_folder+'/fake_or_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

def test():
    predictionStatement_real = 'I heard about this book, so I wanted to read it to see if it was as funny and stupid (unintentionally) as I heard.I was not disappointed. Few things in life are free, and sex is defintely not among them.The perfect coda to this book is that the couple got divroced several years after publishing this book. You can\'t make this stuff up.'
    predictions = model.predict(tfidf_vectorizer.transform([predictionStatement_real]))

def predictComment(comment):
    return str(model.predict(tfidf_vectorizer.transform([comment]))).strip("[]")

def print_axis(axis):
    print('printing axis...')
    print(axis['description'])

def process_csv(file):
    # Turn file to byte stream
    byte_stream = BytesIO(file.read())

    # Move the stream position to the beginning
    byte_stream.seek(0)  

    # Decode the byte stream to a string
    decoded_string = byte_stream.read().decode('utf-8')  

    # Create a file-like object from the decoded string
    csv_file_like_object = io.StringIO(decoded_string)

    # Read the CSV data from the file-like object into a pandas DataFrame
    df = pd.read_csv(csv_file_like_object)

    # Now you have your DataFrame ready to use
    df['fake'] = df['review'].apply(predictComment)

    csv_data = df.to_csv(index=False)  # Convert DataFrame to CSV format
    # return send_file('../datasets/fake_or_not_upload_test.csv', as_attachment=True)
    return send_file(
        io.BytesIO(csv_data.encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='data.csv'
    )
