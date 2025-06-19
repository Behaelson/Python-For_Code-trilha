from sympy import symbols, solve

x, y = symbols('x y')
eq1 = 3*x + 4*y - 13
eq2 = x - 2*y - 1

solution = solve((eq1, eq2), (x, y))

print(solution)