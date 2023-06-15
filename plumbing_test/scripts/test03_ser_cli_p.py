#! /usr/bin/env pyhton

import rospy
from turtlesim.srv import *

if __name__ == "__main__":
    rospy.init_node("ser_call_p")
    client = rospy.ServiceProxy("/spawn",Spawn)
    request  = SpawnRequest()
    request.x = 4.5
    request.y = 2.0
    request.theta  = -3
    request.name  = "turtle3"
    client.wait_for_service()
    try:
        response = client.call(request)
        rospy.loginfo("name of generated turtle is %s",response.name)
    except Exception as e:
        rospy.loginfo(" a bug!!!")
    pass