#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Revolver():
    def __init__(self):
        self._cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def revolve_forever(self):
        self.twist = Twist()

        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.twist.angular.z = 0.1
            self.twist.linear.y = 0.1
            self._cmd_pub.publish(self.twist)
            rospy.loginfo("Revolving robot: %s", self.twist)
            r.sleep()


def main():
    rospy.init_node('revolve')
    try:
        revolver = Revolver()
        revolver.revolve_forever()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()
