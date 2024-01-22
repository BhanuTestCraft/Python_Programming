# calculate the execution time of the program
import time
# start_time=time.time()
# var=0
# for i in range(10000000):
#     var+=1
# print(var)
# end_time=time.time()
# elapsed_time= end_time-start_time
# print(f"Total execution time is : {elapsed_time:.4f} seconds")
# output: Total execution time is : 0.4435 seconds

start_time=time.monotonic()
var=0
for i in range(10000000):
    var+=1
print(var)
end_time=time.monotonic()
elapsed_time= end_time-start_time
print(f"Total execution time is : {elapsed_time:.4f} seconds")
# output: Total execution time is : 0.4417 seconds