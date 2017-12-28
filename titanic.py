import pandas as pd
import numpy as np

titanic_survival = pd.read_csv('titanic_train.csv')
titanic_survival.head()
age = titanic_survival['Age']
#print(age.loc[0:10])
age_is_null = pd.isnull(age)
age_null_true = age[age_is_null]
#print(age_null_true)
len(age_null_true)
#print(titanic_survival.columns)
mean_age = titanic_survival["Age"][age_is_null == False]
average = sum(mean_age) / len(mean_age)
#print(average)
#print(mean_age.mean())
average = titanic_survival.pivot_table(index="Pclass", values="Survived",aggfunc=np.sum)
#print(average)
#print(titanic_survival.loc[10,'Age'])
def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)
column_count = titanic_survival.apply(not_null_count)
print(column_count)