from Predictions.ExercisePlan.Body_Performance_Prediction import body_performance_pred
from Predictions.ExercisePlan.Cardiac_status_prediction import cadiac_status_prediction
from Predictions.ExercisePlan.Diabetic_status_prediction import diabetic_status_prediction

def mainpredection(body_performance_pred_input:list,cadiac_status_prediction_input:list,diabetic_status_prediction_input:list):
    body_performance_pred_output = body_performance_pred(body_performance_pred_input)
    cadiac_status_prediction_output = cadiac_status_prediction(cadiac_status_prediction_input)
    diabetic_status_prediction_output = diabetic_status_prediction(diabetic_status_prediction_input)
    output_list = [body_performance_pred_output,cadiac_status_prediction_output,diabetic_status_prediction_output]
    return output_list


def Implementation():
    body_performance_pred_input = [28,173.8,67.70,17.1,70.0,127,43.5,27.1,45,217,0,1]
    cadiac_status_prediction_input =[56,0,156,85.0,140,90,3,1,0,0,1]
    diabetic_status_prediction_input = [148,72,0,33.6,50]
    output_list = mainpredection(body_performance_pred_input,cadiac_status_prediction_input,diabetic_status_prediction_input)
    return output_list

# print(mainpredection([28,173.8,67.70,17.1,70.0,127,43.5,27.1,45,217,0,1],[56,0,156,85.0,140,90,3,1,0,0,1],[148,72,0,33.6,50]))