import sys
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd

args = sys.argv
for arg in args[1:]:
    if arg.startswith("-environment="):
        environment = arg.split("=")[1]
        print("Environment:", environment)
        from ML_API.misc.utils import get_path_to_csv, csv_exists


def yesterday_and_today():
    # Get today's date
    today = datetime.now().date()

    # Calculate yesterday's date
    yesterday = today - timedelta(days=1)

    # Format dates as strings in 'YYYY-MM-DD' format
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    today_str = today.strftime('%Y-%m-%d')

    # Return dates in a list
    return [yesterday_str, today_str]
    

def get_nvidia_data(start_date, end_date):
    # Define the ticker symbol for Nvidia
    name = 'NVDA'
    print('should be defined',start_date)
        # Define the time period
    if(not start_date):
        # Yesterday
        start_date = yesterday_and_today()[0]
    if(not end_date):
        # Today
        end_date = yesterday_and_today()[1]
    
    nvidia_data = yf.download(name, start=start_date, end=end_date)
    print('Successfully downloaded NVIDIA data:',nvidia_data)
    return nvidia_data 


# Cleanup below

# def csv_exists(path = '', file_name=''):
#     if(path == ''):
#         path = str(os.getcwd())

#     full_url = path+file_name
#     print('full_url:'+full_url)
#     if(os.path.exists(full_url)):
#         return True
#     else:
#         return False
    
# def get_path_to_csv():
#     return str(os.getcwd()+'/nvidia_stock_prediction/')
#     # csv_exists(os.getcwd()+'/nvidia_stock_prediction/','nvidia_stock_data.csv')


# def save_to_csv(data_frame, desiredFileName):
#     # Get the current working directory
#     cwd = os.getcwd()
    
#     # Define the file path where the CSV file will be saved
#     file_path = os.path.join(cwd, desiredFileName)
    
#     # Save the DataFrame to a CSV file in the working directory
#     data_frame.to_csv(file_path, index=False)
    
#     print(f"CSV file '{desiredFileName}' saved successfully in the working directory.")

# def send_email(message = ''):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(config['sender_email'], config['gmail_app_password'])

#     msg = EmailMessage()

#     message = message + 'from: ' + config['environment']
#     msg.set_content(message)
#     msg['Subject'] = 'Test'
#     msg['From'] = config['sender_email']
#     msg['To'] = config['recipient_email']
#     print('msg:',msg)
#     server.send_message(msg)


# def report_daily():
#     starttime=time.time()
#     interval=86400 
#     while True:
#         send_email('Daily email ran: ')
#         time.sleep(interval - ((time.time() - starttime) % interval))



# Run Functions
# def main():



# main()
