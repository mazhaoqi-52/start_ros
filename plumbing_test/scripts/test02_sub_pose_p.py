#! /usr/bin/env python
import rospy
def doPose(pose):
    rospy.loginfo("P position information: coordinate(%.2f,%.2f) toward(%.2f) angular_vole(%.2f) linear_veol(%.2f)",pose.x,pose.y,pose.theta,pose.linear_velocity,pose.angular_velocity)

from turtlesim.msg import Pose
if __name__ == "__main__":

    rospy.init_node("sub_pose_p")
    sub = rospy.Subscriber("turtle1/pose",Pose,doPose,queue_size=100)



    rospy.spin()
    pass