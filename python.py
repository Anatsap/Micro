import psutil
p = psutil.cpu_percent(interval=1)
print("psutil: ", p)