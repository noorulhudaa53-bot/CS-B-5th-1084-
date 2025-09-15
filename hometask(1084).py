#Question#01
class Loan:
    def __init__(self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000, borrower=""):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower
    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = self.__loanAmount * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-self.__numberOfYears * 12))
        return round(monthlyPayment, 2)
    def getTotalPayment(self):
        return round(self.getMonthlyPayment() * self.__numberOfYears * 12, 2)

# Example Usage
loan = Loan(15, 40, 7800, "John Doe")
print("Loan Monthly Payment:", loan.getMonthlyPayment())
print("Loan Total Payment:", loan.getTotalPayment())

#Question#02
class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
    def getBMI(self):
        return round(self.__weight / (self.__height ** 2), 2)
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 20.5:
            return "Underweight"
        elif bmi < 25.8:
            return "Normal weight"
        elif bmi < 30.9:
            return "Overweight"
        else:
            return "Obese"

# Example Usage
bmi1 = BMI("Aqdas", 19, 35, 1.95)
print("BMI:", bmi1.getBMI(), "Status:", bmi1.getStatus())

#Question#03
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / denominator,
                       (self.imag * other.real - self.real * other.imag) / denominator)

# Example Usage
c1 = Complex(9, 3)
c2 = Complex(2, 5)
print("Complex Subtraction:", c1 - c2)
print("Complex Multiplication:", c1 * c2)
print("Complex Division:", c1 / c2)

# Question#04
from math import gcd
class RationalNumber:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common
    def __add__(self, other):
        return RationalNumber(self.numerator * other.denominator + other.numerator * self.denominator,
                              self.denominator * other.denominator)

# Example Usage
r1 = RationalNumber(8, 4)
r2 = RationalNumber(0, 5)
print("Rational Addition:", r1 + r2)

# Question#05
class Polynomial:
    def __init__(self, coefficients):
        """Initialize polynomial with a list of coefficients."""
        self.coefficients = coefficients
    def __del__(self):
        """Destructor to clean up."""
        print("Polynomial object deleted")
    def get_coefficients(self):
        """Returns the list of coefficients."""
        return self.coefficients
    def set_coefficients(self, coefficients):
        """Sets new coefficients."""
        self.coefficients = coefficients
    def __add__(self, other):
        """Overloads the + operator to add two polynomials."""
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for i in range(len(self.coefficients)):
            result[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            result[i] += other.coefficients[i]
        return Polynomial(result)
    def __sub__(self, other):
        """Overloads the - operator to subtract two polynomials."""
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for i in range(len(self.coefficients)):
            result[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            result[i] -= other.coefficients[i]
        return Polynomial(result)
    def __mul__(self, other):
        """Overloads the * operator to multiply two polynomials."""
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, coef1 in enumerate(self.coefficients):
            for j, coef2 in enumerate(other.coefficients):
                result[i + j] += coef1 * coef2
        return Polynomial(result)
    def __iadd__(self, other):
        """Overloads the += operator."""
        self.coefficients = (self + other).coefficients
        return self
    def __isub__(self, other):
        """Overloads the -= operator."""
        self.coefficients = (self - other).coefficients
        return self
    def __imul__(self, other):
        """Overloads the *= operator."""
        self.coefficients = (self * other).coefficients
        return self
    def __eq__(self, other):
        """Overloads the = operator (comparison)."""
        return self.coefficients == other.coefficients
    def __str__(self):
        """Returns a string representation of the polynomial."""
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef:
                terms.append(f"{coef}x^{i}")
        return " + ".join(terms) if terms else "0"

# Example Usage
p1 = Polynomial([2, 3, 4])  # Represents 2 + 3x + 4x^2
p2 = Polynomial([1, 2, 3])  # Represents 1 + 2x + 3x^2
print("Polynomial 1:", p1)
print("Polynomial 2:", p2)
# Addition
p3 = p1 + p2
print("Addition:", p3)
# Subtraction
p4 = p1 - p2
print("Subtraction:", p4)
# Multiplication
p5 = p1 * p2
print("Multiplication:", p5)
# Compound Assignment Operators
p1 += p2
print("p1 after += p2:", p1)
p1 -= p2
print("p1 after -= p2:", p1)
p1 *= p2
print("p1 after *= p2:", p1)