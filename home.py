import streamlit as st
from ultralytics import YOLO
from alert_mode import *
from padestrian_mode import *
from object_det_app import *



model_OCR = YOLO('yolov8n.pt')
model = YOLO('yolov8n.pt')

def padestrian_mode(uploaded_file,conf):
    st.empty()
    st.write('pedestrian mode')
    #results = model(source="bike_r.mp4", show=True, conf=0.4, save=True, project='streamlit') 
    if uploaded_file is not None:
        st.write("File Uploaded")  
        f_path = uploaded_file.name

        obj_detection(f_path,conf/100)
 
    else:
        st.write("Please upload a video file.")


def alert_mode(uploaded_file,conf):
    st.empty()
    st.write('alert mode')

    if uploaded_file is not None:
        st.write("File Uploaded")    

        f_path = uploaded_file.name
        st.write('File Uploaded')
        res = alert(f_path,conf/100)

        obj_list = ['car','cycle','truck','bus','bike']
        print(res)
        for i in range(0,5):
            st.write("Total "+ obj_list[i] +" in frame ",+res[i])

        st.write('File Uploaded')

    else:
        st.write("Please upload a video file.")




def OCR(uploaded_file,conf_level):
    st.empty()
    st.write('OCR mode')

    if uploaded_file is not None:

        st.write('File Uploaded')
        f_path = uploaded_file.name

        vid_cap = cv2.VideoCapture(f_path)
        detected_text = main_func(vid_cap, model_OCR, conf_level/100)
        st.write("Most common text:", detected_text)

    else:
        st.write("Please upload a video file.")



if __name__ == "__main__":
    st.header(" Welcome to Third👁️Eye")
    st.write("_________________________________________________________")

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    mode = st.radio("Select mode", ["Padestrian Mode", "Alert Mode", "OCR Mode"])

    if mode == 'Padestrian Mode':
        conf_level = st.slider('Confidence Level', 0, 100, 25)
        padestrian_mode(uploaded_file,conf_level)

    if mode == 'Alert Mode':
        conf_level = st.slider('Confidence Level', 0, 100, 25)
        alert_mode(uploaded_file,conf_level)

    if mode == 'OCR Mode':
        conf_level = st.slider('Confidence Level', 0, 100, 25)
        OCR(uploaded_file,conf_level)

