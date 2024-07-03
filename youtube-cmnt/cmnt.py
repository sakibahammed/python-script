# pest this line in terminal
# pip install youtube-comment-scraper


from youtube_comment_downloader import *

video_url = 'your video-url'
downloader = YoutubeCommentDownloader()

# Replace with the actual video URL
comments = downloader.get_comments_from_url(video_url, sort_by=SORT_BY_POPULAR)

for comment in comments:
    print(comment['text'])
