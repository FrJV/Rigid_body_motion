from matplotlib import pyplot as plt

def result2plot(Dict):
    '''This fucntions takes a dictionary with a 3 items list as values and returns 4 lists with all te values ordered'''
    keys = []
    Value_0 = []
    Value_1 = []
    Value_2 = []
    for key in Dict:
        keys.append(key)
        Value_0.append(Dict[key][0])
        Value_1.append(Dict[key][1])
        Value_2.append(Dict[key][2])
    return keys, Value_0, Value_1, Value_2

def plot_n(data, axis_name, title):
    '''This functions plots n-1 lists in differnt Y-axis VS 1 list in the X axis'''
    n_axs = len(data)-1
    fig, axs = plt.subplots(n_axs, sharex = True)
    for i in range(n_axs):
        axs[i].plot(data[0], data[i+1])
        axs[i].set_ylabel(axis_name[i+1])
    axs[-1].set_xlabel(axis_name[0])
    axs[0].set_title(title)
    return

def average(X):
    '''Returns the average of the values in list X'''
    return sum(X) / len(X)

def get_intervals(X):
    '''Returns the intervals between the values in list x'''
    intervals = []
    for i in range(1, len(X)):
        intervals.append(X[i]-X[i-1])
    return intervals

def zero_upcrossing_period(t, signal):
    '''This fuctions finds the average zero crossing period for the signal with respect to time T
    index sets the column for wich the period want to be found'''
    zero_crossing_points = []
    for i in range(1, len(signal)):
        if signal[i-1]<0 and (signal[i]==0 or signal[i]>0):
            zero_crossing_points.append(t[i])
    Periods = get_intervals(zero_crossing_points)
    return average(Periods)

def zero_downcrossing_period(t, signal):
    '''This fuctions finds the average zero crossing period for the signal with respect to time T
    index sets the column for wich the period want to be found'''
    zero_crossing_points = []
    for i in range(1, len(signal)):
        if signal[i-1]>0 and (signal[i]==0 or signal[i]<0):
            zero_crossing_points.append(t[i])
    Periods = get_intervals(zero_crossing_points)
    return average(Periods)

def peak_period(t, signal):
    '''This fuctions finds the average peak period for the signal with respect to time T
    index sets the column for wich the period want to be found'''
    peak_points = []
    for i in range(1, len(signal)-1):
        if (signal[i]-signal[i-1])*(signal[i+1]-signal[i])<0:
            peak_points.append(t[i])
    Periods = get_intervals(peak_points)
    return 2*average(Periods)

def remove_offset(signal):
    '''This function centers the values of the list around the average value, making it the new zero'''
    new_zero = average(signal)
    return [x-new_zero for x in signal]
