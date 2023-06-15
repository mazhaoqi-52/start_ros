#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"

/* publisher  the msg of person */
int main(int argc, char  *argv[])
{   
    ROS_INFO("Publishing Msgs");
    ros::init(argc,argv,"banzhuren");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<plumbing_pub_sub::Person>("liaotian",10);
    plumbing_pub_sub::Person person;
    person.name = "zhangsan";
    person.age = 21;
    person.height = 1.81;
    ros::Rate rate(1);
    while (ros::ok())
    {   

        person.age += 1;
        pub.publish(person);
        ROS_INFO("msgs:%s,%d,%.2f",person.name.c_str(),person.age,person.height);
        rate.sleep();
        ros::spinOnce();
    }
    

    return 0;
}
