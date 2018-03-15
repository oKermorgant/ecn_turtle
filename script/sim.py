#!/usr/bin/env python

from std_msgs.msg import Float32
import rospy

rospy.init_node('sim')

u = 0

def input_callback(msg):
    global u
    u = msg.data
    
rospy.Subscriber('/command', Float32, input_callback)
output_pub = rospy.Publisher('/measure', Float32, queue_size=1)

dt = 0.05
out = Float32()
v = 0
m = 5.
k = 1.



while not rospy.is_shutdown():
    
    # update velocity
    v += dt/m*(u - k*v)
    
    # update position
    out.data += v*dt
    
    # publish
    output_pub.publish(out)   
        
    rospy.sleep(dt)
