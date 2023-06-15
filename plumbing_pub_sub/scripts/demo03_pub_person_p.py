#! /usr/bin/env python

import rospy
from plumbing_pub_sub.msg import Person


if __name__ == "__main__":
    rospy.init_node("dama")
    pub = rospy.Publisher("jiaoshetou",Person,queue_size=10)
    p = Person() 
    p.name = "urutoraman"
    p.age = 8
    p.height = 1.82
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(p)
        rate.sleep()
        rospy.loginfo("pub msg:%s,%d,%.2f",p.name,p.age,p.height)

    pass


    