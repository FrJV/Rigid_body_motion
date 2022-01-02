#Classes
class PointMass_1D:
    ''' Class that defines a point mass object moving in one dimention
    It stores the position, speed and acceleration of the object with respect to an initial zero
    In order to "move", it gets as input a time step and a force applied during that time step'''

    ## Modify so pos_init and v_init are modified based on F_init???
    ### Rethink how the F_init is used!!

    def __init__(self, Mass, pos_init = 0.0, v_init = 0.0):
        self.mass = Mass
        self.pos = pos_init
        self.speed = v_init
        self.acc = 0.0
        self.t = 0.0
        self.history = {self.t: [self.pos, self.speed, self.acc]}
        return

    def advance_time_step(self, time_step, Force):
        self.t = self.t + time_step
        self.set_acceleration(Force)
        self.set_speed(time_step)
        self.set_position(time_step)
        self.add_to_history()
        return

    def add_to_history(self):
        self.history[self.t] = [self.pos, self.speed, self.acc]
        return

    def set_acceleration(self, Force):
        """
        Gets the acceleration of the body based on a force. Force is positive is goes forward in x axis
        """
        self.acc = Force / self.mass
        return

    def set_speed(self, time_step):
        """
        Gets the speed based on acceleration.
        """
        delta_v = self.acc*time_step
        self.speed += delta_v

        return

    def set_position(self, time_step):
        """
        Gets the speed based on acceleration.
        """
        delta_pos = self.speed*time_step
        self.pos += delta_pos
        return

class PointMass_3D:
    ''' Class that defines a point mass object moving in three dimentions. Each dimention is an object of class 1D
    It stores the position, speed and acceleration of the object with respect to an initial zero
    In order to "move", it gets as input a time step and a force applied during that time step'''

    ## In Development

    def __init__(self, Mass, pos_init = [0.0, 0.0, 0.0], v_init = [0.0, 0.0, 0.0]):
        self.x = Mass_1D(Mass, pos_init[0], v_init[0])
        self.y = Mass_1D(Mass, pos_init[1], v_init[1])
        self.z = Mass_1D(Mass, pos_init[2], v_init[2])
        self.t = [0.0]
        return

    def advance_time_step(self, time_step, Force):
        self.x.advance_time_step(time_step, Force[0])
        self.y.advance_time_step(time_step, Force[1])
        self.z.advance_time_step(time_step, Force[2])
        current_t = self.t[-1] + time_step
        self.t.append(current_t)
        self.check_time()
        return

    def check_time():
        if self.t[-1] != self.x.t:
            print('Error: Different time in axis. Check code')
        if self.t[-1] != self.y.t:
            print('Error: Different time in axis. Check code')
        if self.t[-1] != self.z.t:
            print('Error: Different time in axis. Check code')

    def get_position_history(self):
        position_history = {}
        for time in self.t:
            X = self.x.history[time][0]
            Y = self.y.history[time][0]
            Z = self.z.history[time][0]
            position_history[time] = [X, Y, Z]
        return position_history

    def get_speed_history(self):
        speed_history = {}
        for time in self.t:
            Vx = self.x.history[time][1]
            Vy = self.y.history[time][1]
            Vz = self.z.history[time][1]
            speed_history[time] = [Vx, Vy, Vz]
        return speed_history

    def get_acceleration_history(self):
        acceleration_history = {}
        for time in self.t:
            Ax = self.x.history[time][3]
            Ay = self.y.history[time][3]
            Az = self.z.history[time][3]
            acceleration_history[time] = [Ax,Ay, Az]
        return acceleration_history
