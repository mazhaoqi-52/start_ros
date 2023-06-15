import rospy
from std_msgs.msg import String


if __name__ == "__main__":
    rospy.init_node("hello")
    rospy.Publisher("~yyy/chatter",String,queue_size=10)


    while not rospy.is_shutdown():
        pass
