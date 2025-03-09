import receiver, graphic



def main():
    print("waiting for a new connection")
    cm = receiver.CommunicationManager()
    vm = graphic.VideoManager()
    while True:

        msg = cm.listen()
        if msg[0]==1:
            vm.load_frame(msg[1]) # load frame from bytes
        # show video 
        if (vm.show_video()):
            break


if __name__=="__main__":
    print("program start")
    #after connection wait for new connections
    # while True:
    main()
    print("program end")
