import vlc
import cv2
import numpy as np
import time


class MyMediaPlayer():
	def __init__(self, name1):
		self.detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		self.cap = cv2.VideoCapture(0)


	def play_music(self, target_dir):
		music = vlc.MediaPlayer(target_dir)

		music.play()

		time.sleep(15)

	def stream_webcam(self):
		while True:
			ret, frame = self.cap.read()

			if ret:
				frame = cv2.flip(frame, 1)

				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

				results = self.detector.detectMultiScale(gray)

				for (x, y, w, h) in results:
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
					
				cv2.imshow("Webcam", frame)

				q = cv2.waitKey(1)
				if q == ord('q'):
					break
			else:
				break

		self.cap.release()
		cv2.destroyAllWindows()

mp = MyMediaPlayer("Mostafa Lotfi")

mp.stream_webcam()
# mp.play_music("music.mp3")


