

## FNK-LT12x 

Front Load Pluggable Optical Transceiver 

The FNK-LT12 singlemode optical fiber transceivers provide low profile, cost effective solutions for Gigabit Ethernet and 1x Fiber Channel optical fiber data links with a duplex LC connector interface. These transceivers are fully compliant with the IEEE Gigabit Ethernet and ANSI 1x Fiber Channel standards but can be used for any other data communications purpose within their operating parameters. 


This transceiver consist of transmitter and receiver functions combined in a Low Profile RJ module. The optical transmitter is a high output 1310 nm FP laser. The transmitter input lines are driven with differential LVPECL signals applied to the Transmit (TX+ and TX-) pins. These signals are internally converted to a suitable modulation current by a CMOS integrated circuit. The optical transmitter can be disabled by applying an LVTTL signal to the Transmit Disable (TDIS) pin. 

The optical receivers consist of PIN and Preamplifier assemblies and CMOS limiting post-amplifier integrated circuits. Outputs from the receivers consist of differential CML data signals on the Receive (RX+ and RX-) pins and a single ended LVTTL loss of signal function on Loss of Signal (LOS) pin. The RX data is squelched (JAM) upon LOS Assert to prevent garbage data output when no optical signal is present. 


## Features & Benefits 

- Gigabit Ethernet and 1x FC Applications, up to 10 km 

- 3.3 V, 1310 nm, FP, Singlemode 

- Front load pluggable miniature transceiver 

- MSA height, but half the footprint 

- MSA compliant Digital Diagnostics 

- Surface Mount I/O pins for high speed signal integrity 

- Industrial Temp Range, Vibration tolerant design 

- Individual (separate) +3.3 V power supply per port 

- Industry standard duplex multimode LC receptacle 

- Full compliance to IEEE and ANSI requirements 

- EN-60825 / IEC-825 / CDRH Class 1 Compliant 


**belfuse.com/cinch** 

Please read our datasheet & drawing disclaimer here. 

## FNK-LT12x 

## Ordering Information 



**----- Start of picture text -----**<br>
F N K -LT12 H<br>F = Front Load Low Rider H  = No Conf Coat<br>M  = Conf Coat<br>N = No GND Tabs<br>K = Fast Ethernet L T12 = SM 1310nm<br>Block Diagram<br>BASELINE<br>CML  REFERENCE<br>DRIVER PIN AND TIA<br>L<br>RX+ C<br>CML  LEVEL<br>RX- BUFFER DETECT<br>I<br>N<br>T<br>SIGNAL<br>SD LASER E<br>DETECT<br>R<br>F<br>A<br>TDIS C<br>E<br>TX-<br>LASER<br>TX+ DRIVER<br>CASE<br>**----- End of picture text -----**<br>



**belfuse.com/cinch** 

**2** 

FNK-LT12x Technical Specifications 


## **Absolute Maximum Ratings** 

Absolute maximum limits mean that no catastrophic damage will occur if the product is subjected to these ratings for short periods, provided each limiting parameter is in isolation and all other parameters have values within the performance specification. It should not be assumed that limiting values of more than one parameter can be applied to the product at the same time. 


**----- Start of picture text -----**<br>
Parameter  Symbol  Min  Typical  Max  Unit<br>Storage Temperature  TS  -55  +100  °C<br>Lead Hand Soldering Temperature [1] TSOLD  +260  °C<br>Lead Soldering Time [1 ] tSOLD  10  Second<br>Supply Voltage  VCC  -0.5  +4.5  V<br>Data Input Voltage  VI  -0.5  VCC  V<br>Differential Input Voltage (p-p)  VD 2.0  V<br>Output Current  IO  50  mA<br>**----- End of picture text -----**<br>


1 The Front Load Pluggable Optical Transceiver is not soldered, rather it is the Cage and Connector that are soldered to the application card. Therefore, these Solder specifications apply only for the Cage and Connector 

## **Recommended Operating Conditions** 


**----- Start of picture text -----**<br>
Parameter  Symbol  Min  Typical  Max  Unit<br>Operating Temperature Limit  TA  -40  +85  °C<br>Supply Voltage  VCC +3.135  +3.465  V<br>Tx Common Mode Voltage  VCM 2.0  V<br>Tx Differential Input Voltage (p-p)  VD  0.35  1.25  V<br>Rx Data Output Load  RL  50  W<br>**----- End of picture text -----**<br>


## **Transmitter** 


**----- Start of picture text -----**<br>
Parameter [2] Symbol  Min  Typical  Max  Unit<br>Optical Output Power [1 ] PO -9.5 -3.0 dBm<br>Optical Output Wavelength  λ OUT 1285  1310 1343 nm<br>Spectral Width (RMS)  ∆ λ RMS 4 nm<br>Extinction Ratio  ER  9 dB<br>Supply Current  ICC 120 160 mA<br>Optical Rise/Fall Time (20% - 80%) tR,F 0.26 ns<br>Relative Intensity Noise RIN 120 -116 dB/Hz<br>Total Jitter Tj 153 ps<br>Transmit Disable Voltage VD 2.0 120 VCC V<br>Transmit Enable Voltage VEN VEE 0.8 V<br>**----- End of picture text -----**<br>


1 BER = 10-10 @ 125 Mbps, PRBS 27-1, NRZ, Compliant with IEEE-802.3z and ANSI X3.297 / FC-PH-2 

> 2 Vcc Tx = 3.15 – 3.45 V, T A = Operating temperature range 


**belfuse.com/cinch** 

**3** 

## FNK-LT12x Technical Specifications 


## **Receiver** 


**----- Start of picture text -----**<br>
Parameter Symbol  Min  Typical  Max  Unit<br>Optical Sensitivity [1] PI  -20.0 0.0 dBm<br>Optical Input Wavelength λIN 1270 1355 nm<br>Optical Return Loss ORL 12 dB<br>Supply Current ICC 70 120 mA<br>Loss of Signal Assert Time TLOSAS <10 100 µs<br>Loss of Signal Deassert Time TLOSDS  <10 350 µs<br>Loss of Signal Deassert Level [2] LOSON -30 dBm<br>Loss of Signal Assert Level LOSOFF -20 dBm<br>Loss of Signal Hysteresis HYS  1.5 2.25 3.5 dB<br>RX Data Output – Low VOL-VCC -1.810 -1.475 V<br>RX Data Output – High VOH-VCC -1.165 -0.880 V<br>**----- End of picture text -----**<br>


1 BER = 10-10 @ 1.25 Gbps, PRBS 27-1, NRZ, Compliant with IEEE-802.3z and ANSI X3.297 / FC-PH-2 

2 Rx Data output are squelched when Loss of Signal is asserted to prevent garbage data output when no optical signal is present 

## **Conformal Coating Option** 


**----- Start of picture text -----**<br>
Parameter Value<br>Specification MIL-I-46058C, Type XY<br>Coating Parylene type C<br>Deposition Vacuum deposited<br>Film Thickness   1 MIL +/- 0.0002”<br>**----- End of picture text -----**<br>


## **Regulatory Compliance** 


**----- Start of picture text -----**<br>
Requirement  Feature Condition Notes<br>MIL-STD-883-3015.7 ESD Class II 2200 V<br>IEC-801-2 ESD Human Body Model 25 kV<br>IEC-801-3 EMI Immunity 10 V/m<br>FCC EMI Class B >20 dB<br>EN 55022 (CISPR 22A) EMI Class B 10 V/m<br>IEC-825 issue 1993-11 Eye Safety Class 1 TUV Certificate Number on File<br>FDA CDRH 21-CFR 1040 Eye Safety Class 1 CDRH Accession Number on File<br>**----- End of picture text -----**<br>



**belfuse.com/cinch** 

**4** 

## FNK-LT12x 

## Mechanical Details 


## **Front Loader** 


**----- Start of picture text -----**<br>
0.597<br>0.060<br>0.424<br>1.033<br>1.002<br>1.214<br>**----- End of picture text -----**<br>


All dimensions in inches. All dimensions +- 0.005”, unless noted Screw torque 0.50 +/- 0.10 in-lbs 

## **Front Loader Cage** 


**----- Start of picture text -----**<br>
1.028<br>0.426<br>0.012 THK<br>0.618 0.050<br>0.136 0.610  [+_]   0.002<br>1.000<br>**----- End of picture text -----**<br>


All dimensions in inches. All dimensions +- 0.005”, unless noted Screw torque 0.50 +/- 0.10 in-lbs 


**belfuse.com/cinch** 

**5** 

## FNK-LT12x Footprint - PCB 



**----- Start of picture text -----**<br>
0.591<br>0.511<br>0.622<br>SOLDER PAD  0.205<br>8 PLACES<br>0.084<br>0.610<br>0.930<br>0.610<br>0.082 0.610<br>0.069<br>0.630 0.200<br>Ø 0.041   [+_]   0.002 THRU<br>4 HOLES/PART<br> 0.003<br>9 SPACES AT 0.0315<br>0.104 0.284<br>0.040 Ø 0.055                 - 0.003   [+0.000] [THRU]<br>2 HOLES/PART<br> 0.003<br>0.095<br>0.017<br>0.040<br>0.020<br>Ø  [0.029  ]<br>    0.027 THRU<br>2 HOLES/PART<br> 0.003<br>All dimensions in inches.<br>All dimensions +- 0.005”, unless noted<br>**----- End of picture text -----**<br>



**belfuse.com/cinch** 

**6** 

## FNK-LT12x 

Footprint - Panel Cut Out 


## **Double** 


**----- Start of picture text -----**<br>
0.820<br>0.320<br>0.520<br>0.244<br>0.464<br>0.240<br>0.020<br>0.320<br>0.525<br>**----- End of picture text -----**<br>


## **Single** 


**----- Start of picture text -----**<br>
0.520<br>0.320<br>0.244<br>0.464<br>0.240<br>0.520<br>0.020<br>0.320<br>**----- End of picture text -----**<br>


All dimensions in inches. All dimensions +- 0.005”, unless noted 


**belfuse.com/cinch** 

**7** 

FNK-LT12x Pin Functions 



**----- Start of picture text -----**<br>
GND 1 2 GND<br>TX_FAULT 3 4 TD-<br>TX_DISABLE 5 6 TD+<br>MOD_DEF (2) 7 8 GND<br>Towards  MOD_DEF (1) 9 10 VCCT Towards<br>Bezel ASIC<br>MOD_DEF (0) 11 12 VCCR<br>RATE_SELECT 13 14 GND<br>LOS 15 16 RD+<br>GND 17 18 RD-<br>GND 19 20 GND<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
Pin #  Name Function Notes<br>1 GND Ground<br>3 TX_FAULT Transmitter Fault Indication Note 3<br>5 TX_DISABLE Transmitter Disable Note 4: Transmitter disables on high<br>7 MOD_DEF (2) Module Definition 2 Note 5, 2: Wire Serial Data Input<br>9 MOD_DEF (1) Module Definition 1 Note 5, 1: Wire Serial Clock input<br>11 MOD_DEF (0) Module Definition 0 Note 5, 0: Grounded in module<br>13 RATE SELECT No Connect Note 6<br>15 LOS Loss of Signal Note 7<br>17 GND Ground<br>19 GND Ground<br>2 GND Ground<br>4 TD- Inverted Data In Note 10<br>6 TD+ Non-Inverted Data In Note 10<br>8 GND Ground<br>10 VCCT Transmitter Power +3.3 V +-5%, Note 9<br>12 VCCR Receiver Power +3.3 V +-5%, Note 9<br>14 GND Ground<br>16 RD+ Non-Inverted Receiver Data Out Note 8<br>18 RD- Inverted Receiver Data Out Note 8<br>20 GND Ground<br>**----- End of picture text -----**<br>



**belfuse.com/cinch** 

**8** 

FNK-LT12x Pin Functions 



**----- Start of picture text -----**<br>
Note 1 Connector SAMTEC part number TEM-110-02-DH1-H-D-A<br>Note 2 Connector pin numbering matches SAMTEC pin numbering and are not the same pin numbers as defined in MSA SFP standards. However, the<br>physical orientation of the electrical signals is the same as defined in MSA SFP standards<br>Note 3 TX FAULT:   is an open collector/drain output which should be pulled up with a 4.7k – 10k Ω resistor on Host board. Pull up voltage between 2.0 V<br>and VccT, R+0.3 V. When high, output indicates a laser fault of some kind. Low indicates normal operation. In the low state, the output will be pulled<br>to < 0.8 V.<br>Note 4 TX DISABLE : is an input that is used to shut down the transmitter optical output. It is pulled down within the module with a 4.7k – 10k Ω resistor.<br>The states are: Low (0 - 0.8 V): Transmitter ON<br>(>0.8, <2.0 V): Undefined<br>High (2.0 - 3.465 V): Transmitter Disabled<br>Open: Transmitter Enabled<br>Note 5 MOD-DEF 0,1,2:   These are the module definition pins. They should be pulled up with 4.7k – 10k Ω resistor on the host board. Pull up voltage<br>between 2.0V and VccT, R+0.3 V<br>MOD-DEF 0 is grounded by the module to indicate that the module is present.<br>MOD-DEF 1 is the clock input of the 2-wire serial interface for serial ID and DDMI.<br>MOD-DEF 2 is the data input of the 2-wire serial interface serial ID and DDMI.<br>Note 6 RATE SELECT:   Not applicable for this design (leave Not Connected).<br>Note 7 LOS:   is an LVTTL output. When high, this output indicates the received optical signal power is below the receiver sensitivity. Low indicates normal<br>operation.<br>Note 8 RD -/+:   These are the differential receiver signal outputs. They are 100 Ω differential lines which should be terminated with 100 Ω (differential) at<br>the user SERDES. The voltage swing on these lines will be between 400 and 1200 mV p-p differential (200-600 mV p-p single ended) when properly<br>terminated  (Figure 1) .<br>Note 9 VccR and VccT:  are the receiver and transmitter power supplies. They are defined as 3.3 V ± 5% at the FRONT LOAD PLUGGABLE connector pin.<br>Recommended host board power supply filtering is shown in  Figure 2 . When the recommended supply filtering network is used, hot plugging of the<br>FRONT LOAD PLUGGABLE module will result in an inrush current of no more than 30 mA greater than the steady state value. VccR and VccT may be<br>internally connected within the FRONT LOAD PLUGGABLE module<br>Note 10 TD -/+:  are the differential transmitter signal inputs. They are differential lines with a 100 Ω differential termination inside the module. The inputs will<br>accept a swing of 400 - 2500 mV p-p differential (200-1250 mV p-p single ended), though it is recommended that values between 500 and 1200 mV<br>p-p differential (250-600 mV p-p single ended) be used for best EMI performance.<br>Note 11 Consult the SERDES manufacturer’s applications information for biasing required for Tx outputs. Some serializer outputs are internally biased and<br>may not need external bias resistors.<br>Note 12 Consult SERDES manufacturer’s data sheet and application data for appropriate receiver input biasing network. Some de-serializer inputs<br>internally terminated.<br>Note 13 Use low ESR capacitors such as NPO or COG for AC coupling of the TD-/+ and RD -/+ data signals.<br>**----- End of picture text -----**<br>



**belfuse.com/cinch** 

**9** 

## FNK-LT12x Termination Circuits 


Inputs to the FNK-LT12 transmitter are internally terminated with 100 Ω differential. The input signal must have at least a 400mV peak-to-peak differential signal swing. Output from the receiver section of the module is expected to drive into a 100 Ω differential load. Different termination strategies may be required depending on the particular SERDES chip set used. 


**----- Start of picture text -----**<br>
Protocol VCC<br>VEET<br>TRANSMITTER Protocol VCC<br>4.7k Ω to<br>10kΩ<br>4.7k Ω  to   Tx_Fault Tx_Fault<br>10k Ω<br>Tx_Disable<br>Tx_Disable<br>TD+<br>50 Ω TD+<br>DRIVER 100 Ω<br>TD-<br>LASER 50 Ω TD-<br>VCCT ProProtocolol<br>See  Note 11 SerDes ICIC<br>VCCR Fig. 3<br>BIAS IC<br>RD-<br>50 Ω RD-<br>PIN TX AMP POST AMP 100 Ω<br>RD+<br>50 Ω RD+<br>Note 12<br>VEER<br>LOS<br>RECEIVER LOS<br>Rate_Select<br>Rate_Select<br>+3.3V<br>30K Ω<br>4.7k Ω to  4.7k Ω to  4.7k Ω to<br>10kΩ 10kΩ 10kΩ<br>Mod_Def (0)<br>PLD/PAL<br>Mod_Def (1)<br>SFP Mod_Def (2)<br>**----- End of picture text -----**<br>


**Figure 1** Illustrates the recommended transmit and receive data line terminations. 


**belfuse.com/cinch** 

**10** 

## FNK-LT12x Power Coupling 


A suggested layout for power and ground connections is given in **Figure 2** below. Connections are made via separate voltage and ground planes. The mounting posts are at case ground and should not be connected to circuit ground. The ferrite bead should provide an impedance of 220 Ω at 100 MHz. Bypass capacitors should be placed as close to the 20 pin connector as possible. 


**Figure 2** Shows the suggested layout for power and ground connections. 

## **Timing Parameters** 


**----- Start of picture text -----**<br>
Parameter  Symbol Min Max Unit Conditions<br>TX_DISABLE assert time t_off 10 µs Timing for rising edge of TX_DISABLE to when the optical output falls below 10% of nominal<br>Timing for falling edge of TX_DISABLE to when the<br>TX_DISABLE negate time t_on 1 ms modulated optical output rises above 90%<br>of nominal<br>Time to initialize includes reset of TX_FAULT t_init 300 ms From power on or negation of TX_FAULT using<br>TX_DISABLE<br>TX_FAULT Assert time t_fault 100 µs Time TX_DISABLE must be held high to reset TX_FAULT<br>TX_DISABLE to reset t_reset 10 µs Time TX Disable must be held high to reset  TX_FAULT<br>RX_LOS Assert time t_loss_on 100 µs Time from LOS state to RX_LOS assert<br>RX_LOS deassert time t_loss_off 100 µs Time from non-LOS state to RX_LOS deassert<br>Timing from rising or falling edge of Rate<br>Rate-Select Change time t_ratesel 10 µs Select input until receiver bandwidth is in<br>conformance with appropriate specification<br>Serial ID Clock Rate f_serial_clock 100 kHz<br>**----- End of picture text -----**<br>



**belfuse.com/cinch** 

**11** 

## FNK-LT12x 

## DIGITAL DIAGNOSTICS MONITORING INTERFACE – BASE ADDRESS A2h 


Cinch Connectivity Solutions FRONT LOAD PLUGGABLE transceivers support the 2-wire serial communication protocol as defined in the SFP Multi- Source Agreement (MSA). The FNK-LT12 transceivers are provided with enhanced digital diagnostic monitoring interface (DDMI) which allows real-time access to device operating parameters such as transceiver temperature, laser bias current and transceiver supply voltage. It also defines a system of alarm flags that alerts end-users when particular operating parameters are outside of a factory set normal range. The FRONT LOAD PLUGGABLE with DDMI is fully compliant to the SFF-8472 Rev. 9.3 specification. 

Cinch Connectivity Solutions FRONT LOAD PLUGGABLE with DDMI are internally calibrated (bit 5, address 92 @ 2-wire address A0h is set). 


**----- Start of picture text -----**<br>
2-wire address (A0h) 2-wire address (A2h)<br>0 0<br>Alarm☐<br>Thresholds☐<br>Serial ID Defined☐ (56 Bytes)<br>by SFP MSA☐ 55<br>(96bytes)<br>Cal Constants☐<br>(40bytes)<br>95 95<br>Real Time Diagnotics☐<br>Vendor Specific☐ Interface (24bytes)<br>127 (32bytes) 119127 Vendor Specific (8bytes)<br>Reserved in☐ User Writable☐<br>SFP MSA☐ EEPROM (120bytes)<br>(128bytes)<br>247<br>255 255 Vendor Specific (8bytes)<br>**----- End of picture text -----**<br>


**Figure 3** Digital diagnostic memory map specific data field descriptions. 

## **Alarm and Warning Thresholds** 


**----- Start of picture text -----**<br>
Address  Parameter Hex Code Value<br>00-01 Temp High Alarm 5600 +86°C<br>02-03 Temp Low Alarm D600 -42°C<br>04-05 Temp High Warning 5000 +80°C<br>06-07 Temp Low Warning DC00 -36°C<br>08-09 Voltage High Alarm 8751 3.465 V<br>10-11 Voltage Low Alarm 7A76 3.135 V<br>12-13 Voltage High Warning 84D0 3.4 V<br>14-15 Voltage Low Warning 7D00 3.2 V<br>16-17 Bias High Alarm 88B8 70 mA<br>18-19 Bias Low Alarm 1388 10 mA<br>20-21 Bias High Warning 7EF4 65 mA<br>22-23 Bias Low Warning 1572 11 mA<br>24-25 TX Power High Alarm 1397 -3<br>26-27 TX Power Low Alarm 0462 -9.5<br>28-29 TX Power High Warning 1172 -3.5<br>30-31 TX Power Low Warning 04EA -9<br>32-33 RX Power High Alarm 22E0 -0.5<br>34-35 RX Power Low Alarm 0052 -21<br>36-37 RX Power High Warning 1BA7 -1.5<br>38-39 RX Power Low Warning 006F -19.5<br>40-55 Reserved<br>**----- End of picture text -----**<br>



**belfuse.com/cinch** 

**12** 

## FNK-LT12x 


Customer, Program: Part Number: (if known) Data Rate: Wavelength:                            ☐   850                            ☐   1310 Mode:                                     ☐  Singlemode               ☐    Multimode Conformal Coat:                    ☐   Yes ☐    No Post:                                      ☐   Screw Post            ☐    Solder Post Fiber Type: ☐    62.5/125 µm Multimode: OCC AE001CWST5KM or equivalent ☐    50/125 µm Multimode: OCC AE001CAST5KM or equivalent ☐    9/125 µm Singlemode: OCC AE001CSLS5KM or equivalent ☐    Other: 

## **RX Termini:** 

## **TX Termini:** 

## **RX Pigtail Length:** 

(+/- 0.5 inches is default) 

(Not including transceiver body, to tip of termini) 

## **TX Pigtail Length:** 

(+/- 0.5 inches is default) 

(Not including transceiver body, to tip of termini) 

## **Special Notes:** 

(Boot color, heatshrink, labels, special testing, shipping, etc.) 

***Section to be completed by Cinch Connectivity Solutions Assigned by Date** 


**----- Start of picture text -----**<br>
Part Number  Assigned by Date<br>**----- End of picture text -----**<br>



**Asia Pacific Europe, Middle East & Africa North America** +86 21 5442 7668 +44 (0) 1245 342060 +1 321 308 4100 ccs.asia.sales@as.cinch.com CinchConnectivity@eu.cinch.com ccsorders@us.cinch.com 

**belfuse.com/cinch** 

ds-ccs-stratos-FNK-xxxx-series-05262022 **13** 

© 2022 Cinch Connectivity Solutions 

