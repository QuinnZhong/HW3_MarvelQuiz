# HW3 Marvel Quiz 
# Three characters: Captain America, Iron Man, Spider man.
# 5 Questions are related to all characters.
# Questions' answers differ characters.

print(" \n======== Welcome to Marvel Quiz! ======== \nThe Marvel Character Test is an unscientific and “just for fun” personality assessment that will determine which of three characters from the Marvel universe you resemble the most. Who is your Marvel personality match? For each of the following questions, chose the one applies to you most.")

a_count = 0
b_count = 0
c_count = 0

question_answer_one = input ("\n1. Which food do you like most? \n(a)Apple Pie \n(b)Burgers and Booze \n(c)Cherry pie \nYour Answer: ")
if question_answer_one.lower() == 'a':
     a_count += 1
elif question_answer_one.lower() == 'b':
     b_count += 1
elif question_answer_one.lower() == 'c':
     c_count += 1
else: print("Sorry, I don't understand that response :( .")

question_answer_two = input ("\n2. Which colors do you like most? \n(a)Red, white, and blue \n(b)Bright red and gold \n(c)Blue \nYour Answer: ")
if question_answer_two.lower() == 'a':
     a_count += 1
elif question_answer_two.lower() == 'b':
     b_count += 1
elif question_answer_two.lower() == 'c':
     c_count += 1
else: print("Sorry, I don't understand that response :( .")

question_answer_three = input ("\n3. Which hobby do you like? \n(a)Drawing \n(b)Building armers \n(c)Taking photographes \nYour Answer: ")
if question_answer_three.lower() == 'a':
     a_count += 1
elif question_answer_three.lower() == 'b':
     b_count += 1
elif question_answer_three.lower() == 'c':
     c_count += 1
else: print("Sorry, I don't understand that response :( .")

question_answer_four = input ("\n4. Which sentences describe you most? \n(a)You're pretty much an all-around good guy. You are honest, up-front, loyal, extremely noble, and unfailingly dependable. Your strengths do not lie in creativity or brilliance, but You can step in and lead all the complex personalities, skill sets, strengths, and weaknesses of a diverse team. \n(b)You are strongly willful, don't work well with any authority other than your own, and will enthusiastically tear down just about anyone who challenges you. You are complicated, a little self-absorbed, and sometimes moody. \n(c)You exhibit behaviors of caring, kindness, loyalty, bravery, fear, worry, and intelligence. Your behaviors are most influenced by the environment. You exhibit more left brain activity as you use your knowledge to assess situations. \nYour Answer: ")

if question_answer_four.lower() == 'a':
     a_count += 1
elif question_answer_four.lower() == 'b':
     b_count += 1
elif question_answer_four.lower() == 'c':
     c_count += 1
else: print("Sorry, I don't understanf that response :( .")

question_answer_five = input ("\n5. Which song do you like more? \n(a)It's Been a Long, Long Time. \n(b)Back in Black \n(c)Ain’t No Rest for the Wicked \nYour Answer: ")
if question_answer_three.lower() == 'a':
     a_count += 1
elif question_answer_three.lower() == 'b':
     b_count += 1
elif question_answer_three.lower() == 'c':
     c_count += 1
else: print("Sorry, I don't understand that response :( .")

print ("====================")

if a_count > b_count and a_count > c_count: 
     print("You're Captain America!")
     print("======== Explaination ========")
     print("\nQestion 1. Captain America loves all things pure and American, so, of course he regularly partakes in the consumption of apple pie. \nQestion 2. To help him become a symbolic counterpart to the Red Skull, Steve Rogers was given the red, white, and blue costume of Captain America. \nQestion 3. In the comics, he actually won a gold medal once for his artistic ability. While he might not use his artistic skills that much anymore, drawing is clearly one of his favorite hobbies. \nQestion 5. When Rogers time-traveled to return the Infinity Stones the Avengers heisted, he decided to go back to 1945 and live the rest of his life with Peggy. Steve and Peggy dancing together to 'It's Been a Long, Long Time' was a heartwarming and poignant ending. ")

elif b_count > a_count and b_count > c_count: 
     print("You're Iron Man!")
     print("======== Explaination ========")
     print("\nQestion 1. Enjoyer of life. Thus, he likes to nosh on decadent burgers and wash them down with as much booze as his arc reactor-enhanced liver can take. \nQestion 2. Iron Man's classic bright red and gold suit from the comics shows up as more of a muted maroon on film but still keeps that color scheme Tony Stark is known for. \nQestion 3. Building an entire hoard of different armors must truly be Iron Man's sole hobby, due to the sheer amount of suits he's made. \nQestion 5. AC/DC are an Australian rock band. Their song 'Back in Black' is featured in Iron Man and Spider-Man: Far From Home. Their song 'Shoot to Thrill' is featured in The Avengers.")

elif c_count > a_count and c_count > b_count: 
     print("You're Spider-Man!") 
     print("======== Explaination ========")
     print("\nQestion 1. Peter Parker is a huge fan of everything that comes out of Aunt May's kitchen, but his absolute favorite has to be her cherry pie. \nQestion 2. Spiderman's blue is a vibrant cerulean blue. This color is widely available in home supply stores, and you can bring a picture to have this color perfectly color matched. \nQestion 3. Peter Parker being both a photographer and a superhero is amazing and that we wish we could get those crazy angles. \nQestion 5. The song has a similar vibe to 'Left Hand Free' from Marvel movies. This song is one that almost all alternative music junkies have at least heard of.")
else: 
     print("Wow, you're a combination of all three: Captain America, Iron Man, and Spider-Man!")
