import os

for i in range(27):
  os.remove(f"projects{i}.js")

print('Files deleted')