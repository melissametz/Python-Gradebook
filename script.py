last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Challenge 1
subjects = ["physics", "calculus", "poetry", "history"]

# Challenge 2
grades = [98, 97, 85, 88]

# Challenge 3
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Challenge 4
# print(gradebook)

# Challenge 5
gradebook.append(["computer science", 100])

# Challenge 6
gradebook.append(["visual arts", 93])
#print(gradebook)

# Challenge 7
gradebook[-1][-1] = 93 + 5
#print(gradebook)

# Challenge 8
gradebook[2].remove(85)
#print(gradebook)

# Challenge 9
gradebook[2].append("Pass")
#print(gradebook)

# Challenge 10
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
