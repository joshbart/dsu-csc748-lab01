import pwn

if __name__ == "__main__":

    # Similar to Lab1-2, Lab1-3 has a "win" function which provides shell access.
    # It also provides a base address to STDOUT at time of execution.
    # The goal is to use this base address to calculate the "win" address quickly.
    
    # I start by running the process.
    # process_to_exploit = pwn.remote("csc748.hostbin.org", 7013)
    # This next line can replace the one above for testing against a local binary.
    process_to_exploit = pwn.process("./lab1-3.bin")