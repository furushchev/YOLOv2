#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import cv2
from yolov2_darknet_predict import CocoPredictor

def main():
    cap = cv2.VideoCapture(0)
    coco_predictor = CocoPredictor()

    while(True):
        ret, orig_img = cap.read()
        if ret is False:
            print("Could not read image from camera")
            return
        nms_results = coco_predictor(orig_img)

        # draw result
        for result in nms_results:
            left, top = result["box"].int_left_top()
            right, bottom = result["box"].int_right_bottom()
            cv2.rectangle(orig_img, (left, top), (right, bottom), (255, 0, 255), 3)
            text = '%s(%2d%%)' % (result["label"], result["probs"].max()*result["conf"]*100)
            cv2.putText(orig_img, text, (left, top-7), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            print(text)

        cv2.imshow("w", orig_img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()
