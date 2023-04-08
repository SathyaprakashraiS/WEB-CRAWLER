PROJECT_NAME="bottle"
path=f"{PROJECT_NAME}/content.txt"
# with open(path) as f:
# 	contents = f.read()
# 	print(contents)

print("reading from file")
results=""
with open(path,"rt",encoding="utf8") as f:
	for line in f:
		#print("line in file: ",line)
		try:
			results+=line
		except:
			pass
print("theresults: ",results)
