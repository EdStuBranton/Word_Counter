import re
import sys
import os

# list_of_filenames = ['All thats left is the dialtone.txt', 'BIG FAT.txt', 'Chance Happenstance Stallion Lyrics.txt', 'Collarism heavy.txt', 'Collarism lyrics.txt', 'Collarism the new approach.txt', 'Cuteness overload.txt', 'Cutiful.txt', 'deep with sex in it.txt', 'did you use everything you had at hand.txt', 'Down with you boy!.txt', 'Du bist nicht Schuld Rap.txt', 'Du bist nicht schuld.txt', 'DudeDaFUCK.txt', 'Es geht ihm scheiße, punk.txt', 'Foxboy - Monoko.txt', 'Furry Drama metal.txt', 'Furry little critters.txt', 'Germany stands behind you we.txt', 'Got my audi a8 in the garage.txt', 'Hey Yarnball.txt', 'i always wanted you.txt', 'I am a fog.txt', 'I avert my eyes from the sadness inside of me.txt', 'I came down from the mountain and lived to tell the tale.txt', 'I dont know how to make money.txt', 'I get up every day and find a new reason to live.txt', 'I had a grand ol.txt', 'I have done so much research to find myself a cure Rap.txt', 'I havent reached it all yet.txt', 'I shall lay thy body greatly.txt', 'I told you I would lick your paws.txt', 'I transition to empty.txt', 'I want synthetic leather.txt', 'I want to rise to the top.txt', 'I want to write a song but my chords all sound the same.txt', 'Ich will keine kleinen Hunde.txt', 'If furries were real what would they look like.txt', 'In the end of the weekend.txt', 'It sounded so much better in my head.txt', 'Its a dogs day.txt', 'Its right there on your screen.txt', 'Kicked out thrown out Script and song.txt', 'Leaves are falling.txt', 'Live 11 - PCD.txt', "Look who's talking.txt", 'many syllables rap.txt', 'My collar Room.txt', 'My friends are all electronics technicians and computer scientists.txt', 'My parents are telling me put.txt', 'my past can disrupt.txt', 'My paws glide on four wheels.txt', 'My smartphone is almost empty but my glass is only half full.txt', 'No longer wearing a collar.txt', 'Not 18 yet 2.0.txt', 'Not 18 yet.txt', 'Now hes here and Im here too.txt', 'On the back of a ridgeback.txt', 'Please wait.txt', 'rageinducedoverloadedstackoverflow.txt', 'Rap Zu viel Geld.txt', 'Restraints.txt', 'Right where you want me to be me.txt', 'run that by me again.txt', 'say may I sit right next to you.txt', 'Snapping the leash.txt', 'So easy to get but so hard to please.txt', 'So hot in blue collars.txt', "something doesn't feel right.txt", 'Song about free exploring sexuality.txt', 'Stop pulling my ears 2.txt', 'Stop pulling my ears.txt', 'the clock is ticking.txt', 'The colored light of my computer screen.txt', 'The perversion of a commission 2.txt', 'The perversion of a commission.txt', 'There always someone thing bigger.txt', 'There is just something about you.txt', 'there is one day where I will leave you.txt', 'There is this place in the middle of europe.txt', 'There they lie after a hard night.txt', 'These blue spots on your snout Sea Salt Kopie.txt', 'These blue spots on your snout Sea Salt.txt', 'These blue spots on your snout Sea Salt2.txt', 'They say Im a real K9.txt', 'The_perversion_of_a_commission_3.txt', 'This door has not opened yet.txt', 'tippity toes tipping tapping down the corridor.txt', 'To know that you think I.txt', 'Today I got blown off again.txt', 'Two furries occupying my backseats.txt', 'unpenetratable.txt', 'very dark Lyrics.txt', 'walking in your minefield 2.txt', 'walking in your minefield.txt', 'Wanderstiefel Nackte Straßen.txt', 'Was ist denn nun mit dem Job.txt', 'We are furries Polka.txt', 'We are the employees.txt', 'We dont look into your eyes.txt', 'Wearing a collar alternate Version.txt', 'Wearing a collar.txt', 'What happened in the meantime.txt', 'Who do you serve.txt', 'you got so many dudes.txt', 'Youre mine.txt', 'youre unemployed once more.txt', 'youtube Lifestyle.txt']

# for filename in os.listdir(r'C:\code\WordCounter project\Songtexte_test_ordner'):
#     list_of_filenames.append(filename)
#     
# print(list_of_filenames)

filepath = r'C:\code\WordCounter project\Songtexte_test_ordner'

def collect_filenames(path):
    list_of_filenames = []
    for filename in os.listdir(path):
        list_of_filenames.append(filename)
    return list_of_filenames

def open_file(filename):
    with open(r'C:\code\WordCounter project\Songtexte_test_ordner' + '\\' + filename) as f:
        content = f.read()
    return content

def unwanted_char_check(filecontent):
    pattern = "[^'a-zA-Z0-9 ]"
    clean_content = re.sub(pattern, " ", filecontent)
    return clean_content

def split_into_list(string):
    split_content = string.split(' ')
    return split_content

def words_counter(array):
    word_dictionary = {}
    for word in array:
        if isinstance(word, str):
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1
    return word_dictionary

for filename in collect_filenames(filepath):
    content_of_file = open_file(filename)
    cleaned_up_content = unwanted_char_check(content_of_file)
    split_content_array = split_into_list(cleaned_up_content)
    result = words_counter(split_content_array)
    print(result)
    

    
    
# pattern = "[^'a-zA-Z0-9 ]"

# with open(r'E:\Textdokumente\Songtexte_kopie\The_perversion_of_a_commission_3.txt') as f:
#     result = f.read()
#     new_result = re.sub(pattern, " ", result)
#     final = new_result.split(' ')
#     
#     word_dictionary = {}
#     for word in final:
#         if isinstance(word, str):
#             if word in word_dictionary:
#                 word_dictionary[word] += 1
#             else:
#                 word_dictionary[word] = 1
#     
# print(word_dictionary)

