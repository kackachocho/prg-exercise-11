import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    n = len(values) #jednodussi ney porad psat len(values
    for j in range(n):
        min_index = j
        min_value = values[min_index]
        for i in range(j +1, n): #postupne prochazime cely seznam
            if values[i] < min_value:
                min_index = i
                min_value = values[i]
        values[j], values[min_index] = values[min_index], values[j]
    return values

def bubble_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)
    plt.ion()
    plt.show()
    for i in range(n -1):
        for j in range(n - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    plt.ioff()
    plt.show()
    return numbers


# print(bubble_sort([5, 9, 45, 3]))



if __name__ == "__main__":
    # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    a = selection_sort(values)
    print(f"ukol a: {a}")
    numbers = random_numbers(10)
    b = bubble_sort(numbers)
    print(f"ukol b: {b}")

    