import psutil

thresholds = 10

# Check CPU usage

cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")
# if cpu_usage > thresholds:
#     print(f"Warning: CPU usage is at {cpu_usage}%")

# Check Memory usage
memory_info = psutil.virtual_memory()
if memory_info.percent > thresholds:
    print(f"Warning: Memory usage is at {memory_info.percent}%")

# Check Disk usage
disk_info = psutil.disk_usage('/')
if disk_info.percent > thresholds:
    print(f"Warning: Disk usage is at {disk_info.percent}%")


