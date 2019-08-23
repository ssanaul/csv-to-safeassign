import csv
with open('../safeassign.csv', encoding='utf-8-sig') as csvfile:
	reader = csv.reader(csvfile)

	i = 0
	for row in reader:
		if i > 0 and i <= 10: #First 10 students
			username = row[0]
			lastname = row[1]
			firstname = row[2]
			questions_answers = row[3:]

			textfile = open(username + '.txt', 'w')
			textfile.write(lastname + ', ' + firstname + '\n' + username + '\n---\n')

			for j in range(len(questions_answers)):
				textfile.write(questions_answers[j] + '\n' + ('---\n' if j%2!=0 else '\n'))

			textfile.close()
		i += 1
