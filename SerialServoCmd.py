#!/usr/bin/python3
# encoding: utf-8
import serial
import pigpio
import time
import ctypes

LOBOT_SERVO_FRAME_HEADER         = 0x55
LOBOT_SERVO_MOVE_TIME_WRITE      = 1
LOBOT_SERVO_MOVE_TIME_READ       = 2
LOBOT_SERVO_MOVE_TIME_WAIT_WRITE = 7
LOBOT_SERVO_MOVE_TIME_WAIT_READ  = 8
LOBOT_SERVO_MOVE_START           = 11
LOBOT_SERVO_MOVE_STOP            = 12
LOBOT_SERVO_ID_WRITE             = 13
LOBOT_SERVO_ID_READ              = 14
LOBOT_SERVO_ANGLE_OFFSET_ADJUST  = 17
LOBOT_SERVO_ANGLE_OFFSET_WRITE   = 18
LOBOT_SERVO_ANGLE_OFFSET_READ    = 19
LOBOT_SERVO_ANGLE_LIMIT_WRITE    = 20
LOBOT_SERVO_ANGLE_LIMIT_READ     = 21
LOBOT_SERVO_VIN_LIMIT_WRITE      = 22
LOBOT_SERVO_VIN_LIMIT_READ       = 23
LOBOT_SERVO_TEMP_MAX_LIMIT_WRITE = 24
LOBOT_SERVO_TEMP_MAX_LIMIT_READ  = 25
LOBOT_SERVO_TEMP_READ            = 26
LOBOT_SERVO_VIN_READ             = 27
LOBOT_SERVO_POS_READ             = 28
LOBOT_SERVO_OR_MOTOR_MODE_WRITE  = 29
LOBOT_SERVO_OR_MOTOR_MODE_READ   = 30
LOBOT_SERVO_LOAD_OR_UNLOAD_WRITE = 31
LOBOT_SERVO_LOAD_OR_UNLOAD_READ  = 32
LOBOT_SERVO_LED_CTRL_WRITE       = 33
LOBOT_SERVO_LED_CTRL_READ        = 34
LOBOT_SERVO_LED_ERROR_WRITE      = 35
LOBOT_SERVO_LED_ERROR_READ       = 36

pi = pigpio.pi()  # 初始化 pigpio库
serialHandle = serial.Serial("/dev/ttyAMA0", 115200)  # 初始化串口， 波特率为115200


def portInit():  # 配置用到的IO口
    pi.set_mode(17, pigpio.OUTPUT)  # 配置RX_CON 即 GPIO17 为输出
    pi.write(17, 0)
    pi.set_mode(27, pigpio.OUTPUT)  # 配置TX_CON 即 GPIO27 为输出
    pi.write(27, 1)


portInit()


def portWrite():  # 配置单线串口为输出
    pi.write(27, 1)  # 拉高TX_CON 即 GPIO27
    pi.write(17, 0)  # 拉低RX_CON 即 GPIO17


def portRead():  # 配置单线串口为输入
    pi.write(17, 1)  # 拉高RX_CON 即 GPIO17
    pi.write(27, 0)  # 拉低TX_CON 即 GPIO27


def portRest():
    time.sleep(0.1)
    serialHandle.close()
    pi.write(17, 1)
    pi.write(27, 1)
    serialHandle.open()
    time.sleep(0.1)


def angleMap(x,in_min,in_max,out_min,out_max):
    return (x-in_min)*(out_max - out_min)/(in_max-in_min)+out_min


def checksum(buf):
    # 计算校验和
    sum = 0x00
    for b in buf:  # 求和
        sum += b
    sum = sum - 0x55 - 0x55  # 去掉命令开头的两个 0x55
    sum = ~sum  # 取反
    return sum & 0xff


def serial_serro_wirte_cmd(id=None, w_cmd=None, dat1=None, dat2=None):
    '''
    写指令
    :param id:
    :param w_cmd:
    :param dat1:
    :param dat2:
    :return:
    '''
    portWrite()
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(id)
    # 指令长度
    if dat1 is None and dat2 is None:
        buf.append(3)
    elif dat1 is not None and dat2 is None:
        buf.append(4)
    elif dat1 is not None and dat2 is not None:
        buf.append(7)

    buf.append(w_cmd)  # 指令
    # 写数据
    if dat1 is None and dat2 is None:
        pass
    elif dat1 is not None and dat2 is None:
        buf.append(dat1 & 0xff)  # 偏差
    elif dat1 is not None and dat2 is not None:
        buf.extend([(0xff & dat1), (0xff & (dat1 >> 8))])  # 分低8位 高8位 放入缓存
        buf.extend([(0xff & dat2), (0xff & (dat2 >> 8))])  # 分低8位 高8位 放入缓存
    # 校验和
    buf.append(checksum(buf))
    # for i in buf:
    #     print('%x' %i)
    ID = ''
    dat1 =int(angleMap(dat1,0,1000,612,2388))	
    def case1():                            # 第一种情况执行的函数
        print('This is the case1')
        return '16'
	
    def case2():                            # 第二种情况执行的函数
        print('This is the case2')
        return '14'
    def case3():                            # 第三种情况执行的函数
        print('This is the case3')
        return '12'	
    def case4():                            # 第二种情况执行的函数
        print('This is the case4')
        return '10'
		
    def case5():                            # 第三种情况执行的函数
        print('This is the case5')
        return '8'
    def case6():                            # 第一种情况执行的函数
        print('This is the case6')
        return '6'    
    def case7():                            # 第二种情况执行的函数
        print('This is the case7')
        return '5'
		
    def case8():                            # 第三种情况执行的函数
        print('This is the case8')
        return '4'
		
    def case9():                            # 第一种情况执行的函数
        print('This is the case9')
        return '15'	
		
    def case10():                            # 第二种情况执行的函数
        print('This is the case10')
        return '13'
    def case11():                            # 第三种情况执行的函数
        print('This is the case11')
        return '11'		
    def case12():                            # 第一种情况执行的函数
        print('This is the case12')
        return '9'	
    def case13():                            # 第二种情况执行的函数
        print('This is the case13')
        return '7'
    def case14():                            # 第三种情况执行的函数
        print('This is the case14')
        return '1'		
    def case15():                            # 第一种情况执行的函数
        print('This is the case15')
        return '2'	
    def case16():                            # 第二种情况执行的函数
        print('This is the case16')
        return '3'
    def default():                          # 默认情况下执行的函数
        print('No such case')
        return '17'
    switch = {  '1': case1,                # 注意此处不要加括号
	        '2': case2,                # 注意此处不要加括号
	        '3': case3,                # 注意此处不要加括号
	        '4': case4,                # 注意此处不要加括号
	        '5': case5,                # 注意此处不要加括号
	        '6': case6,                # 注意此处不要加括号
	        '7': case7,                # 注意此处不要加括号
	        '8': case8,                # 注意此处不要加括号
	        '9': case9,                # 注意此处不要加括号
	        '10': case10,              # 注意此处不要加括号
	        '11': case11,              # 注意此处不要加括号
	        '12': case12,              # 注意此处不要加括号
	        '13': case13,              # 注意此处不要加括号
	        '14': case14,              # 注意此处不要加括号
	        '15': case15,              # 注意此处不要加括号
	        '16': case16,             # 注意此处不要加括号
	     }
    choice = str(id)                       # 获取选择
    ID = switch.get(choice, default)()        # 执行对应的函数，如果没有就执行默认的函数
    print(ID)
    buf ='#'+ID+'P'+str(dat1)+'T'+str(dat2)+'!'
   # print "pos= %d" %dat1
   # print "time=%d" %dat2
   # print buf
    serialHandle.write(buf.encode())  # 发送
    print(buf)

def serial_servo_read_cmd(id=None, r_cmd=None):
    '''
    发送读取命令
    :param id:
    :param r_cmd:
    :param dat:
    :return:
    '''
    portWrite()
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(id)
    buf.append(3)  # 指令长度
    buf.append(r_cmd)  # 指令
    buf.append(checksum(buf))  # 校验和
    serialHandle.write(buf)  # 发送
    time.sleep(0.00034)


def serial_servo_get_rmsg(cmd):
    '''
    # 获取指定读取命令的数据
    :param cmd: 读取命令
    :return: 数据
    '''
    serialHandle.flushInput()  # 清空接收缓存
    portRead()  # 将单线串口配置为输入
    time.sleep(0.005)  # 稍作延时，等待接收完毕
    count = serialHandle.inWaiting()    # 获取接收缓存中的字节数
    if count != 0:  # 如果接收到的数据不空
        recv_data = serialHandle.read(count)  # 读取接收到的数据
        # for i in recv_data:
        #     print('%#x' %ord(i))
        # 是否是读id指令
        try:
            if recv_data[0] == 0x55 and recv_data[1] == 0x55 and recv_data[4] == cmd:
                dat_len = recv_data[3]
                serialHandle.flushInput()  # 清空接收缓存
                if dat_len == 4:
                    # print ctypes.c_int8(ord(recv_data[5])).value    # 转换成有符号整型
                    return recv_data[5]
                elif dat_len == 5:
                    pos = 0xffff & (recv_data[5] | (0xff00 & (recv_data[6] << 8)))
                    return ctypes.c_int16(pos).value
                elif dat_len == 7:
                    pos1 = 0xffff & (recv_data[5] | (0xff00 & (recv_data[6] << 8)))
                    pos2 = 0xffff & (recv_data[7] | (0xff00 & (recv_data[8] << 8)))
                    return ctypes.c_int16(pos1).value, ctypes.c_int16(pos2).value
            else:
                return None
        except BaseException as e:
            print(e)
    else:
        serialHandle.flushInput()  # 清空接收缓存
        return None
