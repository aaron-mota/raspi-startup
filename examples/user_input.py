while True:
    try:
        CMD = input("What color do you want the LED to be? ")
        print(CMD)
    except KeyboardInterrupt:
        break
print("Finished.")
