#! /usr/bin/env python
import rospy


if __name__ == "__main__":
    rospy.init_node("get_param_p")
    radius = rospy.get_param("radius_p",0.5)
    rospy.loginfo("radius = %.2f",radius)
    radius2 = rospy.get_param("radius_psc",0.5)
    rospy.loginfo("radius2 = %.2f",radius2)


    radius3 = rospy.get_param_cached("radius_p",0.5)
    rospy.loginfo("radius3 = %.2f",radius3)
    radius4 = rospy.get_param_cached("radius_psc",0.5)
    rospy.loginfo("radius4 = %.2f",radius4)

    names = rospy.get_param_names()
    for name in names:
        rospy.loginfo("name = %s",name)
    

    flag1 = rospy.has_param("radius_p")
    if flag1:
        rospy.loginfo("radius_p exsits")
    else:
        rospy.loginfo("radius_p not exist")
    flag2 = rospy.has_param("radius_psc")
    if flag2:
        rospy.loginfo("radius_psc exsits")
    else:
        rospy.loginfo("radius_pscnot exist")


    key = rospy.search_param("radius_p")
    rospy.loginfo("key  = %s",key)
    pass