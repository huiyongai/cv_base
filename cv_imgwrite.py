#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 图片显示及保存

import cv2

image = cv2.imread('123.png', cv2.IMREAD_ANYCOLOR)

# 开窗口显示
cv2.imshow('show image', image)

# 保存成文件
cv2.imwrite('copy.jpg', image)

# 接收键盘输入,相当于是一个loop循环
cv2.waitKey(0)

# 删除创建的所有窗口，删除特定窗口cv2.destroyWindow(winname=**)
cv2.destroyAllWindows()
