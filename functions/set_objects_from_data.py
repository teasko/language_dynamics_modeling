from classes.Parameters import ParametersConst
from classes.EmpData import Data

import numpy as np


def get_params(data):
    p = ParametersConst()
    
    # population dynamics  
    p.pop.mu = data["pop"]["mu"]
    p.pop.lam = data["pop"]["lam"]    

    # migration relative
    p.mig_mode_abs = data["mig"]["mode_abs"]
    p.mig_rel.nu = data["mig"]["nu"]
    p.mig_rel.mh = data["mig"]["mh"]
    p.mig_rel.ml = data["mig"]["ml"]
    p.mig_rel.mb = data["mig"]["mb"]

    # schooling
    p.s.sHB = data["s"]["sHB"]
    p.s.sBH = data["s"]["sBH"]
    p.s.sLB = data["s"]["sLB"]
    p.s.sLH = data["s"]["sLH"]

    # adult language learning
    p.a.a_HB = data["a"]["aHB"]
    p.a.a_LB = data["a"]["aLB"]
    p.a.a_BH = data["a"]["aBH"]
    p.a.a_BL = data["a"]["aBL"]

    # Concentration
    p.C.C1 = data["C"]["C1"]
    p.C.C2 = data["C"]["C2"]

    

      
    
    #   HH HB LL LB BB
    p.q.q_mat = np.array([data["q"]["H"],
                          data["q"]["L"],
                          data["q"]["B"]
                         ])
    
    
    
    
    # transmission
    
    return p


def get_emp_data(data):
    emp = Data()
    emp.Years = np.array(data["emp"]["Years"])
    emp.Rel.xB = np.array(data["emp"]["Rel"]["xB"])
    emp.Rel.xH = np.array(data["emp"]["Rel"]["xH"])
    emp.Rel.xL = np.array(data["emp"]["Rel"]["xL"])
    N = np.array(data["emp"]["N"])
    emp.Abs.NH = N * emp.Rel.xH
    emp.Abs.NL = N * 0
    emp.Abs.NB = N * emp.Rel.xB
   
    return emp