from fugacity_coeff import fugacity_scf
from mixing_parameters import a_mix, a_PRK, alpha, b_mix, b_PRK, a_star, b_star, a_m_cosolvent, a_s_cosolvent, b_m_cosolvent, b_s_cosolvent
from Z_prk import Z_PRK
from P_sat import P_sat

import sympy as sp
import numpy as np
from sympy import pprint

def find_solubility_cosol(y_co, v_solid, P_num, P_sub_num, R_num, T_num, a_1, a_2, a_3,  b_1, b_2, b_3, k_num, l_num, disp=False):

    """        
        l_num is 3x3 matrix which consists of   |l11 l12 l13|
                                                |l21 l22 l23|
                                                |l31 l32 l33|

        k_num is 3x3 matrix which consists of   |k11 k12 k13|
                                                |k21 k22 k23|
                                                |k31 k32 k33|                                              
    """

    y_init = P_sub_num/P_num
    display = disp

    a_mix_num_f = a_m_cosolvent(1 - y_init - y_co, y_init, a_1, a_2, a_3, k_num)
    b_mix_num_f = b_m_cosolvent(1 - y_init- y_co, y_init, b_1, b_2, b_3, l_num)

    
    a_s_num_f = a_s_cosolvent(y_init, 1 - y_init - y_co, a_2, a_1, a_3, k_num)
    b_s_num_f = b_s_cosolvent(y_init, 1 - y_init - y_co, b_2, b_1, b_3, b_mix_num_f, l_num)

    Z_f = Z_PRK(P_num, T_num, R_num, a_mix_num_f, b_mix_num_f)


    if Z_f.size == 0:
        y_solu = y_init

    else:
        Z_num_f = np.amax(Z_f)
        ln_phi_scf_num_f = fugacity_scf(P_num, R_num, T_num, Z_num_f, a_mix_num_f, b_mix_num_f, a_s_num_f, b_2)  
        y_solu = y_init*np.exp(v_solid * (P_num - P_sub_num)/(R_num*T_num))/np.exp(ln_phi_scf_num_f)
    
    y = [y_init, y_solu]
    
    while np.abs(y[-1] - y[-2])/y[-1]> 0.001:        
        
        a_mix_num = a_m_cosolvent(1 - y[-1] - y_co, y[-1], a_1, a_2, a_3, k_num)
        b_mix_num = b_m_cosolvent(1 - y[-1] - y_co, y[-1], b_1, b_2, b_3, l_num)
        a_s_num = a_s_cosolvent(y[-1], 1-y[-1]-y_co, a_2, a_1, a_3, k_num)
        b_s_num = b_s_cosolvent(y[-1], 1-y[-1]-y_co, b_2, b_1, b_3, b_mix_num, l_num)
        
        Z_num = np.amax(Z_PRK(P_num, T_num, R_num, a_mix_num, b_mix_num))
                
        ln_phi_scf_num_f = fugacity_scf(P_num, R_num, T_num, Z_num, a_mix_num, b_mix_num, a_s_num, b_2) 
        y_sol = y_init*np.exp(v_solid * (P_num - P_sub_num)/(R_num*T_num))/np.exp(ln_phi_scf_num_f)

        y.append(y_sol)
        if display == True:
            print(a_mix_num_f, b_mix_num_f)
            print(a_mix_num, b_mix_num)
            Poytning = np.exp(v_solid * (P_num - P_sub_num)/(R_num*T_num))
            E = np.exp(v_solid * (P_num - P_sub_num)/(R_num*T_num))/np.exp(ln_phi_scf_num_f)
            fugacity = np.exp(ln_phi_scf_num_f)
            print('Enhancement Factor: {0} \nPoynting Correction: {1}\nFugacity: {2}'.format(E, Poytning, fugacity))
            pprint('Z= {0}'.format(Z_num))
            print(y)
            print(y[-1])
            print(P_num)

    return y[-1]


def find_solubility(v_solid, P_num, P_sub_num, R_num, T_num, a_1, a_2, b_1, b_2, k_num, l_num, disp=False):

    """        
        l_num is 2x2 matrix which consists of   |l11 l12|
                                                |l21 l22|
    

        k_num is 2x2 matrix which consists of   |k11 k12|
                                                |k21 k22|
                                                                                              
    """

    y_init = P_sub_num/P_num
    display = disp

    a_mix_num_f = a_mix(1 - y_init, y_init, a_1, a_2, k_num)
    b_mix_num_f = b_mix(1 - y_init, y_init, b_1, b_2, l_num)

    a_s_num_f = a_star(y_init, 1 - y_init, a_2, a_1, k_num)
    b_s_num_f = b_star(y_init, 1 - y_init, b_2, b_1, l_num)

    Z_f = Z_PRK(P_num, T_num, R_num, a_mix_num_f, b_mix_num_f)

    if Z_f.size == 0:
        y_solu = y_init

    else:
        Z_num_f = np.amax(Z_f)
        ln_phi_scf_num_f = fugacity_scf(P_num, R_num, T_num, Z_num_f, a_mix_num_f, b_mix_num_f, a_s_num_f, b_2)  
        y_solu = y_init*np.exp(v_solid * (P_num - P_sub_num)/(R_num*T_num))/np.exp(ln_phi_scf_num_f)
    y = [y_init, y_solu]
    
    while np.abs(y[-1] - y[-2])/y[-1]> 0.001:        
        
        a_mix_num = a_mix(1 - y[-1], y[-1], a_1, a_2, k_num)
        b_mix_num = b_mix(1 - y[-1], y[-1], b_1, b_2, l_num)

        a_s_num = a_star(y[-1], 1-y[-1], a_2, a_1, k_num)
        b_s_num = b_star(y[-1], 1-y[-1], b_2, b_1, l_num)


        Z_num = Z_PRK(P_num, T_num, R_num, a_mix_num, b_mix_num)
        ln_phi_scf_num_f = fugacity_scf(P_num, R_num, T_num, Z_num, a_mix_num, b_mix_num, a_s_num, b_2) 
        y_sol = y_init*np.exp(v_solid * (P_num - P_sub_num)/(R_num*T_num))/np.exp(ln_phi_scf_num_f)

        y.append(y_sol)
        if display == True:
            Poytning = np.exp(v_solid * (P_num - P_sub_num)/(R_num*T_num))
            E = np.exp(v_solid * (P_num - P_sub_num)/(R_num*T_num))/np.exp(ln_phi_scf_num_f)
            fugacity = np.exp(ln_phi_scf_num_f)
            print('Enhancement Factor: {0} \nPoynting Correction: {1}\nFugacity: {2}'.format(E, Poytning, fugacity))
            pprint('Z= {0}'.format(Z_num))
            print(y)
            print(y[-1])

    return y[-1]