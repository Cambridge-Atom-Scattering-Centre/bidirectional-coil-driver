# bidirectional-coil-driver

This repository contains the files necessary to build the bidirectional coil driver, which is used to drive the phase coil and spin rotator coil in the Cambridge spin echo spectrometer.

## Building the printed circuit boards

The two zipped Gerber files contain information about the PCB of the coil driver itself and another board that can provide interface between the Raspberry Pi Pico and the coil driver. The BOM files have the bill of materials. The two pdf files show the schematics of the circuits.

The Gerber files and the BOM files can be given to a commercial PCB fabrication company like JLCPCB for them to produce it.

A Raspberry Pi Pico microcontroller is needed to control the current.

## Connecting the boards

The two PCBs needs to be powered by a 5V power supply (the power inputs are marked as 0V and 5V). A temperary choice is to use a battery which supplies roughly 5V; a better and proper solution is to use a USB cable.

S2 on the pico board needs to be connected to the SPI interface of the driver board, as shown in the picure.

The load should be connected to the Iout+ and Iout- ports on the coil driver board.

## Controlling the current

After everything is connected in the same way as the picutre, you can program the Raspberry Pi Pico. A popular application to do that is Thonny.

Copy set_curret.py and main.py to the directory of the Pi Pico.

set_current.py is a function that send a number via SPI to the driver board and set the current. Note that when setting the current, you need to have a load connected, otherwise the driver board might break.

main.py is a file that run automatically after the Pi Pico is powered, because it is called "main". It receives signal via RS232 (the three ports on the Pico board). You can connect a PC to it via serial port. talk_to_pico.m is a MATLAB file that can be used on a PC to set the current.

## Characterisation of the coil driver

characterisation_20231130.mat is a file that contains the information about the characterisation of the power supply. It contains a variable called msg, which is the numbers sent to the digital to analogue converter on the driver board. Another viriable, I, stores the measured current.

Keithley_Allanvar.mat records the current of the power supply every 0.1 seconds for about 12.5 hours, when the output of the DAC was set to 0. The results can be used for calculating the Allan variance.

# Revision Notes:

## Noise and risetime of Precision Current Source

The Technical Design Note published in measurement and Technology describes the original version of a precision current source. In that application, rapid response was more important than current noise.  These notes are intended for those whose requirements are different and are beyond the brief of the original Technical Note.

The rise time of the original circuit was ~2 s and it settles within about 20 microseconds with a resistive load, as described in the manuscript. However, there is significant overshoot with a resistive load, due to the high bandwidth with respect to the positive input of the AD8607 integrating amplifier. Noise measurements in the manuscript are performed with a Keithley integrating voltmeter (and the internal resistor of the Keithley in order to measure current).  It has a minimum sample rate of 0.1 s. The measured noise reported in the manuscript, therefore represents the noise averaged over the sample time and although the current deviation is less than 1 lsb in all the measurements reported, the rms noise current at full bandwidth is significantly greater.

Bandwidth and rise-time can be traded to improve the rms noise current; however, that requires some modification to the schematic and printed circuit board. The notes here are the result of simcape/simulink models, which give a good representation of the original circuit and are, therefore, believed to be reliable.

## Noise sources:

Wideband noise taken from the respective data sheets are given in the table:

| Device  | Voltage noise / nV/√Hz |
| ------- | ---------------------- |
| MAX6071 |           30           |
| AD8607  |	          22           |
| LTC2642 |	          10           |

The total noise voltage is estimated by adding contributions, in quadrature, from MAX6071, LTC2642, giving  ~32 nV/√Hz.
Note that the major component is the voltage reference.  Note also that, in the original configuration, the bandwidth for the DAC signal is unaffected by stabilising capacitor of U5.2, Cf, as noted above.

## Noise reduction strategies:
