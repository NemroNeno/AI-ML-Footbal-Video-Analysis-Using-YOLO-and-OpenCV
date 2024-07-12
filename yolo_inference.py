from ultralytics import YOLO
model=YOLO("yolov8x.pt")
results=model.predict(rf'C:\Users\Nemro Neno\Desktop\Football Analysis Project\input_video\test.mp4',save=True)

print("))))))))))))))))))))))))))")
for box in results[0].boxes:
    print(box)