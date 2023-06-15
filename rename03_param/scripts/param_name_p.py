import rospy
from std_msgs.msg import String


if __name__ == "__main__":
    rospy.init_node("hello")
    rospy.set_param("/radius",100)
    rospy.set_param("radius",1100)
    rospy.set_param("~radius",11100)




    while not rospy.is_shutdown():
        pass
