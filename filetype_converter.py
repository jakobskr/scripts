import os
import sys

def convert (old, new):
	files = os.listdir()
	print("."+ old)
	for file in files:
		if file.endswith("."+ old):
			file_parts = file.split("." + old)
			os.rename(file, file_parts[0] + "." + new)
	

if __name__ == "__main__":
	print(sys.argv)
	if len(sys.argv) < 3:
		print("usage filetype_converter.py OLD NEW")
		sys.exit()
	convert(sys.argv[1], sys.argv[2])	
