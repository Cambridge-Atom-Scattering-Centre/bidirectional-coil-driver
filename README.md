# bidirectional-coil-driver

This repository contains the files necessary to build the bidirectional coil driver, which is used to drive the phase coil and spin rotator coil in the Cambridge spin echo spectrometer.

## building the printed circuit boards

The two Gerber files contain information about the PCB of the coil driver itself and another board that can provide interface between the Raspberry Pi Pico and the coil driver. The BOM files have the bill of materials. The two pdf files show the schematics of the circuits.

The Gerber files and the BOM files can be given to a commercial PCB fabrication company like JLCPCB for them to produce it.

## connecting the boards

The two PCBs needs to be powered by a 5V power supply (the power inputs are marked as 0V and 5V). A temperary choice is to use a battery which supplies roughly 5V; a better and proper solution is to use a USB cable.

S2 on the pico board needs to be connected to the SPI interface of the driver board, as shown in the picure.

The load should be connected to the Iout+ and Iout- ports on the coil driver board.
