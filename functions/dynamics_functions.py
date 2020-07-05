from classes.PsiClass import PsiClass
from classes.Parameters import ParametersConst
import sys
import numpy as np




# 1. psi function for language transmission within the family

def psi_function(param, xh, xl, xb):
    """
    calculates the psi-function for language transmission in the family
    
    input:  floats xh,xl,xb with xh+hl+xb = 1
            param: model parameters
    output: psi object 
    """
    
    param_local = ParametersConst()
    try:
            param_local = param
    except TypeError:
        print("param input is no proper Parameters object")

    c1 = param_local.C.C1
    c2 = param_local.C.C2

    psi =  PsiClass()

    if xh == 1:
        psi.HH = 1
        psi.HL = 0
        psi.HB = 0
        psi.LL = 0
        psi.LB = 0
        psi.BB = 0
    else:
        quot = 1 + c1*xh / (1 - xh)
        psi.HH = xh**2 + c1 * xh * (1 - xh) + (1 - c1) * xh * xl
        psi.HL = 0
        psi.HB = 2 * (1 - c1) * xh * xb
        psi.LL = quot * (xl + c2 * xb) * xl
        psi.LB = 2 * quot * (1 - c2) * xl * xb + (1 - c1) * xh * xl
        psi.BB = quot * (c2 * xl + xb) * xb

    test_sum = psi.HH + psi.HL + psi.HB + psi.LL + psi.LB + psi.BB
    if (test_sum > 1 + 0.00000001) or (test_sum < 1 - 0.00000001):
        raise ValueError("psi does not add up to 1")
        
        
        #print("xh, xl, xb = %.2f, %.2f, %.2f" % (xh, xl, xb))
        #print(test_sum)
        #sys.exit("psi does not add up to 1")

    return psi







# 2. derivative of the dynamic model

def n_r_dot_const(param, nh, nl, nb):
    """
    calculates derivative of the vector (nh,nl,nb)
    
    input:  vectors nh, nl, nb
            param: model parameters
    output: vectors NHdot = dot(nh), NLdot = dot(nl), NBdot = dot(nb) as [NHdot, NLdot, NBdot]
    """
    param_local = ParametersConst()

    try:
        param_local = param
    except TypeError:
        print("param is no proper Parameters object")

    try:
        if (not np.array(nh).shape == np.array(nl).shape) or (not np.array(nh).shape == np.array(nb).shape):
            sys.exit("N_H, N_L and N_B have to be of the same size")
    except TypeError:
        print("error in test of N_H, N_L, N_B")

    # population size
    n = nh + nl + nb

    # relative numbers
    xh = nh / n
    xl = nl / n
    xb = nb / n

    # family formation
    psi = psi_function(param_local, xh, xl, xb)
    psi_vec = np.array([psi.HH, psi.HB, psi.LL, psi.LB, psi.BB])

    # calculate f functions
    f = np.matmul(param_local.q.q_mat, psi_vec.transpose())
    f_H = f[0]
    f_L = f[1]
    f_B = f[2]

    # adult learning parameters
    a_HB = param_local.a.a_HB
    a_LB = param_local.a.a_LB

    g_H = (1 - param_local.s.sHB) * f_H + param_local.s.sBH * f_B + param_local.s.sLH * f_L
    g_L = (1 - param_local.s.sLB - param_local.s.sLH) * f_L
    g_B = (1 - param_local.s.sBH) * f_B + param_local.s.sHB * f_H + param_local.s.sLB * f_L

    if param_local.mig_mode_abs:
        NHdot = -(param_local.pop.mu + (1 - param_local.pop.mu) * a_HB) * nh \
                + param_local.pop.lam * n * g_H + param_local.mig_abs.MH
        NLdot = -(param_local.pop.mu + (1 - param_local.pop.mu) * a_LB) * nl \
                + param_local.pop.lam * n * g_L + param_local.mig_abs.ML
        NBdot = -param_local.pop.mu * nb + (1 - param_local.pop.mu) * a_HB * nh + (
                1 - param_local.pop.mu) * a_LB * nl + param_local.pop.lam * n * g_B + param_local.mig_abs.MB
    else:
        NHdot = -(param_local.pop.mu + (1 - param_local.pop.mu) * a_HB) * nh + param_local.pop.lam * n * g_H \
                + param_local.mig_rel.nu * param_local.mig_rel.mh * n

        NLdot = -(param_local.pop.mu + (1 - param_local.pop.mu) * a_LB) * nl + param_local.pop.lam * n * g_L \
                + param_local.mig_rel.nu * param_local.mig_rel.ml * n

        NBdot = -param_local.pop.mu * nb + (1 - param_local.pop.mu) * a_HB * nh + (
                1 - param_local.pop.mu) * a_LB * nl + param_local.pop.lam * n * g_B \
                + param_local.mig_rel.nu * param_local.mig_rel.mb * n

    return [NHdot, NLdot, NBdot]


# 3. derivative of the dynamic model

def x_r_dot_const(param, xh, xl, xb):
    """
    calculates derivative of the vector (xh,xl,xb)
    
    input:  vectors xh, xl, xb
            param: model parameters
    output: vectors NHdot = dot(nh), NLdot = dot(nl), NBdot = dot(nb) as [NHdot, NLdot, NBdot]
    """
    
    
    param_local = ParametersConst()

    try:
        param_local = param
    except TypeError:
        print("param is no proper Parameters object")


    if (xh+xl+xb > 1+0.0000001) or (xh+xl+xb < 1-0.0000001):
        raise ValueError('xh+xl+xb not equal to 1.')
        
 
    # family formation
    psi = psi_function(param_local, xh, xl, xb)
    psi_vec = np.array([psi.HH, psi.HB, psi.LL, psi.LB, psi.BB])

    # calculate f functions
    f = np.matmul(param_local.q.q_mat, psi_vec.transpose())
    f_H = f[0]
    f_L = f[1]
    f_B = f[2]

    # adult learning parameters
    a_HB = param_local.a.a_HB
    a_LB = param_local.a.a_LB

    g_H = (1 - param_local.s.sHB) * f_H + param_local.s.sBH * f_B + param_local.s.sLH * f_L
    g_L = (1 - param_local.s.sLB - param_local.s.sLH) * f_L
    g_B = (1 - param_local.s.sBH) * f_B + param_local.s.sHB * f_H + param_local.s.sLB * f_L

    
    if param_local.mig_mode_abs:
        # not implemented here
        raise NotImplementedError("the absolute case is not implemented here")
    else:
        xhdot = -(1 - param_local.pop.mu) * a_HB * xh + param_local.pop.lam * (g_H - xh) \
                + param_local.mig_rel.nu * (param_local.mig_rel.mh - xh)

        xldot = -(1 - param_local.pop.mu) * a_LB * xl + param_local.pop.lam * (g_L -xl)\
                + param_local.mig_rel.nu * (param_local.mig_rel.ml -xl)

        xbdot = -xhdot-xldot

    return [xhdot,xldot,xbdot]
