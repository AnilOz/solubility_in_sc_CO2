import sympy as sp

def P_sat(A_num, B_num, C_num, T_num):
    """
    Antoine Equation → in MPa
    """

    A, B, C, T = sp.symbols('A B C T')
    P_sat = sp.exp(A-B/(T+C))
    P_sat_fun = sp.lambdify([A, B, C, T], P_sat, 'numpy')
    P_sat_num = P_sat_fun(A_num, B_num, C_num, T_num)

    return P_sat_num
    