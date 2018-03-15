# ecn_turtle

A package using TurtleBot / TurtleSim simulation to illustrate Gazebo, RViz and joystick control.

Lauching the simulation :
`roslaunch ecn_turtle gazebo.launch`

This will publish the `/scan` topic with laser data and wait for command on the `/cmd_vel` topic (vx and wz commands).

Laser points can be visualized in RViz:
`roslaunch ecn_turtle rviz.launch`
