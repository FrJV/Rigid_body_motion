# Import libraries
import Classes
import helper
from matplotlib import pyplot as plt
import math

# Get input values
## Body properties
M = float(input("Specify object's mass [kg]: "))
Stiffness = input("Does the system has a spring? (Yes[Y]; No[N]): ")
if Stiffness == "Y":
    k = float(input("Specify spring's restoring coefficient [kg]: "))
else:
    k = 0.0
## Initial condition
x_0 = float(input("Specify object's initial position with respect to origin [m]: "))
v_0 = float(input("Specify object's initial speed [m/s]: "))
## External force
Force = input("Is the system affected by an external force? (Yes[Y]; No[N]) ")
if Force == "Y":
    Force_type = input("How is this force? [Uniform [U] or Sinusoidal[S]] ")
    if Force_type == "U":
        F0 = float(input("Specify Force value [N]: "))
    if Force_type == "S":
        F0 = float(input("Specify Force maximum value [N]: "))
        w = float(input("Specify Force angular frequency [rad / s]: "))
else:
    Force_type = "U"
    F0 = 0.0
## Other input
t_exp = float(input("Specify time of experiment [s]: "))
dt = float(input("Specify time step [s]: "))

# Initialize
## Generate object
Mass = Classes.PointMass_1D(M, x_0, v_0)
## Prepare list to plot force
F_plot = [0]

# Pipeline
while Mass.t < t_exp:
    # Calculate force
    ## External force
    if Force_type == "U":
        Fext = F0
    if Force_type == "S":
        Fext = F0*math.cos(w*Mass.t)
    F_plot.append(Fext)
    ## Spring force
    F_r = -k*Mass.pos
    # Advance time_step, applying force
    Mass.advance_time_step(dt, (Fext+F_r))

# Calculate result parameters
## Period of the force
if Force_type == "S":
    Tf = 2*math.pi/w
## System natural period
if Stiffness:
    T0 = 2*math.pi*math.sqrt(M/k)

# Extract results
time, X, V, A = helper.result2plot(Mass.history)

# Measure parameters of the response
if Stiffness or Force_type == "S":
    Tp = helper.peak_period(time, X)
    Tz_u = helper.zero_upcrossing_period(time, X)
    Tz_d = helper.zero_downcrossing_period(time, X)

# Plot the results
print("\n___RESULTS___\n")
if Force_type == "S":
    print('Force period: ', round(Tf,2))
if Stiffness:
    print('Calculated sytem period: ', round(T0,2))
if Stiffness or Force_type == "S":
    print('Measured response zero (up)crossing period: ', round(Tz_u,2))
    print('Measured response zero (down)crossing period: ', round(Tz_d,2))
    print('Measured response peak period: ', round(Tp,2))
helper.plot_n([time, F_plot, X, V, A], ["Time [s]","External force [N]", "Position [m]", "Speed [m/s]", "Acceleration [m/s2]"], 'Sinusoidal-Force and spring')
plt.show()
