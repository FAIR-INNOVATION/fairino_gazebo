#!/usr/bin/env python3
"""
FR3WMS ros2_control 关节运动演示
控制: /joint_trajectory_controller/joint_trajectory (JointTrajectory)
"""
import math, time
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

RAD_90 = math.pi / 2
STEP_MS = 50
STEP_DUR = 2.0


class FR3WMSDemo(Node):
    def __init__(self):
        super().__init__('fr3wms_demo')
        self.pub = self.create_publisher(JointTrajectory,
            '/joint_trajectory_controller/joint_trajectory', 10)

    def move_joint(self, joint_idx, target_rad, current):
        """平滑移动单个关节到目标角度"""
        start = current[joint_idx]
        end = target_rad
        steps = int(STEP_DUR / (STEP_MS / 1000.0))

        for step in range(steps + 1):
            t = step / steps
            pos = current[:]
            pos[joint_idx] = start + (end - start) * t
            self._send(pos)
            time.sleep(STEP_MS / 1000.0)

        pos = current[:]
        pos[joint_idx] = end
        self._send(pos)
        return pos

    def _send(self, positions):
        msg = JointTrajectory()
        msg.joint_names = ['j1','j2','j3','j4','j5','j6']
        pt = JointTrajectoryPoint()
        pt.positions = [float(p) for p in positions]
        pt.time_from_start.sec = 0; pt.time_from_start.nanosec = int(STEP_MS * 1e6)
        msg.points = [pt]
        self.pub.publish(msg)


def main():
    rclpy.init()
    # Wait for controller_manager to be ready
    import subprocess, sys
    print("Waiting for controller_manager...")
    for i in range(1, 120):
        result = subprocess.run(["ros2", "service", "list"], capture_output=True, text=True)
        if "/controller_manager/load_controller" in result.stdout:
            print(f"controller_manager ready after {i}s")
            break
        time.sleep(1)
    else:
        print("TIMEOUT: controller_manager not ready, commands may be lost!")
    time.sleep(2)  # extra wait for controller to fully initialize
    demo = FR3WMSDemo()
    time.sleep(1)
    pos = [0.0] * 6

    # 归零
    demo.get_logger().info('归零...')
    demo._send(pos)
    time.sleep(1)

    # 逐关节
    for i, (idx, deg, name) in enumerate([
        (0, 90, 'j1'), (1, -90, 'j2'), (2, -90, 'j3'),
        (3, -90, 'j4'), (4, 90, 'j5'), (5, 90, 'j6')]):
        demo.get_logger().info(f'{name}: 0 → {deg}°')
        pos = demo.move_joint(idx, math.radians(deg), pos)
        time.sleep(0.3)

    # 归零
    demo.get_logger().info('归零...')
    for i in range(6):
        pos = demo.move_joint(5-i, 0, pos)
    time.sleep(0.5)
    demo._send([0]*6)

    demo.get_logger().info('演示完成!')
    demo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
