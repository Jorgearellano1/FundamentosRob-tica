#!/usr/bin/env python3
import rclpy, math, time
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JSP(Node):
    def __init__(self):
        super().__init__('jsp')
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        self.t0 = time.time()
        self.create_timer(0.02, self.step)  # 50 Hz

    def step(self):
        t = time.time() - self.t0
        q1 = 0.5*math.sin(t)
        q2 = 0.6*math.cos(0.7*t)
        q3 = 0.4*math.sin(0.9*t)
        q4 = 0.5*math.cos(0.5*t)
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name     = ['joint1','joint2','joint3','joint4']
        msg.position = [q1, q2, q3, q4]
        self.pub.publish(msg)

def main():
    rclpy.init()
    n = JSP()
    rclpy.spin(n)

if __name__ == '__main__':
    main()
