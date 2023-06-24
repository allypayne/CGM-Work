#                          ******************************************
# ~~~~~~~~~~~~~~~~~~~~~~~~ ALLY'S CODE FOR CREATING BINNED DATA PLOTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                          ******************************************
# created June 23 2023


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ~~~~~~~~~~~~~~~~~~ Bordoloi Plot with 3 binned data points~~~~~~~~~~~~~~~~~~~

# data will be a data frame with the detections of interest (ie detections_h1_1r)
# all of the other parameters should written as strings
#the title will say 'Bordoloi Comparison:' + whatever you set for title
def bordoloi_plot_3(data_frame, x_of_interest, y_of_interest, title, xmin=None, xmax=None, ymin=None, ymax= None):
    # the separation between each of the 3 data points is = to 1/3 the range of the data
    lim_1= max(data_frame[x_of_interest])/3
    lim_2=max(data_frame[x_of_interest])*(2/3)
    
    # Creating "coordinate pairs" to plot each of the binned data points
    # Separate between polar and disk regions
    disk= data_frame[data_frame['azimuthal_angle']>45]
    polar= data_frame[data_frame['azimuthal_angle']<45]
    
    # first coord (index=[0])= x coord= x_of_interest, second one= (index=[1])= y coord= y_of_interest
    bin1_disk= (np.mean(disk[disk[x_of_interest]<lim_1][x_of_interest]), np.mean(disk[disk[x_of_interest]<lim_1][y_of_interest]))
    bin1_polar= (np.mean(polar[polar[x_of_interest]<lim_1][x_of_interest]), np.mean(polar[polar[x_of_interest]<lim_1][y_of_interest]))
    

    bin2_disk= (np.mean(disk[(disk[x_of_interest]>lim_1) & (disk[x_of_interest]<lim_2)][x_of_interest]),np.mean(disk[(disk[x_of_interest]>lim_1) & (disk[x_of_interest]<lim_2)][y_of_interest]))
    bin2_polar= (np.mean(polar[(polar[x_of_interest]>lim_1) & (polar[x_of_interest]<lim_2)][x_of_interest]),np.mean(polar[(polar[x_of_interest]>lim_1) & (polar[x_of_interest]<lim_2)][y_of_interest]))


    bin3_disk= (np.mean(disk[disk[x_of_interest]>lim_2][x_of_interest]),np.mean(disk[disk[x_of_interest]>lim_2][y_of_interest]))
    bin3_polar= (np.mean(polar[polar[x_of_interest]>lim_2][x_of_interest]),np.mean(polar[polar[x_of_interest]>lim_2][y_of_interest]))

    # for the disk region
    x_disk= [bin1_disk[0], bin2_disk[0], bin3_disk[0]]
    y_disk= [bin1_disk[1], bin2_disk[1], bin3_disk[1]]
    data_disk= (x_disk,y_disk)
    binned_disk= pd.DataFrame(data_disk).rename({0:x_of_interest, 1:y_of_interest}).transpose()

    # for the polar region
    x_polar= [bin1_polar[0], bin2_polar[0], bin3_polar[0]]
    y_polar= [bin1_polar[1], bin2_polar[1], bin3_polar[1]]
    data_polar= (x_polar,y_polar)
    binned_polar= pd.DataFrame(data_polar).rename({0:x_of_interest, 1:y_of_interest}).transpose()

    # The Plot
    fig, (ax1,ax2) =plt.subplots(1, 2) #sharey='row' , gridspec_kw={'width_ratios': [1,1]}
    fig.set_size_inches(8,5)
    fig.tight_layout()
    fig.suptitle('Bordoloi Comparison:'+title, size= 30, y=1.1)
    plt.subplots_adjust(hspace=0.25, wspace=0.25)
                        
    # On the first plot, put the binned data
    ax1.plot(binned_disk[x_of_interest], binned_disk[y_of_interest], color= 'blue', linestyle= '--',marker='*', label='$\Phi$ >45$^{\circ}$: Disk')
    ax1.plot(binned_polar[x_of_interest], binned_polar[y_of_interest], color= 'black', linestyle= '--',marker='*', label='$\Phi$ >45$^{\circ}$: Polar')
    ax1.set_xlabel('binned (mean) '+x_of_interest)
    ax1.set_ylabel('binned (mean) '+y_of_interest)
    ax1.set_title('Binned Data Points')
    ax1.set_xlim(xmin=xmin, xmax=xmax)
    ax1.set_ylim(ymin=ymin, ymax=ymax)
    ax1.grid()
    ax1.legend()
    
    # On the second plot, put all of the data
    # this is the disk data
    ax2.scatter(data_frame[data_frame['azimuthal_angle']>45][x_of_interest],data_frame[data_frame['azimuthal_angle']>45][y_of_interest], color= 'blue', linestyle= '--',marker='*', label='$\Phi$ >45$^{\circ}$: Disk')
    #polar data
    ax2.scatter(data_frame[data_frame['azimuthal_angle']<45][x_of_interest],data_frame[data_frame['azimuthal_angle']<45][y_of_interest], color= 'black', linestyle= '--',marker='*', label='$\Phi$ >45$^{\circ}$: Polar')
    ax2.set_xlabel(x_of_interest)
    ax2.set_ylabel(y_of_interest)
    ax2.set_title('All Data')
    ax2.grid()
    ax2.set_ylim(ymin=ymin, ymax=ymax)
    ax2.set_xlim(xmin=xmin, xmax=xmax)
    ax2.legend();
                        
# ~~~~~~~~~~~~~~~~~~ Bordoloi Plot with 4 binned data points~~~~~~~~~~~~~~~~~~~

def bordoloi_plot_4(data_frame, x_of_interest, y_of_interest, title, xmin=None, xmax=None, ymin=None, ymax= None):
    # the separation between each of the 3 data points is = to 1/3 the range of the data
    lim_1= max(data_frame[x_of_interest])/4
    lim_2=max(data_frame[x_of_interest])*(1/2)
    lim_3=max(data_frame[x_of_interest])*(3/4)
    
    # Creating "coordinate pairs" to plot each of the binned data points
    # Separate between polar and disk regions
    disk= data_frame[data_frame['azimuthal_angle']>45]
    polar= data_frame[data_frame['azimuthal_angle']<45]
    
    # first coord (index=[0])= x coord= x_of_interest, second one= (index=[1])= y coord= y_of_interest
    bin1_disk= (np.mean(disk[disk[x_of_interest]<lim_1][x_of_interest]), np.mean(disk[disk[x_of_interest]<lim_1][y_of_interest]))
    bin1_polar= (np.mean(polar[polar[x_of_interest]<lim_1][x_of_interest]), np.mean(polar[polar[x_of_interest]<lim_1][y_of_interest]))

    bin2_disk= (np.mean(disk[(disk[x_of_interest]>lim_1) & (disk[x_of_interest]<lim_2)][x_of_interest]),np.mean(disk[(disk[x_of_interest]>lim_1) & (disk[x_of_interest]<lim_2)][y_of_interest]))
    bin2_polar= (np.mean(polar[(polar[x_of_interest]>lim_1) & (polar[x_of_interest]<lim_2)][x_of_interest]),np.mean(polar[(polar[x_of_interest]>lim_1) & (polar[x_of_interest]<lim_2)][y_of_interest]))

    bin3_disk= (np.mean(disk[(disk[x_of_interest]>lim_2) & (disk[x_of_interest]<lim_3)][x_of_interest]),np.mean(disk[(disk[x_of_interest]>lim_2) & (disk[x_of_interest]<lim_3)][y_of_interest]))
    bin3_polar= (np.mean(polar[(polar[x_of_interest]>lim_2) & (polar[x_of_interest]<lim_3)][x_of_interest]),np.mean(polar[(polar[x_of_interest]>lim_2) & (polar[x_of_interest]<lim_3)][y_of_interest]))

    bin4_disk= (np.mean(disk[disk[x_of_interest]>lim_3][x_of_interest]),np.mean(disk[disk[x_of_interest]>lim_3][y_of_interest]))
    bin4_polar= (np.mean(polar[polar[x_of_interest]>lim_3][x_of_interest]),np.mean(polar[polar[x_of_interest]>lim_3][y_of_interest]))

    # for the disk region
    x_disk= [bin1_disk[0], bin2_disk[0], bin3_disk[0], bin4_disk[0]]
    y_disk= [bin1_disk[1], bin2_disk[1], bin3_disk[1], bin4_disk[1]]
    data_disk= (x_disk,y_disk)
    binned_disk= pd.DataFrame(data_disk).rename({0:x_of_interest, 1:y_of_interest}).transpose()

    # for the polar region
    x_polar= [bin1_polar[0], bin2_polar[0], bin3_polar[0]]
    y_polar= [bin1_polar[1], bin2_polar[1], bin3_polar[1]]
    data_polar= (x_polar,y_polar)
    binned_polar= pd.DataFrame(data_polar).rename({0:x_of_interest, 1:y_of_interest}).transpose()

    # The Plot
    fig, (ax1,ax2) =plt.subplots(1, 2) #sharey='row' , gridspec_kw={'width_ratios': [1,1]}
    fig.set_size_inches(8,5)
    fig.tight_layout()
    fig.suptitle('Bordoloi Comparison:'+title, size= 30, y=1.1)
    plt.subplots_adjust(hspace=0.25, wspace=0.25)
                        
    # On the first plot, put the binned data
    ax1.plot(binned_disk[x_of_interest], binned_disk[y_of_interest], color= 'blue', linestyle= '--',marker='*', label='$\Phi$ >45$^{\circ}$: Disk')
    ax1.plot(binned_polar[x_of_interest], binned_polar[y_of_interest], color= 'black', linestyle= '--',marker='*', label='$\Phi$ >45$^{\circ}$: Polar')
    ax1.set_xlabel('binned (mean) '+x_of_interest)
    ax1.set_ylabel('binned (mean) '+y_of_interest)
    ax1.set_title('Binned Data Points')
    ax1.set_xlim(xmin=xmin, xmax=xmax)
    ax1.set_ylim(ymin=ymin, ymax=ymax)
    ax1.grid()
    ax1.legend()
    
    # On the second plot, put all of the data
    # this is the disk data
    ax2.scatter(data_frame[data_frame['azimuthal_angle']>45][x_of_interest],data_frame[data_frame['azimuthal_angle']>45][y_of_interest], color= 'blue', linestyle= '--',marker='*', label='$\Phi$ >45$^{\circ}$: Disk')
    #polar data
    ax2.scatter(data_frame[data_frame['azimuthal_angle']<45][x_of_interest],data_frame[data_frame['azimuthal_angle']<45][y_of_interest], color= 'black', linestyle= '--',marker='*', label='$\Phi$ >45$^{\circ}$: Polar')
    ax2.set_xlabel(x_of_interest)
    ax2.set_ylabel(y_of_interest)
    ax2.set_title('All Data')
    ax2.grid()
    ax2.set_ylim(ymin=ymin, ymax=ymax)
    ax2.set_xlim(xmin=xmin, xmax=xmax)
    ax2.legend();
