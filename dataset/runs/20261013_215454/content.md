DATASHEET 

6.7 

## **QSFP28 100G COHERENT DWDM SFF-8636 HIGH TX POWER** 

## QSFP28, 100GBASE-ZR Coh 50/100GHz Tunable 120km, 30dB, SFF-8636, LC, Tx=0dBm 

## TQ2032-TUNX-SO 

The TQ2032-TUNx-SO is a pluggable QSFP28 DWDM transceiver designed for high capacity 100 Gigabit Ethernet (100GbE) Data Center Interconnect (DCI) optical communication applications up to 120km unamplified or 300km amplified links. The TQ2032-TUNx-SO has an on-board dispersion compensation that can handle chromatic dispersion up to 2 400ps/nm (~120km), or 6 000ps/nm (~300km) with “Extended mode” over a singlemode fiber. 

The transceiver utilizes a tunable DP-QPSK modulated 28 Gbps wavelength with ability to be tuned with either 50GHz or 100GHz spacing enabling up to 96 channels over a 50GHz DWDM grid system as specified in the ITU-T 694.1 standard. The media side is encoded with Staircase FEC (SC-FEC). The transceiver also includes an EDFA, enabling a Tx power of 0dBm. 

The electrical signals are transmitted and received from the host via a standard 38 pin connector described in the QSFP28 MSA (SFF8679). The electrical interface is compliant to CAUI-4 (IEEE P802.3bm Annex 83E), splitting the 100Gbps signal in to four parallel 25 Gbps NRZ streams. 

The management interface specification of the module is compliant to SFF-8636. For CMIS compliant version, see p/n: TQ2031-TUNx-SO. The transceiver is also available in C-temp version covering a temperature range of 0°C to +70°C (TQ2031-TUNC-SO) and I-temp version covering -40°C to +85°C (TQ2031-TUNI-SO). 

## TECHNICAL DATA 

|**Parameter**|**Value**<br>DWDM QSFP28 100GBASE-ZR<br>SM (2x LC)<br>120km1)<br>120km2)<br>300km3)<br>191.35 – 196.10 THz (96ch)<br>103.12Gbps<br>100GbE<br>±2400ps/nm; ±6000ps/nm3)<br>0 – 30dB<br>< 6.2W (TQ2032-TUNC-SO)<br><6.7W (TQ2032-TUNI-SO)<br>0°C to +70°C (TQ2032-TUNC-SO)<br>-40°C to+85°C (TQ2032-TUNI-SO)<br>-40°C to +85°C|**Parameter**|**Value**|
|---|---|---|---|
|Technology||**Transmitter data:**||
|Transmission media||Output power per lane|Min: 0dBm4)|
|Typical reach, unamplified||Tx output monitor range|-2dBm to +4dBm4)|
|Typical reach, amplified||Transmit wavelength|191.35 – 196.10 THz|
|||Tx OSNR, in-band|39dB/12.5GHz|
|Nominal wavelength||Tx OSNR, out-of-band|30dB/12.5GHz|
|Bit rate support||**Receiver data:**||
|Protocol support||Minimum input power, unamplified|-30.0dBm4) 5) 6)|
|Dispersion tolerance||Minimum input power, amplified|-18dBm4)|
|Power budget|||-22dBm4) 8)|
|Power consumption||Overload (max power)|3.0dBm4)|
|Operating temperature||OSNR Tolerance|16.5 dB/0.1nm6)|
|Storage temperature||Wavelength range|191.35 – 196.10 THz|
|1)Limited by power budget<br>2)Limited by dispersion compensation<br>3)Extended mode, set through the host when the transceiver is in Low Power mode.<br>The Extended mode will increase the worst-case power consumption by 0.2W for I-<br>temp (TQ2032-TUNI-SO) and 0.3W for C-temp (TQ2032-TUNC-SO).<br>4)Average power<br>5)Receiver Sensitivity at unamplified configurations; OSNR >35dB/0.1nm<br>6)100G DQPSK SC-FEC<br>7)100G DQPSK RS-FEC<br>8)Extended range; Rx signal input power range over which performance can be<br>guaranteed with <1dB OSNR penalty relative to Rx OSNR tolerance limit||Misc|Remote Diagnostic Monitoring|
||||FlextuneTM|
|||MSA compliance|SFF-8665, -8661, -8679|
||||SFF-8636|
|||**Media FEC**<br>**Latency [µs]**<br>SC-FEC<br>25||
|<br>**Safety/regulatory compliance:**||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)||||



8) Extended range; Rx signal input power range over which performance can be guaranteed with <1dB OSNR penalty relative to Rx OSNR tolerance limit **Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.7 

## ORDERING INFORMATION 

|**Ordering code**|**Description**|
|---|---|
|TQ2032-TUNC-SO|QSFP28, 100GBASE-ZR Coh 50/100GHz Tunable 120km, w/o TOF, 30dB, SFF-8636, LC|
|TQ2032-TUNI-SO|QSFP28, 100GBASE-ZR Coh 50/100GHz Tunable 80km, w/o TOF, 30dB, SFF-8636, LC, I-temp|



## GENERAL DEFINITIONS 

||**Parameter**|**Description**||
|---|---|---|---|
|||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
|||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
||Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
|||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
|||AOC: Active Optical Cable. Optical cable with attached connectors.||
||Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
||Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
||Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
||Protocols|Protocols within supported bit rate range.||
||Nominal wavelength|Typical wavelength(s) from transmitter.||
||Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
||Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
||Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
|||Max operating case temperature range.||
||Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
|||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
||Power consumption|Worst case power consumption. Will vary over temperature.||
||Transmitter Output power|Average output power. Provided in min and max values.||
||Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
||Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
||DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

