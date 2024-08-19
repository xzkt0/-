def calculate_utility(probability, rain_value, sun_value):
    return probability * rain_value + (1 - probability) * sun_value

def main():
    print("Ймовірність дощу (введіть значення від 0 до 1):")
    probability = float(input("Введіть ймовірність: "))

    if not (0 <= probability <= 1):
        print("Будь ласка, введіть правильне значення ймовірності (від 0 до 1).")
        return

    print("Оцініть відчуття вдома (дощ) від 1 (дуже погано) до 10 (дуже добре):")
    home_rain_value = int(input("Введіть оцінку: "))

    print("Оцініть відчуття вдома (сонце) від 1 (дуже погано) до 10 (дуже добре):")
    home_sun_value = int(input("Введіть оцінку: "))

    print("Оцініть відчуття в лісі (дощ) від 1 (дуже погано) до 10 (дуже добре):")
    forest_rain_value = int(input("Введіть оцінку: "))

    print("Оцініть відчуття в лісі (сонце) від 1 (дуже погано) до 10 (дуже добре):")
    forest_sun_value = int(input("Введіть оцінку: "))

    w_home = calculate_utility(probability, home_rain_value, home_sun_value)
    w_forest = calculate_utility(probability, forest_rain_value, forest_sun_value)

    decision = "Їхати в ліс" if w_forest > w_home else "Залишитися вдома"

    print(f"Корисність вдома: {w_home:.2f}")
    print(f"Корисність в лісі: {w_forest:.2f}")
    print(f"Рекомендація: {decision}")

if __name__ == "__main__":
    main()
