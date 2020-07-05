from classes.Parameters import ParametersConst
from functions.dynamics_functions import psi_function, n_r_dot_const, x_r_dot_const
import sys
import numpy as np



def trajectory(T:int, params, data):
    """
    calculate the vector (NH,NL,NB) for all years between data.Years[0] and T
    input: final year T > data.Years[0]
    output: 4-d np-array --> [ [years], [NH], [NL], [NB] ]
    """
    
    T0 = data.Years[0]
    
    if T <= T0:
        raise ValueError("Final year T has to be larger than first year in empirical data")
    
    
    # set initial values
    nout = np.array([[T0],
                     [data.Abs.NH[0]],
                     [data.Abs.NL[0]],
                     [data.Abs.NB[0]] ])
    
    for year in range(T0+1, T+1):
        [NH_dot, NL_dot, NB_dot] = n_r_dot_const(params,
                                                 nout[1, year - T0 - 1],
                                                 nout[2, year - T0 - 1],
                                                 nout[3, year - T0 - 1])
        nout = np.append(nout, [[year],
                                [nout[1, year - T0 -1] + NH_dot],
                                [nout[2, year - T0 -1] + NL_dot],
                                [nout[3, year - T0 -1] + NB_dot]],
                      axis=1)
    return nout



def trajectory_rel(T:int, params, data):
    """
    calculate the vector (xH,xL,xB) for all years between data.Years[0] and T
    input: final year T > data.Years[0]
    output: 4-d np-array --> [ [years], [xH], [xL], [xB] ]
    """
    
    T0 = data.Years[0]
    
    if T <= T0:
        raise ValueError("Final year T has to be larger than first year in empirical data")
    
    
    # set initial values
    xout = np.array([[T0],
                     [data.Rel.xH[0]],
                     [data.Rel.xL[0]],
                     [data.Rel.xB[0]] ])
    
    for year in range(T0+1, T+1):
        [xH_dot, xL_dot, xB_dot] = x_r_dot_const(params,
                                                 xout[1, year - T0 - 1],
                                                 xout[2, year - T0 - 1],
                                                 xout[3, year - T0 - 1])
        xout = np.append(xout, [[year],
                                [xout[1, year - T0 -1] + xH_dot],
                                [xout[2, year - T0 -1] + xL_dot],
                                [xout[3, year - T0 -1] + xB_dot]],
                      axis=1)
    return xout