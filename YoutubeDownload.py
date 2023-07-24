import requests
import youtube_dl

# Kullanıcıdan bir YouTube videosu URL'si isteyin.
video_url = input("Bir YouTube videosu URL'si girin: ")

# YouTube videosunu indirin.
youtube_dl.YoutubeDL({
    "format": "bestvideo",
    "outtmpl": "video-%(id)s.%(ext)s",
}).download([video_url])

# Kullanıcıya videonun indirildiğini bildirin.
print("Video başarıyla indirildi.")
