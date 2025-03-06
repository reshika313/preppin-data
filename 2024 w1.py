import pandas as pd

file_path = r'C:\Users\Reshika\OneDrive\Documents\PD Datasets\PD 2024 Wk 1 Input.csv'
data = pd.read_csv(file_path)


data['Flight Details'] = data['Flight Details'].str.split('//')

data['Date'] = data['Flight Details'].str[0]
data['Flight Number'] = data['Flight Details'].str[1]
data['From - To'] = data['Flight Details'].str[2]
data['Class'] = data['Flight Details'].str[3]
data['Price'] = data['Flight Details'].str[4]



data['From - To'] = data['From - To'].str.split('-')


data['From'] = data['From - To'].str[0]
data['To'] = data['From - To'].str[1]


data['Date'] = pd.to_datetime(data['Date'])
data['Price'] = data['Price'].astype(float)


data['Flow Card?'] = data['Flow Card?'].replace({1: 'yes', 0: 'no'})


removed_fields = ['Flight Details', 'From - To']
data = data.drop(columns = removed_fields)

yes_flow_card_data = data[data['Flow Card?'] == 'yes']
no_flow_card_data = data[data['Flow Card?'] == 'no']

print(yes_flow_card_data)
print(no_flow_card_data)

yes_flow_card_data.to_csv('yes_flow_card_data', index=False)
no_flow_card_data.to_csv('no_flow_card_data', index=False)