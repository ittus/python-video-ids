# Get video id from url

A python utility to get video_id from url

It supports Youtube, Dailymotion and Vimeo at the moment.

# How to use
```
>>> from videos_id.video_info import VideoInfo
>>> video_info = VideoInfo()
>>> video_info.check_video_id('https://www.youtube.com/watch?v=FvqgvWx_l8g')
'FvqgvWx_l8g'
>>> video_info.platform
'Youtube'
>>> video_info.video_id
'FvqgvWx_l8g'
>>> video_info.check_video_id('http://www.dailymotion.com/video/x51sxcf_tum-bin-2-full-movie_tv')
'x51sxcf'
>>> video_info.platform
'Dailymotion'
>>> video_info.video_id
'x51sxcf'
>>> video_info.check_video_id('https://vimeo.com/190614417')
'190614417'
>>> video_info.platform
'Vimeo'
>>> video_info.video_id
'190614417'
>>>

```

# Pattern

## Youtube

```
https://www.youtube.com/embed/[video-id]'
https://youtu.be/[video-id]'
https://www.youtube.com/watch?v=[video-id]'
```

## Dailymotion

```
http://www.dailymotion.com/video/[video-id]
http://www.dailymotion.com/video/[video-id]_[seo-string]
http://dai.ly/[video-id]
```

## Vimeo

```
http://vimeo.com/[video-id]
http://player.vimeo.com/video/[video-id]
http://vimeo.com/channels/staffpicks/[video-id]
https://vimeo.com/groups/name/videos/[video-id]
https://vimeo.com/album/[album-id]/video/[video-id]
```

# Testing

Unit test
```
python -m unittest discover
```

```
...........
----------------------------------------------------------------------
Ran 11 tests in 0.003s

OK
```
