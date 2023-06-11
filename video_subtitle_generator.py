import moviepy.editor as mp
import speech_recognition as sr
import os
import cv2
import csv
import time
r = sr.Recognizer()

if os.path.exists("audio_result.wav") == True:
    os.remove("audio_result.wav")
else:
    pass

if os.path.exists("final_video.avi") == True:
    os.remove("final_video.avi")
else:
    pass







def main_function():
    my_clip = mp.VideoFileClip(r"C:\Users\Shrey\Downloads\Y2Mate.is - COVID-19 Vaccine Providers Working On Booster Shot Aimed At Omicron Variant-bekPxTck_x4-720p-1641930234484.mp4")
    
    length_of_vid = float(my_clip.duration)
    i= float(0)
    with open ('subtitles.csv','w',newline = '') as f:
            x= csv.writer(f,delimiter = ',')
            my_clip_snip = my_clip.subclip(i,i+5)
            my_clip_snip.audio.write_audiofile(r"audio_result.wav")
            audio_file = sr.AudioFile("audio_result.wav")
            with audio_file as source:
                    audio_text = r.record(source)
            try:   
                    list = [i,i+5,r.recognize_google(audio_text, language='en')]
                    x.writerow(list)
            except:
                    pass
            
            i=i+5    
            while (i+5) < length_of_vid :
                my_clip_snip = my_clip.subclip(i,i+5)     #change this to change the start time of recorded text
                my_clip_snip.audio.write_audiofile(r"audio_result.wav")
                audio_file = sr.AudioFile("audio_result.wav")
                with audio_file as source:
                    audio_text = r.record(source)
                try:   
                    list = [i,i+5,r.recognize_google(audio_text, language='en')]
                    x.writerow(list)
                except:
                    pass
                i=i+5
            else: 
                my_clip_snip = my_clip.subclip(i-2,length_of_vid)
                my_clip_snip.audio.write_audiofile(r"audio_result.wav")
                audio_file = sr.AudioFile("audio_result.wav")
                with audio_file as source:
                    audio_text = r.record(source)
                try:   
                    list = [i,i+5,r.recognize_google(audio_text, language='en')]
                    x.writerow(list)
                except:
                    pass
            f.close()
        
def cv2_funtion():
    cap = cv2.VideoCapture(r"C:\Users\Shrey\Downloads\Y2Mate.is - COVID-19 Vaccine Providers Working On Booster Shot Aimed At Omicron Variant-bekPxTck_x4-720p-1641930234484.mp4")
    frames= 0
    with open ('subtitles.csv','r',newline = '') as f:
            x= csv.reader(f)
            for i in x:
                print()
                run= True
                
                while run :
                    ret,frame = cap.read()
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fps= float(cap.get(cv2.CAP_PROP_FPS))
                    print(type(fps))
                    end_time = float(i[1])
                    end_time_fps = end_time*fps
                    print(end_time_fps)
                    frame_width = int(cap.get(3))
                    frame_height = int(cap.get(4))
                    size = (frame_width,frame_height)
                    result = cv2.VideoWriter("final_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'),10,size)
                    
                    if (((end_time_fps)>float(frames)) or ((end_time_fps)==float(frames))) and ret:
                        
                        cv2.putText(frame,'H'*int(len(i[2])+100),(int(float(cap.get(cv2.CAP_PROP_FRAME_WIDTH))/1000),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)-1)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),20,cv2.LINE_4)
                        cv2.putText(frame,i[2],(int(float(cap.get(cv2.CAP_PROP_FRAME_WIDTH))/10),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)-11)),font,0.5,(255,255,255),2,cv2.LINE_4)
                        cv2.imshow('video',frame)
                        result.write(frame)
                        
                        
                    else:
                        run = False
                        break
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        run= False
                    frames= frames+1
                        
        
            result.release()
            cap.release()
            cv2.destroyAllWindows()
            f.close()

                





#main_function()
cv2_funtion()
