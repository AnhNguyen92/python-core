import os
if os.path.exists("/Users/manlyhumg/Documents/myfile.txt"):
  os.remove("/Users/manlyhumg/Documents/myfile.txt")
else:
  print("The file does not exist") 