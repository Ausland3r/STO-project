from OperateRobot import OperateRobot
from OperateCamera import OperateCamera
import time


rob = OperateRobot("172.31.1.25")
pos = rob.getl()
pos[0] += 0.1

moving_coordinates = {"x": pos[0], "y": pos[1], "z": pos[2], "rx": pos[3], "ry": pos[4], "rz": pos[5]}

rob.movel(moving_coordinates)
rob.open_gripper()
time.sleep(5)
rob.close_gripper();
time.sleep(2)
rob.close()