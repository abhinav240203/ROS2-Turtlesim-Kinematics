import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import math

class SimpleTurtlesimKinematics(Node):
    def __init__(self):
        super().__init__("simple_turtlesim_kinematics")

        
        self.turtle1_pose_sub_ = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.turtle1PoseCallback,
            10
        )

        self.turtle2_pose_sub_ = self.create_subscription(
            Pose,
            "/turtle2/pose",
            self.turtle2PoseCallback,
            10
        )

        
        self.last_turtle1_pose_ = Pose()
        self.last_turtle2_pose_ = Pose()

    def turtle1PoseCallback(self, msg):
        self.last_turtle1_pose_ = msg

    def turtle2PoseCallback(self, msg):
        self.last_turtle2_pose_ = msg

        Tx = self.last_turtle2_pose_.x - self.last_turtle1_pose_.x
        Ty = self.last_turtle2_pose_.y - self.last_turtle1_pose_.y
        theta_diff = self.last_turtle2_pose_.theta - self.last_turtle1_pose_.theta
        theta_deg = 180 * theta_diff/ 3.14 

        self.get_logger().info("""\n
    Translation Vector turtle1 -> turtle2 \n
    Tx: %f \n
    Ty: %f \n
    Rotation Matrix turtle1 -> turtle2\n
    theta(rad): %f\n
    theta(deg): %f\n
    |R11      R12| : |%f      %f|\n
    |R21      R22| : |%f      %f|\n""" % (Tx, Ty, theta_diff, theta_deg, math.cos(theta_diff),
                                         -math.sin(theta_diff), math.sin(theta_diff), math.cos(theta_diff)))


       


def main():
    rclpy.init()

    Simple_turtlesim_kinematics = SimpleTurtlesimKinematics()

    rclpy.spin(Simple_turtlesim_kinematics)

    Simple_turtlesim_kinematics.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
