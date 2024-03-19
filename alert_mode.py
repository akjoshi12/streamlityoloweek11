from ultralytics import YOLO
import pandas as pd
import numpy as np
import cv2
import streamlit as st



def alert(filepath):
    class_list = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 
              'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']


    model=YOLO('yolov8n.pt')

    cap = cv2.VideoCapture(filepath)
    fps=cap.get(cv2.CAP_PROP_FPS)
    fps2=fps*2

    car=0
    bus=0
    truck=0
    cycle=0
    bike=0
    area_cycle=[]
    area_car=[]
    area_bus=[]
    area_bike=[]
    area_truck=[]

    while True:
        if car>fps2:
            first10_Car=area_car[:10]
            avg_first_car=sum(first10_Car)/len(first10_Car)
            last10_car=area_car[-10:]
            avg_last_car=sum(last10_car)/len(last10_car)
            x_car=avg_first_car
            y_car=avg_last_car
            percentage_increase_car = ((y_car - x_car) / x_car) * 100
            print(percentage_increase_car)
            if percentage_increase_car>0:
                st.write('Alert! Car is Approaching')
                car=0
                area_car.clear()
            else:
                car=0
                area_car.clear()
        if bus>fps2:
            first10_bus=area_bus[:10]
            avg_first_bus=sum(first10_bus)/len(first10_bus)
            last10_bus=area_bus[-10:]
            avg_last_bus=sum(last10_bus)/len(last10_bus)
            x_bus=avg_first_bus
            y_bus=avg_last_bus
            percentage_increase_bus = ((y_bus - x_bus) / x_bus) * 100
            if percentage_increase_bus>0:
                st.write('Alert! Bus is Approaching')
                bus=0
                area_bus.clear()
            else:
                bus=0
                area_bus.clear()
        if truck>fps2:
            first10_truck=area_truck[:10]
            avg_first_truck=sum(first10_truck)/len(first10_truck)
            last10_truck=area_truck[-10:]
            avg_last_truck=sum(last10_truck)/len(last10_truck)
            x_truck=avg_first_truck
            y_truck=avg_last_truck
            percentage_increase_truck = ((y_truck - x_truck) / x_truck) * 100
            if percentage_increase_truck>0:
                st.write('Alert! Truck is Approaching')
                truck=0
                area_truck.clear()
            else:
                truck=0
                area_truck.clear()
        if cycle>fps2:
            first10_cycle=area_cycle[:10]
            avg_first_cycle=sum(first10_cycle)/len(first10_cycle)
            last10_cycle=area_cycle[-10:]
            avg_last_cycle=sum(last10_cycle)/len(last10_cycle)
            x_cycle=avg_first_cycle
            y_cycle=avg_last_cycle
            print(avg_first_cycle)
            print(avg_last_cycle)
            percentage_increase_cycle = ((y_cycle - x_cycle) / x_cycle) * 100
            print(percentage_increase_cycle)
            if percentage_increase_cycle>0:
                st.write('Alert! Cycle is Approaching')
                cycle=0
                area_cycle.clear()
            else:
                cycle=0
                area_cycle.clear()
        if bike>fps2:
            first10_bike=area_bike[:10]
            avg_first_bike=sum(first10_bike)/len(first10_bike)
            last10_bike=area_bike[-10:]
            avg_last_bike=sum(last10_bike)/len(last10_bike)
            x_bike=avg_first_bike
            y_bike=avg_last_bike
            percentage_increase_bike = ((y_bike - x_bike) / x_bike) * 100
            if percentage_increase_bike>0:
                st.write('Alert! Bike is Approaching')
                bike=0
                area_bike.clear()
            else:
                bike=0
                area_bike.clear()
        ret, frame = cap.read()
        if not ret:
            break
        height,width=frame.shape[:2]
        crop_width=int(width*0.25)
        crop_height=int(height*5)
        start_x=(width-crop_width)//2
        start_y=(height-crop_height)//2
        cropped_frame=frame[start_y:start_y+crop_height,start_x:start_x+crop_width]
        results=model(cropped_frame,show=False)
        a=results[0].boxes.data
        a=a.detach().cpu().numpy()
        px = pd.DataFrame(a).astype("float")
        list_id=[]
        for value in px.iloc[:, -1]: 
            list_id.append(value)
        if 1.0 not in list_id:
            cycle=max(0,cycle-5)
            area_cycle=area_cycle[5:]
        if 2.0 not in list_id:
            car=max(0,car-5)
            area_car=area_car[5:]
        if 3.0 not in list_id:
            bike=max(0,bike-5)
            area_bike=area_bike[5:]
        if 5.0 not in list_id:
            bus=max(0,bus-5)
            area_bus=area_bus[5:]             
        if 7.0 not in list_id:
            truck=max(0,truck-5)
            area_truck=area_truck[5:]
        if not list_id:
            cycle=max(0,cycle-5)
            area_cycle=area_cycle[5:]
            car=max(0,car-5)
            area_car=area_car[5:]
            bike=max(0,bike-5)
            area_bike=area_bike[5:]
            bus=max(0,bus-5)
            area_bus=area_bus[5:]
            truck=max(0,truck-5)
            area_truck=area_truck[5:]
        else:
            pass    
        list = []
        for index, row in px.iterrows():
            d = int(row[5])
            c = class_list[d]
            if 'car' in c:
                x1 = int(row[0])
                y1 = int(row[1])
                x2 = int(row[2])
                y2 = int(row[3])
                area=(x2-x1)*(y2-y1)
                height_crop, width_crop = cropped_frame.shape[:2]
                area_frame=height_crop*width_crop
                prop=area/area_frame
                if prop>0.001:
                    centre_car=x1+x2/2
                    left_margin=width_crop*0.25
                    right_margin=width_crop*0.75
                    if left_margin<centre_car<right_margin:
                        car=car+1
                        area_car.append(area)
                    
            elif 'bicycle' in c:
                x1 = int(row[0])
                y1 = int(row[1])
                x2 = int(row[2])
                y2 = int(row[3])
                area=(x2-x1)*(y2-y1)
                height_crop, width_crop = cropped_frame.shape[:2]
                area_frame=height_crop*width_crop
                prop=area/area_frame
                if prop>0.001:
                    cycle=cycle+1
                    area_cycle.append(area)
                    

            elif 'truck' in c:
                x1 = int(row[0])
                y1 = int(row[1])
                x2 = int(row[2])
                y2 = int(row[3])
                area=(x2-x1)*(y2-y1)
                height_crop, width_crop = cropped_frame.shape[:2]
                area_frame=height_crop*width_crop
                prop=area/area_frame
                if prop>0.001:
                    centre_truck=x1+x2/2
                    left_margin=width_crop*0.25
                    right_margin=width_crop*0.75
                    if left_margin<centre_truck<right_margin:
                        truck=truck+1
                        area_truck.append(truck)
            elif 'bus' in c:
                x1 = int(row[0])
                y1 = int(row[1])
                x2 = int(row[2])
                y2 = int(row[3])
                area=(x2-x1)*(y2-y1)
                height_crop, width_crop = cropped_frame.shape[:2]
                area_frame=height_crop*width_crop
                prop=area/area_frame
                if prop>0.001:
                    centre_bus=x1+x2/2
                    left_margin=width_crop*0.25
                    right_margin=width_crop*0.75
                    if left_margin<centre_bus<right_margin:
                        bus=bus+1
                        area_bus.append(area)
            elif 'motorcycle' in c:
                x1 = int(row[0])
                y1 = int(row[1])
                x2 = int(row[2])
                y2 = int(row[3])
                area=(x2-x1)*(y2-y1)
                height_crop, width_crop = cropped_frame.shape[:2]
                area_frame=height_crop*width_crop
                prop=area/area_frame
                if prop>0.001:
                    bike=bike+1
                    area_bike.append(area)
            else:
                pass

    cap.release()
    cv2.destroyAllWindows()
    return car,cycle,truck,bus,bike



