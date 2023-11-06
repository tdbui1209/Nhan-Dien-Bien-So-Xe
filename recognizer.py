import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Recognizer:
  def __init__(self, path):
    self.path = path
    self.img = cv2.imread(self.path)
    self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

  def recognize(self):
    information = pytesseract.image_to_string(self.img, config='--oem 3', lang='eng')
    return information
