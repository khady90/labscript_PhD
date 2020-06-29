from lyse import *
from pylab import *
import scipy
from scipy.optimize import curve_fit
import numpy as np
import math

# Let's obtain our data for this shot -- globals, image attributes and
# the results of any previously run single-shot routines:
#ser = data(path)
ser = data(filepath=None, host='localhost')

# Get a global called x:
#load_time = ser['load_time']
#initial_voltage = ser['initial_voltage']

# Get a result saved by another single-shot analysis routine which has
# already run. The result is called 'y', and the routine was called
# 'some_routine':
#y = ser['some_routine','y']

# Image attributes are also stored in this series:
#w_x2 = ser['side','absorption','OD','Gaussian_XW']

# If we want actual measurement data, we'll have to instantiate a Run object:
run = Run(path)

# Obtaining a trace:
t, fluorescence = run.get_trace('fluorescence') #get fluorescence in V as an array
#print(fluorescence)
#atom_number = fluorescence * 3e6 #change flourescence into number of atoms
#print(atom_number)

# Now we might do some analysis on this data. Say we've written a
# expone fit function (or we're calling some other libaries exp
# fit function):

#popt, pcov = scipy.optimize.curve_fit(lambda x,n_inf,tau,const: n_inf*(1-np.exp(-x/tau))+const,  t,  fluorescence)
popt, pcov = scipy.optimize.curve_fit(lambda x, n_eq, tau, c: n_eq*(1-np.exp(-x/tau))+c, t, fluorescence)
perr = np.sqrt(np.diag(pcov))
print(popt) #popt = optimal values for the parameters; array
atom_number = popt[0]*3e6
print(atom_number)
print(pcov) #pcov = estimated covariance of the popt; 2D array
print(perr) #perr = one standard deviation errors on the parameters

# We might wish to plot the fit on the trace to show whether the fit is any good:

plot(t, fluorescence, 'bo', label='data')
plot(t, popt[0]*(1-np.exp(-t/popt[1])) + popt[2], 'r', label='fit')
#plot(t, popt[0]*(1-np.exp(-t/popt[1]))+popt[2], 'r', label='n_inf*(1-np.exp(-tl/tau))+const') #this is for 1/exp function
ticklabel_format(axis='y',style='sci', scilimits=(0,0))
xlabel('load time')
ylabel('fluorescence')
legend()

# Don't call show() ! lyse will introspect what figures have been made
# and display them once this script has finished running. If you call
# show() it won't find anything. lyse keeps track of figures so that new
# figures replace old ones, rather than you getting new window popping
# up every time your script runs.

# We might wish to save this result so that we can compare it across
# shots in a multishot analysis:
run.save_result('mot_n_equlibrium', atom_number)
run.save_result('mot_tau', popt[1])
run.save_result('mot_c', popt[2])













'''
# Get a global called x
x = ser['hold_time_first']

# Get a result saved by another single-shot analysis routine which has
# already run. The result is called 'y', and the routine was called
# 'some_routine':
#y = ser['some_routine','y']

# Image attributes are also stored in this series:
# w_x2 = ser['side','absorption','OD','Gaussian_XW']

# If we want actual measurement data, we'll have to instantiate a Run object:
run = Run(path)

# Obtaining a trace:
M = run.get_trace('fluorescence')

# Now we might do some analysis on this data. Say we've written
# linear fit function (or we're calling some other libaries linear
# fit function):
#m, c = linear_fit(t, M)

# We might wish to plot the fit on the trace to show whether the fit is any good:
#plot(t,MOT_fluorescence,label='data')
#plot(t,m*t + x,label='linear fit')
#xlabel('time')
#ylabel('MOT_fluorescence')
#legend()

# Don't call show() ! lyse will introspect what figures have been made
# and display them once this script has finished running. If you call
# show() it won't find anything. lyse keeps track of figures so that new
# figures replace old ones, rather than you getting new window popping
# up every time your script runs.

# We might wish to save this result so that we can compare it across
# shots in a multishot analysis:
#run.save_result('MOT_fluorescence', 1)
#run.save_result_array(name='MOT_fluorescence',data=(t, M))
run.save_result_array(name='fluorescence',data=(M))
run.save_result_array(name='Test_channel_0',data=(N))
'''
