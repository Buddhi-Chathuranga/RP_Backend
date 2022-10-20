# %%
import pandas as pd
import numpy as np
import seaborn as sb
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import ensemble
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import pickle

def cadiac_status_prediction(cadiac_status_prediction_list:list):
    df = pd.read_csv(r'AIModel/ExercisePlan/cardio_train.csv', sep=';', engine='python')
    def age_yrs(age):
        ages = age/365
        return ages
    df['age'] = df['age'].apply(age_yrs)
    df['age'] = df['age'].astype(float).apply(np.ceil)
    df['age']= df['age'].astype(int)
    df['age'].head(5)
    df['gender'] = df['gender'].replace({1 : 0,
                                        2 : 1})
    df.rename(columns = {'ap_hi':'systolic','ap_lo':'diastolic','gluc':'glucose','alco':'alcohol_intake','active':'physical_activity','cardio':'cv_disease'},inplace = True)
    df.head()
    print(df.info())
    plt.figure(figsize=[7,7])
    sns.heatmap(df.corr(), annot= True, fmt= '.0%')
    df.plot(kind="box",subplots=True,layout=(7,2),figsize=(15,20));
    df=df.drop(columns=['id'])
    X = df.values
    X = np.delete(X,11,axis=1)
    y = df['cv_disease'].values


    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)
    X_train.shape,X_test.shape
    def model_acc(model):
        model.fit(X_train,y_train)
        acc=model.score(X_test,y_test)
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
    
    parameters = {'n_estimators':[10, 50,100],'learning_rate':[0.1]}
    grid_obj = GridSearchCV(estimator=gb_clf, param_grid=parameters)
    grid_fit = grid_obj.fit(X_train,y_train)
    best_model = grid_fit.best_estimator_
    best_model.score(X_train,y_train)
    
    with open('Cadiac.pkl','wb') as file:
        pickle.dump(grid_fit, file)
    return_val = best_model.predict([cadiac_status_prediction_list])[0]
    if return_val == 0:
        return('cardio_0')
    elif return_val ==1:
        return('cardio_1')


