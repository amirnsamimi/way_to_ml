highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

highlighted_poems_stripped = []

for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())

print(highlighted_poems_stripped)

highlighted_poems_details = []

for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(":"))

print(highlighted_poems_details)

titles=[]
poets=[]
dates=[]

for i in highlighted_poems_details:
  titles.append(i[0])
  poets.append(i[1])
  dates.append(i[2])
  text = "The poem {title} was published by {poet} in {date}.".format(title=i[0],poet=i[1],date=i[2])
  print(text)
