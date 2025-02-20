
import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int64

class NumberPublisher(Node):

    # runs just once
    def __init__(self):
        # log message that it started
        super().__init__('number_publisher')
        # message type, topic it's publishing it, type the node publishes
        self.publisher_ = self.create_publisher(Int64, 'topic', 10)
        # self.publisher_ = self.create_publisher(String, 'topic', 10)

        # creates it a timer
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        # does this after every 0.5 seconds
        msg = Int64()
        msg.data = self.i

        # publishes this string
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    number_publisher = NumberPublisher()

    # keeps the node running
    rclpy.spin(number_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
