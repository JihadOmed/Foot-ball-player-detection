from ultralytics import YOLO


model = YOLO("Models/best.pt")


results = model.predict('Input_Videos/Football.mp4', save=True)

print(results[0])

print('==================================')

for box in results[0].boxes:
    print(box)