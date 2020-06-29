from lyse import *
from pylab import *
import numpy
import pylab
import mise


# Please don't forget to write a path to your detuning file !!!! like this way:

#path = 'C:\\Experiments\\example_experiment\\MOT_loading with acquire JC\\2019\\10\\29\\n_inf_param.h5'
path = 'C:\\Experiments\\example_experiment\\MOT_loading\\2020\\01\\28\\b_field'

# Let's obtain the dataframe for all of lyse's currently loaded shots:
df = data()

# Now let's see how the MOT load rate varies with, say a global called
# 'detuning', which might be the detuning of the MOT beams:
mot_b_field = df['mot_b_field'] #global name from runmanager; changing mot_b_field

# mot load rate was saved by a routine called ....:

mot_n_equlibrium = df['single_exp_fit', 'mot_n_equlibrium']
mot_tau = df['single_exp_fit', 'mot_tau']
#mot_c = df['single_exp_fit', 'mot_c']

#load_rates = df['mot loadrate']

# Let's plot them against each other:

#plot(loadtime, mot_n_equlibrium, 'bo', label='data')
subplot(2,1,1)
plot(mot_b_field, mot_n_equlibrium, 'co', label='data')
ticklabel_format(axis='y',style='sci', scilimits=(0,0))
#xlabel('mot_b_field')
ylabel('mot_n_equlibrium')
legend()

subplot(2,1,2)
plot(mot_b_field, mot_tau, 'bo', label='data')
ticklabel_format(axis='y',style='sci', scilimits=(0,0))
xlabel('mot_b_field')
ylabel('mot_tau')
legend()

'''subplot(3,1,3)
plot(mot_b_field, mot_c, 'bo', label='data')
ticklabel_format(axis='y',style='sci', scilimits=(0,0))
xlabel('mot_b_field')
ylabel('mot_c')
legend()
'''
