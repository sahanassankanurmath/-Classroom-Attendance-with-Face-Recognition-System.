# import os
# import time
# import cv2
# import numpy as np
# from PIL import Image
# from threading import Thread



# # -------------- image labesl ------------------------
# def getImagesAndLabels(path):
#     # Check if the folder exists
#     if not os.path.exists(path):
#         print(f"Error: The folder {path} does not exist.")
#         return [], []

#     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
#     faces = []
#     Ids = []

#     for imagePath in imagePaths:
#         pilImage = Image.open(imagePath).convert('L')
#         imageNp = np.array(pilImage, 'uint8')
#         Id = int(os.path.split(imagePath)[-1].split(".")[1])
#         faces.append(imageNp)
#         Ids.append(Id)
#     return faces, Ids


# # def getImagesAndLabels(path):
# #     # get the path of all the files in the folder
# #     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
# #     # print(imagePaths)

# #     # create empth face list
# #     faces = []
# #     # create empty ID list
# #     Ids = []
# #     # now looping through all the image paths and loading the Ids and the images
# #     for imagePath in imagePaths:
# #         # loading the image and converting it to gray scale
# #         pilImage = Image.open(imagePath).convert('L')
# #         # Now we are converting the PIL image into numpy array
# #         imageNp = np.array(pilImage, 'uint8')
# #         # getting the Id from the image
# #         Id = int(os.path.split(imagePath)[-1].split(".")[1])
# #         # extract the face from the training image sample
# #         faces.append(imageNp)
# #         Ids.append(Id)
# #     return faces, Ids


# # ----------- train images function ---------------
# def TrainImages():
#     recognizer = cv2.face_LBPHFaceRecognizer.create()
#     harcascadePath = "haarcascade_frontalface_default.xml"
#     detector = cv2.CascadeClassifier(harcascadePath)
#     faces, Id = getImagesAndLabels("TrainingImage")
#     Thread(target = recognizer.train(faces, np.array(Id))).start()
#     # Below line is optional for a visual counter effect
#     Thread(target = counter_img("TrainingImage")).start()
#     recognizer.save("TrainingImageLabel"+os.sep+"Trainner.yml")
#     print("All Images")

# # Optional, adds a counter for images trained (You can remove it)
# def counter_img(path):
#     imgcounter = 1
#     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
#     for imagePath in imagePaths:
#         print(str(imgcounter) + " Images Trained", end="\r")
#         time.sleep(0.008)
#         imgcounter += 1

import os
import time
import cv2
import numpy as np
import PIL.Image as Image
from threading import Thread

# Function to get images and labels
def getImagesAndLabels(path):
    # if not os.path.exists(path):
    #     print(f"Error: The folder {path} does not exist.")
    #     return [], []
    if not os.path.exists("TrainingImage"):
        os.makedirs("TrainingImage")
    
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []

    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])  # Ensure image naming convention is correct
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids

# Train images function
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)

    # Ensure the "TrainingImageLabel" directory exists
    if not os.path.exists("TrainingImageLabel"):
        os.makedirs("TrainingImageLabel")

    faces, Id = getImagesAndLabels("TrainingImage")
    
    # Train the recognizer in a separate thread
    def train_recognizer():
        recognizer.train(faces, np.array(Id))
        recognizer.save("TrainingImageLabel" + os.sep + "Trainner.yml")
        print("Training complete and model saved!")

    # Start training in a separate thread
    Thread(target=train_recognizer).start()

    # Optional: start the counter for images trained
    Thread(target=counter_img, args=("TrainingImage",)).start()

# Optional: counter function for images trained (you can remove this if unnecessary)
def counter_img(path):
    imgcounter = 1
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        print(str(imgcounter) + " Images Trained", end="\r")
        time.sleep(0.008)
        imgcounter += 1
