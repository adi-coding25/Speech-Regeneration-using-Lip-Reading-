print ("0]Exit\n1]Record Video\n2]Play Recorded Video\n")
ch=int(input("enter choice\n"))

if(ch==1):
            print("press q to exit the video")
            execfile('recordvideo.py')
elif(ch==2):
            print("press q to exit the video")
            execfile('playvideo.py')
elif(ch==0):
            exit()
else:
            print("invlid choice")
