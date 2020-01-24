#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Name: add.py
Author: Evi1ran
Date Created: January 24, 2020
Description: None
'''

# built-in imports
import cv2
import dlib
import numpy as np
import os

def add(path, filename, mode, isGoggle):
    img1 = cv2.imread(path)
    if (isGoggle):
        x_min, x_max, y_min, y_max, size = get_eye(img1)
        img2 = cv2.imread('masks/goggle.png', cv2.IMREAD_UNCHANGED)
        img2 = cv2.resize(img2,size)
        alpha_channel = img2[:, :, 3]
        _, mask = cv2.threshold(alpha_channel, 220, 255, cv2.THRESH_BINARY)
        color = img2[:, :, :3]
        img2 = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))
        rows,cols,channels = img2.shape
        roi = img1[y_min: y_min + rows, x_min:x_min + cols]
        img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 254, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
        img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
        dst = cv2.add(img1_bg,img2_fg)
        img1[y_min: y_min + rows, x_min:x_min + cols] = dst
    x_min, x_max, y_min, y_max, size = get_mouth(img1)
    img2 = cv2.imread('masks/mask' + str(mode) + '.png', cv2.IMREAD_UNCHANGED) 
    img2 = cv2.resize(img2,size)
    alpha_channel = img2[:, :, 3]
    _, mask = cv2.threshold(alpha_channel, 220, 255, cv2.THRESH_BINARY)
    color = img2[:, :, :3]
    img2 = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))
    rows,cols,channels = img2.shape
    roi = img1[y_min: y_min + rows, x_min:x_min + cols]
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 254, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
    dst = cv2.add(img1_bg,img2_fg)
    img1[y_min: y_min + rows, x_min:x_min + cols] = dst
    img_processed = "static/output/" + filename
    cv2.imwrite(img_processed, img1)
    output = img_processed
    return output

def get_mouth(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
    faces = detector(img_gray, 0)
    for k, d in enumerate(faces):
        x = []
        y = []
        height = d.bottom() - d.top()
        width = d.right() - d.left()
        shape = predictor(img_gray, d)
        for i in range(48, 68):
            x.append(shape.part(i).x)
            y.append(shape.part(i).y)
        y_max = (int)(max(y) + height / 3)
        y_min = (int)(min(y) - height / 3)
        x_max = (int)(max(x) + width / 3)
        x_min = (int)(min(x) - width / 3)
        size = ((x_max-x_min),(y_max-y_min))
        return x_min, x_max, y_min, y_max, size

def get_eye(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
    faces = detector(img_gray, 0)
    for k, d in enumerate(faces):
        x = []
        y = []
        height = d.bottom() - d.top()
        width = d.right() - d.left()
        shape = predictor(img_gray, d)
        for i in range(36, 48):
            x.append(shape.part(i).x)
            y.append(shape.part(i).y)
        y_max = (int)(max(y) + height / 3)
        y_min = (int)(min(y) - height / 3)
        x_max = (int)(max(x) + width / 3)
        x_min = (int)(min(x) - width / 3)
        size = ((x_max-x_min),(y_max-y_min))
        return x_min, x_max, y_min, y_max, size