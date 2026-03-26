import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class OdomMonitor(Node):
    """
    ROS 2 subscriber node that monitors TurtleBot3 odometry.

    Subscribes to /odom and logs:
      - Position:   (x, y)
      - Velocities: (linear.x, angular.z)
    """

    def __init__(self):
        super().__init__('odom_monitor')

        # Subscribe to /odom with QoS depth 10
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10)

        self.get_logger().info(
            'OdomMonitor started — listening to /odom')

    def odom_callback(self, msg):
        # Extract position
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        # Extract velocities
        vx = msg.twist.twist.linear.x
        wz = msg.twist.twist.angular.z

        self.get_logger().info(
            f'Position: x={x:.2f}, y={y:.2f} | '
            f'Velocity: linear.x={vx:.2f}, angular.z={wz:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = OdomMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
