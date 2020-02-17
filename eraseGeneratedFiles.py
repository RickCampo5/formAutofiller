import os

for i in range(44):
  os.remove(f"projects{i}.js")

print('Files deleted')