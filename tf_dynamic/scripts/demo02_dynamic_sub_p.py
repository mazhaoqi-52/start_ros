#! /usr/bin/env python
import rospy
import tf2_ros
import tf
from tf2_geometry_msgs import tf2_geometry_msgs
if __name__ == "__main__":
    rospy.init_node("static_sub_p")
    #make cached item and import
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)
    ps = tf2_geometry_msgs.PointStamped()
    ps.header.stamp = rospy.Time()
    ps.header.frame_id = "turtle1"
    ps.point.x = 2.0
    ps.point.y = 3.0
    ps.point.z = 5.0
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            ps_out = buffer.transform(ps,"world")
            rospy.loginfo("the changed pos is %.2f,%.2f,%.2f,the frame is %s",ps_out.point.x,ps_out.point.y,ps_out.point.z,ps_out.header.frame_id)
        except Exception as e:
            rospy .loginfo("bug!!! is %s",e)  
        rate.sleep()



    rospy.spin()




    pass