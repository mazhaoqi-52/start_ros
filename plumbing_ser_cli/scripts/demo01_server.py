#!/usr/bin/env python

import rospy
from plumbing_ser_cli.srv import  AddInts , AddIntsResponse , AddIntsRequest

def doNum(request):
    num1 = request.num1
    num2 = request.num2
    sum = num1 + num2
    response  = AddIntsResponse()
    response.sum = sum

    rospy.loginfo("the server is ok! the result is %d ", num1 + num2)

    return response
    pass
if __name__ == "__main__":

    rospy.init_node("heishui")
    server = rospy.Service("addInts",AddInts,doNum)
    rospy.loginfo("on!!")
    rospy.spin()
    pass
