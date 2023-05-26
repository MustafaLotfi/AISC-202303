import face_recognition
import cv2
import os
import pickle


with open('known_faces.pickle', 'rb') as f:
	names, encodings = pickle.load(f)

UNKNOWN_DIR = 'data/unknown_faces/'

file_names = os.listdir(UNKNOWN_DIR)

for fn in file_names:
	img = cv2.imread(UNKNOWN_DIR+fn)
	rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	locs = face_recognition.face_locations(rgb, model='hog') 		# cnn
	encods = face_recognition.face_encodings(rgb, locs)

	for (loc, encod) in zip(locs, encods):
		top_left = loc[3], loc[0]
		bottom_right = loc[1], loc[2]

		results = face_recognition.compare_faces(encodings, encod, 0.9)

		for (i, res) in enumerate(results):
			if res:
				new_name = names[i]
				cv2.putText(img, new_name, top_left,
					cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 1)
				break

		cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

	cv2.imshow("Image", img)

	q = cv2.waitKey(0)
	if (q == ord('q')) or (q == ord('Q')):
		stop_program = True

cv2.destroyAllWindows()

