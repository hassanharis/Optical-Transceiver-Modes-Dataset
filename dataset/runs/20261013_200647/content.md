
## **Data Sheet** 

## **HFBR-5963LZ/ALZ** 

**Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector** 

## **Description** 

## **Features** 

The HFBR-5963xxZ transceiver provides the system designer with a product to implement a range of solutions for multimode fiber Fast Ethernet and SONET OC-3 (SDH STM-1) physical layers for ATM and other services. 

This transceiver is supplied in the industry-standard 2 x 5 DIP style with an LC fiber connector interface with an external connector shield. 

- RoHS compliant 

- Multisourced 2 x 5 package style 

- Operates with 62.5/125 mm and 50/125 mm multimode fiber 

- Single +3.3V power supply 

- Wave solder and aqueous wash process compatibility 

- Manufactured in an ISO 9001 certified facility 

- Full compliance with ATM Forum 

## **Applications** 

- SONET/SDH equipment interconnect, OC-3/SDH STM-1 rate 

- Fast Ethernet 

- Multimode fiber ATM backbone links 

- UNI SONET OC-3 multimode fiber physical layer specification 

- Full compliance with the optical performance requirements of the FDDI PMD standard 

- Full compliance with the optical performance requirements of 100Base-FX version of IEEE802.3u 

- +3.3V TTL signal detect output 

- Temperature range: – HFBR-5963LZ: 0 °C to +70 °C 

   - HFBR-5963ALZ: –40 °C to +85 °C 

AV02-1088EN December 14, 2018 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Transmitter Section** 

The transmitter section of the HFBR-5963xxZ utilizes a 1300 nm InGaAsP LED. This LED is packaged in the optical subassembly portion of the transmitter section. It is driven by a custom silicon IC, which converts differential PECL logic signals, ECL referenced (shifted) to a +3.3V supply, into an analog LED drive current. 

## **Receiver Section** 

The receiver section of the HFBR-5963xxZ utilizes an InGaAs PIN photodiode coupled to a custom silicon transimpedance preamplifier IC. It is packaged in the optical subassembly portion of the receiver. 

This PIN/preamplifier combination is coupled to a custom quantizer IC that provides the final pulse shaping for the logic output and the signal detect function. The data output is differential. The data output is PECL compatible, ECL referenced (shifted) to a +3.3V power supply. The receiver outputs, data output and data out bar, are squelched at signal detect deassert. The signal detect output is single ended. The signal detect circuit works by sensing the level of the received signal and comparing this level to a reference. The SD output is +3.3V TTL. 

## **Package** 

The overall package concept for the Broadcom[®] transceiver consists of three basic elements: the two optical subassemblies, an electrical subassembly, and the housing as illustrated in the block diagram in Figure 1. 

The package outline drawing and pinout are shown in Figure 2 and Figure . The details of this package outline and pinout are compliant with the multisource definition of the 2 x 5 DIP. The low profile of the Broadcom transceiver design complies with the maximum height allowed for the LC connector over the entire length of the package. 

The optical subassemblies utilize a high-volume assembly process together with low-cost lens elements that result in a cost-effective building block. 

The electrical subassembly consists of a high volume multilayer printed circuit board on which the ICs and various surface-mounted passive circuit elements are attached. 

The receiver section includes an internal shield for the electrical and optical subassemblies to ensure high immunity to external EMI fields. 

The outer housing including the LC ports is molded of filled nonconductive plastic to provide mechanical strength. The solder posts of the Broadcom design are isolated from the internal circuit of the transceiver. 

The transceiver is attached to a printed circuit board with the ten signal pins and the two solder posts that exit the bottom of the housing. The two solder posts provide the primary mechanical strength to withstand the loads imposed on the transceiver by mating with the LC connector fiber cables. 

**Figure 1:  Block Diagram** 


**----- Start of picture text -----**<br>
R X  SUPPLY<br>DATA OUT<br>QUANTIZER IC PIN PHOTODIODE<br>DATA OUT<br>PRE-AMPLIFIER<br>SUBASSEMBLY<br>SIGNAL R X  GROUND<br>DETECT LC<br>RECEPTACLE<br>T X  GROUND<br>LED<br>DATA IN<br>OPTICAL<br>LED DRIVER IC SUBASSEMBLY<br>DATA IN<br>T X  SUPPLY<br>**----- End of picture text -----**<br>


AV02-1088EN 2 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Figure 2:  Pinout Diagram** 


**----- Start of picture text -----**<br>
RX                 TX<br>Mounting<br>Studs/Solder<br>Posts<br>Top<br>View<br>RECEIVER SIGNAL GROUND o 1 10 o TRANSMITTER DATA IN BAR<br>RECEIVER POWER SUPPLY o 2 9 o TRANSMITTER DATA IN<br>SIGNAL DETECT o 3 8 o NC<br>RECEIVER DATA OUT BAR o 4 7 o TRANSMITTER SIGNAL GROUND<br>RECEIVER DATA OUT o 5 6 o TRANSMITTER POWER SUPPLY<br>**----- End of picture text -----**<br>


## **Pin Descriptions** 

## **Pin 1 Receiver Signal Ground VEE RX:** 

Directly connect this pin to the receiver ground plane. 

## **Pin 5 Receiver Data Out RD+:** 

No internal terminations are provided. See Figure 3 and Figure 4. 

## **Pin 6 Transmitter Power Supply VCC TX:** 

Provide +3.3V dc via the recommended transmitter power supply filter circuit. 

Locate the power supply filter circuit as close as possible to the VCC TX pin. 

## **Pin 7 Transmitter Signal Ground VEE TX:** 

Directly connect this pin to the transmitter ground plane. 

## **Pin 8 NC:** 

No connection. 

## **Pin 9 Transmitter Data In TD+:** 

No internal terminations are provided. See Figure 3 and Figure 4. 

## **Pin 10 Transmitter Data In Bar TD–:** 

No internal terminations are provided. See Figure 3 and Figure 4. 

## **Pin 2 Receiver Power Supply VCC RX:** 

## **Mounting Studs/Solder Posts:** 

Provide +3.3 V dc via the recommended receiver power supply filter circuit. Locate the power supply filter circuit as close as possible to the VCC RX pin. 

## **Pin 3 Signal Detect SD:** 

The mounting studs are provided for transceiver mechanical attachment to the circuit board. 

It is recommended that the holes in the circuit board be connected to chassis ground. 

Normal optical input levels to the receiver result in a logic 1 output. 

Low optical input levels to the receiver result in a logic 0 output. 

This Signal Detect output can be used to drive a +3.3V TTL input on an upstream circuit, such as Signal Detect input or Loss of Signal-bar. 

## **Pin 4 Receiver Data Out Bar RD–:** 

No internal terminations are provided. See Figure 3 and Figure 4. 

AV02-1088EN 

Broadcom 

3 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Application Information** 

The Applications Engineering group is available to assist you with the technical understanding and design trade-offs associated with these transceivers. You can contact them through your Broadcom sales representative. 

The following information is provided to answer some of the most common questions about the use of these parts. 

## **Transceiver Optical Power Budget versus Link Length** 

Optical Power Budget (OPB) is the available optical power for a fiber optic link to accommodate fiber cable losses plus losses due to in-line connectors, splices, optical switches, and to provide margin for link aging and unplanned losses due to cable plant reconfiguration or repair. 

Broadcom LED technology has produced 1300-nm LED devices with lower aging characteristics than normally associated with these technologies in the industry. The industry convention is 1.5-dB aging for 1300-nm LEDs. The 1300-nm Broadcom LEDs are specified to experience less than 1 dB of aging over normal commercial equipment mission life periods. 

Contact your Broadcom sales representative for additional details. 

## **Recommended Handling Precautions** 

Broadcom recommends that normal static precautions be taken in the handling and assembly of these transceivers to prevent damage that may be induced by electrostatic discharge (ESD). 

## **Solder and Wash Process Compatibility** 

The transceivers are delivered with protective process plugs inserted into the LC receptacle. 

This process plug protects the optical subassemblies during wave solder and aqueous wash processing and acts as a dust cover during shipping. 

These transceivers are compatible with either industrystandard wave or hand solder processes. 

## **Shipping Container** 

The transceiver is packaged in a shipping container designed to protect it from mechanical and ESD damage during shipment or storage. 

## **Board Layout - Decoupling Circuit, Ground Planes and Termination Circuits** 

It is important to take care in the layout of your circuit board to achieve optimum performance from these transceivers. Figure 3 provides a good example of a schematic for a power supply decoupling circuit that works well with these parts. It is further recommended that a contiguous ground plane be provided in the circuit board directly under the transceiver to provide a low inductance ground for signal return current. This recommendation is in keeping with good high frequency board layout practices. Figure 3 and Figure 4 show two recommended termination schemes. 

The HFBR-5963xxZ series of transceivers meet MIL-STD883C Method 3015.4 Class 2 products. 

Care should be used to avoid shorting the receiver data or signal detect outputs directly to ground without proper current limiting impedance. 

AV02-1088EN 

Broadcom 

4 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Figure 3:  Recommended Decoupling and Termination Circuits** 


**----- Start of picture text -----**<br>
PHY DEVICE<br>VCC (+3.3 V)<br>TERMINATE AT<br>TRANSCEIVER  INPUTS Z = 50  Ω<br>TD-<br>100  Ω LVPECL<br>Z = 50  Ω<br>TD+<br>10     9      8      7      6 130  Ω 130  Ω<br>1 μH VCC (+3.3 V)<br>TX C2 C3 10 μF VCC (+3.3 V)<br>RX<br>1 μH<br>RD+<br>C1<br>1      2      3      4      5<br>Z = 50  Ω 100  Ω LVPECL<br>RD-<br>Z = 50  Ω<br>VCC (+3.3 V)<br>R1*<br>130  Ω 130  Ω<br>Z = 50  Ω 4.7K Ω SD<br>LVTTL<br>Notes: TERMINATE AT<br>C1 = C2 = C3 = 10 nF or 100 nF DEVICE INPUTS<br>* Loading of R1 is optional.<br>TD-   o TD+   o N/C   o VEE TX   o VCC TX   o<br>o   V EE R X o   V CC RX o   SD o   RD- o   RD+<br>**----- End of picture text -----**<br>


AV02-1088EN 5 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Figure 4:  Alternative Termination Circuits** 


**----- Start of picture text -----**<br>
TERMINATE AT<br>TRANSCEIVER  INPUTS<br>PHY DEVICE<br>VCC (+3.3 V)<br>VCC (+3.3 V)<br>10 nF<br>130  Ω 130   Ω<br>Z = 50  Ω<br>TD-<br>LVPECL<br>Z = 50   Ω<br>TD+<br>10     9      8      7       6 82  Ω 82  Ω<br>VCC (+3.3 V)<br>TX 1 μH VCC (+3.3 V)10 μF 10 nF VCC (+3.3 V)<br>RX C2 C3 130  Ω 130  Ω<br>RD+<br>1 μH<br>1      2      3      4      5<br>C1 LVPECL<br>Z = 50   Ω<br>RD-<br>VCC (+3.3 V)<br>Z = 50   Ω<br>82  Ω 82  Ω<br>R1*<br>Z = 50   Ω 4.7K Ω SD<br>LVTTL<br>Note: TERMINATE AT DEVICE INPUTS<br>TD-    o TD+    o N/C   o<br>VEE TX   o VCC TX   o<br>o   VEE R X o   VCC RX o   SD o   RD- o   RD+<br>**----- End of picture text -----**<br>


**Note: C1 = C2 = C3 = 10 nF or 100 nF * Loading R1 is optional.** 

## **Board Layout - Hole Pattern** 

## **Regulatory Compliance** 

The Broadcom transceiver complies with the circuit board Common Transceiver Footprint hole pattern defined in the original multisource announcement, which defined the 2 x 5 package style. This drawing is reproduced in Figure 6 with the addition of ANSI Y14.5M compliant dimensioning to be used as a guide in the mechanical layout of your circuit board. Figure 6 illustrates the recommended panel opening and the position of the circuit board with respect to this panel. 

These transceiver products are intended to enable commercial system designers to develop equipment that complies with the various international regulations governing certification of Information Technology Equipment. See Regulatory Compliance for details. Additional information is available from your Broadcom sales representative. 

AV02-1088EN 6 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Figure 5:  Package Outline Drawing** 


**----- Start of picture text -----**<br>
13.59 15.05<br>[0.535] [MAX] [0.593] [UNCOMPRESSED]<br>48.19<br>[1.897]<br>SEE DETAIL 1<br>10.8 6.24<br>9.8 MAX 13.63[0.536] [0.425] [UNCOMPRESSED] [0.246]<br>[0.386]<br>TX RX<br>8.89<br>[0.350]<br>10.16<br>14.68 [0.400]<br> 3.28  2.92 [0.578]<br>[0.129]  TYP [0.115] [MIN.]<br>Tcase REFERENCE POINT<br>� 1.07<br>2X<br>[0.042]<br>� 0.46<br>10X<br>[0.018] 5.72<br>[0.225]<br>10.16 11.84<br>[0.400] [0.466]<br>1.78 13.76<br>[0.070] [0.542]<br>AREA FOR<br>PROCESS PLUG<br>17.79 19.59<br>[0.700] [0.771]<br>DETAIL 1<br>Scale 3x<br>**----- End of picture text -----**<br>


All dimensions are in millimeters (inches). 

AV02-1088EN 7 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Figure 6:  Recommended Board Layout Hole Pattern and Panel Mounting** 


**----- Start of picture text -----**<br>
20 x Ø 0.81 ± .10<br>(.032 ± .004)<br>SEE DETAIL B<br>SEE NOTE 3<br>4 x Ø (.055 ± .004)1.40 ± .10 (NOTE 5) (1.014)25.75 SEE DETAIL A<br>13.34 12.16<br>(.525) (.479) 15.24 MIN. PITCH<br>(.600)<br>5 4 3 2 1 7.59 10.16<br>6 7 8 9 10 (.299) (.400)<br>2 x Ø             MAX. (AREA FOR EYELET'S)2.29<br>(.090)<br>4.57 2 x Ø 1.40 ± .10 (NOTE 4)<br>(.180) (.055 ± .004)<br>3<br>7.11<br>(.118)<br>(.280)<br>3.56 3<br>(.140) 8.89 (.118)<br>(.350) 6<br>1.78 (.236)<br> 9 X<br>(.070) DETAIL A (3 x)<br>1.8<br>.071<br>1<br>.039<br>15.24<br>            MIN. PITCH<br>(.600)<br>+ 1.50 DETAIL B (4 x)<br>1.00<br>-  0 14.22 ± .10<br>(.039) (+.059) A (.560 ± .004)<br>(- .000)<br>TOP OF PCB<br>A<br>10.16 ± .10<br>(.400 ± .004)<br>+ 0 A SECTION A - A<br>15.75<br>-  0.75<br>(+.000)<br>(.620)<br>(- .030)<br>**----- End of picture text -----**<br>


## **NOTE:** 

1. This page describes the recommended circuit board layout and front panel openings for SFF transceivers. 

2. The hatched areas are keep-out areas reserved for housing standoffs. No metal traces allowed in keep-out areas. 

3. This drawing shows extra pin holes for 2 x 6 pin and 2 x 10 pin transceivers. These extra holes are not required for HFBR-5961xxZ and other 2 x 5 pin SFF modules. 

4. Holes for mounting studs must not be tied to signal ground but can be tied to chassis ground. 

5. Holes for housing leads optional and not required for HFBR--5963xxZ. If needed in future, these holes must be tied to signal ground. 

6. All dimensions are in millimeters (inches). 

AV02-1088EN 

Broadcom 

8 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Electrostatic Discharge (ESD)** 

There are two design cases in which immunity to ESD damage is important. The first case is during handling of the transceiver prior to mounting it on the circuit board. It is important to use normal ESD handling precautions for ESD sensitive devices. These precautions include using grounded wrist straps, work benches, and floor mats in ESD controlled areas. 

The second case to consider is static discharges to the exterior of the equipment chassis containing the transceiver parts. To the extent that the LC connector is exposed to the outside of the equipment chassis it may be subject to whatever ESD system level test criteria that the equipment is intended to meet. 

## **Electromagnetic Interference (EMI)** 

Most equipment designs utilizing this high speed transceiver from Broadcom will be required to meet the requirements of FCC in the United States, CENELEC EN55022 (CISPR 22) in Europe, and VCCI in Japan. 

This product is suitable for use in designs ranging from a desktop computer with a single transceiver to a concentrator or switch product with a large number of transceivers. 

## **Immunity** 

Equipment utilizing these transceivers will be subject to radio-frequency electromagnetic fields in some environments. These transceivers have a high immunity to such fields. 

For additional information regarding EMI, susceptibility, ESD, and conducted noise testing procedures and results, refer to Application Note 1166: _Minimizing Radiated Emissions of High-Speed Data Communications Systems_ . 

## **Transceiver Reliability and Performance Qualification Data** 

The 2 x 5 transceivers have passed Broadcom reliability and performance qualification testing and are undergoing ongoing quality and reliability monitoring. Details are available from your Broadcom sales representative. 

These transceivers are manufactured at the Broadcom Singapore location, which is an ISO 9001 certified facility. 

## **Applications Support Materials** 

Contact your local Broadcom Component Field Sales Office for information on how to obtain PCB layouts and evaluation boards for the 2 x 5 transceivers. 

**Figure 7:  Transmitter Output Optical Spectral Width (FWHM) vs. Transmitter Output Optical Center Wavelength and Rise/ Fall Times** 


**----- Start of picture text -----**<br>
200<br>180 3.0 HFBR-5961xxZ TRANSMITTER<br>1.0 TEST RESULTS OF  λ C ,  Δλ   AND t r/f<br>ARE CORRELATED AND  COMPLY<br>WITH THE ALLOWED SPECTRAL<br>160 WIDTH AS A FUNCTION OF CENTER<br>1.5 WAVELENGTH FOR VARIOUS RISE<br>AND FALL TIMES.<br>140<br>2.0<br>120 2.5 tOUTPUT OPTICAL RISE/r/f  – TRANSMITTER<br>FALL TIMES – ns<br>3.0<br>100<br>1260 1280 1300 1320 1340 1360<br>λ C  – TRANSMITTER OUTPUT OPTICAL RISE/FALL TIMES – ns<br> - TRANSMITTER OUTPUT OPTICAL SPECTRAL WIDTH (FWHM) - nm<br>  Δλ<br>**----- End of picture text -----**<br>


**Figure 8:  Relative Input Optical Power vs. Eye Sampling Time Position** 


**----- Start of picture text -----**<br>
6<br>CONDITIONS:<br>1. T A  = +25 C<br>5 2. V CC  = 3.3 V dc<br>3. INPUT OPTICAL RISE/<br>    FALL TIMES = 2.1/1.9 ns.<br>4. INPUT OPTICAL POWER<br>4     IS NORMALIZED TO<br>    CENTER OF DATA SYMBOL.<br>5. NOTE 15 AND 16 APPLY.<br>3<br>2<br>1<br>0<br>-3 -2 -1 0 1 2 3<br>EYE SAMPLING TIME POSITION (ns)<br>RELATIVE INPUT OPTICAL POWER (dB)<br>**----- End of picture text -----**<br>


AV02-1088EN 

Broadcom 

9 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to the<br>Electrical Pins|MIL-STD-883C|Meets Class 2 (2000 to 3999 Volts).Withstand up to<br>2200V applied between electricalpins.|
|Electrostatic Discharge (ESD) to the<br>LC Receptacle|Variation of IEC 61000-4-2|Typically withstand at least 25 kV without damage<br>when the LC connector receptacle is contacted by a<br>Human BodyModelprobe.|
|Electromagnetic Interference (EMI)|FCC Class B<br>CENELEC CEN55022<br>VCCIClass 2|Transceivers typically provide a 10 dB margin to the<br>noted standard limits when tested at a certified test<br>range with the transceiver mounted to a circuit card<br>without a chassis enclosure.|
|Immunity|Variation of IEC 61000-4-3|Typically show no measurable effect from a 10 V/m<br>field swept from 80 MHz to 450 MHz applied to the<br>transceiver when mounted to a circuit card without a<br>chassis enclosure.|
|Eye Safety|AEL Class 1EN60825-1 (+A11)|Compliant per Broadcom testing under single fault<br>conditions.TUV Certification: R 02071015.|
|Component Recognition|Underwriters Laboratories and Canadian<br>Standards Association Joint Component<br>Recognition for Information Technology<br>Equipment Including Electrical Business<br>Equipment|UL File #: E173874.|



## **Absolute Maximum Ratings** 

Stresses in excess of the absolute maximum ratings can cause catastrophic damage to the device. Limits apply to each parameter in isolation, all other parameters having values within the recommended operating conditions. It should not be assumed that limiting values of more than one parameter can be applied to the product at the same time. Exposure to the absolute maximum ratings for extended periods can adversely affect device reliability. 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Storage Temperature|TS|–40|—|+100|°C||
|Lead Soldering Temperature|TSOLD|—|—|+260|°C||
|Lead Soldering Time|tSOLD|—|—|10|sec||
|Supply Voltage|VCC|–0.5|—|3.63|V||
|Data Input Voltage|VI|–0.5|—|VCC|V||
|Differential Input Voltage (p-p)|VD|—|—|2.0|V|a|
|Output Current|IO|—|—|50|mA||



a. This is the maximum voltage that can be applied across the Differential Transmitter Data Inputs to prevent damage to the input ESD protection circuit. 

AV02-1088EN 10 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Case Operating Temperature<br>HFBR-5963LZ<br>HFBR-5963ALZ|TC<br>TC|0<br>–40|—<br>—|+70<br>+85|°C<br>°C||
|Supply Voltage|VCC|2.97|3.3|3.63|V||
|Data Input Voltage, Low|VIL– VCC|–1.810|—|–1.475|V||
|Data Input Voltage, High|VIH– VCC|–1.165|—|–0.880|V||
|Data and Signal Detect Output Load|RL|—|50|—|Ω|a|
|Differential Input Voltage (p-p)|VD|—|0.800|—|V||



- a. The data outputs are terminated with 50Ω connected to VCC – 2V. The signal detect output is terminated with 50Ω connected to a pull-up resistor of 4.7 kΩ tied to VCC. 

## **Transmitter Electrical Characteristics** 

HFBR-5963LZ (TC = 0 °C to +70 °C, VCC = 2.97V to 3.63V) 

HFBR-5963ALZ (TC = –40 °C to +85 °C, VCC = 2.97V to 3.63V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|110|175|mA|a|
|Power Dissipation|PDISS|—|0.4|0.64|W|b|
|Data Input Current, Low|IIL|–350|–2|—|µA||
|Data Input Current, High|IIH|—|18|350|µA||



a. The power supply current needed to operate the transmitter is provided to differential ECL circuitry. This circuitry maintains a nearly constant current flow from the power supply. Constant current operation helps to prevent unwanted electrical noise from being generated and conducted or emitted to neighboring circuitry. 

b. The power dissipation of the transmitter is calculated as the sum of the products of supply voltage and current. 

AV02-1088EN 11 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Receiver Electrical Characteristics** 

HFBR-5963LZ (TC = 0 °C to +70 °C, VCC = 2.97V to 3.63V) 

HFBR-5963ALZ (TC = –40 °C to +85 °C, VCC = 2.97V to 3.63V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|65|120|mA|a|
|Power Dissipation|PDISS|—|0.225|0.44|W|b|
|Data Output Voltage, Low|VOL– VCC|–1.840|—|–1.620|V|c|
|Data Output Voltage, High|VOH– VCC|–1.045|—|–0.880|V|c|
|Data Output Rise Time|tr|0.35|—|2.2|ns|d|
|Data Output Fall Time|tf|0.35|—|2.2|ns|d|
|Signal Detect Output Voltage, Low|SDVOL|—|—|0.6|V|c|
|Signal Detect Output Voltage, High|SDVOH|2.2|—|—|V|c|
|Power SupplyNoise Rejection|PSNR|—|50|—|mV||



a. This value is measured with the outputs terminated into 50Ω connected to VCC – 2V and an Input Optical Power level of –14 dBm average. 

b. The power dissipation of the receiver is calculated as the sum of the products of supply voltage and currents, minus the sum of the products of the output voltages and currents. 

c. The data output low and high voltages are measured with respect to VCC with the output terminated into 50Ω connected to VCC – 2V. 

d. The data output rise and fall times are measured between 20% and 80% levels with the output connected to VCC – 2V through 50Ω. 

## **Transmitter Optical Characteristics** 

HFBR-5963LZ (TC = 0 °C to +70 °C, VCC = 2.97V to 3.63V) 

HFBR-5963ALZ (TC = –40 °C to +85 °C, VCC = 2.97V to 3.63V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|**Figure**|
|---|---|---|---|---|---|---|---|
|Output Optical Power                      BOL<br>62.5/125µm, NA = 0.275 Fiber<br>EOL|PO|–19<br>–20|–15.7<br>—|–14<br>—|dBm avg<br>dBm avg|a||
|Output Optical Power                      BOL<br>50/125µm, NA = 0.20 Fiber<br>EOL|PO|–22.5<br>–23.5|—<br>—|–14<br>—|dBm avg<br>dBm avg|a||
|Optical Extinction Ratio||—<br>—|0.002<br>–47|0.2<br>–27|%<br>dB|b||
|Output Optical Power at Logic Low 0 State|PO(“0”)|—|—|–45|dBm avg|c||
|Center Wavelength|λC|1270|1308|1380|nm|d|7|
|Spectral Width, FWHM<br>Spectral Width, RMS|Δλ|—<br>—|147<br>63|—<br>—|nm<br>nm|e, d|7|
|Optical Rise Time|tr|0.6|2.1|3.0|ns|f, d|7|
|Optical Fall Time|tf|0.6|1.9|3.0|ns|f, d|7|
|Systematic Jitter Contributed by the Transmitter, OC-3|SJ|—|0.4|1.2|ns p-p|g||
|Duty Cycle Distortion Contributed by the Transmitter, FE|DCD|—|0.36|0.6|ns p-p|h||
|Data Dependent Jitter Contributed by the Transmitter, FE|DDJ|—|0.07|0.6|ns p-p|i||



AV02-1088EN 

Broadcom 

12 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|**Figure**|
|---|---|---|---|---|---|---|---|
|Random Jitter Contributed by the Transmitter<br>OC-3<br>FE|RJ|—<br>—|0.1<br>0.1|0.52<br>0.69|ns p-p|j<br>k||



- a. These optical power values are measured with the following conditions: The Beginning of life (BOL) to the End of Life (EOL) optical power degradation is typically 1.5 dB per the industry convention for long wavelength LEDs. The actual degradation observed in the Broadcom 1300-nm LED products is <1 dB, as specified in this data sheet. Over the specified operating voltage and temperature ranges. With 25 MBd (12.5 MHz square-wave), input signal. At the end of one meter of noted optical fiber with cladding modes removed. The average power value can be converted to a peak power value by adding 3 dB. Higher output optical power transmitters are available on special request. Consult with your local Broadcom sales representative for further details. 

- b. The Extinction Ratio is a measure of the modulation depth of the optical signal. The data 0 output optical power is compared to the data 1 peak output optical power and expressed as a percentage. With the transmitter driven by a 25 MBd (12.5 MHz square-wave) input signal, the average optical power is measured. The data 1 peak power is then calculated by adding 3 dB to the measured average optical power. The data 0 output optical power is found by measuring the optical power when the transmitter is driven by a logic 0 input. The extinction ratio is the ratio of the optical power at the 0 level compared to the optical power at the 1 level expressed as a percentage or in decibels. 

- c. The transmitter will provide this low level of Output Optical Power when driven by a logic 0 input. This can be useful in link troubleshooting. 

- d. The HFBR-5963L transceiver complies with the requirements for the trade-offs between center wavelength, spectral width, and rise/fall times shown in Figure 7. This figure is derived from the FDDI PMD standard (ISO/IEC 9314-3 : 1990 and ANSI X3.166 - 1990) per the description in ANSI T1E1.2 Revision 3. The interpretation of this figure is that values of Center Wavelength and Spectral Width must lie along the appropriate Optical Rise/Fall Time curve. 

- e. The relationship between Full Width Half Maximum and RMS values for Spectral Width is derived from the assumption of a Gaussian shaped spectrum, which results in a 2.35 × RMS = FWHM relationship. 

- f. The optical rise and fall times are measured from 10% to 90% when the transmitter is driven by a 25 MBd (12.5 MHz square-wave) input signal. The ANSI T1E1.2 committee has designated the possibility of defining an eye pattern mask for the transmitter optical output as an item for further study. Broadcom will incorporate this requirement into the specifications for these products if it is defined. The HFBR-59XXL products typically comply with the template requirements of CCITT (now ITU-T) G.957 Section 3.2.5, Figure  for the STM- 1 rate, excluding the optical receiver filter normally associated with single mode fiber measurements, which is the likely source for the ANSI T1E1.2 committee to follow in this matter. 

- g. Systematic Jitter contributed by the transmitter is defined as the combination of Duty Cycle Distortion and Data Dependent Jitter. Systematic Jitter is measured at 50% threshold using a 155.52 MBd (77.5 MHz square-wave), 2[23] – 1 pseudorandom data pattern input signal. 

- h. Duty Cycle Distortion contributed by the transmitter is measured at the 50% threshold of the optical output signal using an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. 

- i. Data Dependent Jitter contributed by the transmitter is specified with the FDDI test pattern described in FDDI PMD Annex A.5. 

- j. Random Jitter contributed by the transmitter is specified with a 155.52 MBd (77.5 MHz square-wave) input signal. 

- k. Random Jitter contributed by the transmitter is specified with an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. 

AV02-1088EN 13 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

## **Receiver Optical and Electrical Characteristics** 

HFBR-5963LZ (TC = 0 °C to +70 °C, VCC = 2.97V to 3.63V) 

HFBR-5963ALZ (TC = –40 °C to +85 °C, VCC = 2.97V to 3.63V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|**Figure**|
|---|---|---|---|---|---|---|---|
|Input Optical Power at minimum at Window Edge<br>OC-3<br>FE|PIN MIN(W)|—<br>—|—<br>—|–30<br>–31|dBm avg|a, b|8|
|Input Optical Power at Eye Center<br>OC-3<br>FE|PIN MIN(C)|—<br>—|—<br>—|–31<br>–31.8|dBm avg|c, d|8|
|Input Optical Power Maximum<br>OC-3<br>FE|PIN MAX|–14<br>–14|—<br>—|—<br>—|dBm avg|a, b||
|OperatingWavelength|λ|1270|—|1380|nm|||
|Systematic Jitter Contributed by the Receiver, OC-3|SJ|—|0.2|1.2|ns p-p|e||
|Duty Cycle Distortion Contributed by the Receiver, FE|DCD|—|0.08|0.4|ns p-p|f||
|Data Dependent Jitter Contributed by the Receiver, FE|DDJ|—|0.07|1.0|ns p-p|g||
|Random Jitter Contributed by the Receiver<br>OC-3<br>FE|RJ|—<br>—|0.3<br>0.3|1.91<br>2.14|ns p-p|h<br>i||
|Signal Detect, Asserted, OC-3 FE|PA|PD+ 1.5 dB|—|–31–33|dBm avg|j||
|Signal Detect, Deasserted|PD|–45|—|—|dBm avg|k||
|Signal Detect, Hysteresis|PA– PD|1.5|—|—|dB|||
|Signal Detect Assert Time (off to on)||0|2|100|µs|l||
|Signal Detect Deassert Time (on to off)||0|5|100|µs|m||



a. This specification is intended to indicate the performance of the receiver section of the transceiver when Input Optical Power signal 

characteristics are present per the at the Beginning of Life (BOL) over the specified operating temperature and voltage ranges 23 input is a 155.52 MBd, 2 – 1 PRBS data pattern with 72 1s and 72 0s inserted per the CCITT (now ITU-T) recommendation G.958 Appendix I. Receiver data window time-width is 1.23 ns or greater for the clock recovery circuit to operate in. The actual test data window time-width is set to simulate the effect of worst-case optical input jitter based on the transmitter jitter values from the specification tables. The test window time-width is HFBR-5963L 3.32 ns. 

Transmitter operating with a 155.52 MBd, 77.5 MHz square-wave, input signal to simulate any crosstalk present between the transmitter and receiver sections of the transceiver. 

AV02-1088EN 14 

Broadcom 

Multimode Small Form Factor Transceivers for ATM, FDDI, Fast Ethernet, and SONET OC-3/SDH STM-1 with LC Connector 

**HFBR-5963LZ/ALZ** Data Sheet 

- b. This specification is intended to indicate the performance of the receiver section of the transceiver when Input Optical Power signal characteristics are present per the following definitions. The Input Optical Power dynamic range from the minimum level (with a window timewidth) to the maximum level is the range over which the receiver is guaranteed to provide output data with a Bit Error Rate (BER) better than or equal to 2.5 × 10[–10] . 

   - At the Beginning of Life (BOL). 

   - Over the specified operating temperature and voltage ranges. 

   - Input symbol pattern is the FDDI test pattern defined in FDDI PMD Annex A.5 with 4B/5B NRZI encoded data that contains a duty cycle 

   - base-line wander effect of 50kHz. This sequence causes a near worst-case condition for inter-symbol interference. 

   - Receiver data window time-width is 2.13 ns or greater and centered at mid-symbol. This worst-case window time-width is the minimum 

   - allowed eye-opening presented to the FDDI PHY PM_Data indication input (PHY input) per the example in FDDI PMD Annex E. This minimum window time-width of 2.13 ns is based upon the worst-case FDDI PMD Active Input Interface optical conditions for peak-to-peak DCD (1.0 ns), DDJ (1.2 ns), and RJ (0.76 ns) presented to the receiver. To test a receiver with the worst-case FDDI PMD Active Input jitter condition requires exacting control over DCD, DDJ, and RJ jitter components that is difficult to implement with production test equipment. The receiver can be equivalently tested to the worst case FDDI PMD input jitter conditions and meet the minimum output data window time-width of 2.13 ns. This is accomplished by using a nearly ideal input optical signal (no DCD, insignificant DDJ and RJ) and measuring for a wider window time-width of 4.6 ns. This is possible due to the cumulative effect of jitter components through their superposition (DCD and DDJ are directly additive and RJ components are rms additive). Specifically, when a nearly ideal input optical test signal is used and the maximum receiver peak-topeak jitter contributions of DCD (0.4 ns), DDJ (1.0 ns), and RJ (2.14 ns) exist, the minimum window time-width becomes 8.0 ns – 0.4 ns – 1.0 ns – 2.14 ns = 4.46 ns, or conservatively 4.6 ns. This wider window time-width of 4.6 ns guarantees the FDDI PMD Annex E minimum window time-width of 2.13 ns under worst-case input jitter conditions to the Broadcom receiver. 

   - Transmitter operating with an IDLE Line State pattern, 125 MBd (62.5 MHz square-wave), input signal to simulate any crosstalk present 

   - between the transmitter and receiver sections of the transceiver. 

- c. All conditions of Note a apply except that the measurement is made at the center of the symbol with no window time-width. 

- d. All conditions of Note b apply except that the measurement is made at the center of the symbol with no window time-width. 

- e. Systematic Jitter contributed by the receiver is defined as the combination of Duty Cycle Distortion and Data Dependent Jitter. Systematic Jitter is measured at 50% threshold using a 155.52 MBd (77.5 MHz square- wave), 2[23] – 1 pseudorandom data pattern input signal. 

- f. Duty Cycle Distortion contributed by the receiver is measured at the 50% threshold of the electrical output signal using an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. The input optical power level is –20 dBm average. 

- g. Data Dependent Jitter contributed by the receiver is specified with the FDDI DDJ test pattern described in the FDDI PMD Annex A.5. The input optical power level is –20 dBm average. 

- h. Random Jitter contributed by the receiver is specified with a 155.52 MBd (77.5 MHz square-wave) input signal. 

- i. Random Jitter contributed by the receiver is specified with an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. The input optical power level is at maximum PIN Min. (W). 

- j. This value is measured during the transition from low to high levels of input optical power. 

- k. This value is measured during the transition from high to low levels of input optical power. At Signal Detect Deassert, the receiver outputs Data Out and Data Out Bar go to steady PECL levels High and Low respectively. 

- l. The Signal Detect output shall be asserted within 100 μs after a step increase of the Input Optical Power. 

- m. Signal detect output shall be deasserted within 100 μs after a step decrease in the Input Optical Power. At Signal Detect Deassert, the receiver outputs Data Out and Data Out Bar go to steady PECL levels High and Low respectively 

## **Ordering Information** 

|HFBR-5963LZ|1300-nm LED|OperatingCase Temperature 0 °C to +70 °C|
|---|---|---|
|HFBR-5963ALZ|1300-nm LED|OperatingCase Temperature –40 °C to +85 °C|



AV02-1088EN 15 

Broadcom 

Broadcom, the pulse logo, Connecting everything, Avago Technologies, Avago, and the A logo are among the trademarks of Broadcom and/or its affiliates in the United States, certain other countries, and/or the EU. 

Copyright © 2005–2018 Broadcom. All Rights Reserved. 

The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, please visit www.broadcom.com. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

