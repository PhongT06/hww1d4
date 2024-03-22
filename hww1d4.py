#1
import random
moods = ["happy", "sad", "energetic", "calm", "excited", "bored", "relaxed"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    mood = random.choice(moods)
    print(f"On {day}, you were feeling {mood}.")

#2

moods = ["happy", "sad", "energetic", "calm", "excited", "bored", "relaxed"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternoon", "evening"]

for day in days:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}.")

#3
        

homework = 0
while True:
    print("What? More homework?!", homework)
    homework += 1
    if homework == 5:
        break

homework = 0
while homework < 3:
    print("We're finishing all the homework!", homework)

    homework += 1

#4

colors = ["red", "blue", "orange", "green", "yellow"]

selected_color = random.choice(colors)
guess = input('Guess the selected color from the list: "red", "blue", "orange", "green", "yellow" ')

if guess.lower() == selected_color:
    print("Congratulations! You guessed correctly!")
else:
    print(f"Sorry, the selected item was {selected_color}. Please try again!")

#5
    
# Our playlist of genres
genres = ['EDM', 'Rock', 'Hip-hop', 'Classical']

for i in range(len(genres)):
    print(f"Track {i+1}: The genre is {genres[i]}.")

track_number = 1
while track_number <= len(genres):
    genre = genres[track_number - 1]
    
    print(f"Track {track_number}: The genre is {genre}.")
    if genre == "EDM":
        print("Time to party. Let's goooo!!")
        break
    track_number += 1

genres = ['EDM', 'Rock', 'Hip-hop', 'Classical']

for index in range(len(genres)):
    genre = genres[index]

    if genre == 'Classical':
        print(f"Skipping track {index+1} because {genre} is not suitable for the light show.")
        continue
    print(f"Track {index+1}: {genre} is ready for the light show!")

#6
    
genres = ['EDM', 'Rock', 'Hip-hop', 'Classical']

sublist_genres = genres[1:4]

for genre in sublist_genres:
    print(genre)

genres_with_music = [genre + " Music" for genre in genres]

print(genres_with_music)

for i in range(10, 0, -1):
    print(i)
print("The beat drops now!")


