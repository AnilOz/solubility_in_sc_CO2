import sympy as sp
import numpy as np

from IPython.display import display, Latex




def fugacity_scf(P_num, R_num, T_num, Z_num, a_num, b_num, a_s_num, b_s_num, disp = False):
    """
        ln_phi_scf_num = ln_phi_scf_fun(P_num, R_num, T_num, Z_num, a_num, b_num)

        alpha will be taken into account in a_num.

        return ln_phi_scf_num
        """
    
    phi_scf, P, n, R, T, V, Z, a, b, a_s, b_s, Z_1= sp.symbols('phi_scf P n R T V Z a b a_s b_s Z_1')
    
    A, B = sp.symbols('A B')

    ln_phi_scf_5 = (b_s/b)*(Z_1-1) - sp.log(Z_1 - B) - (A)/(B*sp.sqrt(8))*(a_s/a - b_s/b)*sp.log((Z_1+(1+sp.sqrt(2))*B)/(Z_1+(1-sp.sqrt(2))*B))
    
    ln_phi_scf_6 = ln_phi_scf_5.subs({A: a*P/(R**2*T**2), B: b*P/(R*T)})

    ln_phi_scf_fun = sp.lambdify([P, R, T, Z_1, a, b, a_s, b_s], ln_phi_scf_6, 'numpy')

     
    ln_phi_scf_num = ln_phi_scf_fun(P_num, R_num, T_num, Z_num, a_num, b_num, a_s_num, b_s_num)

    display_equations = disp

    if display_equations==True:
        
        P_EOS = n*R*T/(V-n*b) - n**2*a/(V*(V+n*b)+n*b*(V-n*b))
        ln_phi_scf = sp.Eq(sp.ln(phi_scf), sp.Integral(-P/(n*R*T) + 1/V, (V, sp.oo, V)) + (Z-1) - sp.ln(Z))
        ln_phi_scf_1 = ln_phi_scf.subs(P, P_EOS)
        
        modified_integral_term = -1/(V-n*b)+(n*a/(R*T))/(V*(V+n*b)+n*b*(V-n*b))
        
        ln_phi_scf_1.func
        ln_phi_scf_2 = ln_phi_scf_1.replace(ln_phi_scf_1.args[1].args[3].args[0].args[1], modified_integral_term)
        ln_phi_scf_2.args[1].args[3].args[0]
        first_term = sp.Integral(ln_phi_scf_2.args[1].args[3].args[0].args[0]+ln_phi_scf_2.args[1].args[3].args[0].args[1], (V,sp.oo,V))
        second_term = sp.Integral(ln_phi_scf_2.args[1].args[3].args[0].args[2], (V,sp.oo,V))
        ln_phi_scf_3 = first_term.doit() + second_term.doit() + (Z-1) + - sp.ln(Z)
        ln_phi_scf_4 = sp.simplify(ln_phi_scf_3.subs(V, Z*n*R*T/P))

        print("\nCalculation of the fugacity of the component in supercritical phase\n")
        display(ln_phi_scf, ln_phi_scf_1, ln_phi_scf_2, ln_phi_scf_3, ln_phi_scf_4, ln_phi_scf_5, ln_phi_scf_6)


       
    return ln_phi_scf_num


