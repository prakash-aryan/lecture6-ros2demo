import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class VelocityPublisher(Node):
    """
    ROS 2 node that publishes velocity commands to /cmd_vel.

    Sends Twist messages at 2 Hz to drive the TurtleBot3 forward
    with a slight angular rotation, creating a curved path.
    """

    def __init__(self):
        super().__init__('velocity_publisher')
        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)
        self.timer = self.create_timer(
            0.5,  # 2 Hz
            self.timer_callback)
        self.get_logger().info('Publishing velocity commands')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5   # m/s forward
        msg.angular.z = 0.1  # rad/s turn
        self.publisher.publish(msg)
        self.get_logger().info(
            f'Publishing: linear.x={msg.linear.x:.1f}, angular.z={msg.angular.z:.1f}')


def main(args=None):
    rclpy.init(args=args)
    node = VelocityPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
