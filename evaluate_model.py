import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pyrenn as prn
from IPython.display import display


def evaluate_model(y_test, prediction):
    train_error = np.abs(y_test - prediction)
    mean_error = np.mean(train_error)
    max_error = np.max(train_error)
    min_error = np.min(train_error)
    standard_deviation = np.std(train_error)
    print(f'Mean Error = {mean_error} \nMax Error = {max_error}\nMin Error = {min_error}\nStandard Deviation = {standard_deviation}')

def plot_predictions(y_test, prediction):
    plt.style.use('default')
    plt.figure(figsize=(20,5))
    #plt.plot(train_error)
    plt.plot(prediction)
    plt.plot(y_test)
    plt.show()


def model_predictions(T_num, P_num, T_c_num, P_c_num, w_num, v_num, path):

    sol_model=prn.loadNN(path)
    T_c = np.full([1, len(P_num)], T_c_num)
    P_c = np.full([1, len(P_num)], P_c_num)
    w = np.full([1, len(P_num)], w_num)
    v_s = np.full([1, len(P_num)], v_num)
    T = np.full([1, len(P_num)], T_num)
    x_naphtalene = np.array([T_c[0], P_c[0], w[0], v_s[0], T[0], P_num])
    y_naphtalene = prn.NNOut(x_naphtalene, sol_model) 

    return y_naphtalene


def AARD(y_cal_num, y_exp_num, disp=False):
    
    displayer = disp

    N, i = sp.symbols('N i')
    y_cal = sp.IndexedBase('y_cal')
    y_exp = sp.IndexedBase('y_exp')

    AARD_0 = 100/N*sp.Sum(sp.Abs(y_cal[i] - y_exp[i])/y_exp[i], (i,0,N-1))
    AARD_1 = 100/N*sp.Sum(sp.Abs(y_cal[i] - y_exp[i])/y_exp[i], (i,0,N-1)).doit()
    AARD_fun = sp.lambdify([y_cal, y_exp, N], AARD_1, 'numpy')
    AARD_num = AARD_fun(y_cal_num, y_exp_num, len(y_exp_num))
    

    if displayer == True:
        display(AARD_0, AARD_1)

    return AARD_num
    
