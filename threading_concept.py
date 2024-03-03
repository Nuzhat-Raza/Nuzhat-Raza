import threading
import time
sum = 0
def sum_numbers1():
    sum1 =0
    time.sleep(5)
    for i in range(51):

        sum1 += i
    global sum
    sum += sum1

def sum_numbers2():
    sum2 = 0
    time.sleep(5)
    for j in range(51, 101):

        sum2 += j
    global sum
    sum +=sum2


thread1 = threading.Thread(target=sum_numbers1)
thread2 = threading.Thread(target=sum_numbers2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Total sum is ", sum)
