
# it is exit or not "learning."
def check_for_word():
    word = "learning"
    with open("/Users/nitishkumar/Documents/GitHub/Python_Learning/nitish.txt", "w") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
      
        else:
            print("Not found!..") 
            
check_for_word()



def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("/Users/nitishkumar/Documents/GitHub/Python_Learning/nitish.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
            
            
    return -1

check_for_line()

            