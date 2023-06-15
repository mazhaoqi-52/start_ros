#! /usr/bin/env python
import rospy

if __name__ == "__main__":
    rospy.init_node("del_param_p")
    try:
        rospy.delete_param("radius_p")
    except Exception as e:
        rospy.loginfo("deleted param is not exist")

    pass



