# import datetime
# import os
# import time

# import cv2
# import pandas as pd


# #-------------------------
# def recognize_attendence():
#     recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
#     recognizer.read("./TrainingImageLabel/Trainner.yml")
#     harcascadePath = "haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(harcascadePath)
#     df = pd.read_csv("StudentDetails"+os.sep+"StudentDetails.csv")
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     col_names = ['Id', 'Name', 'Date', 'Time']
#     attendance = pd.DataFrame(columns=col_names)

#     # Initialize and start realtime video capture
#     cam = cv2.VideoCapture(0)
#     cam.set(3, 640)  # set video width
#     cam.set(4, 480)  # set video height
#     # Define min window size to be recognized as a face
#     minW = 0.1 * cam.get(3)
#     minH = 0.1 * cam.get(4)

#     while True:
#         _,im = cam.read()
#         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#         faces = faceCascade.detectMultiScale(gray, 1.2, 5,minSize = (int(minW), int(minH)),flags = cv2.CASCADE_SCALE_IMAGE)
#         for(x, y, w, h) in faces:
#             cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)
#             Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

#             if conf < 100:

#                 aa = df.loc[df['Id'] == Id]['Name'].values
#                 confstr = "  {0}%".format(round(100 - conf))
#                 tt = str(Id)+"-"+aa


#             else:
#                 Id = '  Unknown  '
#                 tt = str(Id)
#                 confstr = "  {0}%".format(round(100 - conf))

#             if (100-conf) > 67:
#                 ts = time.time()
#                 date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#                 aa = str(aa)[2:-2]
#                 attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

#             tt = str(tt)[2:-2]
#             if(100-conf) > 67:
#                 tt = tt + " [Pass]"
#                 cv2.putText(im, str(tt), (x+5,y-5), font, 1, (255, 255, 255), 2)
#             else:
#                 cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

#             if (100-conf) > 67:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font,1, (0, 255, 0),1 )
#             elif (100-conf) > 50:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)
#             else:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)



#         attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
#         cv2.imshow('Attendance', im)
#         if (cv2.waitKey(1) == ord('q')):
#             break
#     ts = time.time()
#     date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#     timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#     Hour, Minute, Second = timeStamp.split(":")
#     fileName = "Attendance"+os.sep+"Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
#     attendance.to_csv(fileName, index=False)
#     print("Attendance Successful")
#     cam.release()
#     cv2.destroyAllWindows()


# import datetime
# import os
# import time
# import cv2
# import pandas as pd

# def recognize_attendence():
#     recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
#     recognizer.read("./TrainingImageLabel/Trainner.yml")  # Load the trained model
#     harcascadePath = "haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(harcascadePath)  # Initialize face detector
#     df = pd.read_csv("StudentDetails" + os.sep + "StudentDetails.csv")  # Read student details CSV

#     # Columns for attendance
#     col_names = ['Id', 'Name', 'Date', 'Time']
#     attendance = pd.DataFrame(columns=col_names)  # Create empty attendance dataframe

#     font = cv2.FONT_HERSHEY_SIMPLEX

#     # Initialize and start real-time video capture
#     cam = cv2.VideoCapture(0)
#     cam.set(3, 640)  # set video width
#     cam.set(4, 480)  # set video height

#     # Define minimum window size to be recognized as a face
#     minW = 0.1 * cam.get(3)
#     minH = 0.1 * cam.get(4)

#     while True:
#         _, im = cam.read()  # Capture frame-by-frame
#         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

#         # Detect faces
#         faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(int(minW), int(minH)), flags=cv2.CASCADE_SCALE_IMAGE)
        
#         for (x, y, w, h) in faces:
#             cv2.rectangle(im, (x, y), (x + w, y + h), (10, 159, 255), 2)  # Draw rectangle around the face
#             Id, conf = recognizer.predict(gray[y:y + h, x:x + w])  # Predict the ID of the face

#             # If confidence is high, display the name and add attendance
#             if conf < 100:
#                 aa = df.loc[df['Id'] == Id]['Name'].values  # Get the name of the student
#                 confstr = "  {0}%".format(round(100 - conf))
#                 tt = str(Id) + "-" + aa[0]  # Id and Name of the student
#             else:
#                 Id = '  Unknown  '
#                 tt = str(Id)
#                 confstr = "  {0}%".format(round(100 - conf))

#             # Only add attendance if the confidence is above a certain threshold (67% in this case)
#             if (100 - conf) > 67:
#                 ts = time.time()  # Timestamp for date and time
#                 date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#                 aa = str(aa)[2:-2]  # Clean up the array format
#                 # Append the attendance record
#                 attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

#             tt = str(tt)[2:-2]
#             if (100 - conf) > 67:
#                 tt = tt + " [Pass]"  # Mark attendance as passed
#                 cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
#             else:
#                 cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

#             # Display confidence level
#             if (100 - conf) > 67:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 0), 1)
#             elif (100 - conf) > 50:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)
#             else:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)

#         # Remove duplicates to ensure each student is only recorded once
#         attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
#         cv2.imshow('Attendance', im)  # Display the webcam feed with annotations

#         # Break the loop when 'q' key is pressed
#         if cv2.waitKey(1) == ord('q'):
#             break

#     # Save the attendance record to a CSV file
#     ts = time.time()
#     date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#     timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#     Hour, Minute, Second = timeStamp.split(":")
#     fileName = "Attendance" + os.sep + "Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
#     attendance.to_csv(fileName, index=False)  # Save the attendance CSV file

#     print("Attendance Successful")
#     cam.release()  # Release the camera
#     cv2.destroyAllWindows()  # Close all OpenCV windows



import datetime
import os
import time
import cv2
import pandas as pd

#------------------------- Function to Recognize Attendance -------------------------
def recognize_attendence():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Create LBPH recognizer
    recognizer.read("./TrainingImageLabel/Trainner.yml")  # Load the trained model
    harcascadePath = "haarcascade_frontalface_default.xml"  # Path to Haar Cascade
    faceCascade = cv2.CascadeClassifier(harcascadePath)  # Initialize face detector
    
    # Ensure the StudentDetails CSV exists
    student_details_path = os.path.join("StudentDetails", "StudentDetails.csv")
    if not os.path.isfile(student_details_path):
        print("Error: StudentDetails.csv not found.")
        return
    
    df = pd.read_csv(student_details_path)  # Read student details CSV

    # Column names for the attendance CSV
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)  # Create an empty DataFrame for attendance

    font = cv2.FONT_HERSHEY_SIMPLEX

    # Initialize and start real-time video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # Set video width
    cam.set(4, 480)  # Set video height

    # Define minimum window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        _, im = cam.read()  # Capture frame-by-frame
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(int(minW), int(minH)), flags=cv2.CASCADE_SCALE_IMAGE)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (10, 159, 255), 2)  # Draw rectangle around the face
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])  # Predict the ID of the face

            # If confidence is high, display the name and add attendance
            if conf < 100:
                aa = df.loc[df['Id'] == Id]['Name'].values  # Get the name of the student
                confstr = "  {0}%".format(round(100 - conf))
                tt = str(Id) + "-" + aa[0]  # Id and Name of the student
            else:
                Id = '  Unknown  '
                tt = str(Id)
                confstr = "  {0}%".format(round(100 - conf))

            # Add attendance regardless of confidence level
            ts = time.time()  # Timestamp for date and time
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            aa = str(aa)[2:-2]  # Clean up the array format
            
            # Append the attendance record
            attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            tt = str(tt)[2:-2]
            if (100 - conf) > 67:
                tt = tt + " [Pass]"  # Mark attendance as passed
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            else:
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

            # Display confidence level
            if (100 - conf) > 67:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 0), 1)
            elif (100 - conf) > 50:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)
            else:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)

        # Remove duplicates to ensure each student is only recorded once
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Attendance', im)  # Display the webcam feed with annotations

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Ensure the Attendance directory exists, if not, create it
    if not os.path.exists("Attendance"):
        os.makedirs("Attendance")

    # Save the attendance record to a CSV file
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = os.path.join("Attendance", "Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv")
    attendance.to_csv(fileName, index=False)  # Save the attendance CSV file

    print(f"Attendance data saved as: {fileName}")
    cam.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows

