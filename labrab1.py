import string

class SetOperations:
    def __init__(self):
        self.universal_set = set(string.ascii_lowercase)  # Универсальное множество (латинский алфавит)

    def union(self, A, B):
        return A.union(B)

    def intersection(self, A, B):
        return A.intersection(B)

    def difference(self, A, B):
        return A.difference(B)

    def complement(self, A):
        return self.universal_set.difference(A)

    def symmetric_difference(self, A, B):
        return A.symmetric_difference(B)

def main():
    set_operations = SetOperations()

    # Пример множеств A, B и C
    A = set(input("Введите элементы множества A (через пробел): ").split())
    B = set(input("Введите элементы множества B (через пробел): ").split())
    C = set(input("Введите элементы множества C (через пробел): ").split())

    print(f"Множество A: {A}")
    print(f"Множество B: {B}")
    print(f"Множество C: {C}")

    # Операции над A и B
    print(f"Объединение A и B: {set_operations.union(A, B)}")
    print(f"Пересечение A и B: {set_operations.intersection(A, B)}")
    print(f"Разность A и B (A - B): {set_operations.difference(A, B)}")
    print(f"Симметрическая разность A и B: {set_operations.symmetric_difference(A, B)}")

    # Операции над A и C
    print(f"\nОбъединение A и C: {set_operations.union(A, C)}")
    print(f"Пересечение A и C: {set_operations.intersection(A, C)}")
    print(f"Разность A и C (A - C): {set_operations.difference(A, C)}")
    print(f"Симметрическая разность A и C: {set_operations.symmetric_difference(A, C)}")

    # Операции над B и C
    print(f"\nОбъединение B и C: {set_operations.union(B, C)}")
    print(f"Пересечение B и C: {set_operations.intersection(B, C)}")
    print(f"Разность B и C (B - C): {set_operations.difference(B, C)}")
    print(f"Симметрическая разность B и C: {set_operations.symmetric_difference(B, C)}")

if __name__ == "__main__":
    main()
