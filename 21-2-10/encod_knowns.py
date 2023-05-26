import face_recognition
import cv2
import os
import pickle


KNOWN_DIR = 'data/known_faces/'

known_names = os.listdir(KNOWN_DIR)

stop_program = False
names = []
encodings = []

for name in known_names:
	file_names = os.listdir(KNOWN_DIR+name)
	for fn in file_names:
		img = cv2.imread(KNOWN_DIR+name+'/'+fn)
		rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		locs = face_recognition.face_locations(rgb, model='hog') 		# cnn
		encods = face_recognition.face_encodings(rgb, locs)

		names.append(name)
		encodings.append(encods[0])

		# print(encods[0].shape)
		# quit()

		# top_left = locs[0][3], locs[0][0]
		# bottom_right = locs[0][1], locs[0][2]

		# cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

		# cv2.imshow("Image", img)

		# q = cv2.waitKey(0)
		# if (q == ord('q')) or (q == ord('Q')):
		# 	stop_program = True

		if stop_program:
			break
	if stop_program:
		break

with open('known_faces.pickle', 'wb') as f:
	pickle.dump([names, encodings], f)

cv2.destroyAllWindows()