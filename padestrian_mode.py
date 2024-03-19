from ultralytics import YOLO
import cv2
import streamlit as st
#initiate YOLO model
model = YOLO('yolov8n.pt')

def obj_detection(filepath,confidence):
    video_path = filepath
    cap = cv2.VideoCapture(video_path)
    pred=''
    while True:
        success, frame = cap.read()
        if not success:
            break  # If no frame is read, break the loop
        #predict
        results = model(frame,conf = confidence,show=False)
        
        #get class id of prediction as a tensor from r.boxes inside results, convert into int and get class name from class id
        for r in results:
            for b in r.boxes:
                class_tensor=b.cls
                class_id=int(class_tensor.item())
                class_name=r.names[class_id]
                class_name=str(class_name)
                if pred==class_name:
                    pass
                else:
                    st.write(class_name)
                    pred=class_name
            
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
