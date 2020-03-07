import math

class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        """String version of quadratic"""
        a, b, c = self.a, self.b, self.c
        if a == 1:
            a = ""
        if b == 1:
            b = ""
        if a == -1:
            a = "-"
        if b == -1:
            b = "-"
        a1 = f"{a}x^2" if self.a else ""
        b1 = f"{b}x" if self.b else ""
        c1 = f"{c}" if self.c else ""
        terms = list(filter(lambda x: bool(x), [a1, b1, c1]))
        output = str(terms[0])
        for term in terms[1:]:
            if str(term).startswith("-"):
                term = term[1:]
                output += " - "
            else:
                output += " + "
            output += term
        return output


    def __repr__(self):
        return self.__str__()

    def factor(self):
        """
        Factors the quadratic into a linear pair
        @return: type<LinearPair>
        """
        if self.a == 0:
            if self.b:
                solution = -self.c / self.b
            else:
                solution = self.c
            return LinearPair(Linear(1, -solution), Linear(0, 1), coeff=1)
        r1, r2 = quadratic_formula(self.a, self.b, self.c)
        if r1 and r2:
            l1, l2 = Linear(1, r1), Linear(1, r2)
            if not l1.is_proper():
                l1 = l1 * self.a
                l1 = l1.reduce()
            if not l2.is_proper():
                l2 = l2 * self.a
                l2 = l2.reduce()
            pair = LinearPair(l1, l2, coeff=self.a)
            return pair
        else:
            return None

    def factor_str(self):
        """
        Returns string form of factored quadratic
        @return: type<str>
        """
        pair = self.factor()
        return str(pair)

class Linear:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reduce(self):
        """Reduces linear equation by dividing both coefficients by greatest common denominator"""
        a, b = self.a, self.b
        if a < 0 and b < 0:
            a = -a
            b = -b
        _gcf = gcf(a, b)
        a /= _gcf
        b /= _gcf
        return Linear(a, b)

    def __mul__(self, other):
        """
        Ex: Linear(a, b) * Linear(x, y)
        """
        return Linear(self.a * other, self.b * other)

    def __rmul__(self, other):
        """
        Ex:  Linear(x, y) * Linear(a, b)
        """
        return Linear(self.a * other, self.b * other)
        

    def __str__(self):
        """
        String version of Linear equation (ax + b)
        """
        a, b = self.a, self.b
        if self.is_proper():
            a = int(a)
            b = int(b)
        if a == 1:
            a = ""
        elif a == -1:
            a = "-"
        a1 = f"{a}x"
        b1 = f" + {b}" if b > 0 else f" - {abs(b)}"
        return a1 + b1

    def __repr__(self):
        return self.__str__()

    def is_proper(self):
        """
        Returns if the linear equation has only whole number coeffcients
        """
        a, b = self.a, self.b
        return int(a) == a and int(b) == b

class LinearPair:
        def __init__(self, a, b, coeff=1):
            assert(isinstance(a, Linear))
            assert(isinstance(b, Linear))
            self.a = a
            self.b = b
            self.coeff = int(coeff)

        def __str__(self):
            if self.a.a == 0:
                return f"({self.b})"
            if self.b.a == 0:
                return f"({self.a})"
            if self.a.a * self.b.a != self.coeff:
                temp_coeff = self.coeff // (self.a.a * self.b.a)
                return f"{temp_coeff}({self.a})({self.b})"
            return f"({self.a})({self.b})"

        def factors(self):
            return (self.a, self.b)

def quadratic_formula(a, b, c):
    assert(a != 0)
    try:
        r1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
        r2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
    except ValueError:
        return (None, None)
    else:
        return (-r1, -r2)

def gcf(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcf(b,a%b) 