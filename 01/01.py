def bisection_method(func, a, b ,error_accept):
    def f(x):
        f = eval(func)
        return f
    error = abs(b - a)
    while error > error_accept:
        c = (b + a ) / 2

        if f(a) * f(b) >= 0:
            print ("Equation cannot be solved")
            quit()
        
        elif f(a) * f(c) < 0:
            b = c
            error = abs(b - a)
        elif f(b) * f(c) < 0:
            a = c
            error = abs(b - a)
        else:
            print("Unexpected Error") 
            quit()
    print(f"The error is {error}")
    print(f"X is between {a} and {b}")    

bisection_method("(4*x ** 3) + 3*x - 1", 0,2,0.0005)           
