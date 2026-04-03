#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time

def draw_square():
    rospy.init_node('turtle_square_node', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    rospy.loginfo("Start drawing square...")
    
    while not rospy.is_shutdown():
        for _ in range(4):
            # Move forward
            move = Twist()
            move.linear.x = 2.0
            pub.publish(move)
            rospy.sleep(2)
            
            # Stop
            stop = Twist()
            pub.publish(stop)
            rospy.sleep(0.5)
            
            # Turn 90 degrees
            turn = Twist()
            turn.angular.z = 1.57
            pub.publish(turn)
            rospy.sleep(1)
            
            # Stop turning
            stop_turn = Twist()
            pub.publish(stop_turn)
            rospy.sleep(0.5)

if __name__ == '__main__':
    try:
        draw_square()
    except rospy.ROSInterruptException:
        pass

