import time
import smtplib
import os
import threading
import sys

from email.message import EmailMessage
from env_secrets import config


def report_daily(reported_material=''):
    starttime=time.time()
    interval=86400 
    while True:
        message = 'Daily email ran with value: '+str(reported_material)+'. '
        send_email(message)
        # time.sleep(interval - ((time.time() - starttime) % interval))


def send_email(message = ''):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config['sender_email'], config['gmail_app_password'])

    msg = EmailMessage()

    message = message + 'from: ' + config['environment']
    msg.set_content(message)
    msg['Subject'] = 'Test'
    msg['From'] = config['sender_email']
    msg['To'] = config['recipient_email']
    print('msg:',msg)
    server.send_message(msg)

def save_to_csv(data_frame, desiredFileName):
    # Get the current working directory
    cwd = os.getcwd()
    
    # Define the file path where the CSV file will be saved
    file_path = os.path.join(cwd, desiredFileName)
    
    print('data_frame:',data_frame)
    # Save the DataFrame to a CSV file in the working directory
    print('attempting to save dataframe to path:',file_path)
    try:
        data_frame.to_csv(file_path, index=True)
        print(f"CSV file '{desiredFileName}' saved successfully in the working directory.")
    except:
        print('attempted to save dataframe but path was wrong')
        pass
    

def csv_exists(path = '', file_name=''):
    if(path == ''):
        path = str(os.getcwd())

    full_url = path+file_name
    print('full_url:'+full_url)
    if(os.path.exists(full_url)):
        return True
    else:
        return False
    
def get_path_to_csv():
    return str(os.getcwd()+'/nvidia_stock_prediction/')
    # csv_exists(os.getcwd()+'/nvidia_stock_prediction/','nvidia_stock_data.csv')

def append_to_csv(path, row):
    with open(path,'a') as fd:
        fd.write(row)

def add_module_directories_to_os():
    # This works by setting a high-up directory, hoisting up our view of the structure.
    sys.path.insert(0, str(config['models_path']))