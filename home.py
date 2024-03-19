import streamlit as st
from ultralytics import YOLO
from alert_mode import *
from padestrian_mode import *
from object_det_app import *



model_OCR = YOLO('yolov8n.pt')
model = YOLO('yolov8n.pt')

def padestrian_mode(uploaded_file):
    st.empty()
    st.write('pedestrian mode')
    #results = model(source="bike_r.mp4", show=True, conf=0.4, save=True, project='streamlit') 
    if uploaded_file is not None:
        st.write("File Uploaded")  
        f_path = uploaded_file.name

        obj_detection(f_path)
 
    else:
        st.write("Please upload a video file.")


def alert_mode(uploaded_file):
    st.empty()
    st.write('alert mode')

    if uploaded_file is not None:
        st.write("File Uploaded")    

        f_path = uploaded_file.name
        st.write('File Uploaded')
        res = alert(f_path)

        obj_list = ['car','cycle','truck','bus','bike']
        print(res)
        for i in range(0,5):
            st.write("Total "+ obj_list[i] +" in frame ",+res[i])

        st.write('File Uploaded')

    else:
        st.write("Please upload a video file.")




def OCR(uploaded_file):
    st.empty()
    st.write('OCR mode')

    if uploaded_file is not None:

        st.write('File Uploaded')
        f_path = uploaded_file.name

        vid_cap = cv2.VideoCapture(f_path)
        detected_text = main_func(vid_cap, model_OCR, 0.4)
        st.write("Most common text:", detected_text)

    else:
        st.write("Please upload a video file.")



if __name__ == "__main__":
    st.write("Welcome to ThirdEye")
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    mode = st.radio("Select mode", ["Padestrian Mode", "Alert Mode", "OCR Mode"])

    if mode == 'Padestrian Mode':
        padestrian_mode(uploaded_file)

    if mode == 'Alert Mode':
        alert_mode(uploaded_file)

    if mode == 'OCR Mode':
        OCR(uploaded_file)

