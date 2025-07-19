import time
import sys

def fake_loading(task_name):
    print(f"\n{task_name}... ", end="")
    for i in range(10):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print(" done ✅")

print("=== Hacker Terminal ===")
fake_loading("Scanning for vulnerabilities")
fake_loading("Cracking password")
fake_loading("Uploading payload")
print("System ready. 🚀")
fake_loading