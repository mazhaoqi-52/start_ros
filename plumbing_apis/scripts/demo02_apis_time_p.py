#! usr/bin/env python
import rospy
def domsg(event):
    rospy.loginfo("====")
    rospy.loginfo("%.2f",event.current_real.to_sec())

if __name__ == "__main__":
    rospy.init_node("hello_time")
    # get time(when now function is executed)
    right_now = rospy.Time.now()
    rospy.loginfo("the time is %.2f",right_now.to_sec())
    rospy.loginfo("the time is %d",right_now.secs)
    time1 = rospy.Time(100)
    time2 = rospy.Time(100,312345678)
    rospy.loginfo("time1 is %.2f",time1.to_sec())
    rospy.loginfo("time2 is %.2f",time2.to_sec())
    time3 = rospy.Time.from_sec(210.12)
    rospy.loginfo("time3 is %.2f",time3.to_sec())

    #stop 5s
    rospy.loginfo("before sleep")
    du = rospy.Duration(5)
    # rospy.sleep(du)
    #calculation of time
    t1 = rospy.Time.now()
    du1 = rospy.Duration(5)
    t2 = t1 + du1
    rospy.loginfo("start is %.2f",t1.to_sec())
    rospy.loginfo("end is %.2f",t2.to_sec())
    dd = du1 +du
    rospy.loginfo("the add is %.2f",dd.to_sec())
    #
    timer = rospy.Timer(rospy.Duration(2),domsg,True)
    rospy.spin()







    rospy.loginfo("after sleep")    



    pass