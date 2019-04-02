def sun_angle(time):
    lst=[]
    lst=time.split(":")
    hour=int(lst[0])
    mins=int(lst[1])
    hour1=(hour)-6
    tot=hour1*3600+(mins)*60
    if tot>=3600 and tot<=43200:
        x=180/(12*3600)
        angle=(tot*x)
        return angle
    elif tot==0:
        return 0 
    else:
        return "I don't see the sun!"
    

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")