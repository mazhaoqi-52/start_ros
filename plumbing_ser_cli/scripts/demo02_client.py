#! /usr/bin/env python
import rospy
import sys
from plumbing_ser_cli.srv import *

if __name__ == "__main__":
    if len(sys.argv )!= 3:
        rospy.logerr("the number is wrong!!")
        sys.exit(1)
    sys.argv
    rospy.init_node("erHei")
    client  =rospy.ServiceProxy("addInts",AddInts)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    client.wait_for_service()
    response = client.call(num1,num2)
    rospy.loginfo("the responsed data is %d", response.sum)


    pass
