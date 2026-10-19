## **HFBR-5961LZ/ALZ/GZ/AGZ** 

Multimode Small Form Factor (SFF) Transceivers for ATM, FDDI, Fast Ethernet and SONET OC-3/SDH STM-1 with LC connector 


## **Data Sheet** 

## **Description** 

The HFBR-5961xxZ transceiver from Avago provides the system designer with a product to implement a range of solutions for multimode fiber Fast Ethernet and SONET OC-3 (SDH STM-1) physical layers for ATM and other services. 

This transceiver is supplied in the industry standard 2 x 5 DIP style with an LC fiber connector interface with an external connector shield. 

## **Transmitter Section** 

The transmitter section of the HFBR-5961xxZ utilizes a 1300 nm InGaAsP LED.  This LED is packaged in the optical subassembly portion of the transmitter section. It is driven by a custom silicon IC which converts differential PECL logic signals, ECL referenced (shifted) to a +3.3 V supply, into an analog LED drive current. 

## **Features** 

- Multisourced 2 x 5 package style 

- Operates with 62.5/125 µm and 50/125 µm multimode fiber 

- Single +3.3 V power supply 

- Wave solder and aqueous wash process compatibility 

- Manufactured in an ISO 9001 certified facility 

- Full compliance with ATM Forum 

- UNI SONET OC-3 multimode fiber physical layer specification 

- Full compliance with the optical performance requirements of the FDDI PMD standard 

- Full compliance with the optical performance requirements of 100Base-FX version of IEEE802.3u 

- RoHS compliant 

- PECL Signal Detect Output 

## **Receiver Section** 

The receiver section of the HFBR-5961xxZ utilizes an InGaAs PIN photodiode coupled to a custom silicon transimpedance preamplifier IC.   It is packaged in the optical subassembly portion of the receiver. 

This PIN/preamplifier combination is coupled to a custom quantizer IC which provides the final pulse shaping for the logic output and the Signal Detect function.  The Data output is differential.  The Signal Detect output is single ended.  Both Data and Signal Detect outputs are PECL compatible, ECL referenced (shifted) to a +3.3 V power supply.   The receiver outputs, Data Output and Data Out Bar, are squelched at Signal Detect deassert.  That is, when the light input power decreases to a typical -38 dBm or less, the Signal Detect deasserts, ie. the Signal Detect output goes to a PECL low state.  This forces the receiver outputs, Data Out and Data Out Bar to go steady PECL levels high and low respectively. 

- Temperature range: 

   - HFBR-5961LZ 0 ° C to +70 ° C HFBR-5961ALZ -40 ° C to +85 ° C HFBR-5961GZ 0 ° C to +70 ° C (No EMI shield) HFBR-5961AGZ -40 ° C to +85 ° C (No EMI shield) 

## **Applications** 

- SONET/SDH equipment interconnect, OC-3/SDH STM-1 rate 

- Fast Ethernet 

- Multimode fiber ATM backbone links 

## **Package** 

The overall package concept for the Avago transceiver consists of three basic elements; the two optical subassemblies, an electrical subassembly, and the housing as illustrated in the block diagram in Figure 1. 

The package outline drawing and pin out are shown in Figures 2 and 5.  The details of this package outline and pin out are compliant with the multisource definition of the 2 x 5 DIP.  The low profile of the Avago transceiver design complies with the maximum height allowed for the LC connector over the entire length of the package. 

The optical subassemblies utilize a high-volume assembly process together with low-cost lens elements which result in a cost effective building block. 

The receiver section includes an internal shield for the electrical and optical subassemblies to ensure high immunity to external EMI fields. 

The outer housing including the LC ports is molded of filled nonconductive plastic to provide mechanical strength.  The solder posts of the Avago design are isolated from the internal circuit of the transceiver. 

The transceiver is attached to a printed circuit board with the ten signal pins and the two solder posts which exit the bottom of the housing.  The two solder posts provide the primary mechanical strength to withstand the loads imposed on the transceiver by mating with the LC connector fiber cables. 

The electrical subassembly consists of a high volume multilayer printed circuit board on which the ICs and various surface mounted passive circuit elements are attached. 


**----- Start of picture text -----**<br>
RX SUPPLY<br>DATA OUT<br>QUANTIZER IC PIN PHOTODIODE<br>DATA OUT<br>PRE-AMPLIFIER<br>SUBASSEMBLY<br>SIGNAL RX GROUND<br>DETECT LC<br>RECEPTACLE<br>TX GROUND<br>LED<br>DATA IN<br>OPTICAL<br>LED DRIVER IC SUBASSEMBLY<br>DATA IN<br>TX SUPPLY<br>**----- End of picture text -----**<br>


**Figure 1.  Block Diagram** 

2 


**----- Start of picture text -----**<br>
RX          TX<br>Mounting<br>Studs/Solder<br>Posts<br>Top<br>View<br>RECEIVER SIGNAL GROUND o 1 10 o TRANSMITTER DATA IN BAR<br>RECEIVER POWER SUPPLY o 2 9 o TRANSMITTER DATA IN<br>SIGNAL DETECT o 3 8 o NC<br>RECEIVER DATA OUT BAR o 4 7 o TRANSMITTER SIGNAL GROUND<br>RECEIVER DATA OUT o 5 6 o TRANSMITTER POWER SUPPLY<br>**----- End of picture text -----**<br>


**Figure 2.  Pin Out Diagram** 

## **Pin Descriptions:** 

## **Pin 1 Receiver Signal Ground VEE RX:** 

Directly connect this pin to the receiver ground plane. 

## **Pin 2 Receiver Power Supply VCC RX:** 

Provide +3.3 V dc via the recommended receiver power supply filter circuit.  Locate the power supply filter circuit as close as possible to the VCC RX pin. 

## **Pin 3 Signal Detect SD:** 

Normal optical input levels to the receiver result in a logic “1” output. 

Low optical input levels to the receiver result in a logic “0” output. 

This Signal Detect output can be used to drive a PECL input on an upstream circuit, such as Signal Detect input of Loss of Signal-Bar. 

## **Pin 4 Receiver Data Out Bar RD-:** 

No internal terminations are provided.  See recommended circuit schematic. 

## **Pin 5 Receiver Data Out RD+:** 

No internal terminations are provided.  See recommended circuit schematic. 

## **Pin 7 Transmitter Signal Ground VEE TX:** 

Directly connect this pin to the transmitter ground plane. 

## **Pin 8 NC:** 

No connection. 

## **Pin 9 Transmitter Data In TD+:** 

No internal terminations are provided.  See recommended circuit schematic. 

## **Pin 10 Transmitter Data In Bar TD-:** 

No internal terminations are provided.  See recommended circuit schematic. 

## **Mounting Studs/Solder Posts** 

The mounting studs are provided for transceiver mechanical attachment to the circuit board.  It is recommended that the holes in the circuit board be connected to chassis ground. 

## **Application Information** 

The Applications Engineering group is available to assist you with the technical understanding and design tradeoffs associated with these transceivers.  You can contact them through your Avago sales representative. 

The following information is provided to answer some of the most common questions about the use of these parts. 

## **Transceiver Optical Power Budget versus Link Length** 

Optical Power Budget (OPB) is the available optical power for a fiber optic link to accommodate fiber cable losses plus losses due to in-line connectors, splices, optical switches, and to provide margin for link aging and unplanned losses due to cable plant reconfiguration or repair. 

Avago LED technology has produced 1300 nm LED devices with lower aging characteristics than normally associated with these technologies in the industry. The industry convention is 1.5 dB aging for 1300 nm LEDs.  The 1300 nm Avago LEDs are specified to experience less than 1 dB of aging over normal commercial equipment mission life periods.  Contact your Avago sales representative for additional details. 

## **Pin 6 Transmitter Power Supply VCC TX:** 

Provide +3.3 V dc via the recommended transmitter power supply filter circuit.  Locate the power supply filter circuit as close as possible to the VCC TX pin. 

3 

## **Recommended Handing Precautions** 

Avago recommends that normal status precautions be taken in the handling and assembly of these transceivers to prevent damage which may be induced by electrostatic discharge (ESD).  The HFBR-5961xxZ series of transceivers meet MIL-STD-883C Method 3015.4 Class 2 products. 

Care should be used to avoid shorting the receiver data or signal detect outputs directly to ground without proper current limiting impedance. 

## **Solder and Wash Process Compatibility** 

The transceivers are delivered with protective process plugs inserted into the LC receptacle. 

This process plug protects the optical subassemblies during wave solder and aqueous wash processing and acts as a dust cover during shipping. 

## **Shipping Container** 

The transceiver is packaged in a shipping container designed to protect it from mechanical and ESD damage during shipment of storage. 

## **Board Layout - Decoupling Circuit, Ground Planes and Termination Circuits** 

It is important to take care in the layout of your circuit board to achieve optimum performance from these transceivers.  Figure 3 provides a good example of a schematic for a power supply decoupling circuit that works will with these parts,  It is further recommended that a contiguous ground plane be provided in the circuit board directly under the transceiver to provide a low inductance ground for signal return current. This recommendation is in keeping with good high frequency board layout practices.  Figures 3 and 4 show two recommended termination schemes. 

These transceivers are compatible with either industry standard wave or hand solder processes. 


**----- Start of picture text -----**<br>
PHY DEVICE<br>VCC (+3.3 V)<br>TERMINATE AT<br>TRANSCEIVER  INPUTS Z = 50  Ω<br>TD-<br>100   Ω LVPECL<br>Z = 50  Ω<br>TD+<br>10     9      8      7      6 130  Ω 130  Ω<br>1 µH VCC (+3.3 V)<br>TX C2 C3 10 µF VCC (+3.3 V)<br>RX<br>1 µH<br>RD+<br>C1<br>1      2      3      4      5<br>Z = 50  Ω 100  Ω LVPECL<br>RD-<br>Z = 50  Ω<br>VCC (+3.3 V)<br>130  Ω 130  Ω 130  Ω<br>Z = 50  Ω<br>SD<br>LVTTL<br>82  Ω<br>Notes:<br>C1 = C2 = C3 = 10 nF or 100 nF<br>* Loading of R1 is optional. TERMINATE AT<br>DEVICE INPUTS<br>TD-   o TD+   o N/C   o VEE TX   o VCC TX   o<br>o   VEE RX o   VCC RX o   SD o   RD- o   RD+<br>**----- End of picture text -----**<br>


**Figure 3.  Recommended Decoupling and Termination Circuits** 

4 

## **Board Layout - Hole Pattern** 

The Avago transceiver complies with the circuit board “Common Transceiver Footprint” hole pattern defined in the original multisource announcement which defined the 2 x 5 package style.  This drawing is reproduced in Figure 6 with the addition of ANSI Y14.5M compliant dimensioning to be used as a guide in the mechanical layout of your circuit board.  Figure 6 illustrates the recommended panel opening and the position of the circuit board with respect to this panel. 

## **Regulatory Compliance** 

These transceiver products are intended to enable commercial system designers to develop equipment that complies with the various international regulations governing certification of Information Technology Equipment.  See the Regulatory Compliance Table for details.  Additional information is available from your Avago sales representative. 


**----- Start of picture text -----**<br>
TERMINATE AT<br>TRANSCEIVER  INPUTS<br>PHY DEVICE<br>VCC (+3.3 V)<br>VCC (+3.3 V)<br>10 nF<br>130  Ω 130   Ω<br>Z = 50  Ω<br>TD-<br>LVPECL<br>Z = 50  Ω<br>TD+<br>10     9      8      7       6 82  Ω 82  Ω<br>VCC (+3.3 V)<br>TX 1 µH VCC (+3.3 V) VCC (+3.3 V)<br>10 µF 10 nF<br>RX C2 C3 130  Ω 130  Ω<br>RD+<br>1 µH<br>1      2      3      4      5<br>C1 LVPECL<br>Z = 50  Ω<br>RD-<br>VCC (+3.3 V)<br>Z = 50  Ω<br>10 nF<br>82  Ω 82  Ω<br>130  Ω<br>Z = 50  Ω<br>SD<br>LVTTL<br>82  Ω<br>Note: TERMINATE AT DEVICE INPUTS<br>TD-   o TD+   o N/C   o VEE TX   o VCC TX   o<br>o   VEE RX o   VCC RX o   SD o   RD- o   RD+<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
Note:<br>C1 = C2 = C3 = 10 nF or 100 nF<br>* Loading R1 is optional.<br>**----- End of picture text -----**<br>


**Figure 4.  Alternative Termination Circuits** 

5 







**ALL DIMENSIONS IN MILIMETERS(INCHES)** 

**Figure 5.  Package Outline Drawing** 

6 

## **Electrostatic Discharge (ESD)** 

There are two design cases in which immunity to ESD damage is important. 

The first case is during handling of the transceiver prior to mounting it on the circuit board.  It is important to use normal ESD handling precautions for ESD sensitive devices.  These precautions include using grounded wrist straps, work benches, and floor mats in ESD controlled areas. 

## **Electromagnetic Interference (EMI)** 

Most equipment designs utilizing this high speed transceiver from Avago will be required to meet the requirements of FCC in the United States, CENELEC EN55022 (CISPR 22) in Europe and VCCI in Japan. 

This product is suitable for use in designs ranging from a desktop computer with a single transceiver to a concentrator or switch product with a large number of transceivers. 

The second case to consider is static discharges to the exterior the equipment chassis containing the transceiver parts.  To the extent that the LC connector is exposed to the outside of the equipment chassis it may be subject to whatever ESD system level test criteria that the equipment is intended to meet. 


**----- Start of picture text -----**<br>
0.81 ± .10<br>20 x Ø<br>(.032 ± .004)<br>SEE DETAIL B<br>SEE NOTE 3<br>4 x Ø(.055 ± .004)1.40 ± .10 (NOTE 5) (1.014)25.75 SEE DETAIL A<br>13.34 12.16<br>(.525) (.479) 15.24 MIN. PITCH<br>(.600)<br>5 4 3 2 1 7.59 10.16 2 x Ø          MAX. (AREA FOR EYELET'S)2.29<br>6 7 8 9 10 (.299) (.400) (.090)<br>2 x Ø 1.40 ± .10 (NOTE 4)<br>(.055 ± .004)<br>4.57 3<br>(.180) (.118)<br>3<br>7.11 (.118)<br>3.56 (.280) 6<br>(.140) 8.89 (.236)<br>(.350) DETAIL A (3 x)<br>1.78<br> 9 X<br>(.070)<br>1.8<br>.071<br>1<br>.039<br>15.24<br>            MIN. PITCH<br>(.600)<br>+ 1.50 DETAIL B (4 x)<br>1.00 -  0 14.22 ± .10<br>(.039) (+.059)(- .000) A (.560 ± .004)<br>TOP OF PCB<br>A<br>10.16 ± .10<br>(.400 ± .004)<br>+ 0 A SECTION A - A<br>15.75<br>-  0.75<br>(+.000)<br>(.620)<br>(- .030)<br>**----- End of picture text -----**<br>


NOTES: 

1. THIS PAGE DESCRIBES THE RECOMMENDED CIRCUIT BOARD LAYOUT AND FRONT PANEL OPENINGS FOR SFF TRANSCEIVERS. 

2. THE HATCHED AREAS ARE KEEP-OUT AREAS RESERVED FOR HOUSING STANDOFFS. NO METAL TRACES ALLOWED IN KEEP-OUT AREAS. 

3. THIS DRAWING SHOWS EXTRA PIN HOLES FOR 2 x 6 PIN AND 2 x 10 PIN TRANSCEIVERS. THESE EXTRA HOLES ARE NOT REQUIRED FOR HFBR-5961xxZ AND OTHER 2 x 5 PIN SFF MODULES. 

4. HOLES FOR MOUNTING STUDS MUST NOT BE TIED TO SIGNAL GROUND BUT MAY BE TIED TO CHASSIS GROUND. 

5. HOLES FOR HOUSING LEADS OPTIONAL AND NOT REQUIRED FOR HFBR-5961L/HFBR-5961G. IF NEEDED IN FUTURE, THESE HOLES MUST BE TIED TO SIGNAL GROUND. 

6. ALL DIMENSIONS ARE IN MILLIMETERS (INCHES). 

**Figure 6.  Recommended Board Layout Hole Pattern** 

7 

## **Immunity** 

Equipment utilizing these transceivers will be subject to radio-frequency electromagnetic fields in some environments.  These transceivers have a high immunity to such fields. 

For additional information regarding EMI, susceptibility, ESD and conducted noise testing procedures and results.  Refer to Application Note 1166, Minimizing Radiated Emissions of High-Speed Data Communications Systems. 

## **Transceiver Reliability and Performance Qualification Data** 

The 2 x 5 transceivers have passed Avago reliability and performance qualification testing and are undergoing ongoing quality and reliability monitoring.  Details are available from your Avago sales representative. 

These transceivers are manufactured at the Avago Singapore location which is an ISO 9001 certified facility. 

## **Applications Support Material** 

Contact your local Avago Component Field Sales Office for information on how to obtain PCB layouts and evaluation boards for the 2 x 5 transceivers. 


**----- Start of picture text -----**<br>
200<br>3.0<br>180 HFBR-5961xxZ TRANS-<br>1.0 MITTER TEST RESULTS<br>OF   λ C,  ∆λ    AND tr/f ARE<br>160 CORRELATED AND COMPLY<br>1.5 WITH THE ALLOWED<br>SPECTRAL WIDTH AS A<br>FUNCTION OF CENTER<br>140 2.0 WAVELENGTH FOR<br>VARIOUS RISE AND<br>tr/f – TRANSMITTER FALL TIMES.<br>120 2.5 OUTPUT OPTICAL RISE/<br>FALL TIMES – ns<br>3.0<br>100<br>1260 1280 1300 1320 1340 1360<br>l C – TRANSMITTER OUTPUT OPTICAL RISE/FALL TIMES – ns<br> - TRANSMITTER OUTPUT OPTICAL SPECTRAL WIDTH (FWHM) - nm<br>∆λ<br>**----- End of picture text -----**<br>


**Figure 7.  Transmitter Output Optical Spectral Width (FWHM) vs. Transmitter Output Optical Center Wavelength and Rise/Fall Times** 


**----- Start of picture text -----**<br>
6<br>5<br>CONDITIONS:<br>4 1. TA = +25 C<br>2. VCC = 3.3 V dc<br>3. INPUT OPTICAL RISE/<br>    FALL TIMES = 2.1/1.9 ns.<br>3<br>4. INPUT OPTICAL POWER<br>    IS NORMALIZED TO<br>    CENTER OF DATA SYMBOL.<br>2 5. NOTE 15 AND 16 APPLY.<br>1<br>0<br>-3 -2 -1 0 1 2 3<br>EYE SAMPLING TIME POSITION (ns)<br>RELATIVE INPUT OPTICAL POWER (dB)<br>**----- End of picture text -----**<br>


**Figure 8.  Relative Input Optical Power vs Eye Sampling Time Position** 

## **Regulatory Compliance Table** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge|MIL-STD-883C|Meets Class 2 (2000 to 3999 Volts).Withstand up to 2200 V|
|(ESD) to the Electrical||applied between electrical pins.|
|Pins|||
|Electrostatic Discharge|Variation of IEC 61000-4-2|Typically withstand at least 25 kV without damage when|
|(ESD) to the LC Recep-||the LC connector receptacle is contacted by a Human Body|
|tacle||Modelprobe.|
|Electromagnetic Inter-<br>ference (EMI)|FCC Class B<br>CENELEC CEN55022 VCCI|Transceivers typically provide a 10 dB margin  to the noted<br>standard limits when tested at a certifed test range with|
||Class 2|the transceiver mounted to  a circuit card without a chassis|
|||enclosure.|
|Immunity|Variation of IEC 61000-4-3|Typically show no measurable efect from a 10 V/m feld|
|||swept from 80 to 450 MHz applied to the transceiver when|
|||mounted to a circuit card withouta chassis enclosure.|
|Eye Safety|AEL Class 1EN60825-1 (+A11)|Compliant per Avago testing under single fault conditions.<br>TUV Certifcation - R 02071015|
|Component Recogni-|Underwriters Laboratories and|UL File #: E173874|
|tion|Canadian Standards Association Joint||
||Component Recognition for Informa-||
||tion Technology Equipment including||
||Electrical Business Equipment||



8 

## **Absolute Maximum Ratings** 

Stresses in excess of the absolute maximum ratings can cause catastrophic damage to the device. Limits apply to each parameter in isolation, all other parameters having values within the recommended operating conditions. It should not be assumed that limiting values of more than one parameter can be applied to the product at the same time. Exposure to the absolute maximum ratings for extended periods can adversely affect device reliability. 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Storage Temperature|TS|-40||+100|°C||
|Lead Soldering Temperature|TSOLD|||+260|°C||
|Lead Soldering Time|tSOLD|||10|sec||
|Supply Voltage|VCC|-0.5||3.63|V||
|Data Input Voltage|VI|-0.5||VCC|V||
|Diferential Input Voltage (p-p)|VD|||2.0|V|1|
|Output Current|IO|||50|mA||



## **Recommended Operating Conditions** 

|**Recommended Operating Conditions**|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|Case Operating Temperature|||||||
|HFBR-5961LZ/GZ|TC|0||+70|°C||
|HFBR-5961ALZ/AGZ|TC|-40||+85|°C||
|Supply Voltage|VCC|2.97|3.3|3.63|V||
|Data Input Voltage - Low|VIL- VCC|-1.810||-1.475|V||
|Data Input Voltage - High|VIH- VCC|-1.165||-0.880|V||
|Data and Signal Detect Output Load|RL||50||W|**2**|
|Diferential Input Voltage (p-p)|VD||0.800||V||



## **Transmitter Electrical Characteristics** 

HFBR-5961LZ/GZ (TC  =  0 ° C to +70 ° C, VCC=2.97 V to 3.63 V) 

HFBR-5961ALZ/AGZ (TC = -40 ° C to +85 ° C, VCC=2.97 V to 3.63V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC||110|175|mA|3|
|Power Dissipation|PDISS||0.4|0.64|W|5a|
|Data Input Current - Low|IIL|-350|-2||µA||
|Data Input Current - High|IIH||18|350|µA||



9 

## **Receiver Electrical Characteristics** 

HFBR-5961LZ/AGZ (TC  =  0 ° C to +70 ° C, VCC = 2.97V to 3.63 V) HFBR-5961ALZ/AGZ (TC = -40 ° C to +85 ° C, VCC = 2.97 V to 3.63 V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC||65|120|mA|4|
|Power Dissipation|PDISS||0.225|0.44|W|5b|
|Data Output Voltage - Low|VOL- VCC|-1.840||-1.620|V|6|
|Data Output Voltage - High|VOH- VCC|-1.045||-0.880|V|6|
|Data Output Rise Time|tr|0.35||2.2|ns|7|
|Data Output Fall Time|tf|0.35||2.2|ns|7|
|Signal Detect Output Voltage - Low|VOL- VCC|-1.840||-1.620|V|6|
|Signal Detect Output Voltage - High|VOH- VCC|-1.045||-0.880|V|6|
|Signal Detect Output Rise Time|tr|0.35||2.2|ns|7|
|Signal Detect Output Fall Time|tf|0.35||2.2|ns|7|
|Power Supply Noise Rejection|PSNR||50||mV||



## **Transmitter Optical Characteristics** 

HFBR-5961LZ/GZ (TC  = 0 ° C to +70 ° C, VCC = 2.97 V to 3.63 V) HFBR-5961ALZ/AGZ (TC = -40 ° C to +85 ° C, VCC = 2.97 V to 3.63 V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Output Optical Power|||||||
|BOL62.5/125  µm, NA = 0.275 Fiber|PO|-19|-15.7|-14|dBm avg|8|
|EOL||-20|||||
|Output Optical Power|PO|-22.5||-14|dBm avg|8|
|BOL50/125  µm, NA = 0.20 Fiber||-23.5|||||
|EOL|||||||
|Optical Extinction Ratio|||0.02|0.2|%dB|9|
||||-47|-27|||
|Output Optical Power at Logic Low 0 State|PO(“0”)|||-45|dBm avg|10|
|Center Wavelength|lC|1270|1308|1380|nm|23, Figure 7|
|Spectral Width - FWHM|Dl||14763||nm|11, 23|
|Spectral Width - RMS||||||Figure 7|
|Optical Rise Time|tr|0.6|2.1|3.0|ns|12, 23|
|||||||Figure 7|
|Optical Fall Time|tf|0.6|1.9|3.0|ns|12, 23|
|||||||Figure 7|
|Systematic Jitter Contributed|SJ||0.4|1.2|ns p-p|13a|
|bythe Transmitter  OC-3|||||||
|Duty Cycle Distortion Contributed|DCD||0.36|0.6|ns p-p|13b|
|bythe Transmitter  FE|||||||
|Data Dependent Jitter Contributed|DDJ||0.07|0.6|ns p-p|13c|
|bythe Transmitter  FE|||||||
|Random Jitter Contributed by the Transmitter|RJ||0.1|0.52|ns p-p|14a|
|OC-3|||0.1|0.69||14b|
|FE|||||||



10 

## **Receiver Optical and Electrical Characteristics** 

HFBR-5961LZ/GZ (TC  = 0 ° C to +70 ° C, VCC = 2.97 V to 3.63 V) HFBR-5961ALZ/AGZ (TC = -40 ° C to +85 ° C, VCC = 2.97 V to 3.63 V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Input Optical Power at minimum|||||||
|at Window Edge|PIN MIN(W)||||||
|OC-3||||-30|dBm avg|15a, Figure 8|
|FE||||-31||15b|
|Input Optical Power at Eye Center|||||||
|OC-3|PIN MIN(C)|||-31|dBm avg|16a, Figure 8|
|FE||||-31.8||16b|
|Input Optical Power Maximum|||||||
|OC-3|PIN MAX|-14|||dBm avg|15a|
|FE||-14||||15b|
|OperatingWavelength|l|1270||1380|nm||
|Systematic Jitter Contributed|||||||
|by the Receiver|SJ||0.2|1.2|ns p-p|17a|
|OC-3|||||||
|Duty Cycle Distortion Contributed|||||||
|by the Receiver|DCD||0.08|0.4|ns p-p|17b|
|FE|||||||
|Data Dependent Jitter Contributed|||||||
|bythe Receiver  FE|DDJ||0.07|1.0|nsp-p|17c|
|Random Jitter Contributed by the Receiver|||||||
|OC-3|RJ||0.3|1.91|ns p-p|18a|
|FE|||0.3|2.14||18b|
|Signal Detect - Asserted|||||||
|OC-3|PA|PD+ 1.5 dB||-31|dBm avg|19|
|FE||||-33|||
|Signal Detect - Deasserted|PD|-45|||dBm avg|20|
|Signal Detect - Hysteresis|PA- PD|1.5|||dB||
|Signal Detect Assert Time (of to on)||0|2|100|µs|21|
|Signal Detect Deassert Time (on to of)||0|5|100|µs|22|



## **Notes:** 

1. This is the maximum voltage that can be applied across the Differential Transmitter Data Inputs to prevent damage to the input ESD protection circuit. 

2. The outputs are terminated with 50 W connected to VCC – 2 V. 

3. The power supply current needed to operate the transmitter is provided to differential ECL circuitry.  This circuitry maintains a nearly constant current flow from the power supply.  Constant current operation helps to prevent unwanted electrical noise from being generated and conducted or emitted to neighboring circuitry. 

4. This value is measured with the outputs terminated into 50 W connected to  VCC – 2 V and an Input Optical Power level of –14 dBm average. 

- 5a. The power dissipation of the transmitter is calculated as the sum of the products of supply voltage and current. 

- 5b. The power dissipation of the receiver is  calculated as the sum of the products of supply voltage and currents, minus the sum of the products of the output voltages and currents. 

6. This value is measured with respect to VCC with the output terminated into 50 W connected to VCC - 2 V. 

7. The data output rise and fall times are measured between 20% and 80% levels with the output connected to VCC – 2 V through 50 W . 

8. These optical power values are measured 

   - with the following conditions: 

The Beginning of life (BOL) to the End of Life (EOL) optical power degradation is typically 1.5 dB per the industry convention for long wavelength LEDs.  The actual degradation observed in Avago’s 1300 nm LED products is < 1 dB, as specified in this data sheet.  Over the specified operating voltage and temperature ranges.  With 25 MBd (12.5 MHz square-wave), input signal. At the end of one meter of noted optical fiber with cladding modes removed.   The average power value can be converted to a peak power value by adding 3 dB. Higher output optical power transmitters are available on special request. Please consult with your local Avago sales representative for further details. 

11 

9. The Extinction Ratio is a measure of the modulation depth of the optical signal..  The data “0” output optical power is compared to the data “1” peak output optical power and expressed as a percentage. With the transmitter driven by a 25 MBd (12.5 MHz square-wave) input signal, the average optical power is measured. The data “1” peak power is then calculated by adding 3 dB to the measured average optical power. The data “0” output optical power is found by measuring the optical power when the transmitter is driven by a logic “0” input.  The extinction ratio is the ratio of the optical power at the “0” level compared to the optical power at the “1” level expressed as a percentage or in decibels. 

10. The transmitter will provide this low level of Output Optical Power when driven by a Logic “0” input. This can be useful in link troubleshooting. 

11. The relationship between Full Width Half Maximum and RMS values for Spectral Width is derived from the assumption of a Gaussian shaped spectrum which results in a 2.35 X RMS = FWHM relationship. 

12. The optical rise and fall times are measured from 10%  to 90%  when the transmitter is driven by a 25 MBd (12.5 MHz square-wave) input signal. The ANSI T1E1.2 committee has designated the possibility of defining an eye pattern mask for the transmitter optical output as an item for further study. Avago will incorporate this requirement into the specifications for these products if it is defined. The  HFBR-59XXL products typically comply with the template requirements of CCITT (now ITU-T) G.957 Section 3.2.5,  Figure 5 for the STM- 1 rate, excluding the optical receiver filter normally associated with single mode fiber measurements which is the likely source for the ANSI T1E1.2 committee to follow in this matter. 

- 13a. Systematic Jitter contributed by the transmitter is defined as the combination of Duty Cycle Distortion and Data Dependent Jitter. Systematic Jitter is measured at 50%  threshold using a 155.52 MBd (77.5 MHz square-wave), 2[23] -1 pseudorandom data pattern input signal. 

- 13b. Duty Cycle Distortion contributed by the transmitter is measured at the 50% threshold of the optical output signal using an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. 

- 13c. Data Dependent Jitter contributed by the transmitter is specified with the FDDI test pattern described in FDDI PMD Annex A.5. 

- 14a. Random Jitter contributed by the transmitter is specified with a 155.52 MBd (77.5 MHz square-wave) input signal. 

- 14b. Random Jitter contributed by the transmitter is specified with an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. See Application Information - Transceiver Jitter Performance Section of this data sheet for further details. 

- 15a. This specification is intended to indicate  the performance of the receiver section of the transceiver when Input Optical Power  signal characteristics are present per the following definitions. The Input Optical Power dynamic range from the minimum level (with a window time-width) to the maximum level is the range over which the receiver is guaranteed to provide output data with a Bit Error Rate (BER) better than or equal to 1 x 10[-10] . 

   - At the Beginning of Life (BOL) over the specified operating temperature and voltage ranges 23 input is a 155.52 MBd, 2 -  1 PRBS data pattern with 72  “1” s and 72 “0”s inserted per the CCITT (now ITU-T) recommendation G.958 Appendix I. Receiver data window time-width is 1.23 ns or greater for the clock recovery circuit to operate in. The actual test data window time-width is set to simulate the effect of worst case optical input jitter based on the transmitter jitter values from the specification tables. The test window time-width is  HFBR-5961L  3.32 ns. 

- Transmitter operating with a 155.52 MBd, 77.5 MHz square-wave, input signal to simulate any cross-talk present between the transmitter and receiver sections of the transceiver. 

- 15b. This specification is intended to indicate the performance of the receiver section of the transceiver when Input Optical Power signal characteristics are present per the following definitions. The Input Optical Power dynamic range from the minimum level (with a window timewidth) to the maximum level is the range over which the receiver is guaranteed to provide output data with a Bit Error Rate (BER) better than or equal to 2.5 x 10[-10] . 

   - At the Beginning of Life (BOL) 

   - Over the specified operating temperature and voltage ranges 

   - Input symbol pattern is the FDDI test pattern defined in FDDI PMD Annex A.5 with 4B/5B NRZI encoded data that contains a duty cycle base- 

   - line wander effect of 50 kHz. This sequence causes a near worst case condition for inter-symbol interference. 

   - Receiver data window time-width is 2.13 ns or greater and centered at mid-symbol. This worst case window time-width is the minimum allowed eye-opening presented to the FDDI PHY PM_Data indication input (PHY input) per the example in FDDI PMD Annex E. This minimum window time-width of 2.13 ns is based upon the worst case FDDI PMD Active Input Interface optical conditions for peak-to-peak DCD (1.0 ns), DDJ (1.2 ns) and RJ (0.76 ns) presented to the receiver. 

   - To test a receiver with the worst case FDDI PMD Active Input jitter condition requires exacting control over DCD, DDJ and RJ jitter components that is difficult to implement with production test equipment. The receiver can be equivalently tested to the worst case FDDI PMD input jitter conditions and meet the minimum output data window time-width of 2.13 ns. This is accomplished by using a nearly ideal input optical signal (no DCD, insignificant DDJ and RJ) and measuring for a wider window time-width of 4.6 ns. This is possible due to the cumulative effect of jitter components through their superposition (DCD and DDJ are directly additive and RJ components are rms additive). Specifically, when a nearly ideal input optical test signal is used and the maximum receiver peak-to-peak jitter contributions of DCD (0.4 ns), DDJ (1.0 ns), and RJ (2.14 ns) exist, the minimum window time-width becomes 8.0 ns -0.4 ns - 1.0 ns - 2.14 ns = 4.46 ns, or conservatively 4.6 ns. This wider window time-width of 4.6 ns guarantees the FDDI PMD Annex E minimum window time-width of 2.13 ns under worst case input jitter conditions to the Avago receiver. 

   - Transmitter operating with an IDLE Line State pattern, 125 MBd (62.5 MHz square-wave), input signal to simulate any cross-talk present between the transmitter and receiver sections of the transceiver. 

- 16a. All conditions of Note 15a apply except that the measurement is made at the center of the symbol with no window time- width. 16b. All conditions of Note 15b apply except that the measurement is made at the center of the symbol with no window time-width. 17a. Systematic Jitter contributed by the receiver is defined as the combination of Duty Cycle Distortion and Data Dependent Jitter. Systematic Jitter is measured at 50% threshold using a 155.52 MBd (77.5 MHz square- wave), 2[23] -  1 psuedorandom data pattern input signal. 

- 17b. Duty Cycle Distortion contributed by the receiver is measured at the 50% threshold of the electrical output signal using an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. The input optical power level is -20 dBm average. 

- 17c. Data Dependent Jitter contributed by the receiver is specified with the FDDI DDJ test pattern described in the FDDI PMD Annex A.5. The input optical power level is -20 dBm average. 

- 18a. Random Jitter contributed by the receiver is specified with a 155.52 MBd (77.5 MHz square- wave) input signal. 

- 18b. Random Jitter contributed by the receiver is specified with an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. The input optical power level is at maximum “PIN Min. (W)”. See Application Information - Transceiver Jitter Section for further information. 

12 

19. This value is measured during the transition from low to high levels of input optical power. 

20.  This value is measured during the transition from high to low levels of input optical power. At Signal Detect Deassert, the receiver outputs Data Out and Data Out Bar go to steady PECL levels High and Low respectively. 

21. The Signal Detect output shall be asserted within 100 us after a step increase of the Input Optical Power. 

22. Signal detect output shall be de-asserted within 350 µs after a step decrease in the Input Optical Power. At Signal Detect Deassert, the receiver outputs Data Out and Data Out Bar go to steady PECL levels High and Low respectively. 

23. The HFBR-5961L transceiver complies with the requirements for the trade-offs between center wavelength, spectral width, and rise/fall times shown in Figure 7.  This figure is derived from the FDDI PMD standard (ISO/IEC 9314-3 : 1990 and ANSI X3.166 - 1990) per the description in ANSI T1E1.2 Revision 3. The interpretation of this figure is that values of Center Wavelength and Spectral Width must lie along the appropriate Optical Rise/Fall Time curve. 

## **Ordering Information** 

**1300 nm LED (Operating Case Temperature 0 to +70** ° **C)** 

HFBR-5961LZ/HFBR-5961GZ 

**1300 nm LED (Operating Case Temperature -40 to +85** ° **C)** 

HFBR-5961ALZ/HFBR-5961AGZ 

For product information and a complete list of distributors, please go to our web site: **www.avagotech.com** 

Avago, Avago Technologies, and the A logo are trademarks of Avago Technologies in the United States and other countries. Data subject to change. Copyright © 2005-2009 Avago Technologies. All rights reserved. AV02-0820EN - April 24, 2009 

