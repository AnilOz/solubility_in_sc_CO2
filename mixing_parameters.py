import sympy as sp
import numpy as np

from IPython.display import display


def alpha(w_num, T_num, T_c_num):
    w, T, T_c = sp.symbols('w T T_C') 
    alpha = (1+(0.37464 + 1.54226*w - 0.26992*w**2)*(1-sp.sqrt(T/T_c)))**2 
    alpha_fun = sp.lambdify([w, T, T_c], alpha, 'numpy')
    alpha_num = alpha_fun(w_num, T_num, T_c_num)
    
    return alpha_num

def a_PRK(P_c_num, T_c_num, R_num):

    R, T_c, P_c = sp.symbols('R T_C P_C')
    a_PRK = 0.45724*R**2*T_c**2/P_c
    a_prk_fun = sp.lambdify([T_c, P_c, R], a_PRK, 'numpy')
    a_prk_num = a_prk_fun(T_c_num, P_c_num, R_num)
    
    return a_prk_num

def a_mix(y1, y2, a_1_num, a_2_num, k_num, disp=False):

    """
        a_mix for two components system
        k_num is 2x2 matrix which consists of   |k11 k12|
                                                |k21 k22|
                                                                                              
    """

    i, j, a_1, a_2 = sp.symbols('i j a_1 a_2')

    y_num = np.array([y1, y2])
    y_indexed = sp.IndexedBase('y')
    k_indexed = sp.IndexedBase('k')

    a_mix = sp.Sum(sp.Sum(y_indexed[i]*y_indexed[j]*sp.Indexed('a', (i,j)),(j,0,1)),(i,0,1))
    a_matrix = sp.Matrix([[(1-k_indexed[0,0])*sp.sqrt(a_1*a_1), (1-k_indexed[0,1])*sp.sqrt(a_1*a_2)], 
    [(1-k_indexed[1,0])*sp.sqrt(a_2*a_1), (1-k_indexed[1,1])*sp.sqrt(a_2*a_2)]])
    a_mix_1 = a_mix.replace(sp.Indexed('a', (i,j)), a_matrix[i,j])
    a_mix_2 = a_mix_1.doit()
    a_mix_fun = sp.lambdify([y_indexed, a_1, a_2, k_indexed], a_mix_2, 'numpy')
    a_mix_num = a_mix_fun(y_num, a_1_num, a_2_num, k_num)

    display_equations = disp

    if display_equations==True:
        print("\nCalculation of constant a_mix in Van der Vaals mixing rules\n")
        display(a_mix, a_mix_1, a_mix_2, a_mix_num)

    return a_mix_num

def a_m_cosolvent(y1, y2, a_1_num, a_2_num, a_3_num, k_num, disp=False):

    """ a_mix for the solutions with cosolvents (Three component system)

        k_num is 3x3 matrix which consists of |k11 k12 k13|
                                              |k21 k22 k23|
                                              |k31 k32 k33|

    """

    i, j, a_1, a_2, a_3 = sp.symbols('i j a_1 a_2 a_3')

    y_num = np.array([y1, y2, 1-y1-y2])
    y_indexed = sp.IndexedBase('y')
    k_indexed = sp.IndexedBase('k')

    a_mix = sp.Sum(sp.Sum(y_indexed[i]*y_indexed[j]*sp.Indexed('a', (i,j)),(j,0,2)),(i,0,2))
    a_matrix = sp.Matrix([[(1-k_indexed[0,0])*sp.sqrt(a_1*a_1), (1-k_indexed[0,1])*sp.sqrt(a_1*a_2), (1-k_indexed[0,2])*sp.sqrt(a_1*a_3)],
                          [(1-k_indexed[1,0])*sp.sqrt(a_2*a_1), (1-k_indexed[1,1])*sp.sqrt(a_2*a_2), (1-k_indexed[1,2])*sp.sqrt(a_2*a_3)],
                          [(1-k_indexed[2,0])*sp.sqrt(a_3*a_1), (1-k_indexed[2,1])*sp.sqrt(a_3*a_2), (1-k_indexed[2,2])*sp.sqrt(a_3*a_3)]])

    a_mix_1 = a_mix.replace(sp.Indexed('a', (i,j)), a_matrix[i,j])
    a_mix_2 = a_mix_1.doit()
    a_mix_fun = sp.lambdify([y_indexed, a_1, a_2, a_3, k_indexed], a_mix_2, 'numpy')
    a_mix_cosl = a_mix_fun(y_num, a_1_num, a_2_num, a_3_num, k_num)

    display_equations = disp

    if display_equations==True:
        print("\nCalculation of constant a_mix in Van der Vaals mixing rules for three component system \n ")
        display(a_mix, a_mix_1, a_mix_2, a_mix_cosl)

    return a_mix_cosl

def a_star(y_1, y_2, a_1_num, a_2_num, k_num, disp=False):


    j, a_1, a_2 = sp.symbols('j a_1 a_2')


    y_num = np.array([y_1, y_2])
    k_indexed = sp.IndexedBase('k')

    a_matrix = sp.Matrix([[(1-k_indexed[0,0])*sp.sqrt(a_1*a_1), (1-k_indexed[0,1])*sp.sqrt(a_1*a_2)]])


    y_indexed = sp.IndexedBase('y')
    a_s = 2*sp.Sum(y_indexed[j]*sp.Indexed('a', (0,j)),(j,0,1))
    a_s_1 = a_s.replace(sp.Indexed('a', (0,j)), a_matrix[0,j])
    a_s_2 = a_s_1.doit()
    a_s_fun = sp.lambdify([y_indexed, a_1, a_2, k_indexed], a_s_2, 'numpy')
    a_s_num = a_s_fun(y_num, a_1_num, a_2_num, k_num)

    display_equations = disp

    if display_equations==True:
        display(a_s, a_s_1, a_s_2, a_s_num)

    return a_s_num


def a_s_cosolvent(y_1, y_2, a_1_num, a_2_num, a_3_num, k_num, disp=False):

    """ a*_i for the solutions with cosolvents (Three component system)

        k_num is 3x3 matrix which consists of |k11 k12 k13|
                                              |k21 k22 k23|
                                              |k31 k32 k33|

    """

    j, a_1, a_2, a_3 = sp.symbols('j a_1 a_2 a_3')


    y_num = np.array([y_1, y_2, 1-y_1-y_2])

    k_indexed = sp.IndexedBase('k')

    a_matrix = sp.Matrix([[(1-k_indexed[0,0])*sp.sqrt(a_1*a_1), (1-k_indexed[0,1])*sp.sqrt(a_1*a_2), (1-k_indexed[0,2])*sp.sqrt(a_1*a_3)]])

    y_indexed = sp.IndexedBase('y')

    a_s = 2*sp.Sum(y_indexed[j]*sp.Indexed('a', (0,j)),(j,0,2))
    a_s_1 = a_s.replace(sp.Indexed('a', (0,j)), a_matrix[0,j])
    a_s_2 = a_s_1.doit()
    a_s_fun = sp.lambdify([y_indexed, a_1, a_2, a_3, k_indexed], a_s_2, 'numpy')
    a_s_num = a_s_fun(y_num, a_1_num, a_2_num, a_3_num, k_num)

    display_equations = disp

    if display_equations==True:
        display(a_s, a_s_1, a_s_2, a_s_num)

    return a_s_num



def b_PRK(P_c_num, T_c_num, R_num):

    R, T_c, P_c = sp.symbols('R T_C P_C')
    b_PRK = 0.07780*R*T_c/P_c
    b_prk_fun = sp.lambdify([T_c, P_c, R], b_PRK, 'numpy')
    b_prk_num = b_prk_fun(T_c_num, P_c_num, R_num)

    return b_prk_num


def b_m_cosolvent(y1, y2, b_1_num, b_2_num, b_3_num, l_num, disp=False):

    """ b_mix for the solutions with cosolvents (Three component system)

        l_num is 3x3 matrix which consists of |l11 l12 l13|
                                              |l21 l22 l23|
                                              |l31 l32 l33|

    """

    i, j, b_1, b_2, b_3 = sp.symbols('i j b_1 b_2 b_3')


    y_num = np.array([y1, y2, 1-y1-y2])
    y_indexed = sp.IndexedBase('y')
    l_indexed = sp.IndexedBase('l')

    b_mix = sp.Sum(1*sp.Sum(y_indexed[i]*y_indexed[j]*sp.Indexed('b', (i,j)),(j,0,2)),(i,0,2))
    b_matrix = sp.Matrix([[0.5*(1-l_indexed[0,0])*(b_1+b_1), 0.5*(1-l_indexed[0,1])*(b_1+b_2), 0.5*(1-l_indexed[0,2])*(b_1+b_3)],
                          [0.5*(1-l_indexed[1,0])*(b_2+b_1), 0.5*(1-l_indexed[1,1])*(b_2+b_2), 0.5*(1-l_indexed[1,2])*(b_2+b_3)],
                          [0.5*(1-l_indexed[2,0])*(b_3+b_1), 0.5*(1-l_indexed[2,1])*(b_3+b_2), 0.5*(1-l_indexed[2,2])*(b_3+b_3)]]) 
    b_mix_1 = b_mix.replace(sp.Indexed('b', (i,j)), b_matrix[i,j])
    b_mix_2 = b_mix_1.doit()
    b_mix_fun = sp.lambdify([y_indexed, b_1, b_2, b_3, l_indexed], b_mix_2, 'numpy')
    b_mix_num = b_mix_fun(y_num, b_1_num, b_2_num, b_3_num, l_num)
    
    display_equations = disp

    if display_equations==True:
        print("\nCalculation of constant b_mix in Van der Vaals mixing rules for three component system \n")
        display(b_mix, b_mix_1, b_mix_2, b_mix_num)

    return b_mix_num


def b_mix(y1, y2, b_1_num, b_2_num, l_num, disp=False):

    """
        b_mix for the solutions without cosolvents (Two component system)        
        l_num is 2x2 matrix which consists of   |l11 l12|
                                                |l21 l22|
                                                                                              
    """   


    i, j, b_1, b_2 = sp.symbols('i j b_1 b_2')


    y_num = np.array([y1, y2])
    y_indexed = sp.IndexedBase('y')
    l_indexed = sp.IndexedBase('l')

    b_mix = sp.Sum(1*sp.Sum(y_indexed[i]*y_indexed[j]*sp.Indexed('b', (i,j)),(j,0,1)),(i,0,1))
    b_matrix = sp.Matrix([[0.5*(1-l_indexed[0,0])*(b_1+b_1), 0.5*(1-l_indexed[0,1])*(b_1+b_2)],
    [0.5*(1-l_indexed[1,0])*(b_2+b_1), 0.5*(1-l_indexed[1,1])*(b_2+b_2)]]) 
    b_mix_1 = b_mix.replace(sp.Indexed('b', (i,j)), b_matrix[i,j])
    b_mix_2 = b_mix_1.doit()
    b_mix_fun = sp.lambdify([y_indexed, b_1, b_2, l_indexed], b_mix_2, 'numpy')
    b_mix_num = b_mix_fun(y_num, b_1_num, b_2_num, l_num)
    
    display_equations = disp

    if display_equations==True:

        print("\nCalculation of constant b_mix in Van der Vaals mixing rules \n")
        display(b_mix, b_mix_1, b_mix_2, b_mix_num)


    return b_mix_num


def b_star(y1, y2, b_1_num, b_2_num, b_mix_num, l_num, disp=False):

    """ b_mix for the solutions with cosolvents (Three component system)

    l_num is 2*2 matrix which consists of   |l11 l12|
                                            |l21 l22|

    """

    j, b_1, b_2, b_mix = sp.symbols('j b_1 b_2 b_mix')

    y_num = np.array([y1, y2])
    y_indexed = sp.IndexedBase('y')
    l_indexed = sp.IndexedBase('l')

    b_s = 2 * sp.Sum(y_indexed[j]*sp.Indexed('b', (0,j)), (j,0,1)) - b_mix  
    b_matrix = sp.Matrix([[0.5*(1-l_indexed[0,0])*(b_1+b_1), 0.5*(1-l_indexed[0,1])*(b_1+b_2)]]) 
    b_s_1 = b_s.replace(sp.Indexed('b', (0,j)), b_matrix[0,j])
    b_s_2 = b_s_1.doit()
    b_s_fun = sp.lambdify([y_indexed, b_1, b_2, b_mix, l_indexed], b_s_2, 'numpy')
    b_s_num = b_s_fun(y_num, b_1_num, b_2_num, b_mix_num, l_num)
    
    display_equations = disp

    if display_equations==True:
        display(b_s, b_s_1, b_s_2, b_s_num)

    return b_s_num


def b_s_cosolvent(y1, y2, b_1_num, b_2_num, b_3_num, b_mix,  l_num, disp=False):

    """ b_mix for the solutions with cosolvents (Three component system)

    l_num is 3x3 matrix which consists of |l11 l12 l13|
                                            |l21 l22 l23|
                                            |l31 l32 l33|

    """

    j, b_1, b_2, b_3 = sp.symbols('j b_1 b_2 b_3')


    y_num = np.array([y1, y2, 1-y1-y2])
    y_indexed = sp.IndexedBase('y')
    l_indexed = sp.IndexedBase('l')

    b_s = 2 * sp.Sum(y_indexed[j]*sp.Indexed('b', (0,j)), (j,0,2)) - b_mix


    b_matrix = sp.Matrix([[0.5*(1-l_indexed[0,0])*(b_1+b_1), 0.5*(1-l_indexed[0,1])*(b_1+b_2), 0.5*(1-l_indexed[0,2])*(b_1+b_3)]]) 
    b_s_1 = b_s.replace(sp.Indexed('b', (0,j)), b_matrix[0,j])
    b_s_2 = b_s_1.doit()
    b_s_fun = sp.lambdify([y_indexed, b_1, b_2, b_3, l_indexed], b_s_2, 'numpy')
    b_s_num = b_s_fun(y_num, b_1_num, b_2_num, b_3_num, l_num)
    
    display_equations = disp

    if display_equations==True:
        display(b_s, b_s_1, b_s_2, b_s_num)

    return b_s_num
