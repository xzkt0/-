import math

def expected_utility_bet(utility_func, bet_amount, win_probability, win_ratio):
    win_utility = utility_func(50 + bet_amount * win_ratio)
    lose_utility = utility_func(50 - bet_amount)
    expected_utility = win_probability * win_utility + (1 - win_probability) * lose_utility
    return expected_utility

def student_decision(utility_func, bet_amount=50, win_probability=0.5, win_ratio=3):
    no_bet_utility = utility_func(50)
    
    bet_utility = expected_utility_bet(utility_func, bet_amount, win_probability, win_ratio)
    
    if bet_utility > no_bet_utility:
        decision = "робити ставку"
    else:
        decision = "не робити ставку"
    
    return decision, no_bet_utility, bet_utility


def U1(x):
    return 1.3 * x

def U2(x):
    return 1.4 * math.sqrt(x)

student1_decision, student1_no_bet_utility, student1_bet_utility = student_decision(U1)
student2_decision, student2_no_bet_utility, student2_bet_utility = student_decision(U2)

print(f"Студент 1: Рішення = {student1_decision}, Корисність без ставки = {student1_no_bet_utility}, Корисність від ставки = {student1_bet_utility}")
print(f"Студент 2: Рішення = {student2_decision}, Корисність без ставки = {student2_no_bet_utility}, Корисність від ставки = {student2_bet_utility}")
