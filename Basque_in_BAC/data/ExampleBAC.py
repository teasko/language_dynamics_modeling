from classes.Parameters import ParametersConst
from classes.EmpData import Data

import numpy as np


def bac_params():
    p = ParametersConst()
    # population dynamics
    p.pop.mu = 0.0087
    p.pop.lam = 0.0085

    # migration
    #p.mig_abs.ML = 626000
    #p.mig_abs.MB = 47000
    #p.mig_abs.MH = 0

    # migration relative
    p.mig_mode_abs = False
    p.mig_rel.nu = 0.0011
    p.mig_rel.mh = 1
    p.mig_rel.ml = 0
    p.mig_rel.mb = 0

    # schooling
    p.s.sHB = 0.2
    p.s.sBH = 0.24
    p.s.sLB = 0.76
    p.s.sLH = 0.24

    # adult language learning
    p.a.a_HB = 0.005
    p.a.a_LB = 0
    p.a.a_BH = 0
    p.a.a_BL = 0

    # Concentration
    p.C.C1 = 0.47
    p.C.C2 = 0

    # transmission
    p.q.q_mat = np.array([[1, 0.5, 0, 0, 0.051],
                          [0, 0.351, 1, 1, 0.88],
                          [0, 0.149, 0, 0, 0.069],
                          ])
    return p


def bac_emp_data():
    emp = Data()
    emp.Years = np.array([1991, 1996, 2001, 2006, 2011, 2016])  
    emp.Rel.xB = np.array([0.241, 0.277, 0.294, 0.301, 0.320, 0.339])
    emp.Rel.xH = 1 - emp.Rel.xB
    N = np.array([2104805, 2099115, 2079210, 2115383, 2174033, 2171886])
    emp.Abs.NH = N * emp.Rel.xH
    emp.Abs.NL = N * 0
    emp.Abs.NB = N * emp.Rel.xB
   
    return emp