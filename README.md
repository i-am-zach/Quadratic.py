# Quadratic.py

### Class: Quadratic
#### Represents a quadratic equation in the form of ax^2 + bx + c
attributes | description
-----------| -----------
a | The coefficient of the squared term
b | The coefficient of the linear term
c | The coefficient of the constant

method | description
-------|------------
factor | Returns a LinearPair object. The LinearPair object consists of two linear equations that when mulitplied equal the quadratic
factor_str | String version of factor() method

### Class: Linear
#### Represents a linear equation in the for of ax + b
attributes | description
-----------| -----------
a | The coefficient of the linear term
b | The coefficient of the constant

method | description
-------|------------
reduce | Reduces the linear equation by the greatest common denominator. Ex: (3x+3) => (x+1)
is_proper | Whether or not the linear equation is composed of whole number coefficients

### Class: LinearPair
#### Represents a factored quadratic equation (ax + b)(cx + d)
attributes | description
-----------| -----------
a | The first linear equation
b | The second linear equation

method | description
-------|------------
factors | Returns a tuple of size two that contains the two linear equations that compose the linear pair

<br />
