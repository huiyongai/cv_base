#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 打开摄像头


import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # 灰度化
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)

    # 接收到q键，退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()