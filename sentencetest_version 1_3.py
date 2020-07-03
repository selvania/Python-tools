#algorithm testing 1.3
#July 1, 2020
#adding json data distribution between the reader and the writer.

#creating word lists in arrays

import json
import random

#adding json to the file
with open('words.txt', 'r') as outfile:
	data = json.load(outfile)

array_subject_singular = data['nouns'][0]
array_subject_plural = data['nouns'][0]
dict_subject_singular = data['nouns'][0]
dict_subject_plural = data['nouns'][0]
#the dictionaries should include the object form

array_verb_singular = data['verbs'][0]
array_verb_plural = data['verbs'][0]
array_verb_need_particle = data['verbs'][0]
#each verb should include their own array of data including necessary particles

array_object_particle = data['particles'][0]
array_object_indirect = ["they", "I"]

array_adverb = data['adverbs'][0]

#It may be good to use prior subjects to actually edit and create other word lists
#depending on the situation. This will allow the create_sentence function to be cleaner
#than it would be otherwise.

#logic function
logic = {"peaches fight":0, "peaches drink":0, "peaches dance":0, "the peach dances":0,
         "the peach fights":0, "peaches walk":0, "the peach walks":0,
         "the peaches fight":0, "the peaches drink":0, "the peaches dance":0, "a peach drinks":0, "a peach prances":0,
         "a peach fights":0, "a peach dances":0, "peaches run":0, "a peach runs":0, "a peach walks":0, "cats dance":0}

def test_logic(string):
    if string in logic:
        return logic[string]
    else:
        return 2

def object_truth():
    n_object = random.randrange (0,2)
    return n_object

def object_particle_truth(x,y):
    if x in array_verb_need_particle:
        if y != "":
            return 1
        else:
            return 0
    else:
       return 0

def transform_object(x):
    if x == "they":
        x = "them"
        return x
    elif x == " they":
        x = " them"
        return x
    elif x == "i":
        x = "me"
        return x
    elif x == " i":
        x = " me"
        return x
    else:
        return x

def create_subject():
    if_plural_subject = random.randrange(1,3)

    if if_plural_subject == 1:
        subject = random.choice(list(array_subject_singular.keys()))
    else:
        subject = random.choice(list(array_subject_plural.keys()))
    return subject

def create_verb(x):
    if x in array_subject_singular:
        verb = " " + random.choice(list(array_verb_singular.keys()))
        subver = x + verb
        subver = subver.lower()
        subver_logtest = test_logic(subver)
        while subver_logtest == 0:
            verb = " " + random.choice(list(array_verb_singular.keys()))
            print("subver logic failure")
            subver = x + verb
            subver = subver.lower()
            subver_logtest = test_logic(subver)
            if subver_logtest != 0:
                print("subver logic success")
                break
    else:
        verb = " " + random.choice(list(array_verb_plural.keys()))
        subver = x + verb
        subver = subver.lower()
        subver_logtest = test_logic(subver)
        while subver_logtest == 0:
            verb = " " + random.choice(list(array_verb_plural.keys()))
            print("subver logic failure")
            subver = x + verb
            subver = subver.lower()
            subver_logtest = test_logic(subver)
            if subver_logtest != 0:
                print("subver logic success")
                break
    return verb

def create_object():
     n_object = object_truth()
     if n_object == 1:
        if_plural_object = random.randrange(1,3)
        if if_plural_object == 1:
            obj = " " + random.choice(list(array_subject_singular.keys()))
            obj = obj.lower()
            obj = transform_object(obj)
        else:
            obj = " " + random.choice(list(array_subject_singular.keys()))
            obj = obj.lower()
            obj = transform_object(obj)
     else:
        obj = ""
     return obj

def create_object_particle(x,y):
    n_object_particle = object_particle_truth(x,y)
    if n_object_particle == 1:
        object_particle = " " + random.choice(list(array_object_particle.keys()))
    else:
        object_particle = ""
    return object_particle

def create_adverb():
    n_adverb = random.randrange(0,2)

    if n_adverb == 1:
        adverb = " " + random.choice(list(array_adverb.keys()))
    else:
        adverb = ""
    return adverb
        
#I should create more sub-functions here, that will allow any necessary repeat functions easier    
def create_sentence():

    subject = create_subject()
    verb = create_verb(subject)
    subject = create_subject()
    verb = create_verb(subject)
    obj = create_object()
    object_particle = create_object_particle(verb,obj)
    adverb = create_adverb ()      
    return print(subject + verb + object_particle + obj + adverb + ".")
        
    
#Now we activate it

takes = 0

while takes <= 100:
    create_sentence()
    answer = input("Continue? >> ")
    if answer == "yes":
        takes = takes + 1
    else:
        break

outfile.close()
