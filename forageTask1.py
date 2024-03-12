# import pandas as pd

# # Read the CSV file into a dataframe
# df = pd.read_csv("transactions.csv")

# # Display the dataframe
# print(df)

# import pandas as pd

# # Read the CSV file into a dataframe
# df = pd.read_csv("transactions.csv")

# # Get the column names as a list
# column_names = df.columns.tolist()

# # Print the column names
# print(column_names)


# import pandas as pd

# # Read the CSV file into a dataframe
# df = pd.read_csv("transactions.csv")

# # Get the column names as a list
# column_names = list(df.columns)

# # Print the column names
# print(column_names)




# import pandas as pd

# # Read the CSV file into a dataframe
# df = pd.read_csv("transactions.csv")

# # Set the value of k
# k = 5

# # Get the first k rows
# first_k_rows = df.head(k)

# # Print the first k rows
# print(first_k_rows)


# import pandas as pd

# # Read the CSV file into a dataframe
# df = pd.read_csv("transactions.csv")

# # Get the top 10 transaction destinations with frequencies
# top_destinations = df["Destination"].value_counts().head(10)

# # Print the top destinations and their frequencies
# print(top_destinations)

# import pandas as pd

# # Read the CSV file into a dataframe
# df = pd.read_csv("transactions.csv")

# # Check if 'Fraud' column exists in the dataframe
# if 'Fraud' in df.columns:
#     # Filter rows where fraud was detected
#     fraud_detected_rows = df[df["Fraud"] == True]

#     # Print the filtered rows
#     print(fraud_detected_rows)
# else:
#     print("Column 'Fraud' not found in the dataframe.")


# import pandas as pd

# # Read the CSV file into a dataframe
# df = pd.read_csv("transactions.csv")

# # Group the dataframe by 'Source' and calculate the number of distinct destinations
# distinct_destinations = df.groupby('Source')['Destination'].nunique()

# # Create a new dataframe with the calculated values and sort in descending order
# result_df = pd.DataFrame({'DistinctDestinations': distinct_destinations}).reset_index().sort_values(by='DistinctDestinations', ascending=False)

# # Print the resulting dataframe
# print(result_df)












