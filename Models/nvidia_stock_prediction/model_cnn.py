import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from yahoo_fin import stock_info
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from sklearn.metrics import mean_squared_error

# Function to fetch stock data from Yahoo Finance API
def fetch_stock_data(symbol, start_date, end_date):
    stock_data = stock_info.get_data(symbol, start_date, end_date)
    return stock_data

# Function to preprocess the data
def preprocess_data(data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.reshape(-1, 1))
    return scaled_data, scaler

# Function to create sequences for the CNN
def create_sequences(data, sequence_length):
    # print('hi there',data[1:5])
    sequences = []
    for i in range(len(data) - sequence_length):
        # print('len:',str(data[i : i + sequence_length]))
        sequences.append(data[i : i + sequence_length])
    print('done:')
    print(np.array(sequences))
    return np.array(sequences)

# Fetch Nvidia stock data
symbol = "NVDA"
start_date = "2020-01-01"
end_date = "2023-01-01"
stock_data = fetch_stock_data(symbol, start_date, end_date)
close_prices = stock_data['close'].values

# Preprocess the data
scaled_data, scaler = preprocess_data(close_prices)

# Create sequences for the CNN
sequence_length = 10
X = create_sequences(scaled_data, sequence_length)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, scaled_data[sequence_length:], test_size=0.2, random_state=42)

# Build the CNN model
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(sequence_length, 1)))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# # Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=2)

# # Evaluate the model
loss = model.evaluate(X_test, y_test)
squared_errors = mean_squared_error(model.predict(X_test), y_test)
print("Test Loss:", loss)
print('RSquaredL',squared_errors)
print('----model.predict(X_test)')
print(model.predict(X_test))


# # Plotting the training and validation loss
# plt.plot(history.history['loss'], label='Training Loss')
# plt.plot(history.history['val_loss'], label='Validation Loss')
# plt.title('Model Loss')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()

# # Predictions
# predictions = model.predict(X_test)

# # Inverse scaling to get actual prices
# predicted_prices = scaler.inverse_transform(predictions)
# actual_prices = scaler.inverse_transform(y_test.reshape(-1, 1))

# # Plotting actual vs predicted prices
# plt.plot(actual_prices, label='Actual Prices')
# plt.plot(predicted_prices, label='Predicted Prices')
# plt.title('Nvidia Stock Price Prediction')
# plt.xlabel('Time')
# plt.ylabel('Stock Price')
# plt.legend()
# plt.show()
