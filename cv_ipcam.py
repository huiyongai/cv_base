#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ip摄像头


import cv2

cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.100:554/Streaming/Channels/101?transportmode=unicast")

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    # 接收到q键，退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()