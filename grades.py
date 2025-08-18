# ==============================
# IMPORTS AND DATA LOADING
# ==============================

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

st_per = pd.read_csv(r'C:\Users\Іван\da_noob\StudentsPerformance.csv')

# ==============================
# DAY 1: Gender comparison (Version 1)
# ==============================

gender_only = st_per[['gender', 'math score', 'reading score', 'writing score']]
# Male average
male = gender_only[gender_only['gender']=='male']
avg_male = male[['math score', 'reading score', 'writing score']].mean()
# Female average
female = gender_only[gender_only['gender']=='female']
avg_female = female[['math score', 'reading score', 'writing score']].mean()

# print("\n(V1) Average male score:")
# display(avg_male)
# print("\n(V1) Average female score:")
# display(avg_female)

# ==============================
# DAY 1: Gender comparison (Version 2)
# ==============================

all_genders = st_per.groupby(
    'gender')[['math score','reading score','writing score']].mean().reset_index()
all_genders_long = all_genders.melt(id_vars='gender',
                                  var_name='Subject',
                                  value_name='Score')

# print("\n(V2) Average male and female score:")
# display(all_genders_long)

sns.barplot(all_genders_long,
            x='Subject', y='Score', hue='gender',
            palette={'male':'skyblue','female':'pink'})
# plt.show()

# ==============================
# DAY 2: Impact of test preparation course (Version 1)
# ==============================

prep = st_per.groupby(
    'test preparation course')[['math score','reading score','writing score']].mean().reset_index()

prep_female = st_per[st_per['gender'] == 'female'].groupby(
    'test preparation course').size().reset_index(name='count')

prep_male = st_per[st_per['gender'] == 'male'].groupby(
    'test preparation course').size().reset_index(name='count')

completed_female = prep_female[prep_female['test preparation course'] == 'completed']['count'].sum()
percent_female = (completed_female / prep_female['count'].sum()) * 100

completed_male = prep_male[prep_male['test preparation course'] == 'completed']['count'].sum()
percent_male = (completed_male / prep_male['count'].sum()) * 100

# print(prep_male)
# print(prep_female)
# print(percent_female)
# print(percent_male)

# ==============================
# DAY 2: Impact of test preparation course (Version 2)
# ==============================

# MALE
prep_male_scores = st_per[st_per['gender'] == 'male'].groupby(
    'test preparation course')[['math score', 'reading score', 'writing score']].mean()
math_diff = prep_male_scores.loc['completed', 'math score'] - prep_male_scores.loc['none', 'math score']
reading_diff = prep_male_scores.loc['completed', 'reading score'] - prep_male_scores.loc['none', 'reading score']
writing_diff = prep_male_scores.loc['completed', 'writing score'] - prep_male_scores.loc['none', 'writing score']

male_rel_diff_math = (math_diff / prep_male_scores.loc['none', 'math score']) * 100
male_rel_diff_reading = (reading_diff / prep_male_scores.loc['none', 'reading score']) * 100
male_rel_diff_writing = (writing_diff / prep_male_scores.loc['none', 'writing score']) * 100

male_diff_all = (male_rel_diff_math + male_rel_diff_reading + male_rel_diff_writing) / 3

# FEMALE
prep_female_scores = st_per[st_per['gender'] == 'female'].groupby(
    'test preparation course')[['math score', 'reading score', 'writing score']].mean()
math_diff = prep_female_scores.loc['completed', 'math score'] - prep_female_scores.loc['none', 'math score']
reading_diff = prep_female_scores.loc['completed', 'reading score'] - prep_female_scores.loc['none', 'reading score']
writing_diff = prep_female_scores.loc['completed', 'writing score'] - prep_female_scores.loc['none', 'writing score']

female_rel_diff_math = (math_diff / prep_female_scores.loc['none', 'math score']) * 100
female_rel_diff_reading = (reading_diff / prep_female_scores.loc['none', 'reading score']) * 100
female_rel_diff_writing = (writing_diff / prep_female_scores.loc['none', 'writing score']) * 100

female_diff_all = (female_rel_diff_math + female_rel_diff_reading + female_rel_diff_writing) / 3

print("\nAbsolute increase in average scores after preparatory courses for males:")
print(male_diff_all)
print("\nAbsolute increase in average scores after preparatory courses for females:")
print(female_diff_all)