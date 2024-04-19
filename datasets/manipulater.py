import pandas as pd

def remove_column(fileName, columnName):
    df = pd.read_csv('./fake_or_not_upload_test.csv')
    print(df)
    df.drop('fake', axis=1, inplace=True)
    print(df)
    df.to_csv('./fake_or_not_upload_test.csv', index=False)

remove_column('./fake_or_not_upload_test.csv','fake')