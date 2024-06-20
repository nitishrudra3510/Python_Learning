import time
initial1 = time.time()

k=0
while(k<45):
    print("This is rudra bhai!")
    time.sleep(2)  # next print after 2 seconds.
    k+=1
print("While loop ran in", time.time()-initial1,"seconds")


initial2=time.time()
for i in range(45):
    print("This is rudra bhai!")
print("For loop ran in", time.time() - initial2, "seconds")



################ local time of computer

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
