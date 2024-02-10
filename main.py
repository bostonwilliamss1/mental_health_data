import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('mental_health_finaldata_1.csv')

"""
First Questions: 
How does the reported increase in stress (Growing_Stress) 
correlate with the number of days spent indoors (Days_Indoors)?
"""

if 'Growing_Stress' in df.columns and 'Days_Indoors' in df.columns:
    # GRAPH STUFF: 
    # Data for Growing Stress
    growing_stress = df['Growing_Stress']

    growing_stress_yes = df[df['Growing_Stress'] == "Yes"]
    growing_stress_no = df[df['Growing_Stress'] == "No"]
    growing_stress_maybe = df[df['Growing_Stress'] == "Maybe"]
    # Data for Days Indoors
    days_indoors_yes_counts = growing_stress_yes['Days_Indoors'].value_counts().sort_index()
    days_indoors_no_counts = growing_stress_no['Days_Indoors'].value_counts().sort_index()
    days_indoors_maybe_counts = growing_stress_maybe['Days_Indoors'].value_counts().sort_index()
    # Creating Graph
    df_counts = pd.DataFrame({
        'Yes': days_indoors_yes_counts,
        'No': days_indoors_no_counts, 
        'Maybe': days_indoors_maybe_counts
    })
    
    ax = df_counts.plot(kind='bar', figsize=(12, 6), width=0.8, colormap='viridis')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel('Days Indoors')
    ax.set_ylabel('Count')
    ax.set_title('Days Indoors for Different Responses to Growing Stress')
    ax.legend(title='Growing Stress Response')
    plt.show()
    # TERMINAL STUFF 
    went_out_every_day = growing_stress_yes[growing_stress_yes['Days_Indoors'] == "Go out Every day"]
    went_out_2weeks = growing_stress_yes[growing_stress_yes['Days_Indoors'] == "1-14 days"]
    went_out_1month = growing_stress_yes[growing_stress_yes['Days_Indoors'] == "15-30 days"]
    went_out_2months = growing_stress_yes[growing_stress_yes['Days_Indoors'] == "31-60 days"]
    went_out_more_than_2_months = growing_stress_yes[growing_stress_yes['Days_Indoors'] == "More than 2 months"]

    every_day_count = len(went_out_every_day)
    week2_count = len(went_out_2weeks)
    total = len(growing_stress)
    yes_count = len(growing_stress_yes)
    no_count = len(growing_stress_no)
    maybe_count = len(growing_stress_maybe)
    month1_count = len(went_out_1month)
    month2_count = len(went_out_2months)
    more_than_2_months_count = len(went_out_more_than_2_months)

    yes_percentage = round((yes_count / total) * 100, 2)
    no_percentage = round((no_count / total) * 100, 2)
    maybe_percentage = round((maybe_count / total) * 100, 2)
    perc_people__out_every_day = round((every_day_count / yes_count) * 100, 2)
    perc_people_out_2weeks = round((week2_count / yes_count) * 100, 2)
    perc_people_out_1month = round((month1_count / yes_count) * 100, 2)
    perc_people_out_2months = round((month2_count / yes_count) * 100, 2)
    perc_people_out_more_2m = round((more_than_2_months_count / yes_count) * 100, 2)

    print("1. Is there a correlation between the amount of days people stay indoors to growing stress levels? ")
    print("-----------------------------------------------")
    print("Percentage of people who said yes, no, or maybe to growing stress: ")
    print(f'YES: {yes_count}/{total}..........{yes_percentage}%')
    print(f'NO: {no_count}/{total}..........{no_percentage}%')
    print(f'MAYBE: {maybe_count}/{total}..........{maybe_percentage}%')
    print("-----------------------------------------------") 
    print("How many of those people went outside every day: ")
    print(f'{every_day_count}/{yes_count}..........{perc_people__out_every_day}%')
    print("-----------------------------------------------") 
    print("How many of those people went outside between 1-14 days: ")
    print(f'{week2_count}/{yes_count}..........{perc_people_out_2weeks}%')
    print("-----------------------------------------------")
    print("How many of those people went outside between 15-30 days: ")
    print(f'{month1_count}/{yes_count}..........{perc_people_out_1month}%')
    print("-----------------------------------------------")
    print("How many of those people went outside between 31-60 days: ")
    print(f'{month2_count}/{yes_count}..........{perc_people_out_2months}%')
    print("-----------------------------------------------")
    print("How many of those people went outside between more than 2 months: ")
    print(f'{more_than_2_months_count}/{yes_count}..........{perc_people_out_more_2m}%')
    print("-----------------------------------------------")
    print("RESULTS: ")
    print("It is hard to form a conclusion from these results due to the fact that this is a limited data set but from ")
    print("looking at these results from the percentages of people and the different amount of times they stayed outdoors, ")
    print("it does not look like there is a correlation to growing stress and the amount of days that people stay inside. I would ")
    print("have thought that there would have been due to the need people have to be social. I would have expected to see that ")
    print("it would have been most people who said they had higher stress levels to be in their house the longest (longer than 2 months)")
    print("but rather the majority is people who have been in their houses 1-14 days.")

"""
Second Questions:
Is there a significant difference in reported frustration during the first two weeks of quarantine 
(Quarantine_Frustration) between different age groups or occupations?
"""
# code 
print("")
print("-----------------------------------------------")
if all(col in df.columns for col in ['Quarantine_Frustrations', 'Age', 'Occupation']):
    #Quarantine Frustrations
    quarantine_frustration = df['Quarantine_Frustrations'].value_counts()
    quarantine_frustration_yes = df[df['Quarantine_Frustrations'] == "Yes"]
    quarantine_frustration_no = df[df['Quarantine_Frustrations'] == "No"]
    quarantine_frustration_maybe = df[df['Quarantine_Frustrations'] == "Maybe"]
    #Occupation
    o_yes_counts = quarantine_frustration_yes['Occupation'].value_counts()
    o_no_counts = quarantine_frustration_no['Occupation'].value_counts()
    o_maybe_counts = quarantine_frustration_maybe['Occupation'].value_counts()
    #Ages
    a_yes_counts = quarantine_frustration_yes['Age'].value_counts()
    a_no_counts = quarantine_frustration_no['Age'].value_counts()
    a_maybe_counts = quarantine_frustration_maybe['Age'].value_counts()

    df_counts_2 = pd.DataFrame({
        'Yes': o_yes_counts,
        'No': o_no_counts, 
        'Maybe': o_maybe_counts
    })
    
    ax = df_counts_2.plot(kind='bar', figsize=(12, 6), width=0.8, colormap='viridis')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel('Occupations')
    ax.set_ylabel('Count')
    ax.set_title('Quarantine Frustrations with Different Occupations')
    ax.legend(title='Quarantine Frustrations in Relation to Occupations')
    plt.show()

    df_counts_3 = pd.DataFrame({
        'Yes': a_yes_counts,
        'No': a_no_counts, 
        'Maybe': a_maybe_counts
    })
    
    ax = df_counts_3.plot(kind='bar', figsize=(12, 6), width=0.8, colormap='viridis')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel('Ages')
    ax.set_ylabel('Count')
    ax.set_title('Quarantine Frustrations with Different Ages')
    ax.legend(title='Quarantine Frustrations in Relation to Peoples Ages')
    plt.show()

    # Terminal Information
    house_wife = quarantine_frustration_yes[quarantine_frustration_yes['Occupation']  == "Housewife"]
    business = quarantine_frustration_yes[quarantine_frustration_yes['Occupation'] == "Business"]
    corporate = quarantine_frustration_yes[quarantine_frustration_yes['Occupation'] == 'Corporate']
    others = quarantine_frustration_yes[quarantine_frustration_yes['Occupation'] == 'Others']
    student = quarantine_frustration_yes[quarantine_frustration_yes['Occupation'] == 'Student']
    #Counts
    yes_count2 = len(quarantine_frustration_yes)
    no_count2 = len(quarantine_frustration_no)
    maybe_count2 = len(quarantine_frustration_maybe)

    house_wife_count = len(house_wife)
    business_count = len(business)
    corporate_count = len(corporate)
    others_count = len(others)
    student_count = len(student)
    # Percentages
    yes_percentage2 = round((yes_count2 / total) * 100, 2)
    no_percentage2 = round((no_count2 / total) * 100, 2)
    maybe_percentage2 = round((maybe_count2 / total) * 100, 2)
    perc_frustration_hw = round((house_wife_count / yes_count2) * 100, 2)
    perc_frustration_b = round((business_count / yes_count2) * 100, 2)
    perc_frustration_c = round((corporate_count / yes_count2) * 100, 2)
    perc_frustration_s = round((student_count / yes_count2) * 100, 2)
    perc_frustration_o = round((others_count / yes_count2) * 100, 2)
    
    print("2. Is there a significant difference in reported frustration during the first two weeks of quarantine (Quarantine_Frustration) between different age groups or occupations?")
    print("-----------------------------------------------")
    print("Percentage of people who said yes, no, and maybe to frustration during the first two weeks of quarantine in relation to their occupation: ")
    print(f'YES: {yes_count2}/{total}..........{yes_percentage2}%')
    print(f'NO: {no_count2}/{total}..........{no_percentage2}%')
    print(f'MAYBE: {maybe_count2}/{total}..........{maybe_percentage2}%')
    print("-----------------------------------------------") 
    print("Percentage of Housewife's reported frustration: ")
    print(f'{house_wife_count}/{yes_count2}..........{perc_frustration_hw}%')
    print("-----------------------------------------------") 
    print("Percentage of Business people reported frustration:  ")
    print(f'{business_count}/{yes_count2}..........{perc_frustration_b}%')
    print("-----------------------------------------------")
    print("Percentage of Corporate people reported frustration: ")
    print(f'{corporate_count}/{yes_count2}..........{perc_frustration_c}%')
    print("-----------------------------------------------")
    print("Percentage of Students reported frustration: ")
    print(f'{student_count}/{yes_count2}..........{perc_frustration_s}%')
    print("-----------------------------------------------")
    print("Percentage of people with other careers who reported frustration: ")
    print(f'{others_count}/{yes_count2}..........{perc_frustration_o}%')
    print("-----------------------------------------------")
    print("RESULTS: ")
    print("Looking at the data from the graphs and the different percentages, it is interesting to note that Housewives take up a quarter ")
    print("of all of the people who said yes to having frustrations with quarantine. I would have thought that they would have been ")
    print("the least because they are used to staying home. I also think it is interesting that students were so low. I know when I was a ")
    print("student in quarantine, it was very hard because I was so used to being social with all of my friends and classes. But maybe ")
    print("the students in this study were able to relax from the stress of school. It is also important to note that this is the frustration ")
    print("in the first two weeks. So this is the initial reaction to getting a few weeks off. The people in the study did not know how long it ")
    print("was going to last.")

    sixteen = quarantine_frustration_yes[quarantine_frustration_yes['Age'] == "16-20"]
    twenty = quarantine_frustration_yes[quarantine_frustration_yes['Age'] == "20-25"]
    twentyfive = quarantine_frustration_yes[quarantine_frustration_yes['Age'] == "25-30"]
    thirty = quarantine_frustration_yes[quarantine_frustration_yes['Age'] == "30-Above"]

    sixteen_count = len(sixteen)
    twenty_count = len(twenty)
    twentyfive_count = len(twentyfive)
    thirty_count = len(thirty)

    perc_16 = round((sixteen_count / yes_count2) * 100, 2)
    perc_20 = round((twenty_count / yes_count2) * 100, 2)
    perc_25 = round((twentyfive_count / yes_count2) * 100, 2)
    perc_30 = round((thirty_count / yes_count2) * 100, 2)

    print("Percentage of people who said yes, no, and maybe to frustration during the first two weeks of quarantine in relation to their age: ")
    print("-----------------------------------------------") 
    print("Percentage of people from ages 16-20 reported frustration: ")
    print(f'{sixteen_count}/{yes_count2}..........{perc_16}%')
    print("-----------------------------------------------") 
    print("Percentage of people from ages 20-25 reported frustration:  ")
    print(f'{twenty_count}/{yes_count2}..........{perc_20}%')
    print("-----------------------------------------------")
    print("Percentage of people from ages 25-30 reported frustration: ")
    print(f'{twentyfive_count}/{yes_count2}..........{perc_25}%')
    print("-----------------------------------------------")
    print("Percentage of people from ages 30-above reported frustration: ")
    print(f'{thirty_count}/{yes_count2}..........{perc_30}%')
    print("-----------------------------------------------")
    print("RESULTS: ")
    print("Based on the percentages of the different ages, the group who had the hardest time with the first two weeks of quarantine ")
    print("were the 16-20 year olds. That is accurate to what I thought it would be because these teenagers/young adults are used to going out ")
    print("and being very social so when they are not able to do that, I could imagine that could be very hard. But the group who had the lowest ")
    print("percentage was the 20-25 year olds. This is surprising because I would have thought that they would have been  ")
    print("second to the youngest group. The 25-30 year old group and 30 and  above group are pretty similar in percentages, which is not surprising to me. ")
    print("This isn't the best data set because it is not very specific. I could come to a better conclusion if there were more sections")
