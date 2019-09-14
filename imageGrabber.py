import cv2
import numpy as np
import os
import urllib.request

def store_raw_imgs():
    # neg_images_link = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09416076"
    neg_images_link = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09618957"
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

    # make neg dir
    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 4000

    # i is a link
    for i in neg_image_urls.split('\n'):
        try:
            print (i)
            # grab image and store it in folder
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+'.jpg')

            # open retrieve image and resize it
            img = cv2.imread("neg/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

def remove_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            # for ugly in os.listdir("uglies"):
                # skip mac hidden file 
                #if str(ugly) == ".DS_Store":
                #    continue
            ugly = "uglies/5.jpg"
            try:
                current_image_path = str(file_type)+'/'+str(img)
                ugly = cv2.imread(ugly)
                question = cv2.imread(current_image_path)
                    
                if ugly.shape == question.shape and not(np.bitwise_xor(ugly, question).any()):
                    print ("Removing ", current_image_path)
                    os.remove(current_image_path)
            except Exception as e:
                print (str(e))

def create_pos_n_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)

            elif file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50 \n'
                with open('info.dat', 'a') as f:
                    f.write(line)

def merge_info_lists():
    filenames = []

    for i in range(0, 28):
        txt = "info/info"+str(i)+".lst"
        filenames.append(txt)
    print (filenames)
    with open('info/info.lst', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def retrieve_cam_imgs():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    pic_num = 3000
    while True:
        try:
            _, frame = cap.read()
            if cv2.waitKey(30) == ord('g'):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                resized_image = cv2.resize(gray, (100, 100)) 
                cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
                pic_num += 1
                print ("saved")
            
            cv2.imshow("Image", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print(str(e))

    cap.release()

#retrieve_cam_imgs()
# create_pos_n_neg()
#remove_uglies()
# store_raw_imgs()
merge_info_lists()
