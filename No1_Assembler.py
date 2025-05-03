def assemble_no1_with_jmp_targets(lines):
    register_map = {
        'da': 'da',
        'db': 'db',
        'dc': 'dc',
        'dd': 'dd',
        'de': 'de',
        'ea': 'ea',
        'eb': 'eb',
        'ec': 'ec'
    }


    opcodes = {
        'ADD': '0b',
        'SUB': '0c',
        'MUL': '0d',
        'DIV': '0e',
        'MOV': '0a',
        'JMP': '0f'
    }

    rom = ['00'] * 256  # Simulierter ROM mit 256 Adressen
    pc = 0
    pending_jmp_targets = []

    for line in lines:
        line = line.strip().split(';')[0]
        if not line:
            continue

        tokens = line.replace(',', '').split()

        if tokens[0] in ('ADD', 'SUB', 'MUL', 'DIV'):
            rom[pc] = opcodes[tokens[0]]
            rom[pc + 1] = register_map[tokens[1]]
            rom[pc + 2] = register_map[tokens[2]]
            rom[pc + 3] = 'c1'
            pc += 5  # +2 padding

        elif tokens[0] == 'MOV':
            rom[pc] = opcodes['MOV']
            rom[pc + 1] = register_map[tokens[1]]
            rom[pc + 2] = tokens[2].replace('#', '')
            rom[pc + 3] = 'fa'
            pc += 5

        elif tokens[0] == 'JMP':
            addr = int(tokens[1], 16)
            rom[pc] = opcodes['JMP']
            rom[pc + 1] = tokens[1]
            rom[pc + 2] = 'c2'
            pending_jmp_targets.append(addr)
            pc += 5

        else:
            raise ValueError(f"Unbekannter Befehl: {tokens[0]}")

    # Setze c2 an allen JMP-Ziel-Adressen
    for addr in pending_jmp_targets:
        if addr < len(rom):
            rom[addr] = 'c2'

    return rom

# 🧪 Beispiel
if __name__ == "__main__":
    program = [
        "MOV da, #02",
        "MOV db, #03",
        "SUB da, db",
        "JMP 09"
    ]
    rom = assemble_no1_with_jmp_targets(program)

    for addr, byte in enumerate(rom):
        print(f"{addr:02X}: {byte}")

