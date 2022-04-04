import sympy as sp
import numpy as np

def Z_PRK(P_num, T_num, R_num, a_num, b_num):
        
    """    Z_PRK(P_num, T_num, R_num, a_num, alpha_num, b_num)

            Real Number
    """
    
    A, B, P, R, T = sp.symbols('A B P R T')
    Z = sp.Symbol('Z', real=True)
    A = a_num*P_num/(R_num**2*T_num**2)
    B = b_num*P_num/(R_num*T_num)
    Z_eq = Z**3 - (1-B)*Z**2 + (A - 3*B**2 - 2*B)*Z - (A*B - B**2 - B**3)
    Z_eq_1 = np.float64(sp.solve(Z_eq, Z))

    return Z_eq_1
