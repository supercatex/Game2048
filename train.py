from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="./Game2048_dataset/data.yaml", epochs=20, imgsz=640)

print("Finished")
