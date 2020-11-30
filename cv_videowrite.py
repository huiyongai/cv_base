#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 视频存储


import cv2

cam = cv2.VideoCapture(0)

wid = int(cam.get(3))
hei = int(cam.get(4))
size = (wid, hei)
print(size)
fps = 30

# 设置编码类型XVID, 如果有其它的解码器，可以设置，如'X264'、'DIVX'等,各个平台支持的也不尽相同，此处以windows为例
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 文件名、编码器、帧率、大小
out = cv2.VideoWriter("./123.avi",fourcc, fps, size)
# out.open("./123.avi",fourcc, fps, size)

#--------------------------------------------------------------
# (640, 480) 未知原因,在mac上保存avi后无法打开
# out = cv2.VideoWriter('test.avi', fourcc, 20.0, (640, 480))
#--------------------------------------------------------------

# 保存mp4
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# out.open("./123.mp4",fourcc, fps, size)

while True:
    ret, frame = cam.read()
    if ret == False:
        break
    frame = cv2.flip(frame,0)

    out.write(frame)
    cv2.imshow("frame", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cam.release()
out.release()
cv2.destroyAllWindows()