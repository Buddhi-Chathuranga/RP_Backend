
import re
from AIPrediction.ExercisePlan import Implementation
from Models.ExercisePlan import ExercisePlan
from Controllers.Exercise import GetOneExercise
import json

def GetExercisePlanToUser(ID):
    try:
        Results = Implementation()
        # Exerciseplan =[]
        Anerobic_exercises=[]
        Streching_exercises=[]
        Aerobic_exercises=[]
        for i in Results:
            
            result = ExercisePlan.objects(ID=i)
            result= json.loads(result.to_json())
            # print("ExercisePlan",result)
            # Exerciseplan.append(result)
            for j in result:
                # execise=[] 
                # print("ExercisePlan",j)
                # for k in j['ExerciseList']:
                #     Eresult= GetOneExercise(k)
                #     execise.append(Eresult['result'])
            #    j['ExerciseList']=execise
                if(j['ExerciseType']=='Aerobic_exercises'):
                    Aerobic_exercises.append(j["ExerciseList"])
                elif(j['ExerciseType']=="Streching_exercises"):
                    Streching_exercises.append(j["ExerciseList"])
                elif(j['ExerciseType']=="Anerobic_exercises"):
                    Anerobic_exercises.append(j["ExerciseList"])
        # print("Aerobic_exercises",Aerobic_exercises)
        # print("Streching_exercises",Streching_exercises)
        # print("Anerobic_exercises",Anerobic_exercises)
        
        Result_Aerobic_exercises=[]
        Result_Streching_exercises=[]
        Result_Anerobic_exercises=[]
        for i in range(len(Aerobic_exercises)):
            Aerobic =[]
            Streching=[]
            Anerobic=[]
            if i+1 < len(Aerobic_exercises):
                if i == 0:
                    Aerobic= list(set(Aerobic_exercises[i]).intersection(Aerobic_exercises[i+1]))
                    Streching= list(set(Streching_exercises[i]).intersection(Streching_exercises[i+1]))
                    Anerobic= list(set(Anerobic_exercises[i]).intersection(Anerobic_exercises[i+1]))
                  
                else:
                    Aerobic = list(set(Aerobic).intersection(Aerobic_exercises[i+1]))
                    Streching = list(set(Streching).intersection(Streching_exercises[i+1]))
                    Anerobic = list(set(Anerobic).intersection(Anerobic_exercises[i+1]))


                Result_Aerobic_exercises = Result_Aerobic_exercises + Aerobic
                Result_Streching_exercises = Result_Streching_exercises + Streching
                Result_Anerobic_exercises = Result_Anerobic_exercises + Anerobic
                
        Finalresult =[]
        for i in Result_Aerobic_exercises:
                Eresult= GetOneExercise(i)
                if Eresult['result'] != None:
                    print("Eresult",Eresult['result'])
                    Finalresult.append(Eresult['result'])
        Result_Aerobic_exercises=Finalresult

        Finalresult2 =[]
        for i in Result_Streching_exercises:
            if Eresult['result'] != None:
                Eresult= GetOneExercise(i)
                Finalresult2.append(Eresult['result'])
        Result_Streching_exercises=Finalresult2

        Finalresult3 =[]
        for i in Result_Anerobic_exercises:
            if Eresult['result'] != None:
                Eresult= GetOneExercise(i)
                Finalresult3.append(Eresult['result'])
        Result_Anerobic_exercises=Finalresult3
            # Result_Aerobic_exercises.append(r)

        return {"Aerobic_exercises":Result_Aerobic_exercises,"Streching_exercises":Result_Streching_exercises,"Anerobic_exercises":Result_Anerobic_exercises}

                
        # for i in range(len(Exerciseplan)):
        #     for j in range(len(Exerciseplan[i])):
        #         execise=[] 
        #         for k in Exerciseplan[i][j]['ExerciseList']:
        #             Eresult= GetOneExercise(k)
        #             execise.append(Eresult['result'])
        #         Exerciseplan[i][j]['ExerciseList']=execise
        Results = Exerciseplan
        # return {"result": Results}
    except Exception as e:
        return {"error": str(e)}