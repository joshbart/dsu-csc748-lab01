import pwn

if __name__ == "__main__":
    local_victim_process = pwn.process("./lab1-1.bin")

    victim_process_standard_output = local_victim_process.recv()
    print(victim_process_standard_output)