import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Recognizer:
  def __init__(self, img):
    self.img = img

  def recognize(self):
    information = pytesseract.image_to_string(self.img, config='--oem 3 --psm 7', lang='eng')
    return information
