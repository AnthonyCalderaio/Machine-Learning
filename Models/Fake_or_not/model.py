import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

dataset_base_url = '../../datasets'

# Functions
def setHeaders(dataSet):
    dataSet.columns = ['stars','title','description']
    dataSet.columns = ['stars','title','description']
    dataSet['fake'] = 0

    dataSet.to_csv(dataset_base_url+'/tain_example.csv', index=False)


def run():
    # Load the dataset
    real_reviews_dataSet = pd.read_csv(dataset_base_url+'/tain_example.csv')
    # setHeaders(dataSet)

    # Features. i.e: descriptions
    X = real_reviews_dataSet.iloc[:, 2:3].values;

    # Preprocessing
    # Assuming 'description' column contains the review text
    # Clean the text data, remove punctuation, stopwords, etc.

    # Feature Extraction
    tfidf_vectorizer = TfidfVectorizer(max_features=1000)  # Adjust max_features as needed
    X = tfidf_vectorizer.fit_transform(X[0])

    y = real_reviews_dataSet['fake'].values  # Assuming 'fake' column contains labels (0 for genuine, 1 for fake)
    X = real_reviews_dataSet.iloc[:, 2:3].values;

    # Split the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model Training
    # model = LogisticRegression()
    # model.fit(X_train, y_train)

    # Evaluation
    # y_pred = model.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy:", accuracy)

    # Deployment
    # Save the model for future use