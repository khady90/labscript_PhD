from lyse import *
from pylab import *
import numpy
import pylab
import mise
# Please don't forget to write a path to your detuning file !!!! like this way:

#path = 'C:\\Experiments\\example_experiment\\MOT_loading with acquire JC\\2019\\10\\29\\n_inf_param.h5'
path = 'C:\\Experiments\\example_experiment\\MOT_loading_wc\\2020\\06\\29\\P600mV'


# Let's obtain the dataframe for all of lyse's currently loaded shots:
df = data()

# Now let's see how the MOT load rate varies with, say a global called
# 'detuning', which might be the detuning of the MOT beams:
#mot_b_field = df['mot_b_field'] #global name from runmanager; changing mot_b_field
#detuning_3D = df['detuning_3D']
detuning_2D = df['detuning_2D']
detuning_pusher = df['detuning_pusher']

# mot loading parameters were saved by a routine called single_exp_fit:

mot_n_equlibrium = df['2Dopt_single_exp_fit_wc', 'mot_n_equlibrium']
mot_tau = df['2Dopt_single_exp_fit_wc', 'mot_tau']
#mot_c = df['single_exp_fit', 'mot_c']



figure(1) #plotting how detuning_2D changes
subplots_adjust(hspace=0.4, wspace=0.4)
subplot(2,1,1)
plot(detuning_2D, mot_n_equlibrium, 'c.', label='data')
ticklabel_format(axis='y',style='sci', scilimits=(0,0))
ylabel('mot_n_equlibrium')
legend()

subplot(2,1,2)
plot(detuning_2D, mot_tau, 'b.', label='data')
#ticklabel_format(axis='y',style='sci', scilimits=(0,0))
xlabel('detuning_2D [MHz]')
ylabel('mot_tau')
legend()
savefig(path + '\\detuning_2D.png')


figure(2) #plotting how detuning_pusher changes
subplots_adjust(hspace=0.4, wspace=0.4)
subplot(2,1,1)
plot(detuning_pusher, mot_n_equlibrium, 'c.', label='data')
ticklabel_format(axis='y',style='sci', scilimits=(0,0))
ylabel('mot_n_equlibrium')
legend()

subplot(2,1,2)
plot(detuning_pusher, mot_tau, 'b.', label='data')
#ticklabel_format(axis='y',style='sci', scilimits=(0,0))
xlabel('detuning_pusher [MHz]')
ylabel('mot_tau')
legend()
savefig(path + '\\detuning_pusher.png')



figure(3)
subplots_adjust(hspace=0.4, wspace=0.4)
subplot(2,1,1)
plot(detuning_2D, mot_n_equlibrium, 'c.', label='data')
ticklabel_format(axis='y',style='sci', scilimits=(0,0))
xlabel('detuning_2D [MHz]')
ylabel('mot_n_equlibrium')
legend()

subplot(2,1,2)
plot(detuning_pusher, mot_n_equlibrium, 'b.', label='data')
ticklabel_format(axis='y',style='sci', scilimits=(0,0))
xlabel('detuning_pusher [MHz]')
ylabel('mot_n_equlibrium')
legend()
savefig(path + '\\detunings.png')
