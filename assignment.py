# Import json module
import json

# Load json data from the file
file = open("quiz.json")
data = json.load(file)

print(""" The two groups are:
           1). sport
           2). maths \n""")

# Take input for the choice from the user       
choice = input("Enter your choice(sport/maths): ")

score = 0
print()

# Display question & options based on user choice
for i in data['quiz'][choice]:
    print("Question: " + str(data['quiz'][choice][i]["question"]))
    print("Options: " )

    num = 1
    for j in data['quiz'][choice][i]["options"]:
        print(str(num) + ".  " + j)
        num += 1
    
    # Take input for the answer from the user in integer(1/2/3/4)
    answer = int(input("\nYour answer: "))
    if data['quiz'][choice][i]['options'][answer - 1] == data['quiz'][choice][i]["answer"]:
        score += 1
    print()

# Print the overall score of the user
print("Congrats, Your final score is: ", score)
print()
# Print the correct answers
if choice == "sport":
    print("""Correct Answer:
- 4 
        """)

if choice == "maths":
    print("""Correct Answer:
- 3 
- 4
        """)