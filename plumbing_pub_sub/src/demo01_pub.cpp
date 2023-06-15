#include "ros/ros.h"
#include "sstream"
#include "std_msgs/String.h"
int main(int argc, char  *argv[])
{
    ros::init(argc,argv,"ergouzi");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("fang",10);
    std_msgs::String msg;
    ros::Rate rate(1);
    int count = 0;
    ros::Duration(3).sleep();
    while (ros::ok())
    {   
        count++;
        //msg.data = "hello";""
        std::stringstream ss;
        ss << "hello --->" << count;
        msg.data = ss.str();
        
    
        pub.publish(msg);
        ROS_INFO("published info is:%s",ss.str().c_str());
        rate.sleep();

        ros::spinOnce();/* advised by ... */

    }
    
    return 0;

}