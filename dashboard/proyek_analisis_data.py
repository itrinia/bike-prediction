# Proyek Analisis Data: Bike Sharing Dataset
# - Nama: Ileene Trinia Santoso
# - Email: m197d4kx2730@bangkit.academy
# - ID Dicoding: ileene

# business questions
# Question 1: How are bike loan patterns affected by variables such as weather, seasons, days of the week, and hours of the day (or even other variables that related to the bike loan)?
#   Even if bike loan patterns are affected, is it possible to find patterns in the historical data that show a correlation between these variables and bike loan rates?
# Question 2: Can certain patterns in bicycle loan data help in organizing bicycle inventory? 
#   For example, does the demand for bicycles increase or decrease during certain seasons? In what ways can these patterns be used to maximize the distribution of bicycles in a particular place?

# =====IMPORT LIB======
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# =====DATA PREPROCESSING/DATA WRANGLING======
# A. GATHERING DATA
# since there are 2 csv datasets, i consider to merge it so it can provide a more detailed and complete picture of bike-sharing patterns -> using inner join
# Load 'day.csv' and 'hour.csv'
df_day = pd.read_csv('./data/day.csv')
df_hour = pd.read_csv('./data/hour.csv')

# df_day.head(10)
# df_hour.head(10)

# B. ASSESING DATA - check for data types, missing values, or the other issues
# print("\nInformation about the merged df:")
# df_day.info()
# df_hour.info()
season_mapping = {1: "springer", 2: "summer", 3: "fall", 4: "winter"}
df_day["season"].replace(season_mapping, inplace=True)

yr_mapping = {0: 2011, 1: 2012}
df_day["yr"].replace(yr_mapping, inplace=True)

month_mapping = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
df_day["mnth"].replace(month_mapping, inplace=True)

holiday_mapping = {0: "no", 1: "yes"}
df_day["holiday"].replace(holiday_mapping, inplace=True)

weekday_mapping = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
df_day["weekday"].replace(weekday_mapping, inplace=True)

workingday_mapping = {0: "no", 1: "yes"}
df_day["workingday"].replace(workingday_mapping, inplace=True)

weather_mapping = {1: "clear", 2: "mist", 3: "light rain", 4: "heavy rain"}
df_day["weathersit"].replace(weather_mapping, inplace=True)

# df_day.head(10)
# df_day.info()
# print("\nUnique values in categorical columns:")
# for column in df_day.select_dtypes(include='object').columns:
#     print(f"{column}: {df_day[column].nunique()} unique values")

#  C. CLEANING DATA
# drop the duplicates data
df_day = df_day.drop_duplicates()
df_day = df_hour.drop_duplicates()

# make sure there's no missing values (if there's missing values, then ill replace it with the mean of the column)
# check for missing values in the entire df
missing_values = df_day.isnull().sum()
missing_values = df_hour.isnull().sum()

# display the missing values
columns_with_missing_values = missing_values[missing_values > 0]
# print(columns_with_missing_values)


# =====EDA======
# check for summary statistics to understand the distribution of numerical columns using 'describe' method
# df_day.describe()
# df_hour.describe()

# adding new feature (hour category to df_hour)
df_hour['hour_category'] = pd.cut(df_hour['hr'], bins=[-1, 5, 11, 17, 23], labels=['Night', 'Morning', 'Afternoon', 'Evening'])

# checking distribution through list
# df_day.hist()
# df_hour.hist()

# checking correlation
# df_hour.corr()
# df_day.corr()


# =====VISUALIZATION======
# 1️⃣visualization hour categorical to get know what the peak hour for bike loan.
# custom_palette = sns.color_palette("Set1", 2)

# plt.figure(figsize=(18, 10))

# # Bar plot for season
# plt.subplot(2, 3, 1)
# sns.countplot(x='hour_category', data=df_hour, palette=custom_palette)
# plt.title('Distribution of Bike Counts by Hour Categorical')
# plt.xlabel('hour category')
# plt.ylabel('Count')

# plt.tight_layout()
# plt.show()

# 2️⃣ visualization of features df day that might affected to the bike loan 
# Set a custom color palette with two colors
# custom_palette = sns.color_palette("Set1", 2)

# plt.figure(figsize=(18, 10))

# # Bar plot for season
# plt.subplot(2, 3, 1)
# sns.countplot(x='season', data=df_day, palette=custom_palette)
# plt.title('Distribution of Bike Counts by Season')
# plt.xlabel('Season')
# plt.ylabel('Count')

# # Bar plot for weather
# plt.subplot(2, 3, 2)
# sns.countplot(x='weathersit', data=df_day, palette=custom_palette)
# plt.title('Distribution of Bike Counts by Weather')
# plt.xlabel('Weather')
# plt.ylabel('Count')

# # Bar plot for month
# plt.subplot(2, 3, 3)
# sns.countplot(x='mnth', data=df_day, palette=custom_palette)
# plt.title('Distribution of Bike Counts by month')
# plt.xlabel('Month')
# plt.ylabel('Count')

# # Bar plot for weekday
# plt.subplot(2, 3, 4)
# sns.countplot(x='weekday', data=df_day, palette=custom_palette)
# plt.title('Distribution of Bike Counts by weekday')
# plt.xlabel('weekday')
# plt.ylabel('Count')

# # Bar plot for holiday
# plt.subplot(2, 3, 5)
# sns.countplot(x='holiday', data=df_day, palette=custom_palette)
# plt.title('Distribution of Bike Counts by holiday')
# plt.xlabel('holiday')
# plt.ylabel('Count')

# plt.tight_layout()
# plt.show()

# 3️⃣ visualization of lineplot the graphs seasonal demand trend
# # Define start_date and end_date
# start_date = '2011-01-01'
# end_date = '2013-12-31'

# # Filter the DataFrame for the selected date range
# df_selected_range = df_day[(df_day['dteday'] >= start_date) & (df_day['dteday'] <= end_date)]

# fig, ax = plt.subplots(figsize=(12, 8))
# sns.lineplot(x='dteday', y='cnt', data=df_selected_range, label='Line 1')

# ax.set_xlabel('Date')
# ax.set_ylabel('Bike Count')
# ax.set_title('Seasonal Demand Trend (Selected Range)')
# plt.legend()  
# plt.show()

# ==================STREAMLIT==================
sns.set(style='dark')

# converting datetime columns to datetime type
datetime_columns = ["dteday"]
df_day.sort_values(by="dteday", inplace=True)
df_day.reset_index(inplace=True)

for column in datetime_columns:
    df_day[column] = pd.to_datetime(df_day[column])

# filter data
min_date = df_day["dteday"].min()
max_date = df_day["dteday"].max()

# left sidebar
with st.sidebar:
    st.image("https://c02.purpledshub.com/uploads/sites/39/2023/05/Specialized-Rockhopper-Elite-29-climb-243ee75.jpg?w=1029&webp=1")

    # Date range selection
    selected_dates = st.date_input(
        label='Choose your duration',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    # Check if the user provided both start and end dates
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    else:
        # Provide a default value for the end date if only the start date is selected (value that shown is the mean of the all data)
        start_date = selected_dates[0]
        end_date = df_day["dteday"].mean().date()

    # Time duration selection
    st.subheader("Filter Duration Range")
    duration_range = st.slider("Choose the time duration range (in hours)", min_value=0, max_value=24, value=(0, 24))

# Convert start_date and end_date to strings for comparison
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# Filter df_hour based on the selected date and time duration range
filtered_df_hour = df_hour[
    (df_hour['dteday'].astype(str) >= start_date_str) & (df_hour['dteday'].astype(str) <= end_date_str) &
    (df_hour['hr'] >= duration_range[0]) & (df_hour['hr'] <= duration_range[1])
]

# Convert to datetime64[ns] for comparison
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Convert 'dteday' column to Timestamps
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Filter the df based on the selected date range
df_filtered = df_day[(df_day["dteday"] >= start_date) & (df_day["dteday"] <= end_date)]

# =====DATA VISUALIZATION======
# Summary Section
st.header("Highlight of the Day(s)")
st.write("ps: you need to type the date range to see the summary, if you only click the start date (without the end date), it will show the mean of the all data")

# create table for the summary (highlight of the days)
col1, col2, col3 = st.columns(3)

# Total Shared Bikes
total_shared_bikes = filtered_df_hour['cnt'].sum()
col1.metric(label="Total Shared Bikes", value=f"{total_shared_bikes:,}", delta="")

# Total Casual Users
total_casual_users = filtered_df_hour['casual'].sum()
col2.metric(label="Total Casual Users", value=f"{total_casual_users:,}", delta="")

# Total Registered Users
total_registered_users = filtered_df_hour['registered'].sum()
col3.metric(label="Total Registered Users", value=f"{total_registered_users:,}", delta="")



# =============== ANSWERING QUESTIONS===============
# ❓Question 1: How are bike loan patterns affected by variables such as weather, seasons, days of the week, and hours of the day (or even other variables that related to the bike loan)?
# ps: for this question, i will to explore different conditions or metrics that make sense for each variable. for exm, i could check if the variable has a specific trend or if certain values are associated with higher or lower bike loan patterns.
#     for numerical variables, i consider comparing with a specific threshold or range of values that i believe would indicate an impact on bike loan patterns. 

# compare 1 affected with df hour (only display hour categorical)
custom_palette = sns.color_palette("Set1", 2)

# Plotting
plt.figure(figsize=(18, 10))

# Bar plot for season
plt.subplot(2, 3, 1)
sns.countplot(x='hour_category', data=filtered_df_hour, palette=custom_palette)
plt.title('Distribution of Bike Counts by Hour Category')
plt.xlabel('Hour Category')
plt.ylabel('Count')

plt.tight_layout()
# Show the plot
st.pyplot(plt)

# ######################################
# compare 2 affected with df day (season, weathersit, mnth, weekday, holiday)
# let the user select a variable from the limited options because we dont want use the features that are not involve in affecting data

if st.checkbox("Explore Bike Loan Patterns to check how they are affected by different variables"):
    selectable_variables = ["dteday", "season", "weathersit", "mnth", "weekday", "temp", "atemp", "hum", "windspeed"]
    selected_variable = st.selectbox("Select a variable you want to compare", selectable_variables)
    affected_not_affected_text = "NOT affected"
    st.subheader(f"Bike Loan Patterns by {selected_variable}")
    st.write(f"Exploring bike loan patterns based on {selected_variable}")

    fig, ax = plt.subplots(figsize=(10, 6))

    # for categorical variables, assume no clear influence on bike loan patterns
    # Check if the variable is categorical
    if pd.api.types.is_categorical_dtype(df_day[selected_variable].dtype):
        sns.countplot(x=selected_variable, data=df_day)

    # Check if the variable is datetime
    elif pd.api.types.is_datetime64_any_dtype(df_day[selected_variable].dtype):
        threshold_lower = pd.to_datetime('2022-01-01')  
        threshold_upper = pd.to_datetime('2022-12-31')  
        affected_not_affected_text = "affected" if ((df_day[selected_variable] > threshold_lower) & (df_day[selected_variable] < threshold_upper)).any() else "NOT affected"
        sns.histplot(df_day[selected_variable], bins=20, kde=True, ax=ax)

    # Check for specific variables
    elif selected_variable == 'weathersit':
        threshold = 2  
        affected_not_affected_text = "affected" if (df_day[selected_variable] > threshold).any() else "NOT affected"
        sns.histplot(x=selected_variable, data=df_day, ax=ax)

    # Handle other numerical variables
    else:
        threshold_lower = 0
        threshold_upper = 30
        affected_not_affected_text = "affected" if ((df_day[selected_variable] > threshold_lower) & (df_day[selected_variable] < threshold_upper)).any() else "NOT affected"
        sns.histplot(df_day[selected_variable], bins=20, kde=True, ax=ax)

    # display   
    st.write(f"The variable {selected_variable} is {affected_not_affected_text} on bike loan patterns.")
    st.pyplot(fig)



######################
# ❓# Question 2: Can certain patterns in bicycle loan data help in organizing bicycle inventory?
if st.checkbox("Explore Bicycle Inventory Patterns to check seasonal demand for bicycles"):
    # Subquestion 1: Seasonal demand
    st.subheader("Seasonal Demand for Bicycles")
    st.write("Distribution of bike counts across different seasons")

    # creating line plot to visualize seasonal demand for the selected date range
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Filter the DataFrame for the selected date range
    df_selected_range = df_day[(df_day['dteday'] >= start_date) & (df_day['dteday'] <= end_date)]
    
    if not df_selected_range.empty:
        sns.lineplot(x='dteday', y='cnt', data=df_selected_range, ax=ax)
        ax.set_xlabel('Date')
        ax.set_ylabel('Bike Count')
        ax.set_title('Seasonal Demand Trend (Selected Range)')

        # determine if demand is increasing or decreasing based on the entire dataset
        demand_trend = "INCREASING" if df_selected_range['cnt'].mean() > df_day['cnt'].mean() else "DECREASING"
        st.write(f"The overall demand for bicycles is {demand_trend} during the selected period.")
        st.pyplot(fig)
    else:
        st.write("No data available for the selected date range.")

    ########################################
    # Subquestion 2: Maximize Bicycle Distribution
    st.subheader("✨Maximize Bicycle Distribution✨")
    st.write("Explore strategies to maximize bicycle distribution:")

    # Strategy 1: Location-Based Distribution
    st.write("1. Location-Based Distribution\n\nIdentify high-demand areas and strategically allocate more bicycles to those locations.")

    # Strategy 2: Time-Optimized Distribution
    st.write("2. Time-Optimized Distribution\n\nAnalyze peak hours and days of the week to ensure an adequate supply of bicycles during high-demand periods.")

    # Strategy 3: Promotions and Incentives
    st.write("3. Promotions and Incentives\n\nImplement promotions or incentives during off-peak hours to encourage bicycle usage and balance demand.")

    # Strategy 4: Dynamic Inventory Adjustments
    st.write("4. Dynamic Inventory Adjustments\n\nUtilize real-time data to dynamically adjust bicycle inventory in response to changing demand patterns.")

    # Strategy 5: Collaborate with Local Events
    st.write("5. Collaborate with Local Events\n\nCoordinate with local events or festivals to anticipate increased demand and plan accordingly.")

    # Strategy 6: User Engagement and Feedback
    st.write("6. User Engagement and Feedback\n\nEncourage user feedback to understand preferences and continuously improve the distribution strategy.")

    # Strategy 7: Expansion Planning
    st.write("7. Expansion Planning\n\nIdentify areas with growing demand and plan expansions or partnerships to meet future needs.")

###########################
st.markdown("# 🏹Conclusion")

## question 1
st.write("1. **How are bike loan patterns affected by variables such as weather, seasons, days of the week, and hours of the day?**")
st.write("  - **Bike Loan Patterns by Variable:**\n - Bike loan patterns based on selected variables can conclude affected or not variable has a specific trend or if certain values are associated with higher or lower bike loan patterns. But, for for numerical variables, it's comparing with a specific threshold or range of values that would indicate an impact on bike loan patterns.\n  - Visualizations include count and bar plots for categorical variables and histograms for numerical variables.")

# Correlation Analysis
st.write("  - **Correlation Analysis:**\n   - A bar plot visualizes correlations between different features.\n  - Insights can be gained into relationships between variables.")

## question 2
st.write("2. **Can certain patterns in bicycle loan data help in organizing bicycle inventory?**")
st.write("   - **Seasonal Demand for Bicycles:**\n  - A boxplot illustrates the distribution of bike counts across different seasons\n  - Understanding seasonal demand aids in inventory planning (increasing/decreasing).")

# Maximize Bicycle Distribution
st.write("   - **Maximize Bicycle Distribution:**\n - Strategies for maximizing bicycle distribution can be explored.\n - Suggestions can be derived from patterns identified in the data.")

# Conclusion Summary
st.write("The analysis and visualizations offer valuable insights into bike loan patterns and inventory management strategies.\n It could help users to get information on whether the selected variable is affected or not, the peak hour, and the seasonal demand.")