# No1-Own-CPU

## My CPU is similar to a RISC CPU
- SPECS:
  - 16 Registers:
    - 8 Main Registers
    - 4 Data Registers (Not used yet)
    - 1 PC (Programcounter)
    - 1 CC (Command Cache; Especially for the MOV command)
    - 1 P0 (Just 0 in it)
    - 1 P1 (Just 1 in it)
  - 1 Instruction decoder
  - 1 Write Enable Register Controller ([Explained Below](#wer_controller-write-enable-register-controller))
  - 1 RAM controller and two RAM banks with 256 bytes each
  - 1 lightweight ALU
  - 8 I/O Ports (Explained Below)
  - 1 CR (Complete Reset)
  - 1 Clock Input (Soon with its own clock)
  - 1 ROM input for Instructions

## WER_CONTROLLER (Write Enable Register Controller)

