from pytube import YouTube
link = input('Enter YouTube Video URL: ')
yt = YouTube(link)
yt = yt.streams.get_highest_resolution()
yt.download()
print('Downloaded', link)