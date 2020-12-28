import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
  
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  
    # each of the races in the dataset
    races = df['race'].unique()
    # count of each race
    counts = []
    for race in races:
      counts.append(df.loc[df['race'] == race].shape[0])

    race_count = pd.Series(counts, index = races)
    
     # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)
    
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.loc[df['education'] == 'Bachelors'].shape[0] / df['education'].count()) * 100, 1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    adv_degrees_over_50K = df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K'), ['salary']].shape[0]
    total_adv_degrees = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'), ['salary']].shape[0]
    
    per_adv_more_50K = round((adv_degrees_over_50K / total_adv_degrees) * 100, 1)

    
    # What percentage of people without advanced education make more than 50K?
    no_adv_over_50K = df.loc[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K'), ['salary']].shape[0]
    total_no_adv_degrees = df.loc[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')), ['salary']].shape[0]
    per_no_adv_over_50K = round((no_adv_over_50K / total_no_adv_degrees) * 100, 1)

    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = adv_degrees_over_50K
    lower_education = no_adv_over_50K

    # percentage with salary >50K
    higher_education_rich = per_adv_more_50K
    lower_education_rich = per_no_adv_over_50K
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers_more50K = df.loc[((df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')), ['salary']].shape[0]
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours].shape[0]

    rich_percentage = round((num_min_workers_more50K / num_min_workers) * 100, 1)
    
    
    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].unique()
    country_over50K_per = []
    for country in countries:
      country_over50K_per.append(((df.loc[(df['native-country'] == country) & (df['salary'] == '>50K')].shape[0]) / (df.loc[df['native-country'] == country].shape[0])) * 100)
    
    highest_earning_country =  countries[country_over50K_per.index(max(country_over50K_per))]
    
    highest_earning_country_percentage = round(max(country_over50K_per), 1)
    
    
    # Identify the most popular occupation for those who earn >50K in India.
    occ_India_over50K = df.loc[((df['native-country'] == 'India') & (df['salary'] == '>50K')), ['occupation']].to_dict()['occupation']

    unique_occ = set(occ_India_over50K.values())
    counts_occ = []
    for occupation in unique_occ:
      counts_occ.append(df.loc[((df['native-country'] == 'India') & (df['salary'] == '>50K')) & (df['occupation'] == occupation)].shape[0])
    unique_occ = list(unique_occ)
    top_IN_occupation = unique_occ[counts_occ.index(max(counts_occ))]


    # DO NOT MODIFY BELOW THIS LINE
    
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    
