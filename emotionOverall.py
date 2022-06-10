# Take the emotion recognized output file and split that file based on white space
with open("output.txt", 'r') as file:
    for line in file:
        grade_data = line.strip().split(' ')
        print(grade_data)

    # Get the array length of recognized data
    x = len(grade_data)
    print(x)

sad, happy, angry, neutral, surprised, fearful, disgust = 0, 0, 0, 0, 0, 0, 0

for y in grade_data:
    if y == 'Sad':
        sad += 1
    elif y == 'Happy':
        happy = happy + 1
    elif y == 'Angry':
        angry = angry + 1
    elif y == 'Neutral':
        neutral = neutral + 1
    elif y == 'Surprised:':
        surprised = surprised + 1
    elif y == 'Fearful':
        fearful = fearful + 1
    else:
        disgust = disgust + 1

overAll = dict({
    'Sad': sad,
    'Happy': happy,
    'Angry': angry,
    'Neutral': neutral,
    'Surprised': surprised,
    'Fearful': fearful,
    'Disgust': disgust
})

max_value = max(overAll, key=overAll.get)
print("Separate counts of the Emotions" + '\n')
print(' Sad: ', sad, '\n', 'Happy: ', happy, '\n', 'Angry: ', angry, '\n', 'Neutral: ', neutral, '\n', 'Surprised: ',
      surprised, '\n', 'Disgust: ', disgust, '\n', 'Fearful:', fearful, '\n')
print("The resulted emotion is: " + max_value)
