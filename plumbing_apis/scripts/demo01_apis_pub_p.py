#! /usr/bin/env/python
import rospy
from std_msgs.msg import String
import tools
import os
import sys
#shezhilinshihuanjingbinliang
path = os.path.abspath(".")

sys.path.insert(0,path + "src/plumbing_apis/scripts")
def cd():
    rospy.loginfo("dddd")

if __name__ == "__main__":
    rospy.init_node("sandai",anonymous=True)
    rospy.loginfo("tools = %d",tools.num)
    path = os.path.abspath(".")
    rospy.loginfo("%s",path)
    pub = rospy.Publisher("che" ,String ,queue_size=10,latch=True)
    msg = String()
    rate = rospy.Rate(1)
    count = 0
    rospy.sleep(3)
    while not rospy.is_shutdown():
        count += 1
        if count <= 10:
            msg.data = "hello" + str(count)
            pub.publish(msg)
            rospy.loginfo("pulishing date is:%s", msg.data)
        else:
            #close node
            rospy.on_shutdown(cd)
            rospy.signal_shutdown("guanbijiedian")
        rate.sleep()

    pass
