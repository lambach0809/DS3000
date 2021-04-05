'''
    DS2500
    Spring 2021
    OOP Lab - Driver
'''

from runner import Runner
import matplotlib.pyplot as plt


RACHLIN = "rachlin.csv"
STRANGE = "strange.csv"

if __name__ == "__main__":
    # Instantiate two Runner objects so we can compare them
    rachlin = Runner("Rachlin", "green", "x")
    strange = Runner("Strange", "orange", "*")
    
    # Call the Runner method to read in the Runners' data
    rachlin.get_run_data(RACHLIN)    
    strange.get_run_data(STRANGE)
    
    # Plot both runners' distance data
    plt.figure(1)
    rachlin.plot_run_dist()
    strange.plot_run_dist()
    
    # Optional but fun!!!!
    # Plot runners' paces histograms to compare
    # plt.figure(2)
    # plt.subplot(1, 2, 1)
    # rachlin.plot_histo()
    # plt.subplot(1, 2, 2)
    # strange.plot_histo()
                     