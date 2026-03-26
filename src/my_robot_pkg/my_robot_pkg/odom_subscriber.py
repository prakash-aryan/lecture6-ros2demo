import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class OdometrySubscriber(Node):
    """
    ROS 2 node that subscribes to /odom and logs the robot's position.

    Listens for Odometry messages published by the TurtleBot3 simulation
    and extracts the robot's (x, y) position, warning if it moves too far.
    """

    def __init__(self):
        super().__init__('odom_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10)
        self.get_logger().info('Listening to odometry')

    def odom_callback(self, msg):
        pos = msg.pose.pose.position
        self.get_logger().info(
            f'Robot at x={pos.x:.2f}, y={pos.y:.2f}')

        # Process the data
        if pos.x > 5.0:
            self.get_logger().warn('Robot too far!')


def main(args=None):
    rclpy.init(args=args)
    node = OdometrySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
