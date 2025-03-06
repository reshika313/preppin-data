import pandas as pd

#opening and reading input file
file_path = r'C:\Users\Reshika\OneDrive\Documents\PD Datasets\PD 2024 Wk 1 Input.csv'
data = pd.read_csv(file_path)

#splitting flight details field
data['Flight Details'] = data['Flight Details'].str.split('//')

#renaming split fields
data['Date'] = data['Flight Details'].str[0]
data['Flight Number'] = data['Flight Details'].str[1]
data['From - To'] = data['Flight Details'].str[2]
data['Class'] = data['Flight Details'].str[3]
data['Price'] = data['Flight Details'].str[4]


#splitting from - to field
data['From - To'] = data['From - To'].str.split('-')

#renaming split fields
data['From'] = data['From - To'].str[0]
data['To'] = data['From - To'].str[1]

#converting data types
data['Date'] = pd.to_datetime(data['Date'])
data['Price'] = data['Price'].astype(float)

#replacing values in flow card field
data['Flow Card?'] = data['Flow Card?'].replace({1: 'yes', 0: 'no'})

#removing unwanted fields
removed_fields = ['Flight Details', 'From - To']
data = data.drop(columns = removed_fields)

#assiging new fields based on values
yes_flow_card_data = data[data['Flow Card?'] == 'yes']
no_flow_card_data = data[data['Flow Card?'] == 'no']

#printing final dataset
print(yes_flow_card_data)
print(no_flow_card_data)

#writing to two new files
yes_flow_card_data.to_csv('yes_flow_card_data', index=False)
no_flow_card_data.to_csv('no_flow_card_data', index=False)
