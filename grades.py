import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

st_per = pd.read_csv(r'C:\Users\Іван\da_noob\StudentsPerformance.csv')

#Gender comparison version 1
gender_only = st_per[['gender', 'math score', 'reading score', 'writing score']]
#Male avarage
male = gender_only[gender_only['gender']=='male']
avg_male = male[['math score', 'reading score', 'writing score']].mean()
#Female avarage
female = gender_only[gender_only['gender']=='female']
avg_female = female[['math score', 'reading score', 'writing score']].mean()

print("(V1)Avarage male score:")
display(avg_male)
print("\n(V1)Avarage female score;")
display(avg_female)

#Gender versin 2 (with plotting)
all_genders= st_per.groupby(
'gender')[['math score','reading score','writing score']].mean().reset_index()
all_genders_long = all_genders.melt(id_vars='gender',
                                  var_name='Subject',
                                  value_name='Score')

print("\n(V2)Avarage male and female score:")
display(all_genders_long)

sns.barplot(all_genders_long,
            x='Subject', y='Score', hue='gender',
            palette={'male':'skyblue','female':'pink'})
plt.show()