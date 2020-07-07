from classes.EmpData import Data
import numpy as np
import matplotlib.pyplot as plt


############### plot absolute #############
def plot_trajectory(trajectory, data,language,**kwargs):
    """
    plot trajectory: theoretic vs empirical
    
    input: 
        - trajectory: array of shape 4xYears (years - XH - XL - XB ) 
        - data: empirical data; data object
        - language: name of the minority language
        - kwargs:
            1) y_scaling: 
                intege
                determines the scale of the y-axis in the plots
                default: 1
            2) y_lim:
                interger
                determines the upper limit of the y-axis in the plots if specified
            3) fname
                string
                if specified, the plot is saved under path and filename specified in fname
    
    """
    
    if "y_scaling" in kwargs.keys():
        y_scaling = kwargs["y_scaling"]
    else:
        y_scaling = 1
        
    
    
    
    plt.figure(figsize=(14,8))

    # N
    plt.plot(trajectory[0, ], (trajectory[1, ] + trajectory[3, ])/y_scaling, color=(.66, 0, .31), label="Population")
    plt.scatter(data.Years, (data.Abs.NB+data.Abs.NH)/y_scaling, color=(.66, 0, .31))

    # NB
    plt.plot(trajectory[0, ], trajectory[3, ]/y_scaling, linestyle = "--",color=(.18, 0.5, .18), label=f"{language} speakers")
    plt.scatter(data.Years, data.Abs.NB/y_scaling, color=(.18, 0.5, .18))
  
    # NH
    plt.plot(trajectory[0, ], trajectory[1, ]/y_scaling, linestyle = ":", color=(.18, .31, .31), label=f"non-{language} speakers")
    plt.scatter(data.Years, data.Abs.NH/y_scaling, color=(.18, .31, .31))
    
    # plot settings
    if "y_lim" in kwargs.keys():
        plt.ylim(0, kwargs["y_lim"]/y_scaling)
    
    
    plt.xlim(trajectory[0, 0] - 1, trajectory[0, -1]+ 1)

    plt.title("Linguistic environment over time",fontweight="bold")
    plt.xlabel("Year",fontweight="bold")
    plt.ylabel(f"Number of speakers in {y_scaling}",fontweight="bold")
    plt.legend()

    if "fname" in kwargs.keys():
        plt.savefig(kwargs["fname"],bbox_inches="tight");
        

        
        
        
############### plot relative #################        
def plot_trajectory_relative(trajectory_abs, data, language, **kwargs):
    """
    plot trajectory relative: theoretic vs empirical
    
        input: 
        - trajectory: array of shape 4xYears (years - XH - XL - XB ) 
        - data: empirical data; data object
        - language: name of minority language, string
        - kwargs:
            1) fname
                string
                if specified, the plot is saved under path and filename specified in fname
    
    
    
    """
    
    trajectory = trajectory_abs.copy()
    trajectory[1:4,:] = trajectory[1:4,:]/(trajectory[1,:]+trajectory[2,:]+trajectory[3,:]) 
    

    N = data.Abs.NB+data.Abs.NH
    
    plt.figure(figsize=(14,8))
    
    # NB
    plt.plot(trajectory[0, ], trajectory[3, ], linestyle = "--",color=(.18, 0.5, .18), label=f"{language} speakers")
    plt.scatter(data.Years, data.Rel.xB, color=(.18, 0.5, .18))
    
    # NH
    plt.plot(trajectory[0, ], trajectory[1, ],linestyle = ":", color=(.18, .31, .31), label=f"non-{language} speakers")
    plt.scatter(data.Years, data.Rel.xH, color=(.18, .31, .31))


    

    
   
    # plot settings

    
    plt.ylim(0, 1)
    plt.xlim(trajectory[0, 0] - 1, trajectory[0, -1]+ 1)


    plt.title("Linguistic environment over time - relative",fontweight="bold")
    plt.xlabel("Year",fontweight="bold")
    plt.ylabel("fraction of speakers",fontweight="bold")
    plt.legend()

    if "fname" in kwargs.keys():
        plt.savefig(kwargs["fname"],bbox_inches="tight");

        
        
        
        
############## plot relative fill #########################
def plot_trajectory_relative_fill(trajectory_abs, data,language, **kwargs):
    """
    plot trajectory relative, filled: theoretic vs empirical
    
    input: 
        - trajectory: array of shape 4xYears (years - XH - XL - XB ) 
        - data: empirical data; data object
        - language: name of minority language, string
        - kwargs:
            1) fname
                string
                if specified, the plot is saved under path and filename specified in fname
    """
    
    trajectory = trajectory_abs.copy()
    trajectory[1:4,:] = trajectory[1:4,:]/(trajectory[1,:]+trajectory[2,:]+trajectory[3,:]) 
    

    N = data.Abs.NB+data.Abs.NH
    
    plt.figure(figsize=(14,8))

    # NH
    plt.fill_between(trajectory[0, ], trajectory[1, ]+trajectory[3, ],trajectory[1, ]*0, color=(.7, .7, .7), label=f"non-{language} speakers")
    #plt.scatter(data.Years, data.Abs.NH/N, color=(.18, .31, .31))
    
    # NL
    #plt.plot(trajectory[0, ], trajectory[2, ], color=(.66, 0, .31), label="XL")
    #plt.scatter(data.Years, data.Abs.NL/N, color=(.66, 0, .31))

    # NB
    plt.fill_between(trajectory[0, ], trajectory[3, ],trajectory[1, ]*0, color=(.31, .31, .31), label=f"{language} speakers")
    plt.scatter(data.Years, data.Abs.NB/N, color=(1, 1, 1))

    
    
   
    # plot settings

    
    plt.ylim(0, 1)
    plt.xlim(trajectory[0,0], trajectory[0,-1])
    


    plt.title("Linguistic environment over time - relative",fontweight="bold")
    plt.xlabel("Year",fontweight="bold")
    plt.ylabel("fraction of speakers",fontweight="bold")
    plt.legend()
    
    
    if "fname" in kwargs.keys():
        plt.savefig(kwargs["fname"],bbox_inches="tight");