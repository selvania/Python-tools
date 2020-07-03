import json

with open('words.txt', 'r') as outfile:
	data = json.load(outfile)

def is_noun(x):
    if x in data['nouns'][0]:
        print(x + " is a noun.")
        return True
    else:
        return False

def is_verb(x):
    if x in data['verbs'][0]:
        print(x + " is a verb.")
        return True
    else:
        return False

def is_particle(x):
    if x in data['particles'][0]:
        print(x + " is a particle")
        return True
    else:
        return False

def is_adverb(x):
    if x in data['adverbs'][0]:
        print(x + " is an adverb")
        return True
    else:
        return False

def is_adjective(x):
    if x in data['adjectives'][0]:
        print(x + " is an adjective")
        return True
    else:
        return False

def add_noun(x):
    print(data['nouns'][0])
    data['nouns'][0][x] = 0
    print(data['nouns'][0])
    
def add_verb(x):
    print(data['verbs'][0])
    data['verbs'][0][x] = 0
    print(data['verbs'][0])

def add_particle(x):
    print(data['particles'][0])
    data['particles'][0][x] = 0
    print(data['particles'][0])

def add_adverb(x):
    print(data['adverbs'][0])
    data['adverbs'][0][x] = 0
    print(data['adverbs'][0])

def add_adjective(x):
    print(data['adjectives'][0])
    data['adjectives'][0][x] = 0
    print(data['adjectives'][0])

def find_word(x):
    noun = is_noun(x)
    verb = is_verb(x)
    particle = is_particle(x)
    adverb = is_adverb(x)
    adjective = is_adjective(x)
    if noun == True:
        print("noun")
    elif verb == True:
        print("verb")
    elif particle == True:
        print("particle")
    elif adverb == True:
        print("particle")
    elif adjective == True:
        print("particle")
    else:
        print("I'm sorry, I don't understant " + x + ".")
        print("Is this a real word or a typo?")
        answer = (input(">> "))
        if answer == "real word":
              print("It is a real word.")
              print("Is it a noun, a verb, adjective, adverb, or a particle?")
              answer_wordtype = input(">> ")
              answer_wordtype = answer_wordtype.lower()
              if answer_wordtype == "noun":
                  add_noun(x)
              if answer_wordtype == "verb":
                  add_verb(x)
              if answer_wordtype == "particle":
                  add_particle(x)
              if answer_wordtype == "adverb":
                  add_adverb(x)
              if answer_wordtype == "adjective":
                  add_adjective(x) 
        elif answer == "type":
              print("Could you correct the word for me?")
        else:
              print("I'm sorry, I don't understand.")
              print("Please enter real word or type.")
              
#We've put the words into parts of speech,
#now we need to identify subjects and objects, etc.
#this is how we will form the sentence.
    
#script
count = 0
while count < 10:
    print("Give me a sentence")
    sentence = input(">> ")
    sentence = sentence.split()
    print(sentence)
    for x in sentence:
        x = x.lower()
        find_word(x)
    print("Would you like to continue?")
    answer = input(">> ")
    answer = answer.lower()
    if answer == 'no':
        break

#print("In your sentence, " + subj + " " + conjugated_verb + " " + particle + " " + obj + " " + location_particle + " " + location.
    

print(data)

outfile.close()

with open('words.txt', 'w') as outfile:
	json.dump(data, outfile)
outfile.close()
