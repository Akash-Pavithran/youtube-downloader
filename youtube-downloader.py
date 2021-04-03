from pytube import YouTube
link = input(" Enter YouTube video URL: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
# stream.download('C:/Users/Blaugrana/Desktop')
