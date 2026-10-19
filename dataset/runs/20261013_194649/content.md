## **Data Sheet** 

## **AFBR-59E5APZ-HT** 

## **Multimode SFF Transceiver with LC Connector for Fast Ethernet** 


## **Description** 

The Broadcom[®] AFBR-59E5APZ-HT is a small form factor transceiver (SFF) with ultra-low power consumption that gives the system designer a product to implement a range of solutions for multimode fiber communication links. 

This transceiver is supplied in the industry-standard 2 × 5 DIP style with a LC fiber connector interface. 

## **Features** 

- SFF package 

- LC duplex connector optical interface 

- Operates with 50/125-µm and 62.5/125-µm multimode fiber 

- Compatible with the 100BASE-FX version of IEEE 802.3u 

- Single +3.3V power supply 

- Data input and output are AC-coupled 

## **Transmitter** 

- Signal Detect Output and TX-Disable feature 

- Squelched receiver outputs 

The transmitter contains a 1310-nm high-reliable LED. This LED is packaged in the optical subassembly of the transmitter. It is driven by an integrated circuit that converts differential LVPECL logic signals into an analog LED drive current. 

LVPECL inputs. 

- Compatible with wave solder and aqueous wash processes 

- Operating temperature range: –40°C to 95°C 

- Manufactured in an ISO 9001 certified facility 

- RoHS compliant 

- Lead free 

## **Applications** 

## **Receiver** 

The receiver uses a PIN photodiode that is integrated with a transimpedance pre- and post-amplifier in a single IC. This IC is packaged in the optical subassembly of the receiver. The data output is differential LVPECL. Rx squelch is activated at the deassert level of signal detect. 

- Factory automation 

- Merging unit 

- Substation automation 

- HVDC systems 

AFBR-59E5APZ-HT-DS101 July 12, 2024 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Module Package** 

The pinout and package outline, shown in Figure 1 and Figure 3, are compliant with the multisource definition of the 2 × 5 DIP. The low profile of the Broadcom transceiver design complies with the maximum height allowed for the LC connector over the entire length of the package. 

The optical subassemblies use a high-volume assembly process together with low-cost lens elements, which results in a cost-effective building block with high immunity to external EMI fields. 

The electrical subassembly consists of a high-volume multilayer printed circuit board on which the TX-IC, the optical subassemblies, and various surface-mounted passive circuit elements are attached. 

The outer metal cover is soldered to the PCB’s TX and RX signal ground. The LC port section with solder posts is attached to the PCB by non-conductive epoxy and is isolated to the metal cover. This provides mechanical strength and full isolation from the internal circuit of the transceiver. 

The transceiver has ten signal pins, two solder posts, and four housing leads. The solder posts provide the primary mechanical strength to withstand the loads imposed on the transceiver by mating with the LC connector fiber cables. 

## **Pin Descriptions** 

## **Pin 1 Receiver Signal Ground VEE RX:** 

Directly connect this pin to the receiver ground plane. 

## **Pin 2 Receiver Power Supply VCC RX:** 

Provide +3.3V DC via the recommended receiver power supply (Figure 2). Locate the power supply filter circuit as close as possible to the VCC RX pin. 

## **Pin 3 Signal Detect SD:** 

The TX-IC analyses the light input power level information of the RX-IC via the “Imon” signal and provides the corresponding SD output levels. To ensure SD functionality, a supply voltage within the recommended range must be applied to the RX-IC and to the TX-IC. 

Typical optical input levels (average) to the receiver result in a logic “1” output. 

Low optical input levels (average) to the receiver result in a logic “0” output. 

## **Pin 4 Receiver Data Out Bar RD-:** 

Rx signal AC-coupled LVPECL. See Figure 2. 

## **Pin 5 Receiver Data Out RD+:** 

Rx signal AC-coupled LVPECL. See Figure 2. 

## **Pin 6 Transmitter Power Supply VCC TX:** 

Provide +3.3V DC via the recommended transmitter power supply (Figure 2). Locate the power supply filter circuit as close as possible to the VCC TX pin. 

## **Pin 7 Transmitter Signal Ground VEE TX:** 

## **Figure 1:  Pinout Diagram** 

Directly connect this pin to the transmitter ground plane. 

## **Pin 8 Transmitter Disable:** 


**----- Start of picture text -----**<br>
RX TX<br>Mounting Studs /<br>Solder Posts<br>Housing Leads<br>Top View<br>Receiver Signal Ground 1 10 Transmitter Data In Bar<br>Receiver Power Supply 2 9 Transmitter Data In<br>Signal Detect 3 8 Transmitter Disable<br>Receiver Data Out Bar 4 7 Transmitter Signal Ground<br>Receiver Data Out 5 6 Transmitter Power Supply<br>**----- End of picture text -----**<br>


The transmitter is disabled when connected to HIGH. 

The transmitter is enabled when connected to GND or left OPEN. 

## **Pin 9 Transmitter Data In TD+:** 

Tx signal AC-coupled LVPECL. See Figure 2. 

## **Pin 10 Transmitter Data In Bar TD-:** 

Tx signal AC-coupled LVPECL. See Figure 2. 

## **Mounting Studs/Solder Posts:** 

The mounting studs are provided for transceiver mechanical attachment to the circuit board. It is recommended to connect them to chassis ground. 

## **Housing Leads:** 

The housing leads are provided for additional signal grounding. The holes in the circuit board must be tied to signal ground. 

AFBR-59E5APZ-HT-DS101 2 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

The following information provides answers to the most common questions about using the part. 

## **Transceiver Optical Power Budget versus Link Length** 

The Optical Power Budget (OPB) is the available optical power for a fiber optic link to accommodate fiber cable losses plus losses due to inline connectors, splices, and optical switches and to provide margin for link aging and unplanned losses due to cable plant reconfiguration or repair. 

The 1310-nm Broadcom LEDs show very stable performance in long-time tests, typically less than 1 dB of aging effect over normal commercial equipment life periods. Contact your Broadcom sales representative for additional details. 

## **Handling and Precautions** 

It is recommended that typical industrial precautions be taken in handling and assembling these transceivers to prevent damage that might be induced by electrostatic discharge (ESD). 

The AFBR-59E5APZ-HT passed the Electrostatic Discharge to all Electrical Pins by the human-body model (HBM) according to JS-001-2017 with U = ± 2000V. 

Care should be taken to avoid shorting the receiver output pins to ground without proper current-limiting impedance. 

## **Solder and Wash Process Compatibility** 

## **Board Layout – Decoupling Circuit, Ground Planes, and Termination Circuits** 

To achieve optimum performance, take care in the layout of your circuit board. Figure 2 provides a schematic for the recommended termination circuit that works well with these parts. 

It is further recommended that a continuous ground plane be provided in the circuit board directly under the transceiver to provide a low-inductance ground for the signal return current. This recommendation is in keeping with good high-frequency board layout practices. 

## **Board Layout – Hole Pattern** 

The Broadcom transceiver complies with the circuit board Common Transceiver Footprint hole pattern defined in the original multisource announcement that defined the 2 × 5 package style. Figure 4 reproduces this drawing with the addition of ANSI Y14.5M compliant dimensioning to be used as a guide in the mechanical layout of your circuit board. It illustrates the recommended panel opening and the position of the circuit board with respect to this panel. 

## **Label** 

The label is attached to the outer metal cover (illustrated in Figure 3) and provides information about the product number, the country of origin, a barcode, and the serial number (XXXXXYYWW; X = numeric counter, YY = production year, WW = production week). 

These transceivers are compatible with industry-standard wave or hand solder processes. 

Protective process plugs are inserted in the LC receptacles of the transceivers during shipping. These process plugs act as a dust cover during shipping, but also protect the optical subassemblies during the wave solder and aqueous wash processing. 

**NOTE:** Hand soldering is a process that is difficult to control and reproduce. Hand soldering may cause overstresses to the product that can affect product performance and reliability. 

AFBR-59E5APZ-HT-DS101 3 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Electrostatic Discharge (ESD)** 

The transceivers are packed in trays and shipped inside moisture barrier bags (MBBs) to keep the devices protected against humidity and to provide protection from mechanical and ESD damage during shipment and storage. 

There are two main cases in which immunity to ESD damage is important. 

The first case is when the transceiver is handled before it is mounted on the circuit board. 

## **Electromagnetic Immunity and Emission** 

Equipment that uses these transceivers will be subject to radio-frequency electromagnetic fields in some environments. These transceivers have a high immunity to such fields. 

For additional information regarding EMI, ESD, and conducted noise testing procedures and results, refer to _Application Note 1166, Minimizing Radiated Emissions of High-Speed Data Communications Systems_ . 

**NOTE:** Use typical industrial precautions for ESDsensitive devices. These precautions include using grounded wrist straps, work benches, floor mats in ESD-controlled areas, and so on. 

An ESD event may damage or degrade the device performance. Typical standards, such as DIN 61340-5-1, must be considered. 

The second case to consider is static discharges to the exterior of the equipment chassis that contains the transceiver parts. 

To the extent that the LC connector is exposed to the outside of the equipment chassis, it might be subject to whatever ESD system-level test criteria that the equipment is intended to meet. 

AFBR-59E5APZ-HT-DS101 4 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Regulatory Compliance Table** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to the<br>Electrical Pins|HBM: ANSI/ESDA/JEDEC - JS-001-2017|Withstand ± 2000V pulses, applied according<br>the human-body model (HBM).|
|Electrostatic Discharge (ESD) to the LC<br>Receptacle|EN/IEC 61000-6-2<br>(Base standard: EN 61000-4-2)|Typically withstand a 9-kV shot without<br>damage when the LC connector receptacle is<br>contacted by an ESD simulator with a<br>discharge network (150 pF / 330Ω).<br>Typically withstand a 15-kV air discharge<br>shot on the LC connector receptacle.|
|Electromagnetic Interference Immunity|EN/IEC 61000-6-2:2019<br>(Base standard: EN 61000-4-2)|Typically show no bit errors while a 10V/m<br>field swept from 80 MHz to 1 GHz is applied,<br>while the transceiver is mounted to a test<br>PCB without a chassis enclosure.|
|Electromagnetic Emission|EN55032:2015, CISPR32:2015<br>(Base standard: EN 55016-2-3)|Typically show a high margin to the emission<br>limits at a test range from 30 MHz to 1 GHz,<br>while the transceiver is mounted to a test<br>PCB without a chassis enclosure.|
|Eye Safety|EN IEC 62368-1, EN 60825-1, EN 60825-2|Compliant with Laser Class 1.<br>TÜV Certification: R 50486881|
|Component Recognition|Underwriters Laboratories and Canadian<br>Standards Association Joint Component<br>Recognition for Information Technology<br>Equipment including Electrical Business<br>Equipment|Compliant.<br>UL File #: E173874|
|RoHS|RoHS Directive|Compliant to RoHS Directive 2011/65EU<br>Annex II.|



For further information, contact your Broadcom sales representative. 

AFBR-59E5APZ-HT-DS101 5 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Figure 2: Recommended Application Circuit** 


**----- Start of picture text -----**<br>
3V3<br>1μH<br>Protocol IC &  Tx Vcc AFBR-59E5APZ-HT<br>SerDes<br>10μF 0.1μF 10μF* 0.1μF<br>Tx dis<br>Tx disable<br>0.1μF<br>50� Tx data +<br>Tx data +<br>TX-IC<br>Tx data - 50� Tx data - LED Driver<br>0.1μF<br>SD  SD Imon<br>10k� 1μH Rx Vcc<br>3V3<br>10μF 0.1μF<br>0.1μF<br>Rx data +<br>50� Rx data + RX-IC<br>��������<br>50� Rx data -<br>&<br>Rx data - Quan�zer<br>0.1μF<br>~7.5k�<br>100�<br>2.7k� 2.7k�<br>100�<br>4.3k� 4.3k�<br>**----- End of picture text -----**<br>


- Optional capacitance (tantalum capacitor) is recommended. 

## **NOTES:** 

1. Refer to the SerDes supplier’s recommendation regarding the interface between the AFBR-59E5APZ-HT and the SerDes. The proposed termination is a general recommendation for AC-coupled LVPECL signals. Other terminations may apply depending on the SerDes interface. 

2. Inductors should have less than a 1Ω series resistor per MSA. 

3. Tx disable has an internal pull-down resistor. 

4. For the Signal Detect SD, termination by a single 10-kΩ pull-down resistor is recommended. The use of another termination (such as a Thevenin equivalent LVPECL) increases power consumption and must be verified for each application. 

AFBR-59E5APZ-HT-DS101 6 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Absolute Maximum Ratings** 

Stresses in excess of the absolute maximum ratings can cause catastrophic damage to the device. Limits apply to each parameter in isolation, all other parameters having values within the recommended operating conditions. It should not be assumed that limiting values of more than one parameter can be applied to the product at the same time. Exposure to the absolute maximum ratings for extended periods can adversely affect device reliability. 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|–40|+100|°C|—|
|Lead Soldering Temperature|Tsold|—|260|°C|a|
|Lead Soldering Time|tsold|—|10|s|—|
|Supply Voltage|VCC|–0.5|3.63|V|—|
|Data Input Voltage|VI|–0.5|VCC|V|—|
|Differential Input Voltage (pk-pk)|VD|—|1.9|V|—|



a. The Moisture Sensitivity Level is MSL-1. 

## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|TC|–40|—|+95|°C|a, b|
|Supply Voltage|VCC|3.0|3.3|3.6|V|—|
|Data Output Load|RL|—|100|—|Ω|Differential|
|Signaling Rate|B|—|125|—|Mbaud|c|



a. The case temperature is measured at the transceiver topside surface using a thermocouple connected to the housing. 

b. Electrical and optical specifications of the product are guaranteed across the recommended case operating temperature. 

c. Fast Ethernet 4B/5B. Ethernet auto-negotiation pulses are not supported. 

AFBR-59E5APZ-HT-DS101 7 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

The following characteristics refer to AFBR-59E5APZ-HT parts that have been tested in the recommended application circuit (Figure 2). The typical data in the following tables represents the average values taken during the product characterization, measured at a case temperature of 25°C and a supply voltage of 3.3V. 

## **Transmitter Electrical Characteristics** 

–40°C to +95°C, 3.0V < VCC < 3.6V 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|45|80|mA|—|
|Power Dissipation|PDISS|—|149|288|mW|—|
|Diferential Input voltage|VDIFF|0.8|1.0|1.6|V|a|
|Input Diferential Impedance|RIN|—|100|—|Ω|b|
|Transmitter Disable High Level|VIH|2.0|—|VCC|V|c|



a. Peak to peak. 

b. Tx data inputs are AC-coupled. 

c. The transmitter is enabled when Pin 8 is connected to GND or left OPEN. The transmitter is disabled when Pin 8 is connected to the HIGH level. 

## **Receiver Electrical Characteristics** 

–40°C to +95°C, 3.0V < VCC < 3.6V 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|35|50|mA|—|
|Power Dissipation|PDISS|—|116|180|mW|—|
|Data Output: Dif. Output Voltage (RD±)||VOH– VOL||0.4|—|2.0|V|a, b|
|Data Output Rise Time (10%–90%)|tr|—|—|2.2|ns|—|
|Data Output Fall Time (90%–10%)|tf|—|—|2.2|ns|—|
|Signal Detect<br>Output Voltage – Low|SDVOL|—|—|VCC– 1.62|V|—|
|Signal Detect<br>Output Voltage – High|SDVOH|VCC– 1.02|—|—|V|—|



a. Differential output voltage is internally AC-coupled. The low and high voltages are measured using 100Ω differential termination. 

b. RD+ and RD- outputs are squelched at SD deassert levels. 

AFBR-59E5APZ-HT-DS101 

Broadcom 

8 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Transmitter Optical Characteristics** 

–40°C to +95°C, 3.0V < VCC < 3.6V 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Output Optical Power<br>62.5/125 µm, NA = 0.275 Fiber|PO|–20|–16.5|–14|dBm|a, b|
|Output Optical Power<br>50/125 µm, NA = 0.20 Fiber|PO|–23.5|–19.5|–14|dBm|a, b|
|Extinction Ratio|ER|10|—|—|dB|—|
|Center Wavelength|λC|1270|1308|1380|nm|—|
|Spectral Width – FWHM|Δλ|—|147|—|nm|—|
|Optical Rise Time (10%–90%)|tr|0.6|1.0|3.0|ns|—|
|Optical Fall Time (90%–10%)|tf|0.6|1.0|3.0|ns|—|
|Duty Cycle Distortion Contributed by the<br>Transmitter|DCD|—|—|0.6|ns|c, d|
|Data Dependent Jitter Contributed by<br>the Transmitter|DDJ|—|—|0.6|ns|c|
|Random Jitter Contributed by the<br>Transmitter|RJ|—|—|0.69|ns|c, e|



a. Optical values are measured over the specified operating voltage and temperature ranges. The average power can be converted to a peak value by adding 3 dB. 

b. Average. 

c. Characterized with a 125-Mbaud, PRBS2[7] -1 pattern. 

d. Duty cycle distortion contributed by the transmitter is measured at 50% of the threshold of the optical signal. 

e. Peak to peak. 

AFBR-59E5APZ-HT-DS101 

Broadcom 

9 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Receiver Optical and Electrical Characteristics** 

–40°C to +95°C, 3.0V < VCC < 3.6V 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Input Optical Power|PIN|–31|—|–14|dBm|a, b|
|Operating Wavelength|λR|1270|—|1380|nm|—|
|Duty Cycle Distortion Contributed by the<br>Receiver|DCD|—|—|0.4|ns|c, d|
|Data Dependent Jitter Contributed by<br>the Receiver|DDJ|—|—|1.0|ns|d|
|Random Jitter Contributed by the<br>Receiver|RJ|—|—|2.14|ns|d, e|
|Signal Detect – Assert|SDA|—|—|–31|dBm|b|
|Signal Detect – Deassert|SDD|–45|—|—|dBm|b|
|Signal Detect – Hysteresis|SDD– SDA|0.5|2|—|dB|—|
|Signal Detect Assert Time (Of to On)|SDon|0|—|100|µs|f|
|Signal Detect Deassert Time (On to Of)|SDof|0|—|350|µs|g|



- a. This specification is intended to indicate the performance of the receiver section when optical input power signal characteristics are present per the following definitions: 

   1. Over the specified operating temperature and voltage ranges. 

   2. Bit error rate (BER) is better than or equal to 1×10[-10] . 

   3. The transmitter operates to simulate any crosstalk present between the transmitter and receiver sections of the transceiver. 

   4. Fiber: 62.5/125 μm, NA = 0.275; or 50/125 μm, NA = 0.20. 

- b. Average. 

c. Duty cycle distortion contributed by the receiver is measured at 50% of the threshold of the electrical signal. 

- d. Characterized with a 125-Mbaud, PRBS2[7] -1 pattern. 

- e. Peak to peak. 

- f. Signal detect output shall be asserted within the specified time after a step increase of the optical input power. 

- g. Signal detect output shall be deasserted within the specified time after a step decrease of the optical input power. 

AFBR-59E5APZ-HT-DS101 10 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Figure 3: Package Outline Drawing** 


**----- Start of picture text -----**<br>
Y (10 : 1)<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
19.6 17.78 10 x ø0.46<br>1<br>0.25 13.7 1.78<br>2x ø1.07<br>13.6 9.8 MAX. 6.25<br>X<br>Tx Rx<br>2<br>Tcase REFERENCE POINT<br>Y<br>14.8 1 3.25 10.16<br>10.9<br>UNCOMPRESSED<br>48.5 MAX. 13.59 MA.X.<br>54.3<br>14.8 Plug<br>UNCOMPRESSED Label (For Information Only) X (5 : 1)<br>**----- End of picture text -----**<br>


**NOTE:** All dimensions are in millimeters. 

AFBR-59E5APZ-HT-DS101 11 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Figure 4: Recommended Board Layout Hole Pattern** 


**----- Start of picture text -----**<br>
SEE DETAIL X 21.3 SEE DETAIL Y Y (10 : 1)<br>20 x ø0.81 X (10 : 1)<br>7.56 X 13.35 MIN PICH15.24 3.5 1.7 2.4<br>4 x ø1.2 4 x ø1.2<br>1.9  Y<br>4 x ø1.6<br>10.16 ø1.2<br>4 x ø1.6<br>ø0.81<br>5.08<br>24.7 4 x ø2.29  1<br>3.4    MAX. (AREA FOR EYELET)<br>2<br>4 x ø1.4<br>4 x 1.78 17.78<br>15.24  14.2<br>MIN. PITCH<br>1<br>10.16<br>TOP OF PCB<br>15.75<br>**----- End of picture text -----**<br>


## **NOTES:** 

1. This page describes the recommended circuit board footprint and front panel openings for SFF transceivers. 

2. The rectangular details (as described; X and Y) are keep-out areas that are reserved for housing standoffs. No metal traces are allowed in keep-out areas. 

3. Holes for mounting studs must not be tied to signal ground; they should be tied to chassis ground. 

4. Holes for housing leads are required for the AFBR-59E5APZ-HT. Their positions deviate from the Common Transceiver Footprint hole pattern defined in the multisource announcement. 

5. All dimensions are in millimeters. 

AFBR-59E5APZ-HT-DS101 12 

Broadcom 

**AFBR-59E5APZ-HT** Data Sheet 

Multimode SFF Transceiver with LC Connector for Fast Ethernet 

## **Figure 5: Recommended Footprint (Top View)** 


**----- Start of picture text -----**<br>
21.3 7.1<br>1.78<br>7.12 17.78<br>10.16 13.35<br>**----- End of picture text -----**<br>


**NOTE:** All dimensions are in millimeters. 

AFBR-59E5APZ-HT-DS101 13 

Broadcom 

Copyright © 2023–2024 Broadcom. All Rights Reserved. The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos referenced herein belong to their respective companies. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

