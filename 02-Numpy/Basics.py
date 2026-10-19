import numpy as np


def show_intro():
    print("NUMPY BASICS")
    print("NumPy helps Python work better with large numeric data.")
    print("It makes operations like mean, arrange, reshape, and maths easier.")
    print("It also reduces the need for manual loops in many cases.\n")


def show_advantages():
    print("ADVANTAGES OF NUMPY")
    print("1. Fast execution")
    print("2. Easy mathematical operations")
    print("3. Better memory usage")
    print("4. Important for AI, ML, and Data Science\n")


def show_uses():
    print("USES OF NUMPY")
    print("1. Data Science")
    print("2. Machine Learning and AI")
    print("3. Stock Market Analysis")
    print("4. Medical Research")
    print("5. Image Processing\n")


def compare_list_and_array():
    python_list = [1, 2, 3, 4, 5]
    numpy_array = np.array([1, 2, 3, 4, 5])

    print("PYTHON LIST VS NUMPY ARRAY")
    print("Python list:", python_list)
    print("NumPy array:", numpy_array)
    print("Mean of NumPy array:", np.mean(numpy_array))
    print("Array created with arange:", np.arange(1, 6))
    print("\nNumPy stores and processes numeric data more efficiently.")


if __name__ == "__main__":
    show_intro()
    show_advantages()
    show_uses()
    compare_list_and_array()
