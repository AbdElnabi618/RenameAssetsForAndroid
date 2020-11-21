import os
import glob

rootPathName = "/home/abd-elnabi/Downloads/Assests/Android/"
children = {"drawable-xxxhdpi", "drawable-xxhdpi", "drawable-xhdpi", "drawable-mdpi", "drawable-ldpi","drawable-hdpi"}
try:
    for child in children:
        os.chdir(rootPathName + child)
        files = glob.glob("*.png")
        for file in files:
            filename = ""
            for c in file:
                if c != '-' and c != ' ':
                    filename = filename + c
                else:
                    filename = filename + '_'
            if child[7:] in filename:
                x = len(filename) - len(child[7:])-5
                filename = filename[:x] + filename[len(filename)-4:]
            if str(os._exists(rootPathName+filename.lower())):
               os.rename(file, filename.lower() +'1')

            print(filename)
        print("---------------------------------------------------------")    

    print("Finish")
except Exception as e:
    print("please make sure when you use \\ use 2 not one like \'\\\\\'")
    print(e)

# logo_hdpi ---> 4+5 --> 9 5

# C:\\Users\\Khaled Abd-Elnabi\\AndroidStudioProjects\\Trill\\app\\src\\main\\res\\
