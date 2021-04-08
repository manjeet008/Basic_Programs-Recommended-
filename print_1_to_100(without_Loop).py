def rec(Start,End):
    if(Start<=End):
        print(Start)
        rec(Start+1,End)
StartInput=int(input("\nEnter start digit here..."))
EndInput=int(input("\nEnter end digit here..."))
rec(StartInput,EndInput)