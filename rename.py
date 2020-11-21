import os
import glob

print("Location Name Example : \nFor linux : \"/home/your_dirction_name/../assets_name_to_change/\" \nlike:\"/home/abd-elnabi/Downloads/Assests/Android/\"\nFor Windows:C:\\Users\\your_dirction_name\\..\\assets_name_to_change\\\nlike:\"C:\\Users\\Khaled Abd-Elnabi\\AndroidStudioProjects\\exampleApp\\app\\src\\main\\res\\")
print("Location name must contain the following folders: drawable-xxxhdpi, drawable-xxhdpi, drawable-xhdpi, drawable-mdpi, drawable-ldpi,drawable-hdpi")
rootPathName = input("Enter Location name For Assets Folder:") #"/home/abd-elnabi/Downloads/Assests/Android/"
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
