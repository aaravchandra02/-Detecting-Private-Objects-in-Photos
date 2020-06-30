l=[]
# Reading inputs and adding it to a list - 'l'
with open('/Users/aarav/Desktop/Securities in emerging technology/Class Projects/Yolo Detection/private_prediction.txt','r') as f:
    l.append(f.read())
# Splitting 'l' on '|' and storing to list - 'lin'
for i in l:
    lin=i.split("|")
# Emptying list - 'l'
l=[]
# Splitting 'l' on '|'
for i in lin:
    l.append(i.split("s."))
# Deleting the first part as it is not necessary
for i in l:
    del i[0]
s2=""
d={}
# Formatting in the required format and storing in a string format.
for i in l:    
    s1=str(i)[3:(len(str(i))-3)]
    if((s1!="\\n")):
        s1=s1[2:]
        s1=s1.rstrip("\\n")
        s1=s1.replace("\\n","")
        l=s1.split("\\")
        s2 = s2+"".join(l) 
# Splitting in order to get individual details      
l=s2.split("%")
# Creating individual key-value pair in a dictionary with values= frequency of the prediction
for i in l:
    colon_index=(i.find(":"))
    key=i[:colon_index]
    value=i[colon_index+2:]
    print(f"Predicted - {key} with {value}% surety")
    if(key not in d):
        d[key]=1
    else:
        tmp=d[key]
        d[key]=(tmp+1)
        
d.popitem()
# Sorted the dictionary 'd' by values
l=(sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
# Writing it to a new text file
for i in l:
    with open('/Users/aarav/Desktop/Securities in emerging technology/Class Projects/Yolo Detection/final_format_private.txt','a+') as f:
        f.write(f"{i}")