import threading
import time

# Function with two input: n (1 to n sum), number of parallel threads t
total_sum = 0
sum_arr = []
lock = threading.Lock()
def threadSum(start, end):
    # time.sleep(5)
    local_sum = 0
    for item in range(start, end + 1):
        local_sum += item
    # sum_arr.append(local_sum)
    with lock:
        global total_sum
        total_sum = total_sum + local_sum


def sum_Nnumbers(n, t):
    x = n // t
    arr = []

    for i in range(t):
        start = (i * x) + 1
        end = (i + 1) * x if i != t else n
        thread = threading.Thread(target=threadSum, args=(start, end))
       # arr.append(thread)
        thread.start()
    for threads in arr:
        threads.join()
    #for items in sum_arr:
     #   global total_sum
      #  total_sum +=items
    return total_sum

n = 1000
t = 10
print(sum_Nnumbers(n, t))
