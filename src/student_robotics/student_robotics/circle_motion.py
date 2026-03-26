import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircleMotion(Node):
    """
    ROS 2 publisher node that drives TurtleBot3 in a circle.

    Publishes Twist messages to /cmd_vel at 10 Hz with:
      - linear.x  = 0.3 m/s   (forward speed)
      - angular.z = 0.5 rad/s  (turn rate)
    """

    def __init__(self):
        super().__init__('circle_motion')

        # Create publisher on /cmd_vel with QoS depth 10
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        # 10 Hz timer → callback every 0.1 s
        self.timer = self.create_timer(0.1, self.timer_callback)

        self.get_logger().info(
            'CircleMotion started — publishing to /cmd_vel at 10 Hz')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.3   # m/s forward
        msg.angular.z = 0.5  # rad/s counter-clockwise
        self.publisher.publish(msg)
        self.get_logger().info(
            f'Velocity → linear.x={msg.linear.x:.1f}, angular.z={msg.angular.z:.1f}')


def main(args=None):
    rclpy.init(args=args)
    node = CircleMotion()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Stop the robot before shutting down
        stop_msg = Twist()
        node.publisher.publish(stop_msg)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
