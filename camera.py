import cv2
from model import predict_emotion
from model_age import predict_age
import numpy as np
from model_gender import predict_gender
import matplotlib.pyplot as plt
#import skvideo.io
#video_path='f2.mp4'
#rgb = cv2.VideoCapture(video_path)
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

def __get_data__():
    """
    __get_data__: Gets data from the VideoCapture object and classifies them
    to a face or no face.

    returns: tuple (faces in image, frame read, grayscale frame)
    """
    _, fr = rgb.read()
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    faces = facec.detectMultiScale(gray, 1.3, 5)

    return faces, fr, gray

#AGE CATEGORIES: Adult(0), Child(1), Old(2), Youth(3)
#EMOTION CATEGORIES: Angry(0), Disgust(1), Fear(2), Happy(3), Sad(4), Suprise(5), Neutral(6)

def start_app(path):
    data=[]
    count_frame=0
    n_frame = 0
    no_emo_det = 0
    
    if(path!=0):
        video_path=path
        cap=path
    else:
        video_path='camera_capture.mp4'
        cap=0
    rgb=cv2.VideoCapture(cap)
    facec=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    font = cv2.FONT_HERSHEY_COMPLEX
    
    frame_h = int(rgb.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_w = int(rgb.get(cv2.CAP_PROP_FRAME_WIDTH))
    
    video_out=video_path[:-4]+'_detected'+video_path[-4:]
    video_writer = cv2.VideoWriter(video_out,cv2.VideoWriter_fourcc('F','M','P','4'), 5.0,(frame_w, frame_h))
    
    while True:
        count_frame+=1
        
        ret,fr=rgb.read()

        if count_frame%5!=0:
            continue
        
        n_frame += 1
        
        if(ret==False):
            break
        
        gray=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY)
        faces=facec.detectMultiScale(gray,1.3,5)
        faces, fr, gray_fr = faces,fr,gray

        if len(faces) == 0:
            no_emo_det+=1
        else:
            frame=[]
            for (x, y, w, h) in faces:

                fc_emo = gray_fr[y:y+h, x:x+w]
                fc_age = fr[y:y+h,x:x+w]
                fc_gen = fr[y:y+h, x:x+w]
                #print(fc_emo.shape)
                roi_emo = cv2.resize(fc_emo, (48, 48))
                roi_age = cv2.resize(fc_age, (128, 128))
                roi_gen = cv2.resize(fc_gen, (128, 128))

                #predictions code
                pred_emo,emo_index = predict_emotion(roi_emo[np.newaxis, :, :, np.newaxis])
                pred_age,age_index = predict_age(roi_age[np.newaxis,:])
                pred_gen, gen_index = predict_gender(roi_gen[np.newaxis, :])
                frame.append((age_index, emo_index, gen_index))

                #cv2 writing code
                cv2.putText(fr, pred_emo, (x, y), font, 1, (255, 255, 0), 2)
                cv2.putText(fr, pred_age, (x+w,y+h), font, 1, (255, 255, 0), 2)
                cv2.putText(fr, pred_gen, (x+w, y), font, 1, (255, 255, 0), 2)
                cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
            data.append(frame)

        if cv2.waitKey(1) == 27:
            break
        cv2.imshow('Filter', fr)
        video_writer.write(np.uint8(fr))
        
    cv2.destroyAllWindows()
    rgb.release()
    video_writer.release()
    
    #emotion counting and other statistics
    #creating counts of emotion
    # ANALYSIS AND PLOTTING SECTION
    # emotion counting and other statistics
    # creating counts of emotion
    male_emotion = []
    female_emotion = []
    for i in range(7):
        male_tmp = [0, 0, 0, 0, 0]
        female_tmp = [0, 0, 0, 0, 0]
        for entry in data:
            for item in entry:
                if item[2] == 0:
                    if item[1] == i:
                        female_tmp[item[0]] += 1
                        female_tmp[4] += 1
                else:
                    if item[1] == i:
                        male_tmp[item[0]] += 1
                        male_tmp[4] += 1
        male_emotion.append(male_tmp)
        female_emotion.append(female_tmp)

    no_emo_det = no_emo_det / n_frame * 100

    female_tmp = []
    male_tmp = []
    for i in female_emotion:
        i = [(x / n_frame) * 100 for x in i]
        female_tmp.append(i)
    for i in male_emotion:
        i = [(x / n_frame) * 100 for x in i]
        male_tmp.append(i)
    female_emotion = female_tmp
    male_emotion = male_tmp

    # populating emotions list
    female_adult = [i[0] for i in female_emotion] + [no_emo_det]
    female_adult = [x / 2 for x in female_adult]
    female_child = [i[1] for i in female_emotion] + [no_emo_det]
    female_child = [x / 2 for x in female_child]
    female_old = [i[2] for i in female_emotion] + [no_emo_det]
    female_old = [x / 2 for x in female_old]
    female_youth = [i[3] for i in female_emotion] + [no_emo_det]
    female_youth = [x / 2 for x in female_youth]
    female_total = [i[4] for i in female_emotion] + [no_emo_det]
    female_total = [x / 2 for x in female_total]

    male_adult = [i[0] for i in male_emotion] + [no_emo_det]
    male_adult = [x / 2 for x in male_adult]
    male_child = [i[1] for i in male_emotion] + [no_emo_det]
    male_child = [x / 2 for x in male_child]
    male_old = [i[2] for i in male_emotion] + [no_emo_det]
    male_old = [x / 2 for x in male_old]
    male_youth = [i[3] for i in male_emotion] + [no_emo_det]
    male_youth = [x / 2 for x in male_youth]
    male_total = [i[4] for i in male_emotion] + [no_emo_det]
    male_total = [x / 2 for x in male_total]

    emo_tup = ('Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Suprise', 'Neutral', 'None')
    y_pos = np.arange(len(emo_tup))

    # ['red','green','black','yellow','magenta','orange','cyan','brown']
    female_colors = ['#D35E60', '#84BA5B', '#808585', '#DD974C', '#9067A7', '#CCC210', '#7293CB', '#AB6857']
    male_colors = ['#CC2529', '#3E9651', '#535154', '#DA7C30', '#6B4C9A', '#948B3D', '#396AB1', '#922428']

    # plotting the graph
    def autolabel(frects, mrects, age_cat):
        """
        Attach a text label above each bar displaying its height
        """
        for i in range(8):
            height = mrects[i].get_height() + frects[i].get_height()
            if age_cat == 'A':
                if height == 0:
                    ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 0.05, 'Adult', ha='center',
                            va='bottom', rotation=45)
                else:
                    ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 2, 'Adult', ha='center',
                            va='bottom', rotation=45)
            elif age_cat == 'C':
                if height == 0:
                    ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 0.05, 'Child', ha='center',
                            va='bottom', rotation=45)
                else:
                    ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 2, 'Child', ha='center',
                            va='bottom', rotation=45)
            elif age_cat == 'O':
                if height == 0:
                    ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 0.05, 'Old', ha='center',
                            va='bottom', rotation=45)
                else:
                    ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 2, 'Old', ha='center', va='bottom',
                            rotation=45)
            elif age_cat == 'Y':
                if height == 0:
                    ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 0.05, 'Youth', ha='center',
                            va='bottom', rotation=45)
                else:
                    ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 2, 'Youth', ha='center',
                            va='bottom', rotation=45)

            if int(height) > 0:
                ax.text(mrects[i].get_x() + mrects[i].get_width() / 2., height + 0.05, str(int(height)) + '%',
                        ha='center', va='bottom')

    bar_width = 0.25
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 18
    fig_size[1] = 9
    plt.rcParams["figure.figsize"] = fig_size
    rects1_m = plt.bar(y_pos, male_adult, width=0.18, color=male_colors, align='edge', edgecolor='none')
    rects1_f = plt.bar(y_pos, female_adult, width=0.18, color=female_colors, bottom=male_adult, align='edge',
                       edgecolor='none')

    rects2_m = plt.bar(y_pos + bar_width, male_child, width=0.18, color=male_colors, align='edge', edgecolor='none')
    rects2_f = plt.bar(y_pos + bar_width, female_child, width=0.18, color=female_colors, bottom=male_child,
                       align='edge', edgecolor='none')

    rects3_m = plt.bar(y_pos + bar_width * 2, male_old, width=0.18, color=male_colors, align='edge', edgecolor='none')
    rects3_f = plt.bar(y_pos + bar_width * 2, female_old, width=0.18, color=female_colors, bottom=male_old,
                       align='edge', edgecolor='none')

    rects4_m = plt.bar(y_pos + bar_width * 3, male_youth, width=0.18, color=male_colors, align='edge', edgecolor='none')
    rects4_f = plt.bar(y_pos + bar_width * 3, female_youth, width=0.18, color=female_colors, bottom=male_youth,
                       align='edge', edgecolor='none')

    plt.xticks(y_pos, emo_tup)
    plt.legend((rects1_m[0], rects1_m[1], rects1_m[2], rects1_m[3], rects1_m[4], rects1_m[5], rects1_m[6], rects1_m[7]),
               emo_tup, loc='best')
    plt.grid()
    ax = plt.gca()
    ax.set_ylim([0, 50])
    ax.set_facecolor('#e5e7ea')
    plt.xlabel('Emotions')
    plt.ylabel('Frame Percentage')
    plt.title('Video Analysis Graph')
    autolabel(rects1_f, rects1_m, 'A')
    autolabel(rects2_f, rects2_m, 'C')
    autolabel(rects3_f, rects3_m, 'O')
    autolabel(rects4_f, rects4_m, 'Y')

    plt.savefig('static/images/video_analysis_graph.jpg')
    # plt.show()
    plt.gcf().clear()
#if __name__ == '__main__':
#     print("called")
#     start_app('static/videos/f3.mp4')
