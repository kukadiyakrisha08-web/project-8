import numpy as np


class DataAnalytics:

    def __init__(self):
        self.__array = None


    # Create Array
    def create_array(self):

        print("\n1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            values = list(map(int, input("Enter values separated by space: ").split()))
            self.__array = np.array(values)

        elif choice == 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            values = list(map(int, input("Enter values separated by space: ").split()))
            self.__array = np.array(values).reshape(rows, cols)

        elif choice == 3:
            d1 = int(input("Enter first dimension: "))
            d2 = int(input("Enter second dimension: "))
            d3 = int(input("Enter third dimension: "))

            values = list(map(int, input("Enter values separated by space: ").split()))
            self.__array = np.array(values).reshape(d1, d2, d3)

        print("\nArray Created:")
        print(self.__array)


    # Indexing
    def indexing(self):

        if self.__array is None:
            print("Create array first.")
            return

        index = input("Enter index values separated by comma: ")

        try:
            indexes = tuple(map(int, index.split(",")))
            print("Element:", self.__array[indexes])

        except:
            print("Invalid index.")


    # Slicing
    def slicing(self):

        if self.__array is None:
            print("Create array first.")
            return

        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))

        print("Sliced Array:")
        print(self.__array[start:end])


    # Concatenate Arrays
    def concatenate_arrays(self):

        arr1 = np.array(
            list(map(int, input("Enter first array values: ").split()))
        )

        arr2 = np.array(
            list(map(int, input("Enter second array values: ").split()))
        )

        result = np.concatenate((arr1, arr2))

        print("Concatenated Array:")
        print(result)


    # Split Array
    def split_array(self):

        if self.__array is None:
            print("Create array first.")
            return

        parts = int(input("Enter number of parts: "))

        try:
            result = np.array_split(self.__array, parts)

            print("Split Array:")
            print(result)

        except:
            print("Cannot split array.")


    # Mathematical Operations
    def mathematical_operations(self):

        if self.__array is None:
            print("Create array first.")
            return

        values = list(
            map(int, input("Enter second array values: ").split())
        )

        arr2 = np.array(values)

        try:
            arr2 = arr2.reshape(self.__array.shape)

            print("Addition:")
            print(self.__array + arr2)

            print("Subtraction:")
            print(self.__array - arr2)

            print("Multiplication:")
            print(self.__array * arr2)

            print("Division:")
            print(self.__array / arr2)

        except:
            print("Array sizes are not matching.")


    # Dot Product
    def dot_product(self):

        arr1 = np.array(
            list(map(int, input("Enter first array values: ").split()))
        )

        arr2 = np.array(
            list(map(int, input("Enter second array values: ").split()))
        )

        try:
            print("Dot Product:", np.dot(arr1, arr2))

        except:
            print("Invalid arrays.")


    # Matrix Multiplication
    def matrix_multiplication(self):

        rows1 = int(input("Enter rows of first matrix: "))
        cols1 = int(input("Enter columns of first matrix: "))

        values1 = list(
            map(int, input("Enter first matrix values: ").split())
        )

        matrix1 = np.array(values1).reshape(rows1, cols1)


        rows2 = int(input("Enter rows of second matrix: "))
        cols2 = int(input("Enter columns of second matrix: "))

        values2 = list(
            map(int, input("Enter second matrix values: ").split())
        )

        matrix2 = np.array(values2).reshape(rows2, cols2)

        try:
            print("Matrix Multiplication:")
            print(np.matmul(matrix1, matrix2))

        except:
            print("Matrix multiplication is not possible.")


    # Search Value
    def search_value(self):

        if self.__array is None:
            print("Create array first.")
            return

        value = int(input("Enter value to search: "))

        result = np.where(self.__array == value)

        print("Found at index:")
        print(result)


    # Sort Array
    def sort_array(self):

        if self.__array is None:
            print("Create array first.")
            return

        print("1. Ascending")
        print("2. Descending")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(np.sort(self.__array))

        elif choice == 2:
            print(np.sort(self.__array)[::-1])


    # Filter Array
    def filter_array(self):

        if self.__array is None:
            print("Create array first.")
            return

        value = int(input("Enter value: "))

        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(self.__array[self.__array > value])

        elif choice == 2:
            print(self.__array[self.__array < value])

        elif choice == 3:
            print(self.__array[self.__array == value])


    # Aggregating Functions
    def aggregating_functions(self):

        if self.__array is None:
            print("Create array first.")
            return

        print("Sum:", np.sum(self.__array))
        print("Mean:", np.mean(self.__array))
        print("Median:", np.median(self.__array))
        print("Standard Deviation:", np.std(self.__array))
        print("Variance:", np.var(self.__array))


    # Statistical Functions
    def statistical_functions(self):

        if self.__array is None:
            print("Create array first.")
            return

        print("Minimum:", np.min(self.__array))
        print("Maximum:", np.max(self.__array))
        print("25 Percentile:", np.percentile(self.__array, 25))
        print("50 Percentile:", np.percentile(self.__array, 50))
        print("75 Percentile:", np.percentile(self.__array, 75))


    # Correlation Coefficient
    def correlation(self):

        arr1 = np.array(
            list(map(int, input("Enter first array values: ").split()))
        )

        arr2 = np.array(
            list(map(int, input("Enter second array values: ").split()))
        )

        try:
            print("Correlation Coefficient:")
            print(np.corrcoef(arr1, arr2))

        except:
            print("Arrays must have same size.")


    # Class Method
    @classmethod
    def project_name(cls):
        print("NumPy Analyzer")


    # Static Method
    @staticmethod
    def developer_message():
        print("Welcome to NumPy Analyzer")


# Object Creation
analytics = DataAnalytics()


# Menu Driven Interface
while True:

    print("\n===== NumPy Analyzer =====")

    print("1. Create Array")
    print("2. Indexing")
    print("3. Slicing")
    print("4. Concatenate Arrays")
    print("5. Split Array")
    print("6. Mathematical Operations")
    print("7. Dot Product")
    print("8. Matrix Multiplication")
    print("9. Search Value")
    print("10. Sort Array")
    print("11. Filter Array")
    print("12. Aggregating Functions")
    print("13. Statistical Functions")
    print("14. Correlation Coefficient")
    print("15. Class Method")
    print("16. Static Method")
    print("17. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        analytics.create_array()

    elif choice == 2:
        analytics.indexing()

    elif choice == 3:
        analytics.slicing()

    elif choice == 4:
        analytics.concatenate_arrays()

    elif choice == 5:
        analytics.split_array()

    elif choice == 6:
        analytics.mathematical_operations()

    elif choice == 7:
        analytics.dot_product()

    elif choice == 8:
        analytics.matrix_multiplication()

    elif choice == 9:
        analytics.search_value()

    elif choice == 10:
        analytics.sort_array()

    elif choice == 11:
        analytics.filter_array()

    elif choice == 12:
        analytics.aggregating_functions()

    elif choice == 13:
        analytics.statistical_functions()

    elif choice == 14:
        analytics.correlation()

    elif choice == 15:
        DataAnalytics.project_name()

    elif choice == 16:
        DataAnalytics.developer_message()

    elif choice == 17:
        print("Program Exited.")
        break

    else:
        print("Invalid Choice.")