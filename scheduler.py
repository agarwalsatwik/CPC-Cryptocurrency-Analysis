import time
import CPC

counter = 0
run_count = 1
interval = 5 #seconds

while (counter < run_count):
    counter+=1
    CPC.cpc_main()
    time.sleep(interval)
    print(f"run: {counter}")

print(f"executed {run_count} times, every {interval} seconds")