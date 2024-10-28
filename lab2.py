import math

# Введення даних
projects = {
    "A": {"probabilities": [0.1, 0.5, 0.4], "values": [-500, 0, 250]},
    "B": {"probabilities": [0.1, 0.5, 0.4], "values": [-250, 0, 50]},
    "C": {"probabilities": [0.1, 0.75, 0.15], "values": [75, 75, 45]},
}

# Функція для обчислення математичного сподівання
def expected_value(probabilities, values):
    return sum(p * x for p, x in zip(probabilities, values))

# Функція для обчислення дисперсії
def variance(probabilities, values, mean):
    return sum(p * (x - mean)**2 for p, x in zip(probabilities, values))

# Функція для обчислення середньоквадратичного відхилення
def std_dev(variance):
    return math.sqrt(variance)

# Обчислення для кожного проекту
results = {}
for project, data in projects.items():
    mean_value = expected_value(data["probabilities"], data["values"])
    var = variance(data["probabilities"], data["values"], mean_value)
    std_deviation = std_dev(var)
    
    results[project] = {
        "mean": mean_value,
        "variance": var,
        "std_deviation": std_deviation
    }

# Виведення результатів
for project, result in results.items():
    print(f"Проект {project}:")
    print(f"  Математичне сподівання (NPV) = {result['mean']} тис. грн.")
    print(f"  Дисперсія = {result['variance']} тис. грн.")
    print(f"  Середньоквадратичне відхилення = {result['std_deviation']} тис. грн.")

# Вибір найкращого варіанту за найбільшим математичним сподіванням
best_project = max(results, key=lambda x: results[x]['mean'])
print(f"\nНайкращий варіант: Проект {best_project}") 