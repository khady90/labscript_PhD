import h5py
import pandas as pd
import os
from decimal import Decimal

fpath = 'C:\\Experiments\\example_experiment\\MOT_loading_wc\\2020\\06\\29\\P600mV'

entries = os.listdir(fpath)
df = pd.DataFrame(columns=['mot_n_equlibrium', 'mot_tau'])
for file in entries:
    try:
        if '.h5' in file:
            f = h5py.File(fpath + '\\' +file, 'r')
            df = df.append({
                'mot_n_equlibrium': f['results/2Dopt_single_exp_fit'].attrs['mot_n_equlibrium'],
                'mot_tau': f['results/2Dopt_single_exp_fit'].attrs['mot_tau']
                },ignore_index=True)
            f.close()
    except:
        print('Empty or damaged file was found')
        pass
mean_mot_n_equlibrium = df['mot_n_equlibrium'].mean()
std_mot_n_equlibrium = df['mot_n_equlibrium'].std()
mean_mot_tau = df['mot_tau'].mean()
std_mot_tau = df['mot_tau'].std()
print('mot_n_equlibrium: mean = {} and std = {}'.format('%.2E' % Decimal(mean_mot_n_equlibrium), '%.2E' % Decimal(std_mot_n_equlibrium)))
print('mot_tau: mean = {} and std = {}'.format(mean_mot_tau, std_mot_tau))
print('rate(mot_n_equlibrium/mot_tau) = {}'.format('%.2E' % Decimal(mean_mot_n_equlibrium/mean_mot_tau)))
results = open(fpath + "\\results.txt","w")
results.write('mot_n_equlibrium: mean = {} and std = {} \n'.format('%.2E' % Decimal(mean_mot_n_equlibrium), '%.2E' % Decimal(std_mot_n_equlibrium)))
results.write('mot_tau: mean = {} and std = {} \n'.format(mean_mot_tau, std_mot_tau))
results.write('rate(mot_n_equlibrium/mot_tau) = {} \n'.format('%.2E' % Decimal(mean_mot_n_equlibrium/mean_mot_tau)))
results.close
