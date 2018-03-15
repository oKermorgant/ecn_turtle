#!/usr/bin/env python

from std_msgs.msg import Float32
import rospy


rospy.init_node('setpoint')


sp_pub = rospy.Publisher('/setpoint', Float32, queue_size=1)

sp = Float32()
sp.data = 1

dt = 0.1

t = 0

while not rospy.is_shutdown():
    
    t += dt
    
    if t > 4:
        sp.data = 1
        t = 0
    elif t > 2:
        sp.data = -1
    
    sp_pub.publish(sp)
        
    rospy.sleep(dt)
