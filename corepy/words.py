from urllib.request import urlopen

story = urlopen('http://www.weather.bm/forecastpublicextended.asp')
story_words = []
for line in story:
    line_words = line.decode('utf-8').split()
    for word in line_words:
        story_words.append(word)
story.close()