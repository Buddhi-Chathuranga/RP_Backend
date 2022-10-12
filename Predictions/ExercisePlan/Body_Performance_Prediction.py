
from typing import List
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import ensemble
from sklearn.linear_model import LogisticRegression

def body_performance_pred(body_performance_pred_input_list:list):
    df = pd.read_csv(r'AIModel/ExercisePlan/bodyPerformance.csv')
    df.head()
    df.describe()
    df.shape
    df.info
    df.isnull().sum()
    print(df.info())
    SexColumnDummy = pd.get_dummies(df['gender'])
    df = pd.concat((df, SexColumnDummy), axis=1)
    df = df.drop(['gender'],axis=1)
    df['class'] = df['class'].replace({"A" : 1,
                                        "B" : 2,
                                        "C" : 3,
                                        "D" : 4})
    df.head()
    df.corr()['class']
    plt.figure(figsize=[7,7])
    sns.heatmap(df.corr(), annot= True, fmt= '.0%')
    df.plot(kind="box",subplots=True,layout=(7,2),figsize=(15,20));
    sns.displot(df['sit and bend forward_cm'])
    q1 = df['sit and bend forward_cm'].quantile(0.25)
    q3 = df['sit and bend forward_cm'].quantile(0.75)
    iqr = q3-q1
    q1,q3,iqr
    upper_limit = q3 + (1.5 * iqr)
    lower_limit = q1 - (1.5 * iqr)
    lower_limit, upper_limit
    df.loc[(df['sit and bend forward_cm'] > upper_limit) | (df['sit and bend forward_cm'] < lower_limit)]
    new_df = df.loc[(df['sit and bend forward_cm'] < upper_limit) & (df['sit and bend forward_cm'] > lower_limit)]
    print('before removing outliers:', len(df))
    print('After removing outliers:', len(new_df))
    print('outliers:', len(df)-len(new_df))
    new_df = df.copy()
    new_df.loc[(new_df['sit and bend forward_cm']>upper_limit),'sit and bend forward_cm'] = upper_limit
    new_df.loc[(new_df['sit and bend forward_cm']<lower_limit),'sit and bend forward_cm'] = lower_limit
    sns.boxplot(new_df['sit and bend forward_cm'])
    X =new_df.drop('class',axis=1)
    Y=new_df['class']  
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
    X_train.shape,X_test.shape
    def model_acc(model):
        model.fit(X_train,Y_train)
        acc=model.score(X_test,Y_test)
        print(str(model)+ '-->'+str(acc))

    rf = RandomForestClassifier()
    model_acc(rf)
    nb_clf = GaussianNB()
    model_acc(nb_clf)
    knn_clf = KNeighborsClassifier()
    model_acc(knn_clf)
    gb_clf = ensemble.GradientBoostingClassifier()
    model_acc(gb_clf)
    lr_clf = LogisticRegression()
    model_acc(lr_clf)
    parameters = {'n_estimators':[10, 50,100],'criterion':['gini','entropy']}
    grid_obj = GridSearchCV(estimator=rf, param_grid=parameters)
    grid_fit = grid_obj.fit(X_train,Y_train)
    best_model = grid_fit.best_estimator_
    best_model
    best_model.score(X_train,Y_train)

    with open('bodyperformance.pkl','wb') as file:
        pickle.dump(grid_fit, file)

    X_train.columns
    array_val = best_model.predict([body_performance_pred_input_list])[0]
    
    if array_val == 0:
        return('body_ performance_1')
    elif array_val == 1:
        return('body_ performance_2')
    elif array_val == 2:
        return('body_ performance_3')
    elif array_val == 3:
        return('body_ performance_4')

