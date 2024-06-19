#solution 1 using for loop

def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

#solution 2 using subsetting

def password_generator(username):
  last_letter = username[-1]
  rest_without_first = username[:-1]
  temp_password = last_letter + rest_without_first
  return temp_password

#solution for splitting sentences

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")

author_last_names = []

for i in author_names:
  last_name = i.split()
  print(last_name)
  author_last_names.append(last_name[1])



