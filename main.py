from ultralytics import YOLO
import cv2
import easyocr


def main(source_path, model_path):
  reader = easyocr.Reader(['en'])
  model = YOLO(model_path)

  cap = cv2.VideoCapture(source_path)
  while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
      break
    detected_frame = model(frame)
    for bbox in detected_frame:
      try:
        bbox = bbox.boxes.xyxy.tolist()[0]
        bbox = [int(i) for i in bbox]
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)

        margin = 0.1
        crop_frame = frame[bbox[1] - int(margin * (bbox[3] - bbox[1])):bbox[3] + int(margin * (bbox[3] - bbox[1])),
                  bbox[0] - int(margin * (bbox[2] - bbox[0])):bbox[2] + int(margin * (bbox[2] - bbox[0]))]  # crop image with margin
        
        crop_frame = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)

        result = reader.readtext(crop_frame, detail=0, text_threshold=0.8)  # detail=0: return only text
        result = ''.join(result)  # convert list to string

        cv2.putText(frame, result, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
      except:
        pass
    
    cv2.imshow('Detected', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  source_path = 'test.mp4'
  model_path = 'model_soxe/best.pt'
  main(source_path, model_path)
