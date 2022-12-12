import os
import shutil

path=input('Enter the path of the folder: ')

vid_exte=['.mp4','.mov','.wmv','.avi','.avch','.flv','.fav','.swf','.mkv','.webm','.html5','.mpeg-2']
aud_exte=['.m4a','.flac','.mp3','.wav','.wma','.aac',]
pic_exte=['.jpeg','.png','.gif','.tiff','.eps','.ai','.indd','.raw','.psd','.pdf','.jpg']

for i in os.listdir(path):
    if os.path.splitext(i)[1] in vid_exte:
        if not os.path.exists(fr'{path}\video'):
            os.mkdir(fr'{path}\video')
            shutil.move(fr'{path}\{i}',fr'{path}\video\{i}')
        else:
            shutil.move(fr'{path}\{i}',fr'{path}\video\{i}')
    elif os.path.splitext(i)[1] in aud_exte:
        if not os.path.exists(fr'{path}\audio'):
            os.mkdir(fr'{path}\audio')
            shutil.move(fr'{path}\{i}',fr'{path}\audio\{i}')
        else:
            shutil.move(fr'{path}\{i}',fr'{path}\audio\{i}')
    elif os.path.splitext(i)[1] in pic_exte:
        if not os.path.exists(fr'{path}\image'):
            os.mkdir(fr'{path}\image')
            shutil.move(fr'{path}\{i}',fr'{path}\image\{i}')
        else:
            shutil.move(fr'{path}\{i}',fr'{path}\image\{i}')
    elif os.path.splitext(i)[1]=='':
        None
    else:
        if not os.path.exists(fr'{path}\others'):
            os.mkdir(fr'{path}\others')
            shutil.move(fr'{path}\{i}',fr'{path}\others\{i}')
        else:
            shutil.move(fr'{path}\{i}',fr'{path}\others\{i}')