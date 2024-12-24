import rclpy
from rclpy.node import Node

# import our new fizzbuzz message type
from fizzbuzz_interfaces.msg import FizzBuzz 

# TODO import the number message used for the numbers topic

class FizzBuzzNode(Node):
    def __init__(self):
        super().__init__('fizzbuzz')
        self.get_logger().info("Starting fizzbuzz node")

        self.total_numbers = 0
        self.total_fizz = 0
        self.total_buzz = 0
        self.total_fizzbuzz = 0

        # create a publisher object to send data
        self.fizzbuzz_pub = self.create_publisher(FizzBuzz, "fizzbuzz_stats", 10)

        # TODO fill in the TOPIC_NAME and MESSAGE_TYPE
        self.number_sub = self.create_subscription(MESSAGE_TYPE, "TOPIC_NAME", self.number_callback, 10)

    def number_callback(self, msg):
        # this function is called whenever a number is received.

        number = msg.data 

        fizzbuzz_str = self.fizzbuzz(number)
        # loginfo to print the string to the terminal
        self.get_logger().info(fizzbuzz_str)

        fizzbuzz_msg = FizzBuzz()
        fizzbuzz_msg.fizzbuzz = fizzbuzz_str
        fizzbuzz_msg.fizz_ratio = 0 # TODO fill in this value
        fizzbuzz_msg.buzz_ratio = 0 # TODO fill in this value
        fizzbuzz_msg.fizzbuzz_ratio = 0 # TODO fill in this value
        fizzbuzz_msg.number_total = 0 # TODO fill in this value

        # publish the message
        self.fizzbuzz_pub.publish(fizzbuzz_msg)

    def fizzbuzz(self, number):
        # TODO complete this function
        # This should return a string equal to:
        #      "fizz" if number divisible my 3
        #      "buzz" if number divisible my 5
        #      "fizzbuzz" if number divisible my 15
        #      an empty string otherwise
        if number % 15 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        return ""

def main(args=None):
    rclpy.init()
    node = FizzBuzzNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
