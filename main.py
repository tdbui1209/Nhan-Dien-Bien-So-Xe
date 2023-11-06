import argparse
from recognizer import Recognizer


def main(img, task):
  if task == 'recognize':
    recognizer = Recognizer(img)
    print(recognizer.recognize())


if __name__ == '__main__':
  img = 'bienso.jpg'
  task = 'recognize'
  main(img, task)
