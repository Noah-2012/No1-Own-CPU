# No1-Own-CPU

## Directory
- [Specs](#my-cpu-is-similar-to-a-risc-cpu)
  - [WER_CONTROLLER](#wer_controller-write-enable-register-controller)
  - [8 I/O Ports](#the-8-io-ports)
- [More Pictures](#more-pictures)
- [Thanks / Credits](#thanks-and-credits)
- [Downloads / My Website](#downloads-and-my-website)

<details>
  <summary><strong>Wie funktioniert meine CPU?</strong></summary>
  <p>
    <ul>
      <a href="#my-cpu-is-similar-to-a-risc-cpu">- Specs</a><br>
      &nbsp;&nbsp;&#8226;<a href="#wer_controller-write-enable-register-controller">  - WER_CONTROLLER</a><br>
      &nbsp;&nbsp;&#8226;<a href="#the-8-io-ports">  - 8 I/O Ports</a><br>
      <a href="#more-pictures">- More Pictures</a><br>
      <a href="#thanks-and-credits">- Thanks / Credits</a><br>
      <a href="#downloads-and-my-website">- Downloads / My Website</a><br>
    </ul>
  </p>
</details>


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
  - 8 I/O Ports ([Explained Below](#the-8-io-ports))
  - 1 CR (Complete Reset)
  - 1 Clock Input (Soon with its own clock)
  - 1 ROM input for Instructions

## WER_CONTROLLER (Write Enable Register Controller)
  The WER_CONTROLLER, also called the Write Enable Register Controller, 
  is designed to enable Write Enable exactly when the clock pulse arrives and then, 
  with a short delay, send the data. 
  Here's a picture:

  ![WER_CONTROLLER1](images/pic1.png)

  In the picture, you can see the inputs REGID1 to REGID8, 
  which stand for Register Instruction Decoder. 
  These are the inputs of the instruction decoder. 
  The outputs are WER1 to WER8 and REG1 to REG8. 
  WER stands for Write Enable Register, and REG stands for Register.

  ---

  To ensure that the data is correctly routed to the PC (Program Counter) 
  so that a new value can be loaded, we use this part of the WER_CONTROLLER:

  ![WER_CONTROLLER2](images/pic2.png)

  This has two inputs and two outputs. The first input, PC_SET_READY, is used to tell the logic to pass the PS_SET_IN value.
  Then it checks whether the given value is the command itself (because that was a bug). 
  If not, the address is passed through. Then there is the PC_SET output, which passes the specified address to the counter. 
  The PC_C_L tells the counter whether it should continue counting normally or load a specified value.

## The 8 (I/O) Ports
  Since my CPU is still in beta, the 8 (I/O) ports are only connected to the 8 main registers. 
  These are located on pins REG1R to REG8R. REG#R stands for Register # Read.
  Here's an image:

  ![REG#R_Ports](images/pic3.png)

## More pictures
  This is the Main Place from the CPU:

  ![CPU_MAIN](images/pic4.png)

  Here are the RAM Banks and the Controller:

  ![RAM](images/pic5.png)

---

## Thanks and Credits

  Thanks to the team at Logisim Evolution for making this all possible. 
  Here is the Logisim Evolution GitHub: [Here](https://github.com/logisim-evolution/logisim-evolution)

  This project I created should continue, and ideally, have several versions. 
  So maybe leave **Star** and feel free to **Fork** it. Thank you guys.

## Downloads and my Website

  - Downloads (3.9.0):
      - [Mac OS](https://github.com/logisim-evolution/logisim-evolution/releases/download/v3.9.0/logisim-evolution-3.9.0-x86_64.dmg)
      - [Windows](https://github.com/logisim-evolution/logisim-evolution/releases/download/v3.9.0/logisim-evolution-3.9.0-x86_64.msi)
      - [Linux](https://github.com/logisim-evolution/logisim-evolution/releases/download/v3.9.0/logisim-evolution_3.9.0_amd64.deb)
   
  - [My Website](https://noah-2012.github.io/pp/)

---

<details>
  <summary><strong>Wie funktioniert meine CPU?</strong></summary>
  <p>Hier steht eine ausführlichere Erklärung, die man erst beim Aufklappen sieht.</p>
</details>

