from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """
    Launch file to start both the velocity publisher and odometry subscriber
    nodes simultaneously with a single command:

        ros2 launch my_robot_pkg robot.launch.py
    """
    return LaunchDescription([
        Node(
            package='my_robot_pkg',
            executable='velocity_publisher',
            name='velocity_publisher',
            output='screen',
        ),
        Node(
            package='my_robot_pkg',
            executable='odom_subscriber',
            name='odom_subscriber',
            output='screen',
        ),
    ])
