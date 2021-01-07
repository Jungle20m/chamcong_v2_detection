import os
import time
import timestring
import datetime

import cv2
import numpy as np
import pickle
import imutils

import face_detection.align.detect_face as detect_face




def draw_border_type1(image, pt1, pt2, name):
	x1,y1 = pt1
	x2,y2 = pt2

	font = cv2.FONT_HERSHEY_SIMPLEX
	font_scale = 0.5
	(text_width, text_height) = cv2.getTextSize(name, font, fontScale=font_scale, thickness=1)[0]

	cv2.rectangle(image, pt1, pt2, (80,180,80), 1)
	cv2.rectangle(image, (x1, y1-text_height), (x1+text_width, y1), (80,180,80), cv2.FILLED)
	cv2.putText(image, name, (x1, y1), font, fontScale=font_scale, color=(50, 50, 50), thickness=1)

	return image


def draw_point(image, points):
	p1 = (int(points[0][0]), int(points[5][0]))
	p2 = (int(points[1][0]), int(points[6][0]))
	p3 = (int(points[2][0]), int(points[7][0]))
	p4 = (int(points[3][0]), int(points[8][0]))
	p5 = (int(points[4][0]), int(points[9][0]))

	font = cv2.FONT_HERSHEY_SIMPLEX
	font_scale = 0.5
	cv2.putText(image, "p1", p1, font, fontScale=font_scale, color=(80,180,80), thickness=1)
	cv2.putText(image, "p2", p2, font, fontScale=font_scale, color=(80,180,80), thickness=1)
	cv2.putText(image, "p3", p3, font, fontScale=font_scale, color=(80,180,80), thickness=1)
	cv2.putText(image, "p4", p4, font, fontScale=font_scale, color=(80,180,80), thickness=1)
	cv2.putText(image, "p5", p5, font, fontScale=font_scale, color=(80,180,80), thickness=1)

	return image


def get_angle(image, points):
	p1 = (int(points[0][0]), int(points[5][0]))
	p2 = (int(points[1][0]), int(points[6][0]))

	if p1[1] < p2[1]: # negative rotate 
		return 360-int(np.arctan(abs(p2[1]-p1[1])/abs(p2[0]-p1[0]))*180/np.pi)
	elif p1[1] > p2[1]: # positive rotate
		return int(np.arctan(abs(p2[1]-p1[1])/abs(p2[0]-p1[0]))*180/np.pi)
	else: # do nothing
		return 0

	
def face_detection(image, pnet, rnet, onet):
	minsize = 55
	threshold = [0.6, 0.7, 0.7]
	factor = 0.709
	c = 0

	scale = 2
	
	frame = image.copy()
	r_g_b_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	# before alignment faces and point
	b_a_faces, b_a_points = detect_face.detect_face(r_g_b_frame, 
													minsize, 
													pnet, 
													rnet, 
													onet, 
													threshold, 
													factor)
	return b_a_faces, b_a_points
	# # if have only one face in image 
	# if b_a_faces.shape[0] == 1:
	# 	angle = get_angle(None, b_a_points)
	# 	rotated = imutils.rotate_bound(image, angle)
	# 	r_g_b_rotated = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
	# 	a_a_faces, a_a_points = detect_face.detect_face(r_g_b_rotated, 
	# 													minsize, 
	# 													pnet, 
	# 													rnet, 
	# 													onet, 
	# 													threshold, 
	# 													factor)
	# 	# if have only one face in image after alignment
	# 	if a_a_faces.shape[0] == 1:
	# 		x = int(a_a_faces[0][0])
	# 		y = int(a_a_faces[0][1])
	# 		w = int(a_a_faces[0][2])
	# 		h = int(a_a_faces[0][3])
	# 		p1 = (int(a_a_points[0][0]-a_a_faces[0][0]), 
	# 			  int(a_a_points[5][0]-a_a_faces[0][1]))
	# 		p2 = (int(a_a_points[1][0]-a_a_faces[0][0]), 
	# 			  int(a_a_points[6][0]-a_a_faces[0][1]))
	# 		p3 = (int(a_a_points[2][0]-a_a_faces[0][0]), 
	# 			  int(a_a_points[7][0]-a_a_faces[0][1]))
	# 		p4 = (int(a_a_points[3][0]-a_a_faces[0][0]), 
	# 			  int(a_a_points[8][0]-a_a_faces[0][1]))
	# 		p5 = (int(a_a_points[4][0]-a_a_faces[0][0]), 
	# 			  int(a_a_points[9][0]-a_a_faces[0][0]))
	# 		return rotated[y:h, x:w], (p1, p2, p3, p4, p5)
	# 	else:
	# 		return None, None
	# else:
	# 	return None, None

	

		






