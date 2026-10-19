## **AFBR-57E6APZC** 

Multimode Small Form Factor Pluggable Transceivers with LC Connector and Conformal Coating, DMI for FDDI and Fast Ethernet 

## **Data Sheet** 



## **Description** 

The AFBR-57E6APZC Small Form Factor Pluggable LC transceiver provides the system designer a product to implement FDDI/Fast Ethernet networks with DMI physical layers. 

As an enhancement to the conventional SFP interface defined in SFF-8074i, the AFBR-57E6APZC is compatible to SFF-8472 (digital diagnostic interface for optical transceivers). Using the 2-wire serial interface defined in the SFF-8472 MSA, the AFBR-57E6APZC provides real time information on temperature, LED bias current, LED average output power and receiver average input power. The interface also adds the ability to monitor the Receiver Loss of Signal (RX_LOS). The PCB has an overall conformal coating except in the contact pad area. 

## **Features** 

- RoHS compliant 

- Lead free 

- Industry standard Small Form Pluggable (SFP) package 

- LC duplex connector optical interface 

- Operates with 50/125-μm and 62.5/125-μm multimode fiber 

- Compatible with 100Base-FX version of IEEE802.3u 

- Single +3.3V power supply 

- +3.3V TTL LOS output 

- Squelched receiver outputs 

- Manufactured in an ISO 9001 certified facility 

- Operating temperature range: –40°C to +85°C 

- Bail de-latch 

- Hot plug capability 

## **Transmitter** 

The transmitter contains a 1310-nm InGaAsP LED. This LED is packaged in the optical subassembly of the transmitter. It is driven by an integrated circuit which converts differential PECL logic signals into an analog LED drive current. This current is monitored by the digital diagnostic interface. The transmitter light output power is inferred from this information. 

The LED is switched off in case a static signal is present at the PECL inputs. 

- Usage in harsh environment enabled by conformal coated PCB 

- Harsh environment tested according to EIA-364-65B Class IIIA and ASTM B 117 

## **Applications** 

- Factory automation at Fast Ethernet speeds 

- Fast Ethernet networking over multimode fiber 

## **Receiver** 

The receiver utilizes an InGaAs PIN photodiode coupled to a transimpedance pre- and postamplifier IC. It is packaged in the optical subassembly of the receiver. The data output is differential LVPECL. The LOS output is +3.3V TTL as per SFF-8074i. The PIN photodiode average current is monitored by the digital diagnostic interface as a measure for input optical power. Rx squelch is activated when a low input power is detected. 

Broadcom - 1 - 

Data Sheet 

AFBR-57E6APZC 

## **Loss of Signal** 

The Loss of Signal (LOS) output indicates that the optical input power to the receiver does not meet the minimum detectable level for FDDI compliance. 

## **Module Package** 

The transceiver package is compliant with the Small Form Pluggable (SFP) MSA with the LC duplex connector option. The hot-pluggable capability of the SFP package allows the module to be installed at any time including when the host system is on-line and operating. This permits the system to be configured or maintained without system downtime. The AFBR-57E6APZC requires a 3.3V DC power supply for optimal performance. 

## **Module Diagrams** 

## **Installation** 

The AFBR-57E6APZC can be installed in or removed from any MultiSource Agreement (MSA) – compliant Small Form Pluggable port regardless of whether the host equipment is operating or not. The module is simply inserted, electrical interface first, under finger pressure. Controlled hot-plugging is ensured by 3-stage pin sequencing at the electrical interface. The module housing makes initial contact with the host board EMI shield mitigating potential damage due to Electro-Static Discharge (ESD). The 3-stage pin contact sequencing involves (1) Ground, (2) Power, and then (3) Signal pins making contact with the host board surface mount connector in that order. 

This printed circuit board card edge connector is depicted in Figure 2 on the next page. 

**NOTE** Note that the pad areas shown in Figure 2 and Figure 7 are not coated. 

Figure 1 illustrates the major functional components of the AFBR-57E6APZC. The connection diagram of the module is shown in Figure 2. Figure 5 to Figure 8 depict the external configuration and dimensions of the module. 

**Figure 1  Transceiver Functional Diagram** 


**----- Start of picture text -----**<br>
OPTICAL INTERFACE ELECTRICAL INTERFACE<br>RECEIVER<br>AMPLIFICATION RD+ (RECEIVE DATA)<br>LIGHT FROM FIBER PHOTO-DETECTOR & QUANTIZATION RD– (RECEIVE DATA)<br>Rx LOSS OF SIGNAL<br>CONTROLLER & MEMORY MOD-DEF2 (SDA)<br>MOD-DEF1 (SCL)<br>MOD-DEF0<br>TRANSMITTER<br>TX_DISABLE<br>TD+ (TRANSMIT DATA)<br>LIGHT TO FIBER LED LED DRIVER<br>TD– (TRANSMIT DATA)<br>TX_FAULT<br>**----- End of picture text -----**<br>


Broadcom - 2 - 

Data Sheet 

AFBR-57E6APZC 

## **Figure 2  Connection Diagram of Module Printed Circuit Board** 

|||||||||||
|---|---|---|---|---|---|---|---|---|---|
|**20**|**VEET**||||**1**|**VEET**||||
|**19**|**TD–**||||**2**|**NU**||||
|**18**|**TD+**||||**3**|**TxDisable**||||
|**17**<br>**16**<br>**15**<br>**14**|**VEET**<br>**VCCT**<br>**VCCR**<br>**VEER**||||**4**<br>**5**<br>**6**<br>**7**|**MOD-DEF(2)**<br>**MOD-DEF(1)**<br>**MOD-DEF(0)**<br>**NU**||||
|**13**|**RD+**||||**8**|**LOS**||||
|**12**|**RD–**||||**9**|**VEER**||||
|**11**|**VEER**||||**10**|**VEER**||||
|||||||||||
||**TOP OF BOARD**||||**BOTTOM OF BOARD**|||||
|||||**(AS**|**VIEWED THROUGH TOP OF BOARD)**|||||



## **Digital Diagnostic Interface and Serial Identification** 

The 2-wire serial interface is based on ATMEL AT24C02C series EEPROM protocol. Conventional EEPROM memory (bytes 0– 255 at memory address 0xA0) is organized in compliance with SFF-8074i. As an enhancement the AFBR-57E6APZC is also compatible to SFF-8472. This enhancement offers digital diagnostic information at bytes 0–255 at memory address 0xA2. 

In addition to monitoring of the LED drive current and photodiode current, the interface also monitors the transmitter supply voltage and the temperature. The transmitter voltage supply must be provided for the digital diagnostic interface to operate. 

## **Data I/O** 

The AFBR-57E6APZC fiber-optic transceiver is designed to accept industry standard differential signals. The transceiver provides an AC-coupled, internally terminated data interface. Coupling capacitors have been included within the module to reduce the number of components on the customer's board. Figure 3 depicts the recommended interface circuitry. 

## **Regulatory Compliance** 

See Table 1 for transceiver Regulatory Compliance performance. The overall equipment design will determine the certification level. The transceiver performance is offered as a figure of merit to assist the designer. 

## **Electrostatic Discharge (ESD)** 

There are two conditions where immunity to ESD damage is important. Table 1 documents the transceiver’s immunity to both these conditions. 

The first condition is static discharge to the transceiver when handling it. For example when the transceiver is inserted into the transceiver port. To protect the transceiver, it is important to use normal ESD handling procedures. These precautions include grounded wrist straps, workbenches, and floor maps in ESD controlled areas. The ESD sensitivity of the AFBR-57E6APZC is compatible with typical industry production environments. 

The second condition is static discharge to the exterior of the host equipment chassis after installation. To the extent that the duplex LC optical interface is exposed to the outside of the host equipment chassis, it may be subject to system-level ESD events. The ESD performance of AFBR-57E6APZC exceeds typical industry standards. 

## **Immunity** 

Equipment hosting the AFBR-57E6APZC will be subjected to radio-frequency electromagnetic fields in some environments. These transceivers have good immunity to such fields due to their shielded design. 

## **Electromagnetic Interference (EMI)** 

Most equipment designs utilizing these high-speed transceivers from Broadcom will be required to meet the requirements of CENELEC EN55022. 

The metal housing design and shielded design of the AFBR-57E6APZC transceiver minimize the EMI challenge facing the host equipment designer. The transceivers provide superior EMI performance. 

## **Eye Safety** 

These transceivers provide Class 1 eye safety by design. Broadcom has tested the transceiver design for compliance with the requirements listed in Table 1 under normal operating conditions and under a single fault condition. 

## **Flammability** 

The AFBR-57E6APZC transceiver housing is made of metal and high strength, heat resistant, chemically resistant and UL-94V-0 flame retardant plastic. 

Broadcom - 3 - 

Data Sheet 

AFBR-57E6APZC 

## **Shipping Container** 

Ten transceivers are packaged in one shipping container designed to protect it from mechanical and ESD damage during shipment or storage. 

## **Regulatory Compliance** 

**Table 1  Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to the electrical<br>pins|JEDEC JESD22-A114|Meets Class 2 (2000 to 3999 Volts).<br>Withstand up to 2000V applied between<br>electrical pins.|
|Electrostatic Discharge (ESD) to the Duplex LC<br>Receptacle|Variation of IEC 61000-4-2|Typically withstand at least 9 kV without<br>damage when the LC connector receptacle is<br>contacted by a Human Body Model probe.<br>Typically withstand 15-kV air discharge on<br>LC-connector receptacle.|
|Electromagnetic Interference (EMI)|FCC Class B, CENELEC EN55022 (CISPR 22)<br>Class B|System margins are dependent on customer<br>board and chassis design.|
|Immunity|IEC 61000-4-3|Typically shows no measurable effect from a<br>10  V/m field swept from 80 to 1 GHz applied to<br>the transceiver without a chassis enclosure.|
|Component Recognition|Underwriters Laboratories and Canadian<br>Standards Association Joint Component<br>Recognition for Information Technology<br>Equipment including Electrical Business<br>Equipment|E173874, Vol. 1.|
|Eye Safety|EN 60950-1:2006+A11+A1+A12+A2<br>EN 60825-1:2007<br>EN 60825-2:2004+A1+A2|Compliant per Broadcom testing under single<br>fault conditions.|
|RoHS Compliance||Reference to RoHS Directive 2011/65EU Annex<br>II.|



Broadcom - 4 - 

Data Sheet 

AFBR-57E6APZC 

## **Figure 3  Recommended Connection Circuitry** 


**----- Start of picture text -----**<br>
1 μH<br>3.3 V<br>10μ 0.1μ 10μ  0.1μ<br>1 μH<br>VccT<br>3.3 V AFBR-57E6APZC<br>7.6k<br>Tx Dis<br>TX_GND<br>4.7k to 10k<br>0.1μ<br>50Ω<br>SO+ LED DRIVER<br>TD+<br>100Ω &<br>50Ω  LED<br>SO- SAFETY<br>3.3 V TD- 0.1μ CIRCUITRY<br>PROTOCOL<br>IC SerDes 2.7k 2.7k VccR<br>10μ 0.1μ<br>0.1μ<br>50Ω<br>SI+<br>RD+<br>100Ω AMPLIFIER<br>50Ω<br>SI- &<br>RD-  PD<br>0.1μ QUANTIZATION<br>4.3k 4.3k<br>RX_LOS<br>Rx_LOS<br>RX_GND<br>MOD_DEF2<br>SDA<br>MOD_DEF1 CONTROLLER<br>SCL<br>MOD_DEF0<br>MODULE<br>DETECT<br>4.7k to  4.7k to  4.7k to<br>10k 10k 10k<br>3.3 V<br>**----- End of picture text -----**<br>


**NOTE** Refer to SerDes supplier´s recommendation regarding the interface between the AFBR-57E6APZC and the SerDes. The proposed termination is a general recommendation for LVPECL AC-coupled signals. Other terminations could also be applicable depending on the SerDes interface. 

**Figure 4  MSA Required Power Supply Filter** 


**----- Start of picture text -----**<br>
AFBR-57E6APZC<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
Vcc TX<br>1uH<br>0.1uF 10uF*<br>Vcc RX 3.3V<br>1uH<br>0.1uF 10uF 0.1uF 10uF<br>**----- End of picture text -----**<br>


**Note: Inductors should have less than 1 Ohm series resitor per MSA * optional capacitance but recommended (required for SFP+)** 

Broadcom 

- 5 - 

Data Sheet 

AFBR-57E6APZC 

## **Pin Description** 

## **Table 2  Pin Description** 

|**Pin**|**Name**|**Function/Description**|**MSA Notes**|
|---|---|---|---|
|1|VEET|Transmitter Ground|a|
|2|NU|Not Used|b|
|3|Tx Disable|Transmitter Disable – Module disables on high or open||
|4|MOD-DEF2|Module Definition 2 – Two wire serial ID interface|c|
|5|MOD-DEF1|Module Definition 1 – Two wire serial ID interface|c|
|6|MOD-DEF0|Module Definition 0 – grounded in module|c|
|7|NU|Not Used||
|8|LOS|Loss of Signal – high indicates loss of signal|d|
|9|VEER|Receiver Ground|a|
|10|VEER|Receiver Ground|a|
|11|VEER|Receiver Ground|a|
|12|RD–|Inverse Received Data Out|e|
|13|RD+|Received Data Out|e|
|14|VEER|Receiver Ground|a|
|15|VCCR|Receiver Power 3.3V||
|16|VCCT|Transmitter Power 3.3V||
|17|VEET|Transmitter Ground|a|
|18|TD+|Transmitter Data In|f|
|19|TD–|Inverse Transmitter Data In|f|
|20|VEET|Transmitter Ground|a|



- a. Transmitter and Receiver grounds are connected in the transceiver PCB. 

- b. Pulled to <0.8V during transceiver operation. 

c. Mod-Def 0, 1, 2 are the module definition pins. They should be pulled up with a 4.7-kW to 10-kW resistor on the host board to a supply less than VCCT + 0.3V or VCCR + 0.3V. In order to use this interface, supply 3.3V to VCCT. 

Mod-Def 0 is grounded by the module to indicate that the module is present. Mod-Def 1 is the clock line of the two-wire serial interface. 

Mod-Def 2 is the data line of the two-wire serial interface. 

- d. LOS (Loss Of Signal) is an open collector/drain output that should be pulled up externally with a 4.7-kW to 10-kW resistor on the host board to a supply less than VCCT,R +0.3V. When high, this output indicates that the received optical power is below the worst case receiver sensitivity (as defined by the standard in use). In the low state, the output will be pulled to a voltage less than 0.8V. LOS only valid if VCCT and VCCR are powered. 

- e. RD±: These are the differential receiver outputs. They are AC-coupled to 100W differential lines which should be terminated with 100W differential at the SERDES. AC-coupling is present inside the module and is not required on the host board. 

- f. TD±: These are the differential transmitter inputs. They are AC-coupled differential lines with 100W differential termination inside the module. AC-coupling is present inside the module and is not required on the host board. 

Broadcom - 6 - 

Data Sheet 

AFBR-57E6APZC 

## **Package Dimensions** 

## **Figure 5  Module Drawing** 


**----- Start of picture text -----**<br>
COMPONENT LABEL YYWW<br>Country of Origin<br>13.8±0.1 13.4±0.1<br>[0.541±0.004] [0.528±0.004]<br>2.60<br>[0.10] 55.2±0.2<br>[2.17±0.01]<br>6.25±0.05 FRONT EDGE OF SFP 0.7MAX. UNCOMPRESSED<br>[0.246±0.002] TRANSCEIVER CAGE [0.028]<br>13.0±0.2 8.5±0.1<br>[0.512±0.008] [0.335±0.004]<br>TX RX<br>AREA FOR PROCESS PLUG<br>6.6<br>[0.261]<br>13.50<br>[0.53]<br>14.8MAX. UNCOMPRESSED<br>[0.583]<br>Tcase Reference Point<br>DEVICE SHOWN WITH DUST CAP<br>AND BAIL WIRE DELATCH<br>DIMENSIONS ARE IN MILLIMETERS [INCHES]<br>**----- End of picture text -----**<br>


Broadcom - 7 - 

Data Sheet 

AFBR-57E6APZC 

## **Figure 6  SFP Host Board Mechanical Layout** 


**----- Start of picture text -----**<br>
X<br>Y<br>34.5<br>10<br>3x<br>10x  ø 1.05 ± 0.01 7.2 7.1<br>16.25 ø 0.1 L X A S 2.5 ø 0.85 ± 0.05<br>MIN. PITCH 1 2.5 ø 0.1 S X Y<br>PCB B A 1<br>EDGE 3.68<br>5.68 PIN 1 20<br>8.58 2x 1.7 8.48<br>11.08 11.93<br>16.25 9.6<br>REF . [14.25]<br>4.8<br>11<br>10<br>SEE DET AIL 1<br>2.0 9x 0.95 ± 0.05<br>11x 11x 2.0 ø 0.1    L X A S<br>26.8 5 2<br>3 10<br>3x<br>41.3<br>42.3<br>5<br>3.2<br>20x 0.5 ± 0.03<br>0.9<br>0.06    L A S B S<br>PIN 1 20 LEGEND<br>10.93 10.53 11.93 1. PADS AND VIAS ARE CHASSIS GROUND<br>9.6<br>0.8<br>TYP. 2. THR OUGH HOLES, PLATING OPTIONAL<br>11<br>10 3. HATCHED AREA DENOTES COMPONENT<br>AND TRACE KEEPOUT (EXCEPT<br>CHASSIS GROUND)<br>4 4. AREA DENOTES COMPONENT<br>2 ±  0.005 TYP.  KEEPOUT (TRACES ALLOWED)<br>2x 1.55 ± 0.05<br>0.06    L A S B S<br>ø 0.1    L A S B S DETAIL 1 DIMENSIONS ARE IN MILLIMETERS<br>**----- End of picture text -----**<br>


Broadcom - 8 - 

Data Sheet 

AFBR-57E6APZC 

## **Figure 7  PCB Contact Pad Area** 


**----- Start of picture text -----**<br>
This area is not coated<br>on both sides<br>4<br>9.2<br>**----- End of picture text -----**<br>


**NOTE** Note that the pad area shown in Figure 7 is not coated. This needs to be considered in the application. 

Broadcom - 9 - 

Data Sheet 

AFBR-57E6APZC 

## **Figure 8  SFP Assembly Drawing** 


**----- Start of picture text -----**<br>
1.7±0.9<br>[.07±.04]<br>3.5±0.3<br>[.14±.01]<br>41.73±0.5<br>PCB<br>[1.64±.02]<br>BEZEL AREA<br>FOR<br>PROCESS<br>PLUG<br>15MAX<br>[.59]<br>Tcase REFERENCE POINT<br>CAGE<br>ASSEMBLY<br>15.25±0.1<br>[.60±0.004] 10.4±0.1<br>12.4REF [.41±0.004]<br>[.49]<br>10REF<br>9.8MAX 1.15REF<br>[.39]<br>[.39] [.05] 16.25±0.1MIN PITCH<br>TO PCB<br>BELOW PCB [.64±0.004]<br>0.4±0.1<br>[.02±0.004]<br>BELOW PCB<br>MSA-SPECIFIED BEZEL<br>**----- End of picture text -----**<br>


DIMENSIONS ARE IN MILLIMETERS [INCHES]. 

Broadcom - 10 - 

Data Sheet 

AFBR-57E6APZC 

## **Absolute Maximum Ratings** 

Stresses in excess of the absolute maximum ratings can cause catastrophic damage to the device. Limits apply to each parameter in isolation, all other parameters having values within the recommended operation conditions. It should not be assumed that limiting values of more than one parameter can be applied to the products at the same time. Exposure to the absolute maximum ratings for extended periods can adversely affect device reliability. 

**Table 3  Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|–40|+100|°C||
|Supply Voltage|VCC|–0.5|3.63|V||
|Data Input Voltage|VI|–0.5|Vcc|V||
|Receiver Optical Input Power|Pin|—|0|dBm||



## **Recommended Operating Conditions** 

All the data in this specification refers to the operating conditions above and over lifetime unless otherwise stated. 

**Table 4  Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|TC|–40|—|+85|°C|a, b|
|Supply Voltage|VCC|3.0|3.3|3.6|V||
|Data Output Load|RL|—|100|—|Ω|Differential|
|Signalling rate (Fast Ethernet)|B|—|125|—|MBd|c|



a. The case temperature is measured at the surface of the topside (see Figure 5, Module Drawing) using a thermocouple connected to the housing. 

b. Electrical and optical specifications of the product are guaranteed across recommended case operating temperature only. 

c. 4B/5B. Ethernet auto-negotiation pulses are not supported. 

## **Transmitter Electrical Characteristics** 

**Table 5  Transmitter Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|45|70|mA|a|
|Power Dissipation|PDISS|—|150|260|mW||
|Differential input voltage|VDIFF|0.5|1.0|1.8|V|b|
|Input Differential Impedance|Rin|—|100|—|Ω|c|
|Transmitter Disable (TX Disable) High|VIH|2.0|—|Vcc|V||
|Transmitter Disable (TX Disable) Low|VIL|0|—|0.8|V||



a. Typical values are for room temperature at 3.3V. 

b. Peak to Peak. 

c. Tx data inputs are AC coupled. 

Broadcom - 11 - 

Data Sheet 

AFBR-57E6APZC 

## **Receiver Electrical Characteristics** 

**Table 6  Receiver Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|31|40|mA|a|
|Power Dissipation|PDISS|—|105|145|mW||
|Data Output: Receiver Differential||—|—|—|||
|Output Voltage (RD±)||VOH– VOL||1.0|—|1.8|V|b, c|
|Data Output Rise Time (10% to 90%)|tr|—|—|2.2|ns||
|Data Output Fall Time (10% to 90%)|tf|—|—|2.2|ns||
|Loss of Signal Output Voltage – Low|LOSVOL|—|—|0.8|V||
|Loss of Signal Output Voltage – High|LOSVOH|2.0|—|—|V||



- a. Typical values are for room temperature at 3.3V. 

- b. Differential output voltage is internally AC-coupled. The low and high voltages are measured using 100Ω differential termination. 

- c. RD+ and RD– outputs are squelched at LOS assert levels. 

## **Transmitter Optical Characteristics** 

**Table 7  Transmitter Optical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Output Optical Power<br>62.5/125 μm NA = 0.275 Fiber|Po|–20.0|–17.0|–14.0|dBm|a, b|
|Output Optical Power<br>50/125 μm NA = 0.20 Fiber|Po|–24.0|–21.0|–17.0|dBm|a, b|
|Extinction Ratio|ER|10|—|—|dB||
|Central Wavelength|λC|1270|1308|1380|nm||
|Spectral width – FWHM|Δλ|—|147|—|nm||
|Optical Rise Time (10% to 90%)|tr|0.6|1.0|3.0|ns|c|
|Optical Fall Time (10% to 90%)|tf|0.6|1.0|3.0|ns|c|
|Duty Cycle Distortion<br>Contributed by the Transmitter|DCD|—|—|0.6|ns|d, e|
|Data Dependent Jitter<br>Contributed by the Transmitter|DDJ|—|—|0.6|ns|d|
|Random Jitter<br>Contributed by the Transmitter|RJ|—|—|0.69|ns|d, f|
|Transmitter Disable (High)|Po(off)|—|—|–45|dBm||



a. Optical values are measured over the specified operating voltage and temperature ranges. The average power can be converted to a peak value by adding 3 dB. 

- b. Average 

- c. Measured with a 400-MHz optical to electrical converter. 

- d. Characterized with 125 MBd, PRBS2[7] – 1 pattern. 

- e. Duty Cycle Distortion contributed by the transmitter is measured at 50% threshold of the optical signal. 

- f. Peak to peak. 

Broadcom - 12 - 

Data Sheet 

AFBR-57E6APZC 

## **Receiver Optical and Electrical Characteristics** 

## **Table 8  Receiver Optical and Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power|PIN|–31.0|—|–12.0|dBm|a, b|
|Operating Wavelength|λR|1270|—|1380|nm||
|Duty Cycle Distortion<br>Contributed by the Receiver|DCD|—|—|0.4|ns|c, d|
|Data Dependent Jitter<br>Contributed by the Receiver|DDJ|—|—|1.0|ns|d|
|Random Jitter<br>Contributed by the Receiver|RJ|—|—|2.14|ns|d, e|
|Loss of Signal – Deasserted|PD|—|—|–32.0|dBm|b|
|Loss of Signal – Asserted|PA|–45|—|—|dBm|b|
|Loss of Signal – Hysteresis|PA– PD|0.5|1.6|—|dB||



- a. This specification is intended to indicate the performance of the receiver section of the transceiver when Optical Input Power signal characteristics are present per the following definitions: 

   - Over the specified operating temperature and voltage ranges. 

   - Bit Error Rate (BER) is better than or equal to 1 × 10[–10] . 

   - Transmitter is operating to simulate any crosstalk present between the transmitter and receiver sections of the transceiver. 

— Fiber: 62.5/125 _m, NA = 0.275; or 50/125 _m, NA = 0.20. 

- b. Average. 

- c. Duty Cycle Distortion contributed by the receiver is measured at 50% threshold of the electrical signal. 

d. Characterized with 125 MBd, PRBS2[7] – 1 pattern. 

- e. Peak to peak. 

Broadcom - 13 - 

Data Sheet 

AFBR-57E6APZC 

## **Transceiver Diagnostics Timing Characteristics** 

**Table 9  Transceiver Diagnostics Timing Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|**Figure**|**Notes**|
|---|---|---|---|---|---|---|
|Hardware TXDIS Assert Time|t_off|—|10|μs|Figure 9|a|
|Hardware TXDIS Deassert Time|t_on|—|30|μs|Figure 9|b|
|Time to Initialize|t_init|—|300|ms|Figure 9|c|
|Hardware LOS Assert Time|t_loss_on|—|100|μs||d|
|Hardware LOS Deassert Time|t_loss_off|—|350|μs||e|
|Software TX_DISABLE Assert Time|t_off_soft|—|100|ms||f|
|Software TX_DISABLE Deassert Time|t_on_soft|—|100|ms||g|
|Software RX_LOS Assert Time|t_loss_on_soft|—|100|ms||h|
|Software RX_LOS Deassert Time|t_loss_off_soft|—|100|ms||i|
|Analog parameter Data Ready|t_data|—|1000|ms||j|
|Serial Hardware Ready|t_serial|—|300|ms||k|
|Write Cycle Time|t_write|—|10|ms||l|
|Serial ID Clock Rate|f_serial_clock|—|400|kHz|||



- a. Time from rising edge of TXDIS to when the optical output falls below 10% of nominal. 

- b. Time from falling edge of TXDIS to when the modulated optical output rises above 90% of nominal. 

- c. Time from Power on or falling edge of TXDIS to when the modulated optical output rises above 90% of nominal. 

- d. Time from loss of optical signal to LOS assertion. 

- e. Time from valid optical signal to LOS deassertion. 

- f. Time from two-wire interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

- g. Time from two-wire interface deassertion of TX_DISABLE (A2h, byte 110, bit 6) to when the modulated optical output rises above 90% of nominal. 

- h. Time for two-wire interface assertion of Rx_LOS (A2h, byte 110, bit 1) from loss of optical signal. 

- i. Time for two-wire interface deassertion of Rx_LOS (A2h, byte 110, bit 1) from presence of valid optical signal. 

- j. From power on to data ready bit asserted (A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. 

- k. Time from power on until module is ready for data transmission over the serial bus (reads or writes over A0h and A2h). 

- l. Time from stop bit to completion of a 1-8 byte write command. 

Broadcom - 14 - 

Data Sheet 

AFBR-57E6APZC 

## **Figure 9  Timing Diagram** 


**----- Start of picture text -----**<br>
TX, RX Vcc > 2.97V TX, RX Vcc > 2.97V<br>TXDIS TXDIS<br>TRANSMITTER SIGNAL TRANSMITTER SIGNAL<br>t_init t_init<br>t_init: TXDIS NEGATED t_init: TXDIS ASSERTED<br>OCCURRENCE<br>OPTICAL SIGNAL OF LOSS TXDIS<br>LOSS OF SIGNAL TRANSMITTED SIGNAL<br>t_loss_on t_loss_off t_off t_on<br>t_loss_on & t_loss_off t_off & t_on: TXDIS ASSERTED THEN NEGATED<br>**----- End of picture text -----**<br>


## **Transceiver Digital Diagnostic Monitor (Read Time Sense) Characteristics** 

**Table 10  Transceiver Digital Diagnostic Monitor (Read Time Sense) Characteristics** 

|**Parameter**|**Symbol**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal<br>Temperature Accuracy|TINT|±3.0|°C|Registers indicate case temperature which is derived from the<br>internally measured temperature. Valid from –40°C to +85°C<br>case temperature with Tx Enabled.|
|Transceiver Internal Supply<br>Voltage Accuracy|VINT|±0.1|V|Supply voltage is measured internal to the transceiver and<br>can, with less accuracy, be correlated to voltage at the SFP<br>VCC pin. Valid over 3.3V ±10%.|
|Transmitter LED DC Bias Current<br>Accuracy|IBIAS|±10|%|IBIAS is better than ±10% nominal value.|
|Transmitter Average Optical<br>Power Accuracy|PT|±3.0|dB|Transmitter power is inferred from the LED bias current.|
|Received Average Optical<br>Input Power Accuracy|PR|±3.0|dB|Coupled from a 62.5/125-μm fiber.|



Broadcom - 15 - 

Data Sheet 

AFBR-57E6APZC 

## **EEPROM Serial ID Memory Contents – Address A0h** 

**Table 11  EEPROM Serial ID Memory Contents – Address A0h** 

|**Byte #**<br>**Decimal**|**Hex**|**ASCII**|**Description**|**Byte #**<br>**Decimal**|**Hex**|**ASCII**|**Description**|
|---|---|---|---|---|---|---|---|
|0|03||SFP transceiver|38|17|||
|1|04|||39|6A|||
|2|07||LC connector|40|41|A||
|3|00|||41|46|F||
|4|00|||42|42|B||
|5|00|||43|52|R||
|6|20||100Base-FX compliance|44|2D|–||
|7|00|||45|35|5||
|8|00|||46|37|7||
|9|00|||47|45|E||
|10|00|||48|36|6||
|11|02||4B/5B Encoding|49|41|A||
|12|01||100 Mbits/s|50|50|P||
|13|00|||51|5A|Z||
|14|00|||52|43|C||
|15|00|||53|20|||
|16|C8|||54|20|||
|17|C8|||55|20|||
|18|00|||56|20|||
|19|00|||57|20|||
|20|41|A||58|20|||
|21|56|V||59|20|||
|22|41|A||60|05||Notea|
|23|47|G||61|1E||Notea|
|24|4F|O||62|00|||
|25|20|||63|||Noteb|
|26|20|||64|00|||
|27|20|||65|12||TX Disable and LOS<br>implemented.|
|28|20|||66|00|||
|29|20|||67|00|||
|30|20|||68 to 83|||Notec|
|31|20|||84 to 91|||Noted|
|32|20|||92|68||Digital diagnostics<br>implemented.<br>Internally calibrated.<br>Average RX power.|



Broadcom - 16 - 

Data Sheet 

AFBR-57E6APZC 

## **Table 11  EEPROM Serial ID Memory Contents – Address A0h (Continued)** 

|**Byte #**<br>**Decimal**|**Hex**|**ASCII**|**Description**|**Byte #**<br>**Decimal**|**Hex**|**ASCII**|**Description**|
|---|---|---|---|---|---|---|---|
|33|20|||93|D0||Alarm warnings,<br>SoftTX_Disable and Soft<br>RX_LOS implemented.|
|34|20|||94|06||Includes functionality<br>described in Rev 11.3 of<br>SFF-8472.|
|35|20|||95|||Noteb|
|36|00|||96–27|00||Notee|
|37|00|||||||



a. LED wavelength is represented in 16 unsigned bits. The hex representation of 1310 (nm) is 0x051E. 

b. Address 63 is the checksum for bytes 0–62 and address 95 is the checksum for bytes 64–94. They are calculated (per SFF-8472) and stored prior to product shipment. 

c. Addresses 68–83 specify a unique module serial number. 

d. Addresses 84–91 specify the date code. 

- e. Addresses 96–127 are vendor specific. 

Broadcom - 17 - 

Data Sheet 

AFBR-57E6APZC 

## **EEPROM Serial ID Memory Contents – Enhanced Features (Address A2h)** 

**Table 12  EEPROM Serial ID Memory Contents – Enhanced Features (Address A2h)** 

|**Byte #**<br>**Decimal**|**Notes**|**Byte #**<br>**Decimal**|**Notes**|**Byte #**<br>**Decimal**|**Notes**|
|---|---|---|---|---|---|
|0|Temp H Alarm MSBa|26|Tx Power L Alarm MSBg|104|Real Time Rx Power MSBb|
|1|Temp H Alarm LSBa|27|Tx Power L Alarm LSBg|105|Real Time Rx Power LSBb|
|2|Temp L Alarm MSBa|28|Tx Power H Warning MSBg|106|Reserved|
|3|Temp L Alarm LSBa|29|Tx Power H Warning LSBg|107|Reserved|
|4|Temp H Warning MSBa|30|Tx Power L Warning MSBg|108|Reserved|
|5|Temp H Warning LSBa|31|Tx Power L Warning LSBg|109|Reserved|
|6|Temp L Warning MSBa|32|Rx Power H Alarm MSBb|110|Status/Control – SeeTable 13|
|7|Temp L Warning LSBa|33|Rx Power H Alarm LSBb|111|Reserved|
|8|Vcc H Alarm MSBc|34|Rx Power L Alarm MSBb|112|Flag Bits – SeeTable 14|
|9|Vcc H Alarm LSBc|35|Rx Power L Alarm LSBb|113|Flag Bits – SeeTable 14|
|10|Vcc L Alarm MSBc|36|Rx Power H Warning MSBb|114|Reserved|
|11|Vcc L Alarm LSBc|37|Rx Power H Warning LSBb|115|Reserved|
|12|Vcc H Warning MSBc|38|Rx Power L Warning MSBb|116|Flag Bits – SeeTable 14|
|13|Vcc H Warning LSBc|39|Rx Power L Warning LSBb|117|Flag Bits – SeeTable 14|
|14|Vcc L Warning MSBc|40–55|Reserved|118–127|Reserved|
|15|Vcc L Warning LSBc|56–94|External Calibration Constantsd|128–247|Customer Writable|
|16|Tx Bias H Alarm MSBe|95|Checksum for Bytes 0–94f|248–255|Vendor Specific|
|17|Tx Bias H Alarm LSBe|96|Real Time Temperature MSBa|||
|18|Tx Bias L Alarm MSBe|97|Real Time Temperature LSBa|||
|19|Tx Bias L Alarm LSBe|98|Real Time Vcc MSBc|||
|20|Tx Bias H Warning MSBe|99|Real Time Vcc LSBc|||
|21|Tx Bias H Warning LSBe|100|Real Time Tx Bias MSBe|||
|22|Tx Bias L Warning MSBe|101|Real Time Tx Bias LSBe|||
|23|Tx Bias L Warning LSBe|102|Real Time Tx Power MSBg|||
|24|Tx Power H Alarm MSBg|103|Real Time Tx Power LSBg|||
|25|Tx Power H Alarm LSBg|||||



- a. Temperature (Temp) is decoded as a 16-bit signed two’s complement integer in increments of 1/256°C. 

- b. Received average optical power (Rx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 μW. 

- c. Supply Voltage (Vcc) is decoded as a 16-bit unsigned integer in increments of 100 μV. 

- d. Bytes 56–94 are not intended for use with AFBR-57E6APZC, but have been set to default values per SFF-8472. 

- e. Tx bias current (Tx Bias) is decoded as a 16-bit unsigned integer in increments of 2 μA. 

- f. Byte 95 is a checksum calculated (per SFF-8472) and stored prior to product shipment. 

- g. Transmitted average optical power (Tx Pwr) is decoded as a 16 bit unsigned integer in increments of 0.1 μW. 

Broadcom - 18 - 

Data Sheet 

AFBR-57E6APZC 

## **EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

**Table 13  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

|**Bit #**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7|TX_DISABLE State|Digital state of Soft TX_DISABLE||
|6|Soft TX_DISABLE|Read/write bit for changing digital state of TX_DISABLE function.||
|5|Reserved|||
|4|Reserved|||
|3|Reserved|||
|2|Reserved|||
|1|RX_LOS State|Digital state of SFP RX_LOS Output Pin (1 = RX_LOS asserted)||
|0|Data Ready (Bar)|Indicates transceiver is powered and real time sense data is ready (0 = ready).||



## **EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

**Table 14  EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

|**Byte**|**Bit**|**Flag Bit Name**|**Description**|
|---|---|---|---|
|112|7|Temp High Alarm|Set when transceiver internal temperature exceeds high alarm threshold.|
||6|Temp Low Alarm|Set when transceiver internal temperature exceeds low alarm threshold.|
||5|Vcc High Alarm|Set when transceiver internal supply voltage exceeds high alarm threshold.|
||4|Vcc Low Alarm|Set when transceiver internal supply voltage exceeds low alarm threshold.|
||3|Tx Bias High Alarm|Set when transceiver LED bias exceeds high alarm threshold.|
||2|Tx Bias Low Alarm|Set when transceiver LED bias exceeds low alarm threshold.|
||1|Tx Power High Alarm|Set when transmitted average optical power exceeds high alarm threshold.|
||0|Tx Power Low Alarm|Set when transmitted average optical power exceeds low alarm threshold.|
|113|7|Rx Power High Alarm|Set when received average optical power exceeds high alarm threshold.|
||6|Rx Power Low Alarm|Set when received average optical power exceeds low alarm threshold.|
||0–5|Reserved||
|116|7|Temp High Warning|Set when transceiver case temperature exceeds high warning threshold.|
||6|Temp Low Warning|Set when transceiver case temperature exceeds low warning threshold.|
||5|Vcc High Warning|Set when transceiver internal supply voltage exceeds high warning threshold.|
||4|Vcc Low Warning|Set when transceiver internal supply voltage exceeds low warning threshold.|
||3|Tx Bias High Warning|Set when transceiver LED bias exceeds high warning threshold.|
||2|Tx Bias Low Warning|Set when transceiver LED bias exceeds low warning threshold.|
||1|Tx Power High Warning|Set when transmitted average optical power exceeds high warning threshold.|
||0|Tx Power Low Warning|Set when transmitted average optical power exceeds low warning threshold.|
|117|7|Rx Power High Warning|Set when received average optical power exceeds high warning threshold.|
||6|Rx Power Low Warning|Set when received average optical power exceeds low warning threshold.|
||0–5|Reserved||



Broadcom - 19 - 

Data Sheet 

AFBR-57E6APZC 

## **Settings of Alarm and Warning Thresholds** 

**Table 15  Settings of Alarm and Warning Thresholds** 

||**Tx Power (dBm)**|**Rx Power (dBm)**|**Transceiver**<br>**Temperature (°C)**|**Supply Voltage (V)**|**Tx Bias Current (mA)**|
|---|---|---|---|---|---|
|High Alarm|–11|–11|85|3.6|120|
|Low Alarm|–23|–33|–40|3|10|
|High Warning|–12|–12|80|3.5|110|
|Low Warning|–22|–32|–35|3.1|15|



Broadcom - 20 - 

For product information and a complete list of distributors, please go to our web site: www.broadcom.com. 

Broadcom, the pulse logo, Connecting everything, Avago Technologies, Avago, and the A logo are among the trademarks of Broadcom in the United States, certain other countries and/or the EU. 

Copyright © 2016-2017 Broadcom. All Rights Reserved. 

The term "Broadcom" refers to Broadcom Limited and/or its subsidiaries. For more information, please visit www.broadcom.com. 



Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. 

Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

pub-005500 – March 30, 2017 

