#!/usr/bin/env python

from std_msgs.msg import Float32
import rospy
from dynamic_reconfigure.server import Server as DRServer
from dynamic_reconfigure.client import Client as DRClient
from ecn_turtle.cfg import GainsConfig

rospy.init_node('pid')

s = 0
sd = 0
gains = None

class dictToNamespace(object):
  def __init__(self, adict):
    self.__dict__.update(adict)

def measure_callback(msg):
    global s
    s = msg.data
    
def setpoint_callback(msg):
    global sd
    sd = msg.data
    
def pid_callback(config, level):
    global gains
    gains = dictToNamespace(config)
    return config
    
# dynamic PID gains
pid_srv = DRServer(GainsConfig, pid_callback)
    
rospy.Subscriber('/measure', Float32, measure_callback)
rospy.Subscriber('/setpoint', Float32, setpoint_callback)

cmd_pub = rospy.Publisher('/cmd', Float32, queue_size=1)

cmd = Float32()
dt = 0.1

i_term = 0
e0 = 0

while not rospy.is_shutdown():
    
    e = sd - s
    i_term += e
    
    cmd.data = gains.Kp*(e + gains.Ki*i_term*dt + gains.Kd*(e - e0)/dt)
    e0 = e
    
    cmd_pub.publish(cmd)
        
    rospy.sleep(dt)
