#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
import tf2_ros
from geometry_msgs.msg import TransformStamped
import tf
def doPose(pose):
    pub = tf2_ros.TransformBroadcaster()###daxiexioxie???
    ts = TransformStamped()
    ts.header.frame_id = "world"
    ts.header.stamp  =rospy.Time.now()
    ts.child_frame_id = "turtle1"
    ts.transform.translation.x = pose.x
    ts.transform.translation.y = pose.y
    ts.transform.translation.z = 0
    qtn  = tf.transformations.quaternion_from_euler(0,0,pose.theta)
    ts.transform.rotation.x  = qtn[0]
    ts.transform.rotation.y  = qtn[1]
    ts.transform.rotation.z  = qtn[2]
    ts.transform.rotation.w  = qtn[3]
    pub.sendTransform(ts)



    pass

if __name__ == "__main__":
    rospy.init_node("dynamic_pub_p")
    sub = rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size=100)
    rospy.spin()
    pass
