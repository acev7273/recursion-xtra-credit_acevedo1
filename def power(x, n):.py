def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / (x * power(x, -n - 1))
    else:
        return x * power(x, n - 1)

if __name__ == "__main__":
    try:
        x = float(input("Enter the base (x): "))
        n = int(input("Enter the exponent (n): "))

        result = power(x, n)
        print(f"{x} to the power of {n} is {result:.4f}")
    except ValueError:
        print("Please enter valid numeric values for x and n.")

