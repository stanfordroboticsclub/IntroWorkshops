State Estimation
----

### Workshop outline

- What is state estimation and why do we need it?
- Simple methods (lowpass filter and compimentary filter)
- Methods that track the uncertanty (kalman filter and particle filter)
- Issues with angles and how to solve them

### What is state estimation

In general sensors are imperfect so state estimation is using fancy code to estimate our best guess of the state of the robot/world. Usually you will have multiple sensors measuring the world, so you often combine their data to get a better measurement then either alone. This is sometimes also called sensor fusion.


### Low pass filter

If you have a single sensor measuring something you can take a moving average of the measurement to smooth out the errors. A downside of this is it makes the filter output slow to respond to any changes in the system. It also doesn't fix any systematic bias you have in the measurement.

### Complimentatry filter

Just watch this [video](https://www.youtube.com/watch?v=whSw42XddsU)

### Kalman filter

[Here](https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/) is a very good graphical explaination of the kalman filter. 

[Here](https://www.kalmanfilter.net/default.aspx) is a very in depth explaination that I think is too long to be helpful but hey

### Particle filter

We didn't cover it in the workshop but its a similar idea to the kalman filter, except using a gaussian distribution the particle filter uses a more brute force representation of the distribution. Here's a high level [overview](https://www.youtube.com/watch?v=aUkBa1zMKv4)

### Issues with angles

Angles pose an intersting problem because there is either a discontinuity in the representation (359deg going to 0deg)or multiple representations map of the same angle (how 370deg is the same as 10deg). This can pose issues for state estimation and control algorythms. 

For example say a compass of a robot heading due north will read somewhere in the range 355deg - 5deg (due to noise). A low pass filter will average the two out and say the robot has a heading of 180deg! Heading the exact opposite direction!

Take a look at the RoverIMU fusion [code](https://github.com/stanfordroboticsclub/RoverIMU/blob/master/compass.py) to see how we solved the issue. (We store the sin and cos of the angle rather then the angle itself, similar to using complex numbers to track rotations).

For an example of a more advanced filter that uses quaterions and a kalman filter to track rotations in 3d check out the MEKF class [here](https://github.com/stanfordroboticsclub/AttitudeEstimators/blob/master/filters.py)