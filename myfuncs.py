def exp(x, n=100, e=2.7182818284590451, tol=None, print_result=False):
    '''
    This function calculates the exponential value of x.
    :param x: float number. we calculate the value of exp(x)
    :param n: integer number. the number of terms to be calculated in the taylor expansion, which is 100 by default.
    :param e: float number. The customized natural logarithm value, which is 2.7182818284590451 by default.
    :param tol: float number. The tolerance between two consecutive iterations, which is None by default. This function will ignore the parameter n if tol is assigned.
    :param print_result:  boolean value. The result will be printed on the screen when this parameter is True. It is False by default.
    :return: the value of exp(x)
    '''
    x0 = int(round(x))
    z = x-x0
    ans = 0
    if tol:
        taylor_term = e**x0
        k = 0
        while tol/e**x0 <= taylor_term:
            tmp = 1
            for i in range(k):
                tmp *= (i + 1)
            taylor_term = z ** k / tmp
            ans += taylor_term
            k += 1
    else:
        if n <= 0 or type(n) != int:
            print("Please set the parameter n to be a positive integer")
            return
        for k in range(n):
            tmp = 1
            for i in range(k):
                tmp *= (i+1)
            ans += z**k/tmp
    output = ans*e**x0
    if print_result:
        print("The exponential value of %d is : %.10f" % (x, output))
    return output

def ln(x, n=100, initial_guess=1.0, tol=None, print_result=False):
    '''
    This function calculates the ln value of x.
    :param x: float number. We calculate the value of ln(x), which should be positive.
    :param n: Interger. The number of iterations for the newton's method, which is 100 by default.
    :param initial_guess: float number. The initial guess of the answer, which is 1.0 by default.
    :param tol: float number. The tolerance between two consecutive iterations, which is None by default. This function will ignore the parameter n if tol is assigned.
    :return: the value of ln(x)
    '''
    if x<=0:
        print("Please input a positive value. Return None")
        return
    s = 1.0
    if tol:
        k = 0
        s_diff = tol + 1
        while tol <= s_diff:
            s_update = s - 1 + x * exp(-s)
            s_diff = abs(s-s_update)
            s = s_update
            k += 1
    else:
        for k in range(n):
            s = s - 1 + x * exp(-s)
    if print_result:
        print("The logarithm value of %d is : %.10f" % (x, s))
    return s

def test_exp():
    exp(5, n=-5)
    exp(5, e=2.7)
    print(exp(5, tol=1e-10))
    exp(5, print_result=True)

def test_ln():
    ln(-5)
    ln(0)
    print(ln(5, n=50))
    print(ln(5, initial_guess=5))
    print(ln(5, tol=1e-5))
    ln(5, print_result=True)
