import numpy as np

F = np.array([
    [8, 2, 4],
    [6, 7, 4],
    [4, 7, 5],
    [3, 5, 6]
])

P1_range = (0.4, 0.6)
P2_range = (0.3, 0.4)
P3_range = (0.1, 0.3)

def expected_return(F, P):
    return np.dot(F, P)

def project_risk(F, P):
    mean_returns = expected_return(F, P)
    variance = np.sum(P * (F - mean_returns[:, None])**2, axis=1)
    return variance

P_avg = np.array([
    (P1_range[0] + P1_range[1]) / 2,
    (P2_range[0] + P2_range[1]) / 2,
    (P3_range[0] + P3_range[1]) / 2
])

expected_returns = expected_return(F, P_avg)
risks = project_risk(F, P_avg)

best_project_max_return = np.argmax(expected_returns)
best_project_min_risk = np.argmin(risks)

print("Очікувані доходи для проектів:", expected_returns)
print("Ризики для проектів:", risks)
print("Найкращий проект за критерієм максимального доходу:", best_project_max_return + 1)
print("Найкращий проект за критерієм мінімального ризику:", best_project_min_risk + 1)
