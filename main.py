details = []
wordlist = []

def main():
	name = input("Persons Name: ")
	details.append(name)
	surname = input("Surname: ")
	details.append(surname)
	birth = input("Year of birth: ")
	details.append(birth)
	color = input("Color: ")
	details.append(color)

	print("Enter other information, seperated by a comma\n")
	other_info = input("-> ")

	arr = other_info.split(",")
	
	for i in arr:
		details.append(i)

	for i in details:
		for j in details:
			wordlist.append(i+j)

	with open("wordlist.txt", 'w') as f:
		for item in wordlist:
			f.write(item+"\n")

if __name__ == "__main__":
	main()