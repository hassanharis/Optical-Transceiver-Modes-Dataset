## **Data Sheet** 

## **AFBR-5972EZ** 

**Compact 650-nm Transceiver with Compact Versatile-Link Connector for Fast Ethernet and up to 250 Mbaud over POF** 


## **Description** 

The Broadcom[®] AFBR-5972EZ transceiver provides the system designer with the ability to implement Fast Ethernet (100 Mb/s) over standard bandwidth 0.5 ± 0.05 NA POF. This transceiver features a compact Versatile-Link duplex connector that is compatible with existing Versatile-Link simplex connectors, and it features a very compact design with a form factor similar to a UTP connector. 

The AFBR-5972EZ transceiver is lead-free and compliant with RoHS. 

## **Features** 

- Fast Ethernet communications over POF 

- Link lengths up to 50m POF (NA 0.5) or 70m POF (NA 0.3) 

- Compact footprint 

- 3.3V operation 

- Data rates up to 250 Mbaud 

- LVDS input and output data connections 

- Analog RSSI (receiver signal strength) monitor output 

- Temperature range –40°C to 85°C 

## **Figure 1:  Block Diagram** 


**----- Start of picture text -----**<br>
Differential<br>Data Output<br>Integrated<br>Receiver<br>Integrated<br>RSSI Output Photodiode<br>LED<br>Driver<br>Differential<br>Data Input<br>LED<br>**----- End of picture text -----**<br>


## **Applications** 

- Factory automation at Fast Ethernet speeds 

- Fast Ethernet networking over POF 

- Proprietary communication over POF up to 250 Mbaud 

AV02-4953EN December 2, 2025 

Broadcom 

Compact 650-nm Transceiver with Compact Versatile-Link Connector for Fast Ethernet and up to 250 Mbaud over POF 

**AFBR-5972EZ** Data Sheet 

## **Transmitter** 

The transmitter contains a 650-nm LED with a driver IC. The LED driver operates at 3.3V. It receives an LVDS electrical input and converts it into a modulated current driving the LED. The IC and LED are packaged in an optical subassembly integrating the transmitter section. The optical subassembly couples the output optical power efficiently into POF fiber. 

## **Receiver** 

The receiver IC integrates a double photodiode with the amplifier and quantizer function. The IC is packaged in an optical subassembly integrating the receiver section. This optical subassembly couples the optical power efficiently from POF fiber to the receiving photodiode. The integrated IC operates at 3.3V and converts the photocurrent into a LVDS electrical output signal. 

## **Package** 

The transceiver package consists of three basic elements: two opto-electrical subassemblies and the housing, as shown in the block diagram in Figure 1. The package outline drawing and pinouts are shown in Figure 2 and Figure 7. 

The opto-electrical subassemblies use a high-volume assembly process together with low-cost lens elements that result in a cost-effective building block. They consist of the active III-V devices, IC chips, and various surface-mounted passive components. 

There are eight signal pins, four EMI shield solder posts, and two mounting posts, which exit the bottom of the housing. The solder posts are isolated from the internal circuit of the transceiver and are to be connected to chassis ground. The mounting posts are to provide mechanical strength to hold the transceiver to the application board. 

## **Figure 2:  PCB Footprint and Pinout Diagram** 


**----- Start of picture text -----**<br>
S TANDOFF<br>AR E A (2 x 0.65 x 1.03)<br>8.89 8.66<br>2 4 6 8<br>6.35 NOTES:<br>1 3 5 7 1) Dimension: mm<br>2) General tolerance: ±0.05<br>3.05 3.18<br>3) Recommended PCB Thickness 1.57 ±0.05<br>4) Pin Description<br>0 0<br>MOUNT POS T PIN FUNC<br>UNPLATE D (2x) 1 TD+<br>∅3.2 +0.1(2x) 3.73 23 TDTxVcc-<br>4 GND<br>5 RxVcc<br>S TANDOFF<br>6 RSSI<br>Top View AR E A (4 x 1.9 x 1) 78 RD+RD-<br>� Front �<br> (8x) S HIE LD GND (2x)<br>∅0.9 ∅1.6<br>+0.1 +0.1<br>7.77 4.44 3.17 1.9 0.63 0 0.64 1.91 3.18 4.45 7.77<br>7.78 6.7 5.76 2.45 0 2.45 5.76 6.7 7.78<br>**----- End of picture text -----**<br>


AV02-4953EN 2 

Broadcom 

Compact 650-nm Transceiver with Compact Versatile-Link Connector for Fast Ethernet and up to 250 Mbaud over POF 

**AFBR-5972EZ** Data Sheet 

## **Pin Descriptions** 

**Table 1:  Pin Descriptions** 

|**Pin Number**|**Name**|**Description**|
|---|---|---|
|1|TData+|Transmitter data in positive. This input is an LVDS compatible differential line.|
|2|TData-|Transmitter data in negative. This input is an LVDS compatible differential line.|
|3|TxVCC|Transmitter power supply pin. Provides +3.3V DC via a transmitter power supply filter circuit. Locate the<br>power supply filter circuit as close as possible to the TxVCC pin.|
|4|GND|Common ground pin. Directly connect this pin to the signal ground plane of the host board.|
|5|RxVCC|Receiver power supply pin. Provides +3.3V DC via a receiver power supply filter circuit. Locate the power<br>supply filter circuit as close as possible to the RxVCC pin.|
|6|RSSI|Receiver signal strength pin. Delivers a DC output current proportional to the average incoming light power.|
|7|RData+|Receiver data out positive. This data line is an LVDS-compatible differential output line that should be prop-<br>erly terminated. In absence of an optical input signal, this line is squelched.|
|8|RData-|Receiver data out negative. This data line is an LVDS-compatible differential output line that should be prop-<br>erly terminated. In absence of an optical input signal, this line (same as RData+) is squelched.|
|Shield|Shield|This is to be connected to the equipment chassis ground.|



## **Application Circuit** 

The recommended application circuit is shown in Figure 3. 

## **Figure 3:  Recommended Application Circuit** 


**----- Start of picture text -----**<br>
1μH<br>VCC 3.3V L1 100nF<br>C9<br>1μH<br>10μF 100nF L2<br>AFBR-5972EZ<br>C5 C6<br>Control Circuitry<br>TxVcc<br>LED Driver<br>TD+ 50 100nF TD+ K<br>C1<br>TD- LVDS<br>A<br>50 100nF Tx<br>C2 TD-<br>10μF 100nF<br>RxVcc<br>100nF<br>RD+ 50 C7 C8<br>C3 Amplifier K Rx<br>LVDS RD+ and<br>RD- 50 100nF RD- Quantizer A<br>C4<br>RSSI<br>RRSSI C10<br>2k 100nF<br>GND Chassis  GND<br>R2 100 LL<br>R1 100 LL<br>**----- End of picture text -----**<br>


AV02-4953EN 3 

Broadcom 

Compact 650-nm Transceiver with Compact Versatile-Link Connector for Fast Ethernet and up to 250 Mbaud over POF 

**AFBR-5972EZ** Data Sheet 

## **Board Layout – Decoupling Circuit and Ground Planes** 

The layout of the application circuitry is important to achieve optimum performance of the transceiver. Designers should use the following guidelines: 

- Use a power-supply decoupling circuit to filter out noise and ensure optimal product performance. 

- Provide a contiguous signal ground plane in the circuit board directly under the transceiver to provide a low-inductance ground for signal return current. 

- Connect the shield posts to the chassis ground to provide optimum EMI, ESD, and EMS performance, which is in keeping with good high-frequency board layout practices. 

## **Regulatory Compliance Table** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic discharge (ESD) to the<br>electrical pins|ESD22-A114|Withstands up to 2000V HBM applied between the electrical pins.|
|Immunity|Variation of IEC 61000-4-3|Typically shows no measurable effect from a 15V/m field swept from<br>80 MHz to 1 GHz applied to the transceiver when mounted on a circuit<br>board without chassis enclosure.|
|Eye safety|EN 60825-1:52007|Laser class 1 product (LED radiation only). TÜV certificate: R 50483935.<br>**CAUTION:**Use of controls or adjustments of performance or procedures<br>other than those specified herein can result in hazardous radiation<br>exposure.|
|Component recognition|Underwriter Laboratories|UL File #: E173874.|



## **Transceiver Diagnostics Timing Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Time to Initialize|t_init|—|5|ms|Notea,Figure 4|
|Assert Time|t_ass|—|100|µs|Noteb,c|
|Deassert Time|t_deass|—|100|µs|Notec,d|



- a. Time from power-on to when the modulated optical output rises above 90% of nominal. 

- b. Time from valid optical signal to assertion. 

- c. There is an internal signal detect (SD) signal that is directly related to assert (PA) and deassert (PD) levels as specified in Receiver Optical Characteristics. There is no direct access to the SD signal; however, the Rx data outputs will squelch and the RSSI will switch off once the optical input power falls below PD. Furthermore, the Rx data and RSSI outputs will be activated once the optical input power exceeds PA. 

- d. Time from loss of optical signal to deassertion. 

AV02-4953EN 4 

Broadcom 

Compact 650-nm Transceiver with Compact Versatile-Link Connector for Fast Ethernet and up to 250 Mbaud over POF 

**AFBR-5972EZ** Data Sheet 

## **Figure 4:  Transceiver Timing Diagrams** 


**----- Start of picture text -----**<br>
OCCURANCE<br>TX, RX Vcc > 2.97V OPTICAL SIGNAL OF LOSS<br>SD (internal)<br>TRANSMITTER SIGNAL t_ass t_deass<br>t_init<br>t_init:  t_ass & t_deass<br>**----- End of picture text -----**<br>


## **Absolute Maximum Ratings** 

Stresses in excess of the absolute maximum ratings can cause catastrophic damage to the device. Limits apply to each parameter in isolation, all other parameters having values within the recommended operation conditions. It should not be assumed that limiting values of more than one parameter can be applied to the products at the same time. Exposure to the absolute maximum ratings for extended periods can adversely affect device reliability. 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|–40|+100|°C|—|
|Case Operating Temperature|TC|–40|+85|°C|Notesa, b|
|Lead Soldering Temperature|Tsold|—|260|°C|Notec|
|Lead Soldering Time|tsold|—|10|s|Notec|
|Supply Voltage|VCC|–0.5|4.0|V|—|
|Data Input Voltage|VI|–0.5|VCC|V|—|



- a. Operating the product outside the maximum-rated case operating temperature range will compromise its reliability and can damage the product. 

b. The temperature is measured using a thermocouple connected to the hottest position of the housing. 

c. The transceiver is Pb-free wave solderable. 

## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|TC|–40|—|+85|°C|Notesa, b|
|Supply Voltage|VCC|2.97|3.30|3.63|V|—|
|Receiver Output Termination Impedance|RL|—|100|—|Ω|—|
|Signaling Rate (Fast Ethernet)|BFE|—|125|—|Mbaud|4B/5B; Notec|
|Signaling Rate (General)|BG|10|—|250|Mbaud|Noted|



a. The temperature is measured using a thermocouple connected to the housing. 

b. Electrical and optical specifications of the product are guaranteed across the recommended case operating temperature range only. 

c. Ethernet autonegotiation pulses are not supported. 

d. Minimum signaling rate for bi-phase coded signal. Maximum signaling rate for 8B/10B coded signal (verified by the PRBS 2[7] – 1 test pattern). 

AV02-4953EN 5 

Broadcom 

Compact 650-nm Transceiver with Compact Versatile-Link Connector for Fast Ethernet and up to 250 Mbaud over POF 

**AFBR-5972EZ** Data Sheet 

## **Transceiver Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|45|55|mA|—|
|Power Dissipation|PDISS|—|150|200|mW|—|
|Power Supply Noise Immunity|PSNI|50|—|—|mV|Peak to peak; Notea|
|Tx Differential Input Voltage (pk-pk)|VDII|200|—|1800|mV|—|
|Tx Input Voltage Range to Circuit Common|VI|0|—|2.4|V|—|



a. Frequencies from 0.1 MHz to 100 MHz. 

## **Transmitter Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Average Launched Power (1-mm POF; NA = 0.5)|PO-POF|–10|–6.5|–3.0|dBm|Notea|
|Extinction Ratio|EXT|10|—|—|dB|Notea|
|Central Wavelength|λC|635|650|675|nm|Notesa, b|
|Spectral RMS|Δλ|—|—|17|nm|Notesb, c|
|Optical Rise Time (10% to 90%)|tr|—|1.7|2|ns|Notea|
|Optical Fall Time (90% to 10%)|tf|—|1.6|2|ns|Notea|
|Duty Cycle Distortion Contributed by the Transmitter|DCD|—|—|1|ns|Peak to peak;<br>Notea|
|Data-Dependent Jitter|JDD|—|—|0.6|ns|Notea|
|Random Jitter Contributed by the Transmitter|JR|—|—|0.76|ns|Peak to peak;<br>Notesa, d|
|Overshoot|OS|—|7|25|%|Notea|



a. Measured at the end of 1-meter plastic optical fiber with a PRBS 2[7] – 1 sequence, running at 250 Mbaud data rate. 

b. Central wavelength is defined as: (Ref: EIA/TIA standard FOTP-127/6.1, 1991) 


**----- Start of picture text -----**<br>
� =1<br>=<br>� =1<br>**----- End of picture text -----**<br>


c. Spectrum RMS is defined as: (Ref: EIA/TIA standard FOTP-127/6.3, 1991) 


**----- Start of picture text -----**<br>
1<br>� = � =1 2 �  2 2<br>� =1<br>[( ) ]<br>d. Based on BER = 2.5 × 10 [–10] .<br>**----- End of picture text -----**<br>


AV02-4953EN 6 

Broadcom 

Compact 650-nm Transceiver with Compact Versatile-Link Connector for Fast Ethernet and up to 250 Mbaud over POF 

**AFBR-5972EZ** Data Sheet 

## **Receiver Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Differential Output Voltage (pk-pk)|VDO|500|—|900|mV|Notea|
|Output Common Mode Voltage|VOCM|—|1.2|—|V|Notea|
|Data Output Rise Time (10% to 90%)|tr|—|0.8|1.5|ns|Notea|
|Data Output Fall Time (90% to 10%)|tf|—|0.8|1.5|ns|Notea|
|Duty Cycle Distortion|DCD|—|—|1.0|ns|Notea, b|
|Data Dependent Jitter|JDD|—|—|1.2|ns|Notea, b|
|Random Jitter|JR|—|—|2.14|ns|Peak to peak;<br>Notesa, b, c|
|RSSI Output Responsivity|IRSSI/PIN|—|0.55|—|A/W|See Figures5and6.|
|Voltage at RSSI Output|VRSSI|0|—|VCC– 1.5|V|—|



a. Characterized with LVDS termination (100Ω). 

b. Contributed by Rx only. 

c. Based on BER = 2.5 × 10[–10] . 

**Figure 5:  Typical RSSI Output Voltage across RRSSI = 2 kΩ** 

**Figure 6:  Typical Responsivity vs. Temperature** 



AV02-4953EN 7 

Broadcom 

Compact 650-nm Transceiver with Compact Versatile-Link Connector for Fast Ethernet and up to 250 Mbaud over POF 

**AFBR-5972EZ** Data Sheet 

## **Receiver Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Unstressed Receiver Sensitivity (POF) for<br>Fast Ethernet Data Rate (125 Mbaud)|CSEN125|–26|—|—|dBm|Notea|
|Unstressed Receiver Sensitivity (POF) for<br>Data Rate 250 Mbaud|CSEN250|–22|—|—|dBm|Noteb|
|Input Optical Power Maximum (POF)|PIN-MAX|—|—|–3.0|dBm|Notesa, c|
|Operating Wavelength|C|635|650|675|nm|—|
|Assert Input Power Level|PA|—|–31|—|dBm|Notesd, e|
|Deassert Input Power Level|PD|—|–32.5|—|dBm|Notesd, e|
|Hysteresis between Assert and Deassert|PA-PD|—|2|—|dB|Notee|



a. Measured with a PRBS 2[7] – 1 sequence at 125 Mbaud. BER < 2.5 × 10[–10] . 

b. Measured with a PRBS 2[7] – 1 sequence at 250 Mbaud. BER < 2.5 × 10[–10] . 

- c. Input Optical Power Maximum is defined as the maximum optical average amplitude where the receiver duty cycle distortion reaches ±1 ns. 

- d. Asserted and deasserted levels are indicated as dB below the unstressed receiver sensitivity level for POF. 

- e. There is an internal signal detect (SD) signal that is directly related to assert (PA) and deassert (PD) levels. There is no direct access to the SD signal; however, the Rx data outputs will squelch and the RSSI will switch off once the optical input power falls below PD. Furthermore, the Rx data and RSSI outputs will be activated once the optical input power exceeds PA. 

**Figure 7:  Package Outline Drawing** 


**----- Start of picture text -----**<br>
2.54<br>0<br>0.63<br>1.5<br>1.9<br>3.4<br>5.75<br>7.65<br>15.9 21.45<br>Optical Axes<br>TX RX<br>1<br>7.35 0.25 (2x) 11.52<br>3.04<br>n0.4 (8x) 10.8<br>NOTES (unless otherwise specified):<br>1) Dimension: mm<br>2) Label with Partnumber, Lotnumber and Datecode<br>    (10mm x 12mm)<br>2)<br>R0.5 (4x)<br>2.54 (6x)<br>6.35 3.68 2.68 0 3.23 4.23<br>12.6 11.9<br>6.65<br>(0.3)<br>3<br>2.67<br>**----- End of picture text -----**<br>


AV02-4953EN 8 

Broadcom 

Copyright © 2015–2025 Broadcom. All Rights Reserved. The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos referenced herein belong to their respective companies. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 


**Lead (Pb) Free RoHS Compliant** 

