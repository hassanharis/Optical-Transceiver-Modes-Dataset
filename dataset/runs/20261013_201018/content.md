## **HFBR-57E0LZ/ALZ/PZ/APZ** 

## Multimode Small Form Factor Pluggable Transceivers with LC connector for ATM, FDDI, Fast Ethernet and SONET OC-3/SDH STM-1 

## **Data Sheet** 


## **Description** 

The HFBR-57E0 Small Form Factor Pluggable LC transceivers provide the system designer with a product to implement a range of solutions for multimode fiber Fast Ethernet and SONET OC-3 (SDH STM-1) physical layers for ATM and other services. 

This transceiver operates at a nominal wavelength of 1300 nm with an LC fiber connector interface with an external connector shield (HFBR-57E0). 

## **Transmitter Section** 

The transmitter section of the HFBR-57E0 utilizes a 1300 nm InGaAsP LED. This LED is  packaged in the optical subassembly portion of the  transmitter section. It is driven by a custom silicon IC which  converts differential PECL logic signals, ECL referenced (shifted) to a +3.3 V supply, into an analog LED drive current. 

## **Receiver Section** 

The receiver section of the HFBR-57E0 utilizes an InGaAs PIN photodiode coupled to a custom silicon transimpedance preamplifier IC. It is packaged in the optical subassembly portion of the receiver. 

This PIN/preamplifier combination is coupled to a custom quantizer IC which provides the final pulse shaping for the logic output and the Loss of Signal (LOS) function. The data output is differential. The data output is PECL compatible, ECL referenced (shifted) to a +3.3 V power supply. This circuit also includes a loss of signal (LOS) detection circuit which provides an open collector logic high output in the absence of a usable input optical signal. The LOS output is +3.3 V TTL. 

## **Features** 

- RoHS compliant 

- Full compliance with ATM Forum UNI SONET OC-3 multimode fiber physical layer specification 

- Full compliance with the optical performance requirements of the FDDI PMD Standard 

- Full compliance with the optical performance requirements of 100Base-FX version of IEEE802.3u 

- Industry standard Small Form  Pluggable (SFP) package 

- LC duplex connector optical interface 

- Operates with 62.5/125 μm and 50/125 μm multimode fiber 

- Single +3.3 V power supply 

- +3.3 V TTL LOS output 

- Receiver outputs are squelch enabled 

- Manufactured in an ISO 9001 certified facility 

- Temperature range: 

   - 0 °C to +70° C HFBR-57E0LZ/PZ: 

   - -40 °C to +85 °C HFBR-57E0ALZ/APZ: 

- Bail de-latch option 

## **Applications** 

- OC-3 SFP transceivers are designed for ATM LAN and WAN applications such as: 

   - ATM switches and routers 

   - SONET/SDH switch infrastructure 

- Multimode fiber ATM backbone links 

- Fast Ethernet 

## **Loss of Signal** 

The Loss of Signal (LOS) output indicates that the optical input signal to the receiver does not meet the minimum detectablelevel for FDDI and OC-3 compliant signals. When LOS is high it indicates loss of signal. When LOS is low it indicates normal operation. The LOS thresholds are set to indicate a definite optical fault has occurred (e.g., disconnected or broken fiber connection to receiver, failed transmitter). 

## **Module Package** 

The transceiver meets the Small Form Pluggable (SFP) industry standard package utilizing an integral LC duplex optical interface connector. The hot-pluggable capability of the SFP package allows the module to be installed at any time – even with the host system operating and on-line. This allows for system configuration changes or maintenance without system down time. The HFBR-57E0 uses a reliable 1300 nm LED source and requires a 3.3 V dc power supply for optimal design. 

## **Module Diagrams** 

Figure 1 illustrates the major functional components of the HFBR-57E0. The connection diagram of the module is shown in Figure 2. Figures 5 and 7 depict the external configuration and dimensions of the module. 

## **Installation** 

The HFBR-57E0 can be installed in or removed from any MultiSource Agreement (MSA) – compliant Small Form Pluggable port regardless of whether the host equip- 


**----- Start of picture text -----**<br>
20 V EET 1 VEET<br>19 TD- 2 NC**<br>18 TD+ 3 Tx Disable<br>17 VEET 4 MOD-DEF(2)<br>16 VCC T 5 MOD-DEF(1)<br>15 V CC R 6 MOD-DEF(0)<br>14 V EER 7 NC<br>13 RD+ 8 LOS<br>12 RD- 9 VEER<br>11 VEER 10 VEER<br>TOP OF BOARD BOTTOM OF BOARD<br>(AS VIEWED THROUGH TOP OF BOARD)<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
**  Connect to Internal Ground.<br>**----- End of picture text -----**<br>


**Figure 2.  Connection diagram of module printed circuit board.** 

ment is operating or not. The module is simply inserted, electrical interface first, under finger pressure. Controlled hot-plugging is ensured by design and by 3-stage pin sequencing at the electrical interface. The module housing makes initial contact with the host board EMI shield mitigating potential damage due to Electro-Static Discharge (ESD). The 3-stage pin contact sequencing involves (1) Ground, (2) Power, and then (3) Signal pins, making contact with the host board surface mount connector in that order. This printed circuit board card-edge connector is depicted in Figure 2. 


**----- Start of picture text -----**<br>
OPTICAL INTERFACE ELECTRICAL INTERFACE<br>RECEIVER<br>RD+ (Receive Data)<br>Light from Fiber Photodetector Amplification & RD- (Receive Data)<br>Quantizattion<br>Loss of Signal<br>TRANSMITTER<br>TD+ (Transmit Data)<br>Light to Fiber LED LED DRIVER<br>TD- (Transmit Data)<br>TX Disable<br>MOD-DEF2<br>EEPROM MOD-DEF1<br>MOD-DEF0<br>**----- End of picture text -----**<br>


**Figure 1.  Transceiver functional diagram** 

2 

## **Serial Identification (EEPROM)** 

The HFBR-57E0 complies with the industry standard MSA that defines the serial identification protocol. This protocol uses the 2-wire serial CMOS E2PROM protocol of the ATMEL AT24C01A or equivalent. The contents of the HFBR-57E0 serial ID memory are defined in Table 3 as specified in the SFP MSA. 

## **Functional Data I/O** 

The HFBR-57E0 fiberoptic transceiver is designed to accept industry standard differential signals. In order to reduce the number of passive components required on the customer’s board, Avago has included the functionality of the transmitter bias resistors and coupling capacitors within the fiberoptic module. The transceiver is compatible with an “ac-coupled” configuration and is internally terminated. Figure 5 depicts the functional diagram of the HFBR-57E0. 

## **Regulatory Compliance** 

See Table 1 for transceiver Regulatory Compliance performance. The overall equipment design will determine the certification level. The transceiver performance is offered as a figure of merit to assist the designer. 

## **Electrostatic Discharge (ESD)** 

There are two conditions in which immunity to ESD damage is important. Table 1 documents our immunity to both of these conditions. The first condition is during handling of the transceiver prior to insertion into the transceiver port. To protect the transceiver, it is important to use normal ESD handling precautions. 

These precautions include using grounded wrist straps, workbenches, and floor mats in ESD controlled areas. The ESD sensitivity of the HFBR-57E0 is compatible with typical industry production environments. The second condition is static discharges to the exterior of the host equipment chassis after installation. To the extent that the duplex LC optical interface is exposed to the outside of the host equipment chassis, it may be subject to systemlevel ESD requirements. The ESD performance of the HFBR-57E0 exceeds typical industry standards. 

## **Immunity** 

Equipment hosting the HFBR-57E0 modules will be subjected to radio-frequency electro magnetic fields in some environments. These transceivers have good immunity to such fields due to their shielded design. 

**Table 1.  Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD)|MIL-STD-883C|Meets Class 2 (2000 to 3999 Volts).Withstand up to|
|to the Electrical Pins||2200 V applied between electrical pins.|
|Electrostatic Discharge (ESD)|Variation of IEC 61000-4-2|Typically withstand at least 25 kV without damage|
|to the Duplex LC Receptacle||when the LC connector receptacle is contacted by|
|||a Human Body Model probe.|
|Electromagnetic Interference|FCC Class B|System margins are dependent on customer|
|(EMI)|CENELEC CEN55022|board and chassis design.|
||Class B (CISPR 21)||
||VCCI Class 1||
|Immunity|Variation of IEC 61000-4-3|Typically shows a negligible efect from a 10 V/m|
|||feld swept from 80 to 450 MHz applied to the|
|||transceiver without a chassis enclosure.|
|Eye Safety|AEL Class 1|Compliant per Avago testing under single fault|
||EN60825-1 (+A11)|conditions.|
|||TUV Certifcation:  R 72042022|
|Component Recognition|Underwriters Laboratories and Ca-|UL File#: E173874|
||nadian Standard Associations Joint||
||Component Recognition for Informa-||
||tion Technology Equipment Including||
||Electrical Business Equipment||
|RoHS Compliance||Reference to EU RoHS Directive 2002/95/EC|



3 

## **Electromagnetic Interference (EMI)** 

Most equipment designs utilizing these high-speed transceivers from Avago will be required to meet the requirements of FCC in the United States, CENELEC EN55022 (CISPR 22) in Europe and VCCI in Japan. 

The metal housing and shielded design of the HFBR-57E0 minimize the EMI challenge facing the host equipment designer. These transceivers provide superior EMI performance. This greatly assists the designer in the management of the overall system EMI performance. 

## **Eye Safety** 

These transceivers provide Class 1 eye safety by design. Avago has tested the transceiver design for compliance with the requirements listed in Table 1 under normal operating conditions and under a single fault condition. 

## **Flammability** 

The HFBR-57E0 transceiver housing is made of metal and high strength, heat resistant, chemically resistant, and UL 94V-0 flame retardant plastic. 

## **Shipping Container** 

The transceiver is packaged in a shipping container designed to protect it from mechanical and ESD damage during shipment or storage. 

## **Transceiver Optical Power Budget versus Link Length** 

Optical Power Budget (OPB) is the available optical power for a fiberoptic link to accommodate fiber cable loses plus losses due to in-line connectors, splices, optical switches, and to provide margin for link aging and unplanned losses due to cable plant reconfiguration or repair. 

Avago LED technology has produced 1300 nm LED devices with lower aging characteristics than normally associated with these technologies in the industry. The industry convention is 1.5 db aging for 1300 nm LEDs. The 1300 nm Avago LEDs are specified to experience less than 1 db of aging over normal commercial equipment mission life periods. Contact your Avago sales representative for additional details. 

## **Ordering Information** 

The HFBR-57E0 1300 nm product is available for production orders through the Avago Component Field Sales Offices and Authorized Distributors worldwide. 

For technical information regarding this product, please visit the Avago website at www.avagotech.com. 

Use the quick search feature to search for this part number. You may also contact the Avago Products Customer Response Centre. 

## **Applications Support Materials** 

Contact your local Avago Component Field Sales Office for information on how to obtain PCB layouts and evaluation boards for the transceivers. 


**----- Start of picture text -----**<br>
200<br>3.0<br>180<br>1.0<br>160<br>1.5<br>140<br>2.0<br>120 2.5 OUTPUT OPTICAL RISE/tr/f  – TRANSMITTER<br>FALL TIMES – ns<br>3.0<br>100<br>1260 1280 1300 1320 1340 1360<br>l  C  – TRANSMITTER OUTPUT OPTICAL RISE/FALL TIMES – ns<br>HFBR-57E0 TRANSMITTER TEST RESULTS<br>OF  l C , Dl   AND t r/f  [ARE CORRELATED AND  COMPLY]<br>WITH THE ALLOWED SPECTRAL WIDTH AS A FUNCTION<br>OF CENTER WAVELENGTH FOR VARIOUS RISE AND<br>FALL TIMES.<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>-3 -2 -1 0 1 2 3<br>EYE SAMPLING TIME POSITION (ns)<br>CONDITIONS:<br>1. T A = +25 C<br>2. V CC  = 3.3 V dc<br>3. INPUT OPTICAL RISE/FALL TIMES = 1.0/2.1 ns.<br>4. INPUT OPTICAL POWER IS NORMALIZED TO<br>    CENTER OF DATA SYMBOL.<br>5. NOTE 13 AND 14 APPLY.<br>RELATIVE INPUT OPTICAL POWER (dB)<br>SPECTRAL WIDTH (FWHM) - nm<br>  Dl  - TRANSMITTER OUTPUT OPTICAL<br>**----- End of picture text -----**<br>


**Figure 3.  Transmitter Output Optical Spectral Width (FWHM) vs. Transmitter Output Optical Center Wavelength and Rise/Fall Times** 

**Figure 4.  Relative Input Optical Power vs. Eye Sampling Time Position** 

4 


**----- Start of picture text -----**<br>
1 μH<br>3.3 V<br>10 μF 0.1 μF 1 μH 0.1 μF<br>3.3 V<br>Vc cT HFBR-57E0<br>4.7 K to 10 K<br>Tx Dis<br>3.3 V<br>82  Ω 82 Ω<br>50  Ω TD+ 0.1 μF<br>SO+<br>LED DRIVER<br>& SAFETY<br>SO– 50  Ω TD– CIRCUITRY<br>TX GND<br>0.1 μF<br>130  Ω 130  Ω<br>PROTOCOLIC SerDes 4.7 K to 10 K 10 μF 0.1μF VccR130  Ω 130  Ω 3.3 V<br>50  Ω RD+ 0.1 μF<br>SI+<br>AMPLIFICATION<br>SI– 50  Ω RD– &<br>QUANTIZATION<br>Rx_LOS 0.1 μF<br>Rx_LOS<br>RX GND<br>82  Ω 82  Ω<br>MOD_DEF2<br>GPIO(X)<br>MOD_DEF1<br>GPIO(X) EEPROM<br>MOD_DEF0<br>GP14<br>4.7 K to 4.7 K to 4.7 K to<br>10 K 10 K 10 K<br>3.3 V<br>**----- End of picture text -----**<br>


**Figure 5.  Recommended application configuration** 


**----- Start of picture text -----**<br>
1 μH<br>V CC T<br>0.1 μF<br>1 μH<br>V CC R 3.3 V<br>0.1 μF 10 μF 0.1 μF 10 μF<br>SFP MODULE HOST BOARD<br>**----- End of picture text -----**<br>


Note:   Inductors must have less than 1 ohm series resistance per MSA. 

**Figure 6.  MSA required power supply filter** 

5 

**Table 2.  Pin Description** 

|**Pin**|**Name**|**Function/Description**|**MSA Notes**|
|---|---|---|---|
|1|VEET|Transmitter Ground||
|2|NC|NC|1|
|3|Tx Disable|Transmitter Disable- Module disables on high or open||
|4|MOD-DEF2|Module Defnition 2 - Two Wire Serial ID Interface|2|
|5|MOD-DEF1|Module Defnition 1 - Two Wire Serial ID Interface|2|
|6|MOD-DEF0|Module Defnition 0 - grounded in module|2|
|7|NC|NC||
|8|LOS|Loss of Signal - high indicates loss of signal|3|
|9|VEER|Receiver Ground||
|10|VEER|Receiver Ground||
|11|VEER|Receiver Ground||
|12|RD-|Inverse Received Data Out|4|
|13|RD+|Received Data Out|4|
|14|VEER|Receiver Ground||
|15|VCCR|Receiver Power -3.3 V ± 10%|5|
|16|VCCT|Transmitter Power -3.3 V ± 10%|5|
|17|VEET|Transmitter Ground||
|18|TD+|Transmitter Data In|6|
|19|TD-|Inverse Transmitter Data In|6|
|20|VEET|Transmitter Ground||



## **Notes:** 

1. Pin 2 connected to internal ground. 

2. Mod-Def 0, 1, 2. are the module definition pins. They should be pulled up with a 4.7 K - 10 K� resistor on the host board to a supply less than VCCT +0.3 V or VCCR +0.3 V. 

   - Mod-Def 0 is grounded by the module to indicate that the module is present. 

   - Mod-Def 1 is clock line of two wire serial interface for optional serial ID. 

   - Mod-Def 2 is data line of two  wire serial interface for optional serial ID. 

3. LOS (Loss of Signal) is an open collector/drain output which should be pulled up externally with a 4.7 - 10 K��resistor on the host board to a supply < VCCT, R +0.3 V.  When high, this output indicates the received optical power is below the worst case receiver sensitivity (as defined by the standard in use).  Low indicates normal operation.  In the low state, the output will be pulled to <0.8 V. 

4. RD-/+:  These are the differential receiver outputs.  They are ac coupled 100 ��differential lines which should be terminated with 100 � differential at the SERDES.  The ac coupling is done inside the module and is thus not required on the host board.  The voltage swing on these lines will be between 400 and 2000 mV differential (200 - 1000 mV single ended) when properly terminated. 

5. VCCR and VCCT are the receiver and transmitter power supplies.  They are defined as 2.97 - 3.63 V at the SFP connector pin.  The maximum supply current is 230 mA and the associated in-rush current will typically be no more than 30 mA above steady state after 500 nanoseconds. 

6. TD-/+:  These are the differential transmitter inputs.  They are ac coupled differential lines with 100 � differential termination inside the module. The ac coupling is done inside the module and is thus not required on the host board.  The inputs will accept differential swings of 400 - 2000 mV  (200 - 1000 mV single ended), though it is recommended that values between 400 and 1200 mV differential (200 - 600 mV single ended) be used for best EMI performance.  These levels are compatible with CML and LVPECL voltage swings. 

6 

**Table 3.  EEPROM Serial ID Memory Contents** 

|**Add**<br>**Hex**|**ASCII**<br>**Add**<br>**Hex**<br>**ASCII**<br>**Add**<br>**Hex**<br>**ASCII**<br>**Add**<br>**Hex**<br>**ASCII**|
|---|---|
|0<br>03|33<br>20<br>63<br>Note 3<br>95<br>Note 3|
|1<br>04|34<br>20<br>64<br>00<br>96<br>Note 5|
|2<br>07|35<br>20<br>65<br>12<br>97<br>Note 5|
|3<br>00|36<br>00<br>66<br>00<br>98<br>Note 5|
|4<br>00|37<br>00<br>67<br>00<br>99<br>Note 5|
|5<br>01, Note 6|38<br>17<br>68<br>Note 1<br>100<br>Note 5|
|6<br>20, Note 6|39<br>6A<br>69<br>Note 1<br>101<br>Note 5|
|7<br>00|40<br>48<br>H<br>70<br>Note 1<br>102<br>Note 5|
|8<br>00|41<br>46<br>F<br>71<br>Note 1<br>103<br>Note 5|
|9<br>00|42<br>42<br>B<br>72<br>Note 1<br>104<br>Note 5|
|10<br>00|43<br>52<br>R<br>73<br>Note 1<br>105<br>Note 5|
|11<br>03, Note 7|44<br>2D<br>-<br>74<br>Note 1<br>106<br>Note 5|
|12<br>02, Note 8|45<br>35<br>5<br>75<br>Note 1<br>107<br>Note 5|
|13<br>00|46<br>37<br>7<br>76<br>Note 1<br>108<br>Note 5|
|14<br>00|47<br>45<br>E<br>77<br>Note 1<br>109<br>Note 5|
|15<br>00|48<br>30<br>0<br>78<br>Note 1<br>110<br>Note 5|
|16<br>C8|49<br>41, Note 4<br>A<br>79<br>Note 1<br>111<br>Note 5|
|17<br>C8|50<br>50, Note 4<br>P<br>80<br>Note 1<br>112<br>Note 5|
|18<br>00|51<br>5A, Note 4<br>Z<br>81<br>Note 1<br>113<br>Note 5|
|19<br>00|52<br>20, Note 4<br>82<br>Note 1<br>114<br>Note 5|
|20<br>41|A<br>53<br>20, Note 4<br>83<br>Note 1<br>115<br>Note 5|
|21<br>56|V<br>54<br>20<br>84<br>Note 2<br>116<br>Note 5|
|22<br>41|A<br>55<br>20<br>85<br>Note 2<br>117<br>Note 5|
|23<br>47|G<br>56<br>30<br>0<br>86<br>Note 2<br>118<br>Note 5|
|24<br>4F|O<br>57<br>30<br>0<br>87<br>Note 2<br>119<br>Note 5|
|25<br>20|58<br>30<br>0<br>88<br>Note 2<br>120<br>Note 5|
|26<br>20|59<br>30<br>0<br>89<br>Note 2<br>121<br>Note 5|
|27<br>20|60<br>05<br>90<br>Note 2<br>122<br>Note 5|
|28<br>20|61<br>1E<br>91<br>Note 2<br>123<br>Note 5|
|29<br>20|62<br>00<br>92<br>00<br>124<br>Note 5|
|30<br>20|93<br>00<br>125<br>Note 5|
|31<br>20|94<br>00<br>126<br>Note 5|
|32<br>20|127<br>Note 5|



1. Addresses 68 - 83 specify a unique identifier. 

2. Addresses 84 - 91 specify the date code. 

3. Addresses 63 and 95 are check sums.  Address 63 is the check sum for bytes 0 - 62 and address 95 is the check sum for bytes 64 - 94. 

4. Part number options LZ, PZ, ALZ, APZ, etc. Example: for “AP” option, hexes in addresses 49, 50, 51, 52 and 52 will be 41, 50, 5A, 20 and 20 respectively. 

5. Addresses 96-127 are vendor specific data. 

6. Addresses 5 and 6 specify compliance code.  Address 5 with Hex 01 for OC-3 and address 6 with Hex 20 for Fast Ethernet. 

7. Address 11 specifies encoding code.  Hex 03 for OC-3 and Hex 02 for Fast Ethernet. 

8. Address 12 specifies bit rate.  Hex 02 for OC-3 and Hex 01 for Fast Ethernet. 

7 


**----- Start of picture text -----**<br>
AVAGO HFBR-57E0xxZ<br>YYWW<br>Country of Origin<br>Tcase Reference Point<br>13.8±0.1 13.4±0.1<br>[0.541±0.004] [0.528±0.004]<br>DEVICE SHOWN WITH 2.60<br>DUST CAP AND BAIL [0.10] 55.2±0.2<br>WIRE DELATCH  [2.17±0.01]<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
FRONT EDGE OF SFP<br>0.7MAX. UNCOMPRESSED<br>6.25±0.05 TRANSCEIVER CAGE<br>[0.028]<br>[0.246±0.002]<br>13.0±0.2<br>8.5±0.1<br>[0.512±0.008]<br>[0.335±0.004]<br>TX RX<br>AREA<br>FOR<br>PROCESS<br>PLUG<br>DIMENSIONS ARE IN MILLIMETERS (INCHES)<br>6.6<br>[0.261]<br>13.50<br>[0.53]<br>14.8MAX. UNCOMPRESSED<br>[0.583]<br>**----- End of picture text -----**<br>


**Figure 7. Module Drawing** 

8 


**----- Start of picture text -----**<br>
X<br>Y<br>34.5<br>10<br>3x<br>10x ∅ 1.05 ± 0.01 7.2 7.1<br>16.25 ∅ 0.1   L  X  A    S  2.5 ∅ 0.85 ± 0.05<br>MIN. PITCH 1 ∅ 0.1  S   X   Y<br>2.5<br>PCB B A 1<br>EDGE 3.68<br>5.68 PIN 1 20<br>8.58 2x 1.7 8.48<br>11.08 11.93<br>16.25REF . [14.25] 9.6<br>4.8<br>11<br>10<br>SEE DETAIL 1<br>2.0 9x 0.95 ± 0.05<br>11x 11x 2.0 ∅ 0.1  L   X   A   S<br>26.8 5 2<br>3 10<br>3x<br>41.3<br>42.3<br>5<br>3.2<br>20x 0.5 ± 0.03<br>0.9<br>0.06  L   A    S   B  S<br>PIN 1 20 LEGEND<br>10.93 10.53 1. PADS AND VIAS ARE CHASSIS GROUND<br>11.93<br>9.6<br>0.8 2. THROUGH HOLES, PLATING OPTIONAL<br>TYP.<br>11 3. HATCHED AREA DENOTES COMPONENT<br>10 AND TRACE KEEPOUT (EXCEPT<br>CHASSIS GROUND)<br>4. AREA DENOTES COMPONENT<br>KEEPOUT (TRACES ALLOWED)<br>4<br>2 ± 0.005 TYP. DIMENSIONS ARE IN MILLIMETERS<br>2x 1.55 ± 0.05<br>0.06    L    A  S    B   S<br>∅ 0.1    L   A   S   B   S DETAIL 1<br>**----- End of picture text -----**<br>


**Figure 8. SFP host board mechanical layout** 

9 


**----- Start of picture text -----**<br>
1.7±0.9<br>[.07±.04]<br>3.5±0.3<br>[.14±.01]<br>41.73±0.5<br>PCB<br>[1.64±.02]<br>AREA<br>BEZEL FOR<br>PROCESS<br>PLUG<br>15MAX<br>.59<br>Tcase REFERENCE POINT<br>CAGE<br>ASSEMBLY<br>15.25±0.1<br>[.60±0.004] 10.4±0.1<br>12.4REF<br>[.41±0.004]<br>.49<br>10REF<br>1.15REF<br>9.8MAX .39<br>.39 .05 TO PCB 16.25±0.1MIN PITCH<br>BELOW PCB<br>0.4±0.1 [.64±0.004]<br>[.02±0.004]<br>BELOW PCB<br>MSA-SPECIFIED BEZEL<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
DIMENSIONS ARE IN MILLIMETERS [INCHES].<br>**----- End of picture text -----**<br>


**Figure 9. SFP Assembly Drawing** 

10 

## **Absolute Maximum Ratings** 

Stresses in excess of the absolute maximum ratings can cause catastrophic damage to the device. Limits apply to each parameter in isolation, all other parameters having values within the recommended operating conditions. It should not be assumed that limiting values of more than one parameter can be applied to the product at the same time. Exposure to the absolute maximum ratings for extended periods can adversely affect device reliability. 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Storage Temperature|TS|-40||+100|°C||
|Supply Voltage|VCC|-0.5||3.63|V||
|Data Input Voltage|VI|-0.5||VCC|V||
|Diferential Input Voltage (p-p)|VD|||2.4|V|1|
|Output Current|IO|||50|mA||



## **Recommended Operating Conditions** 

|**ecommended Operating Conditions**|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|Case Operating Temperature|||||||
|HFBR-57E0LZ/PZ|TC|0||+70|°C||
|HFBR-57E0ALZ/APZ|TC|-40||+85|°C||
|Supply Voltage|VCC|2.97|3.3|3.63|V||
|Data Input: Transmitter Diferential Input|VI|0.5|0.8|2.4|V||
|Voltage (TD+/-)|||||||
|Data and Loss of Signal Output Load|RL||50||�|2|



## **Transmitter Electrical Characteristics** 

HFBR-57E0LZ/PZ (TC  =  0 ºC to +70 ºC, VCC = 2.97 V to 3.63 V) HFBR-57E0ALZ/APZ (TC = -40 ºC to +85 ºC, VCC = 2.97 V to 3.63 V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC||165|210|mA|3|
|Power Dissipation|PDISS||0.55|0.80|W|5a|
|Transmitter Disable (TX Disable) High|VIH|2.0||3.5|V||
|Transmitter Disable (TX Disable) Low|VIL|0||0.8|V||



## **Receiver Electrical Characteristics** 

HFBR-57E0LZ/PZ (TC =  0 ºC to +70 ºC, VCC = 2.97 V to 3.63 V) HFBR-57E0ALZ/APZ (TC = -40 ºC to +85 ºC, VCC = 2.97 V to 3.63 V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC||95|150|mA|4|
|Power Dissipation|PDISS||0.35|0.55|W|5b|
|Data Output: Receiver Diferential Output|VO|0.4||2.0|V|6a6b|
|Voltage (RD+/-)|||||||
|Data Output Rise Time|tr|0.35||2.2|ns|7|
|Data Output Fall Time|tf|0.35||2.2|ns|7|
|Loss of Signal Output Voltage - Low|LOSVOL|||0.8|V|6a|
|Loss of Signal Output Voltage - High|LOSVOH|2.0|||V|6a|
|Power Supply Noise Rejection|PSNR||50||mV||



11 

Notes: 

1. This is the maximum voltage that can be applied across the Differential Transmitter Data Inputs to prevent damage to the input ESD protection circuit. 

2. The data outputs are terminated with  50� . 

   - The Loss of Signal output is terminated with 50 � connected to a pull-up resistor of 4.7 K� tied to VCC. 

3. The power supply current needed to operate the transmitter is provided to differential ECL circuitry. This circuitry maintains a nearly constant current flow from the power supply. Constant current operation helps to prevent unwanted electrical noise from being generated and conducted or emitted to neighboring circuitry. 

4. This is the receiver supply current measured in mA. 

- 5a. The power dissipation of the transmitter is calculated as the sum of the products of supply voltage and current. 

- 5b.  The power dissipation of the receiver is calculated as the sum of the products     of supply voltage and currents, minus the sum of the products of the output voltages and currents. 

- 6a. Differential Output Voltage is internally ac coupled.  The Loss of Signal low and high voltages are measured with load condition as mentioned in note 2. 

- 6b. Data and Data-bar outputs are squelched at LOS assert level. When the received light  drops below LOS assert point, it will force receiver data and data-bar to go to steady PECL levels High and Low respectively. 

7. The data output rise and fall times are measured between 20% and 80% levels. 

## **Transmitter Optical Characteristics** 

HFBR-57E0LZ/PZ(TC =  0 ºC to +70 ºC, VCC = 2.97 V to 3.63 V) HFBR-57E0ALZ/APZ (TC = -40 ºC to +85 ºC, VCC = 2.97 V to 3.63 V) 

|FBR-57E0ALZ/APZ (TC= -40 ºC to +85 ºC, V|CC= 2.97 V|to 3.63 V)|||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|Output Optical Power                     BOL|PO|-19|-15.7|-14|dBm avg|8|
|62.5/125  μm, NA = 0.275 Fiber    EOL||-20|||||
|Output Optical Power                     BOL|PO|-22.5||-14|dBm avg|8|
|50/125  μm, NA = 0.20 Fiber         EOL||-23.5|||||
|Transmitter Disable (High)|PO(of)|||-45|dBm||
|Center Wavelength|�C|1270|1308|1380|nm|21, Figure 3|
|Spectral Width - FWHM|��||147||nm|9, 21, Figure 3|
|Spectral Width - RMS|||63||||
|Optical Rise Time|tr|0.6|1.2|3.0|ns|10, 21, Figure 3|
|Optical Fall Time|tf|0.6|2.0|3.0|ns|10, 21, Figure 3|
|Systematic Jitter Contributed by the Transmit-|SJ||0.25|1.2|ns p-p|11a|
|ter - OC-3|||||||
|Duty Cycle Distortion Contributed by the|DCD||0.20|0.6|ns p-p|11b|
|Transmitter - FE|||||||
|Data Dependent Jitter Contributed by the|DDJ||0.07|0.6|ns p-p|11c|
|Transmitter - FE|||||||
|Random Jitter Contributed by the Transmitter|RJ||||||
|OC-3|||0.10|0.52|ns|12a|
|FE|||0.10|0.69|p-p|12b|



Notes: 

8. These optical power values are measured with the following conditions: 

   - The Beginning of Life (BOL) to the End of Life (EOL) optical power degradation is typically 1.5 dB per the industry convention for long wavelength LEDs. The actual degradation observed in Avago’s 1300 nm LED products is < 1 dB, as specified in this data sheet.  Over the specified operating voltage and temperature ranges.  With 25 MBd (12.5 MHz square-wave), input signal. 

   - At the end of one meter of noted optical fiber with cladding modes removed. The average power value can be converted to a peak power value by adding 3 dB. Higher output optical power transmitters are available on special request. Please consult with your local Avago sales representative for further details. 

9. The relationship between Full Width Half Maximum and RMS values for Spectral Width is derived from the assumption of a Gaussian shaped spectrum which results in a 2.35 X RMS = FWHM relationship. 

10.  The optical rise and fall times are measured from 10%  to 90%  when the transmitter is driven by a 25 MBd (12.5 MHz square-wave) input signal. The ANSI T1E1.2 committee has designated the possibility of defining an eye pattern mask for the transmitter optical output as an item for further study. Avago will incorporate this requirement into the specifications for these products if it is defined. The  HFBR-57E0 products typically comply with the template requirements of CCITT (now ITU-T) G.957 Section 3.2.5,  Figure 2 for the STM- 1 rate, excluding the optical receiver filter normally associated with single mode fiber measurements which is the likely source for the ANSI T1E1.2 committee to follow in this matter. 

12 

## **Notes:** 

- 11a. Systematic Jitter contributed by the transmitter is defined as the combination of Duty Cycle Distortion and Data Dependent Jitter. Systematic Jitter is measured at 50%  threshold using a 155.52 MBd (77.5 MHz square-wave), 2[23] - 1 psuedorandom data pattern input signal. 

- 11b. Duty Cycle Distortion contributed by the transmitter is measured at the 50% threshold of the optical output signal using an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. 

- 11c. Data Dependent Jitter contributed by the transmitter is specified with the FDDI test pattern described in FDDI PMD Annex A.5. 

- 12a. Random Jitter contributed by the transmitter is specified with a 155.52 MBd (77.5 MHz square-wave) input signal. 

- 12b. Random Jitter contributed by the transmitter is specified with an IDLE Line State, 125 MBd (62.5 MHz square-wave) input signal.  See Application Information - Transceiver Jitter Performance Section of this data sheet for further details. 

## **Receiver Optical and Electrical Characteristics** 

HFBR-57E0LZ /PZ(TC =  0 ºC to +70 ºC, VCC = 2.97 V to 3.63 V) HFBR-57E0ALZ/APZ (TC = -40 ºC to +85 ºC, VCC = 2.97 V to 3.63 V) 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Input Optical Power minimum at Window Edge|PIN MIN(W)|||||13a,|
|OC-3||||-30|dBm avg|Figure 4|
|FE||||-31||13b|
|Input Optical Power at Eye Center|PIN MIN(C)||||dBm avg|14a,|
|OC-3||||-31||Figure 4|
|FE||||-31.8||14b|
|Input Optical Power Maximum|PIN MAX||||dBm avg||
|OC-3||-14||||13a|
|FE||-14||||13b|
|Operating Wavelength|�|1270||1380|nm||
|Systematic Jitter Contributed by the Receiver|SJ||0.11|1.2|ns p-p|15a|
|OC-3|||||||
|Duty Cycle Distortion Contributed by the Receiver|DCD||0.08|0.4|ns p-p|15b|
|FE|||||||
|Data Dependent Jitter Contributed by the Receiver|DDJ||0.02|1.0|ns p-p|15c|
|FE|||||||
|Random Jitter Contributed by the Receiver|RJ||||ns p-p||
|OC-3|||0.14|1.91||16a|
|FE|||0.14|2.14||16b|
|Loss of Signal - Deasserted|PA|PD+||-31|dBm avg|17|
|OC-3||1.5 dB||-33|||
|FE|||||||
|Loss of Signal - Asserted|PD|-45|||dBm avg|18|
|Loss of Signal - Hysteresis|PA- PD|1.5|||dB||
|Loss of Signal Deassert Time (on to of)||0|2|100|μs|19|
|Loss of Signal  Assert Time (of to on)||0|5|350|μs|20|



## **Notes:** 

- 13a. This specification is intended to indicate the performance of the receiver section of the transceiver when Input Optical Power signal characteristics are present per the following definitions. The Input Optical Power dynamic range from the minimum level (with a window time-width) to the maximum level is the range over which the receiver is guaranteed to provide output data with a Bit Error Rate (BER) better than or equal to 1 x 10[-10.  ] 

   - At the Beginning of Life (BOL) 

   - Over the specified operating temperature and voltage ranges 

   - Input is a 155.52 MBd, 2[23] -1 PRBS data pattern with 72  “1” s and 72 “0”s inserted per the CCITT (now ITU-T) recommendation G.958 Appendix I. 

   - Receiver data window time-width is 1.23 ns or greater for the clock recovery circuit to operate in. The actual test data window time-width is set to simulate the effect of worst case optical input jitter based on the transmitter jitter values from the specification tables. The test window time-width is  3.32 ns. 

   - Transmitter operating with a 155.52 MBd, 77.5 MHz square-wave, input signal to simulate any cross-talk present between the transmitter and receiver sections of the transceiver. 

13 

- 13b. This specification is intended to indicate the performance of the receiver section of the transceiver when Input Optical Power signal characteristics are present per the following definitions. The Input Optical Power dynamic range from the minimum level (with a window time-width) to the maximum level is the range over which the receiver is guaranteed to provide output data with a Bit Error Rate (BER) better than or equal to 2.5 x 10[-10] . 

   - At the Beginning of Life (BOL) 

   - Over the specified operating temperature and voltage ranges 

   - Input symbol pattern is the FDDI test pattern defined in FDDI PMD Annex A.5 with 4B/5B NRZI encoded data that contains a duty cycle base-line wander effect of 50 kHz. This sequence causes a near worst case condition for inter-symbol interference. 

   - Receiver data window time-width is 2.13 ns or greater and centered at mid-symbol. This worst case window time-width is the minimum allowed eye-opening presented to the FDDI PHY PM_Data indication input (PHY input) per the example in FDDI PMD Annex E. This minimum window time-width of 2.13 ns is based upon the worst case FDDI PMD Active Input Interface optical conditions for peak-to-peak DCD (1.0 ns), DDJ (1.2 ns) and RJ (0.76 ns) presented to the receiver. 

   - To test a receiver with the worst case FDDI PMD Active Input jitter condition requires exacting control over DCD, DDJ and RJ jitter compo nents that is difficult to implement with production test equipment. The receiver can be equivalently tested to the worst case FDDI PMD input jitter conditions and meet the minimum output data window time-width of 2.13 ns. This is accom plished by using a nearly ideal input optical signal (no DCD, insignificant DDJ and RJ) and measuring for a wider window time-width of 4.6 ns. This is possible due to the cumula tive effect of jitter components through their superposition (DCD and DDJ are directly additive and RJ components are rms additive). Specifically, when a nearly ideal input optical test signal is used and the maximum receiver peak-to-peak jitter contributions of DCD (0.4 ns), DDJ (1.0 ns), and RJ (2.14 ns) exist, the minimum window time-width becomes 8.0 ns -0.4 ns - 1.0 ns - 2.14 ns = 4.46 ns, or conservatively 4.6 ns. This wider window time-width of 4.6 ns guarantees the FDDI PMD Annex E minimum window time-width of 2.13 ns under worst case input jitter conditions to the Avago receiver. 

   - Transmitter operating with an IDLE Line State pattern, 125 MBd (62.5 MHz square-wave), input signal to simulate any cross-talk present between the trans mit ter and receiver sections of the transceiver. 

- 14a. All conditions of Note 13a apply except that the measurement is made at the center of the symbol with no window time- width. 

- 14b. All conditions of Note 13b apply except that the measurement is made at the center of the symbol with no window time-width. 

- 15a.  Systematic Jitter contributed by the receiver is defined as the combination of Duty Cycle Distortion and Data Dependent Jitter. Systematic Jitter is measured at 50%  threshold using a 155.52 MBd (77.5 MHz square- wave), 2[23] -1 psuedorandom data pattern input signal. 

- 15b Duty Cycle Distortion contributed by the receiver is measured at the 50% threshold of the electrical output signal using an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal. The input optical power level is -20 dBm average. 

- 15c. Data Dependent Jitter contributed by the receiver is specified with the FDDI DDJ test pattern described in the FDDI PMD Annex A.5.  The input optical power level is -20 dBm average. 

- 16a.  Random Jitter contributed by the receiver is specified with a 155.52 MBd (77.5 MHz square- wave) input signal. 

- 16b. Random Jitter contributed by the receiver is specified with an IDLE Line State, 125 MBd (62.5 MHz square-wave), input signal.  The input optical power level is at maximum “PIN MIN (W)”.  See Application Information - Transceiver Jitter Section for further information. 

17. This value is measured during the transition from low to high levels of input optical power. 

18.  This value is measured during the transition from high to low levels of input optical power. At Loss of Signal assert, the receiver outputs Data Out and Data Out Bar go to steady PECL levels High and Low respectively. 

19. The Loss of Signal output shall be de-asserted within 100 μs after a step increase of the Input Optical Power. 

20.  Loss of Signal output shall be asserted within 350 μs after a step decrease in the Input Optical Power. At Loss of Signal  Assert, the receiver outputs Data Out and Data Out Bar go to steady PECL levels High and Low respectively. 

21. The HFBR-57E0 transceiver complies with the requirements for the trade-offs between center wavelength, spectral width, and rise/fall times shown in Figure 3. This figure is derived from the FDDI PMD standard (ISO/IEC 9314-3 : 1990 and ANSI X3.166 - 1990) per the description in ANSI T1E1.2 Revision 3. The interpretation of this figure is that values of Center Wavelength and Spectral Width must lie along the appropriate Optical Rise/Fall Time curve. 

14 

## **Ordering Information** 

## **1300 nm LED (Operating Case Temperature 0 to +70 °C)** 

HFBR-57E0LZ Standard de-latch HFBR-57E0PZ Bail de-latch 

## **1300 nm LED (Operating Case Temperature -40 °C to +85 °C)** 

HFBR-57E0ALZ Standard de-latch HFBR-57E0APZ Bail de-latch 

## **EEPROM contents and/or label options** 

HFBR-57E0LZ-YYY Standard de-latch, 0 to +70°C HFBR-57E0PZ-YYY Bail de-latch, 0 to +70°C HFBR-57E0ALZ-YYY Standard de-latch, -40°C to +85°C HFBR-57E0APZ-YYY Bail de-latch, -40°C to +85°C 

Where “YYY” is customer specific. 

## **Handling Precaution** 

The HFBR-57E0xxZ  is a pluggable module and is NOT designed for aqueous wash,  IR reflow or wave soldering processes. 

For product information and a complete list of distributors, please go to our web site: **www.avagotech.com** 

Avago, Avago Technologies, and the A logo are trademarks of Avago Technologies in the United States and other countries. Data subject to change. Copyright © 2005-2011 Avago Technologies. All rights reserved. Obsoletes AV01-0456EN AV02-2810EN - Januaray 20, 2011 

