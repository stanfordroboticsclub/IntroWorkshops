
import matplotlib.pyplot as plt
import math
import random

class Robot:
    def __init__(self,ax, x=0,y=0,alpha=0):
        self.ax = ax # matplotlib axes object

        self.x = x
        self.y = y
        self.a = alpha

        self.arrow_length = 1
        self.circle_radius = 0.4
        self.circle = plt.Circle((0, 0), self.circle_radius, color='r')
        self.ax.add_artist(self.circle)
        self.arrow = ax.arrow(0,0, 0,1)

        self.wheel_bias = random.gauss(0,0.1) #is one motor faster then the other?

    def update_display(self):
        pos = (self.x, self.y)
        self.circle.set_center(pos)

        arrow_head = (
            self.x + self.arrow_length * math.sin(self.a), 
            self.y + self.arrow_length * math.cos(self.a))
        self.arrow.set_xy((pos, arrow_head))

    def get_state(self):
        return (self.x, self.y, self.a)

    def drive(self, motor_left, motor_right):
        # simulates the errors we would encounter on the real system
        # another thing to add would be the values in get_state to be 
        # delayed a couple iterations to simulate the network delay

        add_errors = True
        if add_errors:
            motor_left  += random.gauss(0,0.1) + self.wheel_bias
            motor_right += random.gauss(0,0.1) - self.wheel_bias

        wheel_base = 1          # changes how fast robot turns
        dt = 0.1                # changes simulation speed

        # calculations explained here:
        # http://faculty.salina.k-state.edu/tim/robotics_sg/Control/kinematics/odometry.html
        d_center = (motor_right + motor_left)/2
        d_angle  = (motor_left - motor_right)/wheel_base
        self.x += dt * d_center * math.sin(self.a + d_angle/2)
        self.y += dt * d_center * math.cos(self.a + d_angle/2)
        self.a += dt * d_angle


if __name__ == "__main__":

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

    target = (5,6) # import a sequence of those from your yaml files
    ax.plot(target[0], target[1], "g.")

    robot = Robot(ax)
    fig.show()

    def control(state):
        x,y,a= state
        ## TODO: write the control loop to make the robot goes the target

        motor_left = 1
        motor_right = 0.5

        return motor_left, motor_right

    while 1:
        plt.pause(0.01)
        motor_speeds = control(robot.get_state())
        robot.drive(*motor_speeds)
        robot.update_display()


