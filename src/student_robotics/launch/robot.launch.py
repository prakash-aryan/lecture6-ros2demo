from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """
    Launch both circle_motion (publisher) and odom_monitor (subscriber)
    with a single command:

        ros2 launch student_robotics robot.launch.py
    """
    return LaunchDescription([
        Node(
            package='student_robotics',
            executable='circle_motion',
            name='circle_motion',
            output='screen',
        ),
        Node(
            package='student_robotics',
            executable='odom_monitor',
            name='odom_monitor',
            output='screen',
        ),
    ])
