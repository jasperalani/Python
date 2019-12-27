# [1, 2, 3, 4, 5]

def listify(str):
    split = str.split(', ');
    split[0] = split[0][1:]
    split[-1] = split[-1][:-1]
    return split

def mostfreq(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num

#####

rangei = input('Enter range:\n')
list = listify(rangei)

method = input('Enter method:\n')
if(method == 'mean'):
    total = 0
    for x in range(0, len(list)):
        total += int(list[x])
    print(total/len(list))
elif(method == 'median'):
    print(list[int((len(list) + 1) / 2)])
elif(method == 'mode'):
    print(mostfreq(list))
