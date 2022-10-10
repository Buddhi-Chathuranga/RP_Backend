import pandas as pd


def cal_bmi_statues(height_feet, weight):
    height_meters = height_feet * 0.3048
    bmi = weight / (height_meters ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Healthy"
    elif 24.9 <= bmi < 30:
        status = "Overweight"
    elif bmi >= 30:
        status = "Obesity"
    return status


def cal_mean_Arterial_Pressure(systolic_blood_pressure, diastolic_blood_pressure):
    map = ((2 * diastolic_blood_pressure) + (systolic_blood_pressure / 3))
    if map < 69.9:
        status = "Low"  # Low
    elif 70 <= map < 110:
        status = "Normal"
    elif map >= 110:
        status = "High"
    return status


def get_age_bin(age):
    data = [age]
    df = pd.DataFrame(data, columns=['age'])
    df['age'] = pd.cut(df['age'], [0, 20, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
                       labels=['0-20', '20-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60-65', '65-70',
                               '70-75', '75-80', '80-85', '85-90', '90-95', '95-100'])
    age_bin = df.loc[0].at["age"]
    return age_bin


def get_final_meal_plan(meal_planner):
    # ----------------------------- for calculate BMR & BMI status -----------------
    calories = 0
    gender = meal_planner[0]
    # print(gender)
    height_feet = float(meal_planner[1])
    # print(height_feet)
    weight = float(meal_planner[2])
    # print(weight)
    age = int(meal_planner[3])
    # print(age)
    activity_level = meal_planner[4]
    # print(activity_level)
    goals = meal_planner[5]
    # print(goals)
    foodtype = meal_planner[6]
    # print(foodtype)
    Risk = meal_planner[7]

    height_inches = height_feet * 12
    height_meters = height_feet * 0.3048

    if gender == 'male' or gender == 'Male' or gender == 'm' or gender == 'M':
        c1 = 66
        hm = 6.2 * height_inches
        wm = 12.7 * weight
        am = 6.76 * age

    elif gender == 'female' or gender == 'Female' or gender == 'f' or gender == 'F':
        c1 = 655.1
        hm = 4.35 * height_inches
        wm = 4.7 * weight
        am = 4.7 * age

    bmr_result = c1 + hm + wm - am

    # --------------------------------------------------------------------------------------

    if activity_level == 'none':
        activity_level = 1.2 * bmr_result

    elif activity_level == 'light':
        activity_level = 1.375 * bmr_result

    elif activity_level == 'moderate':
        activity_level = 1.55 * bmr_result

    elif activity_level == 'heavy':
        activity_level = 1.725 * bmr_result

    elif activity_level == 'extreme':
        activity_level = 1.9 * bmr_result

    # --------------------------------------------------------------------------------------

    if goals == 'lose':
        calories = activity_level - 500

    elif goals == 'maintain':
        calories = activity_level

    elif goals == 'gain':

        calories = activity_level + 500

    calorie_amount = calories

    if calorie_amount < 1100:
        calorie_amount = 1000

    elif calorie_amount >= 1100 or calorie_amount < 1300:
        calorie_amount = 1200


    elif calorie_amount >= 1300 or calorie_amount < 1600:
        calorie_amount = 1500


    elif calorie_amount >= 1600 or calorie_amount < 1800:
        calorie_amount = 1700


    elif calorie_amount >= 1800 or calorie_amount < 2100:
        calorie_amount = 2000


    elif calorie_amount >= 2100 or calorie_amount < 2300:
        calorie_amount = 2200

    elif calorie_amount <= 2300:
        calorie_amount = 2500

    # print(' ')
    # print('-------------------------------------------------')
    #
    # print('in order to ', goals, 'weight, your daily calori goals should be', int(calories), '!')
    # print()
    # print("suggested meal category ", foodtype)
    # print('So suggested calories Amount : ', int(calorie_amount), '!')

    meal_planner_id = foodtype + '_' +Risk+'_'+str(calorie_amount)
    return meal_planner_id
