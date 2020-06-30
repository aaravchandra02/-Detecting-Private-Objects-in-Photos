"""
It is a program that I wrote to get all the pathnames of the test images.
"""
# Importing this required header file
import os

# Storing public image folder path in a string
public_path="/Users/aarav/Desktop/Securities in emerging technology/Class Projects/Yolo Detection/dataset/public"
# Storing private image folder path in a string
private_path="/Users/aarav/Desktop/Securities in emerging technology/Class Projects/Yolo Detection/dataset/private"

# Storing all public image filenames onto a list
public_l=os.listdir(public_path)
# Storing all private image filenames onto a list
private_l=os.listdir(private_path)

# Storing Complete paths in a list
for i in range(len(public_l)):
    temp=str(public_path)+"/"+str(public_l[i])
    public_l[i]=temp
# Storing Complete paths in a list
for i in range(len(private_l)):
    temp=str(private_path)+"/"+str(private_l[i])
    private_l[i]=temp
# Writing to public_path.text
f1= open("public_paths.txt","w+")
for i in public_l:
    f1.write(f"{i}|")
f1.close()
# Writing to private_paths.txt
f2= open("private_paths.txt","w+")
for i in private_l:
    f2.write(f"{i}|")
f2.close()


