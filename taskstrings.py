#  Clean up the following variable
# name = "JOHn ." to "john"

name = "JOHn ."
namef = name.strip().lower()[0:4]
print(namef)

# Sentence_one
# "The Dog Breed is German Shepherd" only display "Breed is German"

sent_one = "The Dog Breed is German Shepherd"
sent_onef = sent_one[8:23]
print(sent_onef)

# Setence_two
# "Defeats for the Clinton forces, this was her moment of triumph"
# only display "Clinton forces"

sent_two = "Defeats for the Clinton forces, this was her moment of triumph"
sent_twof = sent_two[16:29]
print(sent_twof)

# Split the sentence using semicolon and display length of the results
sent = "The lazy dog; ran so fast; it hit the wall"
sentf = sent.split(";")
print(len(sentf))

# Clean up and display full name "John Doe"
# first_name = 'Joh.n' last_name ="Do,e"

first_name = "Joh.n"
last_name ="Do,e"

first_namef = first_name[0:3] + first_name[4:5]
last_namef = last_name[0:2] + last_name[3:4]
full_name = first_namef +" "+ last_namef
print(full_name)
