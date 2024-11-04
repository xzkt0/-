import numpy as np

F = np.array([
    [6.0, 6.2, 5.5],
    [7.5, 7.1, 7.0],
    [7.7, 7.1, 7.0],
    [7.0, 5.8, 6.0]
])

p = np.array([0.3, 0.5, 0.2])

def semivariance(matrix, probabilities):
    semivars = []
    for row in matrix:
        mean_value = np.dot(row, probabilities)
        deviations = np.maximum(0, mean_value - row)
        semivar = np.dot(deviations**2, probabilities)
        semivars.append(semivar)
    return np.array(semivars)

def modified_semivariance(matrix, probabilities):
    modified_semivars = []
    for row in matrix:
        mean_value = np.dot(row, probabilities)
        deviations = np.maximum(0, mean_value - row)
        semivar = np.dot(deviations**2, probabilities)
        mod_semivar = semivar / np.mean(row)
        modified_semivars.append(mod_semivar)
    return np.array(modified_semivars)

def modified_lambda(matrix, probabilities, lambd=0.7):
    mean_values = np.dot(matrix, probabilities)
    semivars = semivariance(matrix, probabilities)
    return lambd * mean_values + (1 - lambd) * semivars

def hodges_lehmann(matrix, probabilities, lambd=0.9):
    mean_values = np.dot(matrix, probabilities)
    semivars = semivariance(matrix, probabilities)
    return lambd * mean_values + (1 - lambd) * semivars

semivariance_criterion = semivariance(F, p)
modified_semivariance_criterion = modified_semivariance(F, p)
modified_lambda_criterion = modified_lambda(F, p, lambd=0.7)
hodges_lehmann_criterion = hodges_lehmann(F, p, lambd=0.9)

print("Критерій мінімальної семіваріації:", semivariance_criterion)
print("Критерій мінімального модифікованого коефіцієнта семіваріації:", modified_semivariance_criterion)
print("Критерій модифікованого з λ = 0.7:", modified_lambda_criterion)
print("Критерій Ходжеса-Лемана з λ = 0.9:", hodges_lehmann_criterion)

optimal_semivariance = np.argmin(semivariance_criterion)
optimal_modified_semivariance = np.argmin(modified_semivariance_criterion)
optimal_modified_lambda = np.argmax(modified_lambda_criterion)
optimal_hodges_lehmann = np.argmax(hodges_lehmann_criterion)

print("Оптимальне рішення за критерієм мінімальної семіваріації:", optimal_semivariance + 1)
print("Оптимальне рішення за критерієм мінімального модифікованого коефіцієнта семіваріації:", optimal_modified_semivariance + 1)
print("Оптимальне рішення за критерієм модифікованого з λ = 0.7:", optimal_modified_lambda + 1)
print("Оптимальне рішення за критерієм Ходжеса-Лемана з λ = 0.9:", optimal_hodges_lehmann + 1)
