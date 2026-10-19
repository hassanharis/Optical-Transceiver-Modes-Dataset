**Stratos Optical Technologies** 



## **MIL-SxF-LT11M** Military SFF Optical Transceiver 

## **Fast Ethernet Applications 3.3 V, 1310 nm LED, multimode, up to 2.0 km** 

The Cinch Connectivity Solutions’ optical transceivers consist of transmitter and receiver functions combined in a Small Form Factor (SFF) module. The optical transmitter is a high output 1310nm LED. The transmitter input lines are driven with differential LVPECL signals applied to the Transmit (TX+ and TX-) pins. These signals are internally converted to a suitable modulation current by a CMOS integrated circuit. The optical receivers consist of PIN and Preamplifier assemblies and CMOS limiting post-amplifier integrated circuits. Outputs from the receivers consist of differential data signals on the Receive (RX+ and RX-) pins and a single ended LVTTL signal detect function on the Signal Detect (SD) pin. The RX data is squelched (JAM) upon Signal Detect deassert to prevent garbage data output when no optical signal is present. 

The MIL-SxF-LT11M multimode glass optical fiber transceivers provide low profile, cost effective solutions for Fast Ethernet multimode (up to 2.0 Km) optical fiber data links with a duplex LC connector interface. These transceivers are fully compliant with the IEEE 802.3u Fast Ethernet standard but can be used for any other data communications purpose within their operating parameters. 

## **Features & Benefits** 

- Industry standard MSA 2x5 footprint 

- IPC Class III assembly and construction 

- Industrial Temp range -40°C to +85°C operational 

- All metal construction for rugged environments 

- Parylene C conformal coating 

- RX Signal Detect pin 

- RX data squelch on Signal Detect deassert 

- Separate +3.3 V power pins per TX/RX port 

- Industry standard duplex multimode LC receptacle 

- Full compliance to IEEE and ANSI requirements 

- EN-60825/ IEC-825 / CDRH Class 1 Compliant 

## **Applications** 

- Rugged Network equipment 

- Mobile comms 

- Aircraft Mission Computer 

   - MRI scan equipment 

   - Oil and Gas exploration 

   - Fire and Rescue 

- UAV, UUV 


**cinch.com** 

Please read our datasheet & drawing disclaimer here. 

**Stratos Optical Technologies** 

## **MIL-SxF-LT11M** Military SFF Optical Transceiver 

## **Ordering Information** 


**----- Start of picture text -----**<br>
Part Number Date Rate Optical Link Conformal Coating Temperature Range EMI Clip<br>MIL-SNF-LT11M  125 Mbps 1310 nm MMF Parylene C -40 to +85°C Flat shell (no clip)<br>MIL-STF-LT11M 125 Mbps 1310 nm MMF Parylene C -40 to +85°C EMI clip<br>**----- End of picture text -----**<br>


## **Absolute Maximum Ratings** 

Absolute maximum limits mean that no catastrophic damage will occur if the product is subjected to these ratings for short periods, provided each limiting parameter is in isolation and all other parameters have values within the performance specification. It should not be assumed that limiting values of more than one parameter can be applied to the product at the same time. 


**----- Start of picture text -----**<br>
Parameter  Symbol  Min  Typical  Max  Unit<br>Storage Temperature  TS  -55  +100  °C<br>Lead Soldering Temperature [1] TSOLD +260  °C<br>Lead Soldering Time [1] t SOLD  10  seconds<br>Supply Voltage  VCC -0.5  +4.5  V<br>Data Input Voltage  VI  -0.5  VCC V<br>Differential Input Voltage (p-p)  VD 2.0  V<br>Output Current  IO  50  mA<br>**----- End of picture text -----**<br>


_¹ Recommended for hand solder or hot bar soldering only. Convection or IR reflow oven profiles may damage internal solder joints. Reference Low Rider Soldering Application Note._ 

## **Recommended Operating Conditions** 


**----- Start of picture text -----**<br>
Parameter  Symbol  Min  Typical  Max  Unit<br>Operating Temperature Limit  TA  -40  +85  °C<br>Supply Voltage  VCC  +3.135  +3.465  V<br>TX Common Mode Voltage  VCM 2.0  V<br>TX Differential Input Voltage (p-p)  VD  0.20 2.20 V<br>Transmit Disable Voltage VTD 2.0   VCC V<br>RX Data Output Load  RL  50  Ω<br>**----- End of picture text -----**<br>


## **Transmitter[ 2]** 


**----- Start of picture text -----**<br>
Parameter  Symbol  Min  Typical  Max  Unit<br>Optical Output Power [1 ] PO -20.0 -13.0 dBm<br>Optical Output Wavelength  λOUT 1285 1310 1355 nm<br>Spectral Width ∆λRMS 63 nm<br>Extinction Ratio  ER  12 dB<br>Supply Current  ICC 180 230 mA<br>Optical Rise/Fall Time (20% - 80%) TR,F 3.0 ns<br>**----- End of picture text -----**<br>


_1  BER = 10 -10 @ 1.25 Gbps, PRBS 27-1, NRZ, compliant with FDDI PMD ISO / IEC 9314-3 and IEEE-802.3u testing with 62.5 MM fiber_ 

_2  VCC TX = 3.135 to 3.465 V, TA = Operating Temperature Range_ 


**cinch.com** 

_Specification subject to change without notice._ 

**Stratos Optical Technologies** 

## **MIL-SxF-LT11M** Military SFF Optical Transceiver 

## **Receiver[ 3]** 


**----- Start of picture text -----**<br>
Parameter  Symbol  Min  Typical  Max  Unit<br>Optical Sensitivity [1] PI  -32.0 -23 -8.0 dBm<br>Optical Input Wavelength  λIN 1260 1380 nm<br>Supply Current  ICC 150 170 mA<br>Signal Detect Assert Time  tSDAS <10 100 µs<br>Signal Detect Deassert Time  tSDDA <10  350 µs<br>Signal Detect Deassert Level [2] SDOFF -45.0 -32.5  dBm<br>Signal Detect Assert Level  SDON -45.0 -32.0 dBm<br>Signal Detect Hysteresis  HYS 0.5 2.25 3.5 dB<br>RX Data Output – Low  VOL-VCC -1.810 -1.475 V<br>RX Data Output – High  VOL+VCC -1.165 -0.880 V<br>**----- End of picture text -----**<br>


_1 BER = 10-10 @ 1.25 Gbps, PRBS 27-1, NRZ. Compliant with ANSI X3.297 / FC-PH-2 2 Rx Data output are squelched when Signal Detect is deasserted to prevent garbage data output when no optical signal is present 3  VCCTX = 3.135 to 3.465 V, TA = Operating Temperature Range_ 

## **Block Diagram** 


**----- Start of picture text -----**<br>
BASELINE<br>LVPECL REFERENCE<br>DRIVER PIN AND TIA L<br>C<br>RX+ LVPECL LEVEL<br>RX- BUFFER DETECT I<br>N<br>SIGNAL T<br>SD LED<br>DETECT E<br>R<br>LVPECL F<br>RCVR A<br>C<br>TX-<br>PULSE CURRENT E<br>TX+ SHAPING AMPLIFIER<br>CASE<br>**----- End of picture text -----**<br>


## **Conformal Coating Option** 


**----- Start of picture text -----**<br>
Parameter  Value<br>Specification MIL-I-46058C, Type XY<br>Coating Parylene type C<br>Deposition Vacuum deposited<br>Film Thickness 1 MIL +/- 0.0002<br>**----- End of picture text -----**<br>



**cinch.com** 

_Specification subject to change without notice._ 

**Stratos Optical Technologies** 

**MIL-SxF-LT11M** Military SFF Optical Transceiver 

## **Link Distance** 


**----- Start of picture text -----**<br>
Application  Fibre Specification Distance<br>Fast Ethernet – IEEE 802.3u 62.5/125 – 60 MHz*km 2.0  km<br>FDDI PMD ISO / IEC 9314-3 50/125 – 500 MHz*km 2.0  km<br>**----- End of picture text -----**<br>


## **Regulatory Compliance** 


**----- Start of picture text -----**<br>
Requirement  Feature Condition Notes<br>MIL-STD-883-3015.7  ESD Class II  2200 V<br>IEC-801-2  ESD Human Body Model  25 kV<br>IEC-801-3  EMI Immunity 10 V/M<br>FCC  EMI Class B  >20 dB<br>EN 55022 (CISPR 22A)  EMI Class B  10 V/M<br>**----- End of picture text -----**<br>


## **Military Small Form Factor Transceiver Pin Number Assignments** 

Top View Shown 


**----- Start of picture text -----**<br>
5 4 3 2 1 MS<br>RX<br>TX<br>6 7 8 9  10 MS<br>**----- End of picture text -----**<br>


## **Pin Functions** 


**----- Start of picture text -----**<br>
Pin #  Symbol Description Logic Family<br>MS MS Mounting Studs Connect to chassis ground N/A<br>1 VEERX  Receiver Signal Ground N/A<br>2 VCCRX Receiver Power Supply N/A<br>3 SD Signal Detect (1=detect, 0=no signal) LVTTL<br>4 RD- Receive Data Out - LVPECL<br>5 RD+ Receive Data Out + LVPECL<br>6 VCCTX Transmit Power Supply N/A<br>7 VEETX Transmit Signal Ground N/A<br>8 N/C No Connect  N/A<br>9 TD+ Transmit Data In + LVPECL<br>10 TD- Transmit Data In - LVPECL<br>**----- End of picture text -----**<br>



**cinch.com** 

_Specification subject to change without notice._ 

**Stratos Optical Technologies** 

**MIL-SxF-LT11M** Military SFF Optical Transceiver 

## **Parallel Termination (Thevenin Equivalent) for DC Coupled LVPECL PHY Devices** 


**----- Start of picture text -----**<br>
Vcc = 3.3 V<br>L1<br>0.01 μ F 22 μ F<br>L2<br>10 μ F 0.01 μ F<br>0.01 μ F 10 μ F<br>130 Ω Vcc = 3.3 V 6               2<br>130 Ω VccTx          VccRx<br>TD + Z0 = 50 Ω 9 TD +<br>TD - 10 TD -<br>130 Ω Vcc = 3.3 V 82 Ω 8 ND<br>82 Ω<br>(LVPECL)RD +PHY 130 Ω Z0 = 50 Ω 5 MIL-SXF-LT11XRD +<br>4<br>RD -  82 Ω 3 RD -  GP<br>SD 82 Ω SD GP<br>  VeeTx        VeeRx<br>7               1<br>**----- End of picture text -----**<br>


_Notes:_ 

_1. L1 and L2 = MuRata BLM21A601S or equivalent (600_ Ω _at 100 MHz or better)._ 

_2. Place LVPECL termination resistors (130 / 82 W) as close as possible to termination points._ 

_3. Route the differential pairs (TD +/- and RD +/-) together using 50 W impedance matched traces._ 

_4. Other DC coupled LVPECL termination techniques are also valid._ 

_5. Use separate power supply filtering for VCCTX and VCCRX, as shown._ 

_6. Ground Posts (GP) are isolated from Signal Ground (Vee), and may be connected to Chassis Ground (as shown) or to Signal Ground if a Chassis Ground is not available._ 

## **For AC Coupled LVPECL PHY Devices** 

Similar to DC-coupled, except addition of emitter follower pull-down resisters (180 Ω), different Vt operating point (2.0 V versus 1.1 V), and addition of series RF capacitors. 


**----- Start of picture text -----**<br>
Vcc = 3.3 V<br>L1<br>0.01 μ F 22 μ F<br>L2<br>10 μ F 0.01 μ F<br>0.01 μ F 10 μ F<br>180 Ω<br>180 Ω 82 Ω Vcc = 3.3 V 6               2<br>82 Ω VccTx          VccRx<br>TD + Z0 = 50 Ω 0.01 μ F 9 TD +<br>TD - 0.01 μ F 10 TD -<br>82 Ω Vcc = 3.3 V 130 Ω 8 ND<br>130 Ω<br>(LVPECL)PHY 82 Ω Z0 = 50 Ω 0.01 μ F 5 MIL-SXF-LT11X<br>RD + RD +<br>RD -  130 Ω 0.01 μ F 43 RD -  GP<br>SD 130 Ω SD GP<br>180 Ω 180 Ω   VeeTx        VeeRx<br>7               1<br>**----- End of picture text -----**<br>


## _Notes:_ 

_1. L1 and L2 = MuRata BLM21A601S or equivalent (600_ Ω _at 100 MHz or better)._ 

_2. Place LVPECL termination resistors (82 / 130_ Ω _) as close as possible to termination points. Place LVPECL emitter follower pull-down (180_ Ω _) as close as possible to source points._ 

_3. Route the differential pairs (TD +/- and RD +/-) together using 50_ Ω _impedance matched traces._ 

_4. Other DC coupled LVPECL termination techniques are also valid._ 

_5. Use separate power supply filtering for VCCTX and VCCRX, as shown._ 

_6. Ground Posts (GP) are isolated from Signal Ground (Vee), and may be connected to Chassis Ground (as shown) or to Signal Ground if a Chassis Ground is not available.  Use low ESR capacitors, such as NPO or COG, for AC coupling of TD+/- and RD+/- signals._ 


**cinch.com** 

_Specification subject to change without notice._ 

**Stratos Optical Technologies** 

## **MIL-SxF-LT11M** Military SFF Optical Transceiver 


**----- Start of picture text -----**<br>
17.11<br>0.280<br>7.11<br>0.81 +/- 0.1 0.280<br>Ø<br>0.032 +/- 0.004<br>(10)<br>1.4 +/- 0.1<br>Ø<br>0.055 +/- 0.004<br>(2)<br>10.16<br>0.400<br>13.97<br>Min.<br>0.550<br>7.59 9.59<br>0.299 0.378<br>3.0 2.0<br>0.118 3.0 1.78 2.0 0.079<br>0.118 0.070<br>0.079<br>6.0 3.08<br>0.236 0.121<br>Cross-hatched areas should have no signal traces on the top layer<br>**----- End of picture text -----**<br>


**cinch.com** 

_Specification subject to change without notice._ 

**Stratos Optical Technologies** 

**MIL-SxF-LT11M** Military SFF Optical Transceiver 

**Mechanical Detail, EMI Clip Shell Option Part number MIL-STF-LT11M** 


**Mechanical Detail, Flat Shell Option Part number MIL-SNF-LT11M** 


**North America** +1 507.833.8822 ccsorders@us.cinch.com 

**cinch.com** ds-Stratos-MIL-SxF-LT11M-Optical-Transceivers_06-2025_2.0R 

© 2025 Cinch Connectivity Solutions 

