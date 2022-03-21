from OperateRobot import OperateRobot


import time


def Moving_to(pos, rob):


    moving_coordinates = {"x": pos[0], "y": pos[1], "z": pos[2], "rx": pos[3], "ry": pos[4], "rz": pos[5]}


    rob.movel(moving_coordinates)


    time.sleep(0.3)


    return


def Merge_Cords(pos, x=0, y=0, z=0, rx=0, ry=0, rz=0):


    pos[0] += x;


    pos[1] += y;


    pos[2] += z;


    pos[3] += rx;


    pos[4] += ry;


    pos[5] += rz;


    return pos


def PixCor(cord):


    Right_Down =[-0.683340, 0.241990, 0.656260, 1.23, 2.889, 0.006]


    Right_Down[0] = cord[0] * 0.70/1920


    Right_Down[1] = cord[1] * 0.70/1920


    return Right_Down


def Grab_pos(pos):


    pos[3] = 1.23


    pos[4] = 2.889


    pos[5] = 0.006


    return pos


def Gripper_get(pos, rob):


    rob.open_gripper()


    pos[2] = 0.330040


    Moving_to(pos, rob)


    time.sleep(0.3)


    rob.close_gripper()


    pos[2] = 0.656260


    Moving_to(pos, rob)


    return


def Gripper_out(pos, rob, flag):


    rob.close_gripper()


    pos[2] = 0.333140 + 0.030 * flag[6]


    Moving_to(pos, rob)


    time.sleep(0.3)


    rob.open_gripper()


    pos[2] = 0.656260


    Moving_to(pos, rob)


    flag[6] += 1


    return flag


red_fl = [-0.745090, 0.250270, 0.656260, 1.23, 2.889, 0.006, 0]


blue_fl = [-0.906090, 0.250270, 0.656260, 1.23, 2.889, 0.006, 0]


pos_cam = [-0.871730, -0.158140, 0.656260, 1.449, 3.487, -0.508] #coordinats of base position


pos_long = [0, 0, 0, 0.915, -0.437, 0]


rob = OperateRobot("172.31.1.25")


Moving_to(pos_cam, rob)


pos = rob.getl()


pos = Grab_pos(pos)


pos = Merge_Cords(pos, 0.1)


Moving_to(pos, rob)


Gripper_get(pos, rob)


pos = red_fl


Moving_to(pos, rob)


red_fl = Gripper_out(pos, rob, red_fl)


Moving_to(pos_cam, rob)


pos = rob.getl()


pos = Grab_pos(pos)


pos = Merge_Cords(pos, -0.1)


Moving_to(pos, rob)


Gripper_get(pos, rob)


pos = blue_fl


pos = [x+y for x,y in zip(pos,pos_long)]


Moving_to(pos, rob)


blue_fl = Gripper_out(pos, rob, blue_fl)


pos = [x-y for x,y in zip(pos,pos_long)]


#moving_coordinates = {"x": pos[0], "y": pos[1], "z": pos[2], "rx": pos[3], "ry": pos[4], "rz": pos[5]}


#rob.movel(moving_coordinates)


rob.close()