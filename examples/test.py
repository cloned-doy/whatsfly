import psutil

# get the current process
process = psutil.Process()

from whatsfly import WhatsApp



number = "6283139755157"

message = "Takbirrr, World! - "

chat = WhatsApp()

totals = 10
while 0 < totals:
	message = message+str(totals)
	chat.send_message(message=message, phone=number)
	totals -= 1

# get the memory usage after running the script
memory_info = process.memory_info()

# get the RAM usage in MB
ram_usage = memory_info.rss / (1024 * 1024)

# get the memory usage in MB
memory_usage = memory_info.vms / (1024 * 1024)

print(f"RAM usage: {ram_usage:.2f} MB")
print(f"Memory usage: {memory_usage:.2f} MB")
