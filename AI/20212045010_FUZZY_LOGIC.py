# Problem
# Input:
# ● Relative distance (0-100%) (low, average, high) ● Speed(0-30) (high, low) Output: Break (0-100%) (mild, controlled, hard) Evaluation Rules:

# If the relative distance is low or the speed is high, then apply a hard break
# If the relative distance is high, apply a mild break
# If the relative distance is average and the speed is high, then apply a controlled break
# If the relative distance is average and the speed is low, then apply a mild break

def relative_distance(car):
    degree = {}

    if car < 0 or car > 100:
        degree["low"] = 0
        degree["average"] = 0
        degree["high"] = 0
    elif car <= 30:
        degree["low"] = 1
        degree["average"] = 0
        degree["high"] = 0
    elif 30 < car < 40:
        degree["low"] = (40 - car) * (1 / (40 - 30))
        degree["average"] = (car - 30) * (1 / (40 - 30))
        degree["high"] = 0
    elif 40 <= car <= 60:
        degree["low"] = 0
        degree["average"] = 1
        degree["high"] = 0
    elif 60 < car < 70:
        degree["average"] = (70 - car) * (1 / (70 - 60))
        degree["high"] = (car - 60) * (1 / (70 - 60))
        degree["low"] = 0
    elif car >= 70 and car <= 100:
        degree["low"] = 0
        degree["average"] = 0
        degree["high"] = 1

    return degree

def speed(car):
    degree = {}

    if car < 0 or car > 30:
        degree["high"] = 0
        degree["low"] = 0
    elif car <= 10:
        degree["low"] = 1
        degree["high"] = 0
    elif 10 < car < 20:
        degree["low"] = (20 - car) * (1 / (20 - 10))
        degree["high"] = (car - 10) * (1 / (20 - 10))
    elif car >= 20 and car <= 30:
        degree["low"] = 0
        degree["high"] = 1

    return degree

def rule_evaluation(relative_degree, speed_degree):
    hard = max(relative_degree['low'], speed_degree['high'])
    mild = relative_degree['high']
    controlled = min(relative_degree['average'], speed_degree['high'])
    mild = max(mild, min(relative_degree['average'], speed_degree['low']))

    return mild, controlled, hard

def defuzzification(mild, controlled, hard):
    cog = 0
    total_weight = 0
    step = 10

    for i in range(0, 101, step):
        if i <= 30:
            cog += i * mild
            total_weight += mild
        elif i <= 60:
            cog += i * controlled
            total_weight += controlled
        elif i <= 100:
            cog += i * hard
            total_weight += hard

    return cog / total_weight if total_weight != 0 else 0

relative_input = 50
speed_input = 20

relative_degree = relative_distance(relative_input)
speed_degree = speed(speed_input)

mild, controlled, hard = rule_evaluation(relative_degree, speed_degree)

brake_intensity = defuzzification(mild, controlled, hard)
print("Calculated Brake Intensity:", brake_intensity)
