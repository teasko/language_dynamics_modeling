import numpy as np
import sys


class PopulationParam(object):
    def __int__(self, lam=None, mu=None):
        self.lam = lam
        self.mu = mu
    


class MigrationParamAbs(object):
    def __int__(self, MH=None, ML=None, MB=None):
        self.ML = ML
        self.MB = MB
        self.MH = MH


class MigrationParamRel(object):
    def __init__(self, nu=None, mh=None, ml=None, mb=None):
        self.nu = nu
        self.mh = mh
        self.ml = ml
        self.mb = mb


class ConcentrationParam(object):
    def __init__(self, c1=None, c2=None):
        self.C1 = c1
        self.C2 = c2


class StatusParam(object):
    def __init__(self, sH=None, sL=None):
        self.SH = sH
        self.SL = sL


class FamilyTransmissionParamQ(object):
    def __init__(self, ee1=None, ee2=None, zeta1=None, zeta2=None):
        self.ee1 = ee1
        self.ee2 = ee2
        self.zeta1 = zeta1
        self.zeta2 = zeta2
    # No checks yet


class FamilyTransmissionParamQCost(object):
    def __init__(self, q_mat=None):
        self.q_mat = q_mat

    def check_numbers(self):
        try:
            if not np.array(self.q_mat).shape == (3, 5):
                print(np.array(self.q_mat).shape)
                sys.exit("q_mat is not of dimensions [3, 5]")
        except TypeError:
            print("q_mat is not a matrix")
        return True


class SchoolingParam(object):
    def __init__(self, sHB=None, sBH=None, sLB=None, sLH=None):
        self.sHB = sHB
        self.sBH = sBH
        self.sLB = sLB
        self.sLH = sLH


class AdultLearningParam(object):
    def __init__(self, theta=None, phi=None, vH=None, vL=None):
        self.theta = theta
        self.phi = phi
        self.vH = vH
        self.vL = vL


class AdultLearningParamConst(object):
    def __init__(self, a_LB=None, a_HB=None, a_BL=None, a_BH=None):
        self.a_LB = a_LB
        self.a_HB = a_HB
        self.a_BL = a_BL
        self.a_BH = a_BH


class Parameters(object):
    def __init__(self):
        self.pop = PopulationParam()
        self.mig_mode_abs = []
        self.mig_abs = MigrationParamAbs()
        self.mig_rel = MigrationParamRel()
        self.C = ConcentrationParam()
        self.S = StatusParam()
        self.q = FamilyTransmissionParamQ()
        self.s = SchoolingParam()
        self.a = AdultLearningParam()

    def print_params(self):
        self.pop.print_p()
        
    # there are no tests whatsoever yet


class ParametersConst(object):
    def __init__(self):
        self.pop = PopulationParam()
        self.mig_mode_abs = []
        self.mig_abs = MigrationParamAbs()
        self.mig_rel = MigrationParamRel()
        self.C = ConcentrationParam()
        self.q = FamilyTransmissionParamQCost()
        self.s = SchoolingParam()
        self.a = AdultLearningParamConst()

    def print_params(self):
        print(f"lam = {self.pop.lam}")
        print(f"mu = {self.pop.mu}")
        print("")
        if self.mig_mode_abs == True:
            print(f"M_L = {self.mig_abs.ML}")
            print(f"M_B = {self.mig_abs.MB}")
            print(f"M_H = {self.mig_abs.MH}")       
        else:
            print(f"nu = {self.mig_rel.nu}")
            print(f"m_H = {self.mig_rel.mh}")
            print(f"m_L = {self.mig_rel.ml}")
            print(f"m_B = {self.mig_rel.mb}")
        print("")
        print(f"C1 = {self.C.C1}")
        print(f"C2 = {self.C.C2}")
        print("")
        print("q = ")
        print(self.q.q_mat)
        print("")
        print(f"sHB = {self.s.sHB}")
        print(f"sBH = {self.s.sBH}")
        print(f"sLB = {self.s.sLB}")
        print(f"sLH = {self.s.sLH}")
        print("")
        print(f"a_LB = {self.a.a_LB}")
        print(f"a_HB = {self.a.a_HB}")
        print(f"a_BL = {self.a.a_BL}")
        print(f"a_BH = {self.a.a_BH}")
        

    
        
        
        
        
        
        
        
        
