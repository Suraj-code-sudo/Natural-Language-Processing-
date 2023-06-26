import moviepy.editor as mp
video = mp.VideoFileClip("Family.mp4")

file = open("transcript.txt", "r")  
text = file.read()
pattern = "countryside"


# Define the Base value. Here I am using d = 127 to represent all characters
base = 127

# Define the size of text and pattern
textSize = len(text)
patternSize = len(pattern)
m = patternSize

prime = 117
# Calculate the Hash value using the hash function for pattern

def calculateHash(patt):
    hashValue = -1
    m = patternSize
    for char in patt:
        hashValue += ord(char) * (base ** (m-1))
        m -= 1

    hashValue = hashValue % prime
    return hashValue

## Finding the pattern match

patternHash = calculateHash(pattern)

start = 0
final = 0
while start < textSize-patternSize+1:
    curr_hash = calculateHash(text[start:start+patternSize])
    if curr_hash == patternHash and text[start:start+patternSize] == pattern: final = start
    start += 1
    


target_time = final/textSize * 76

video = video.subclip(int(target_time))
video.preview()