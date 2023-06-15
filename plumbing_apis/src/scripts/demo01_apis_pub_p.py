#! /usr/bin/env python
import rospy
if __name__ == "__main__":
    rospy.init_node("saiDai",anonymous=True)

    pub = rospy.Publisher("che",String,queue_size=10,latch=True)
    msg  =String()







    pass




