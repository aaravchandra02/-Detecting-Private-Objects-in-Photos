# Importing this required header file
from subprocess import Popen, PIPE

l=[]
# Reading the 'public_paths.txt' and appending to list 'l'
with open('/Users/aarav/Desktop/Securities in emerging technology/Class Projects/Yolo Detection/public_paths.txt','r') as fil:
    l.append(fil.readline())
lin=[]
# Splitting at "|" sybmbol to get individual pathnames.
for i in l:
    lin=i.split("|")
l=[]
# Removing whitespace
lin=lin[:len(lin)-1]
# Sorting the pathnames
lin=sorted(lin)

# Running Yolo for each file and writing it in 'public_prediction.txt'
for i in lin:
    print(f"\n{i}")
    p = Popen(['./darknet', 'detect', 'cfg/yolov3.cfg', 'yolov3.weights', i],cwd = '/Users/aarav/darknet', stdout = PIPE, stderr = PIPE)
    stdout, stderr = p.communicate()
    with open('/Users/aarav/Desktop/Securities in emerging technology/Class Projects/Yolo Detection/public_prediction.txt','a+') as fil:
        fil.write(f"{str(stdout)}|")