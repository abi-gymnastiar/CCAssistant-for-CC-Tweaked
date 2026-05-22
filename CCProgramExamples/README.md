## How to use the example programs
* drag and drop the desired program to ur CC:Tweaked computer (ingame)
* run the program by entering file name in the terminal (ex: audio-play-loop)
* note that some programs require specific folders or files to work (ex: images/ or audios/)
* note that some programs require parameters to be inputted when executing the code (ex: `audio-play-loop burenyuu 10 60`)

## Program Examples Usage
### audio-play-loop
How to use:
1. place a speaker near computer (touching)
2. mkdir audios
3. cd audios/
4. drag and drop .dfpwm files into this folder
5. cd ..
6. run this: `audio-play-loop [audio name] [interval min] [interval max]`
7. for example, `audio-play-loop burenyuu 10 60` will play burenyuu.dfpwm from folder audios/ every 10-60 seconds
8. you can use CCAssistant program (main.py) to convert mp3, mp4, wav, etc... into .dfpwm

### image-viewer
How to use: 
1. place monitors near computer (touching)
2. mkdir images
3. cd images/
4. drag and drop .nfp files into this folder
5. cd ..
6. run this: `image-viewer [image name]`
7. for example, `image-viewer myimage` will display myimage.nfp from folder images/ on to the monitors
8. you can use CCAssistant program (main.py) to convert png, jpg, etc... into .nfp

### image-slides-viewer
How to use: 
1. place monitors near computer (touching)
2. mkdir slides
3. cd slides/
4. drag and drop .nfp files into this folder
5. cd ..
6. run this: `image-slides-viewer [folder name] [interval]`
7. for example, `image-slides-viewer slides 5` will renders display all .nfp images inside slides/ every 5 seconds
8. you can use CCAssistant program (main.py) to convert png, jpg, etc... into .nfp