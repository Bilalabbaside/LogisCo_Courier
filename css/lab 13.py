import math

def ReadData():
    with open ('training.csv','r') as file:
        data = file.read().split('\n')
    positives = 0
    negatives = 0
    for i in range(len(data) - 1):
        if 'Yes' in data[i].split(',')[4]:
            positives = positives + 1
        if 'No' in data[i].split(',')[4]:
            negatives = negatives + 1
    return positives,negatives,data

def ReadIns(inst,vari):
    with open ('training.csv','r') as file:
        data_t = file.read().split('\n')
    pos = 0
    neg = 0
    for i in range(len(data_t) - 1):
       da = data_t[i].split(',')[vari]
       if da == inst:
           if 'Yes' in data_t[i].split(',')[4]:
               pos = pos + 1
           if 'No' in data_t[i].split(',')[4]:
               neg = neg + 1         
    return pos,neg


def Entropy(positives,negatives):
    if positives==0 or negatives ==0:
        return 0
    total = positives + negatives
    term_a = positives / total
    term_b = negatives / total
    entropy = 0
    entropy = - term_a * math.log2(term_a) - term_b * math.log2(term_b)
    return entropy

def Sa(string,va):
    s = 0
    with open ('training.csv','r') as file:
        my_data = file.read().split('\n')
        for i in range(len(my_data) - 1):
            da = my_data[i].split(',')[va]
            if da == string:
                s = s+1
    return s        

def arrOfInstances(my_data):
    arr = []
    for i in range(len(my_data) - 1):
        if i !=0:
            da = my_data[i].split(',')[0]
            if da not in arr:
                arr.append(da)

    return arr


def arrOfInstan(my_data,var):
    arr = []
    for i in range(len(my_data) - 1):
        if i !=0:
            da = my_data[i].split(',')[var]
            if da not in arr:
                arr.append(da)

    return arr

def Gain(my_data,va):

    arr = arrOfInstan(my_data,va)
    length = len(arr)
    # S_total = len(my_data) - 2 
    print("Unique Instances are " , len(arr))
    entrop = 0
    positives,negatives,data = ReadData()
    S_total = positives + negatives
    print("Total Training Examples are " , S_total )
    totalEntropy = Entropy(positives,negatives)    
    print("Total Entropy is " , totalEntropy)
    gain_val = 0
    print("total ins are " , S_total)
    for i in range(length):
         posi,negi = ReadIns(arr[i],va)
         entrop = Entropy(posi,negi)
         print("Entropy Of " , arr[i] , "is " , entrop)
         sOfa = Sa(arr[i],va)
         gain_val = gain_val + ((sOfa  / S_total) * entrop)    
        

         """
         if i == 0:
             gain_val = totalEntropy - ((sOfa  / S_total) * entrop)
         if i!=0:
             gain_val = gain_val - ((sOfa  / S_total) * entrop)

             """
    total_gain = totalEntropy - gain_val
    return total_gain
        

    
"""
    
    gain = 0
    S = len(my_data) - 1 
    Sa1 = Sa(arr[0])
    Sa2 = Sa(arr[1])
    Sa3 = Sa(arr[2])

    print("Total Training Examples are " , S )
    print("Unique Instances are " , len(arr))
    positives,negatives,data = ReadData()
    Es = Entropy(positives,negatives)    
    print("Es is ",Es)
    pos,neg = ReadIns(arr[0])
    Es1 = Entropy(pos,neg)
    print("Entropy of S1 ( " + arr[0]  + " ) is " , Es1)
    pos,neg = ReadIns(arr[1])
    Es2 = Entropy(pos,neg)
    print("Entropy of S2 ( " + arr[1]  + " ) is " , Es2)
    pos,neg = ReadIns(arr[2])
    Es3 = Entropy(pos,neg)
    print("Entropy of S3 ( " + arr[2]  + " ) is " , Es3)
    
    gain = Es - (( Sa1 / S )* Es1) - (( Sa2 / S )* Es2) - (( Sa3 / S )* Es3)  
   """ 
    
#Main

with open ('training.csv','r') as file:
    my_data = file.read().split('\n')

arrOfName = []
for i in range(4):
    da = my_data[0].split(',')[i]
    arrOfName.append(da)

print(my_data[0].split(',')[0])
   # arrOfName[i] = my_data[0].split(',')[i]                       


arr = []

for i in range(4):
    gain = Gain(my_data,i)
    arr.append(gain)
    print("Gain of" , arrOfName[i] , "is "  , gain )



maximum = max(arr)
IndexOfMax = 0

print("Minimum of array is " , maximum)
for i in range(len(arr) - 1):
    if(arr[i] == maximum):
        IndexOfMax = i
        print("Maximum index is " , i)


print("Root Node will be " , arrOfName[IndexOfMax] )
# print("Gain of "  "  , gain)

