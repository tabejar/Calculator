def commands():
  # I added a variabe that equals 1 so that I could use while loops and then subtract the 1 if I need the while loops to stop running.
  a = 1
  while a == 1:
    # I added this user input to allow the user to type their command and a .lower() so that there's no issue with capital letters when used.
    command = input("\nEnter a command (help for help): ").lower()
    if command == "help":
      print("Commands: (n and m represent integers) \n- help: see all available commands \n- add: adds two integers “n add m” \n- sub: subtracts two integers “n sub m” \n- div: divides two integers “n div m” \n- mult: multiplies two integers “n mult m” \n- ^: takes n to the power of m “n ^ m” \n- !: finds factorial of n “n!”")
    