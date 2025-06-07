import pandas as pd

#importing and reading input files
file_path_1 = r'C:\Users\Reshika\OneDrive\Documents\PD Datasets\PD 2024 Wk 2 Input (1).csv'
file_path_2 = r'C:\Users\Reshika\OneDrive\Documents\PD Datasets\PD 2024 Wk 2 Input (2).csv'
data_1 = pd.read_csv(file_path_1)
data_2 = pd.read_csv(file_path_2)

#union both datasets
union_data = pd.concat([data_1, data_2])

#convert data into quarter number
union_data['Date'] = pd.to_datetime(union_data['Date'], dayfirst=True)
union_data['Quarter_1'] = union_data['Date'].dt.to_period('Q')

#splitting the quarter field to get rid of year
union_data['Quarter_1'] = union_data['Quarter_1'].astype(str)
union_data['Quarter_1'] = union_data['Quarter_1'].str.split('Q')

#assigning quarter number to field
union_data['Quarter'] = union_data['Quarter_1'].str[1]

#aggregating data, group by quarter, flow card and class, aggregation median, min and max
aggregrated_data = union_data.groupby(['Quarter', 'Flow Card?', 'Class']).agg({
    'Price': ['median', 'min', 'max']
}).reset_index()

#renaming aggregated columns
aggregrated_data.columns = ['Quarter', 'Flow Card?', 'Class', 'Median Price', 'Min Price', 'Max Price']

#creating median price dataset
keep_median_price = ['Min Price', 'Max Price']
median_data = aggregrated_data.drop(columns=keep_median_price)

#pivoting flow card and price
median_data = median_data.pivot(index=['Quarter', 'Flow Card?'], columns='Class', values='Median Price')

#renaming columns for economy and first class
median_data = median_data.rename(columns={'Economy': 'First ', 'First Class': 'Economy', 'Business Class': 'Premium', 'Premium Economy': 'Business'})

#creating min price dataset
keep_min_price = ['Median Price', 'Max Price']
min_data = aggregrated_data.drop(columns=keep_min_price)

#pivoting flow card and price
min_data = min_data.pivot(index=['Quarter', 'Flow Card?'], columns='Class', values='Min Price')

#renaming columns for economy and first class
min_data = min_data.rename(columns={'Economy': 'First ', 'First Class': 'Economy', 'Business Class': 'Premium', 'Premium Economy': 'Business'})

#creating max price dataset
keep_max_price = ['Median Price', 'Min Price']
max_data = aggregrated_data.drop(columns=keep_max_price)

#pivoting flow card and price
max_data = max_data.pivot(index=['Quarter', 'Flow Card?'], columns='Class', values='Max Price')

#renaming columns for economy and first class
max_data = max_data.rename(columns={'Economy': 'First ', 'First Class': 'Economy', 'Business Class': 'Premium', 'Premium Economy': 'Business'})

#union data abck together
cleaned_data = pd.concat([median_data, min_data, max_data])

#resetting index
cleaned_data = cleaned_data.reset_index()

#checking data by printing
print(cleaned_data)

#writing to csv file
cleaned_data.to_csv('aggregated_data.csv', index=False)
