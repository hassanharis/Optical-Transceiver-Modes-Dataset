DATASHEET 

6.7 

## **QSFP28 100G COHERENT DWDM CMIS** QSFP28, 100GBASE-ZR/OTU4 Coh 50/100GHz Tunable 80km, 22dB, CMIS, LC 

## TQ2025-TUNC-SO 

The TQ2025-TUNC-SO is a pluggable QSFP28 DWDM transceiver designed for high capacity 100 Gigabit Ethernet (100GbE) Data Center Interconnect (DCI) optical communication applications up to 80km unamplified or 300km amplified over a singlemode fiber. 

The transceiver utilizes a tunable DP-QPSK modulated 28 Gbps wavelength with ability to be tuned with either 50GHz or 100GHz spacing enabling up to 96 channels over a 50GHz DWDM grid system as specified in the ITU-T 694.1 standard. The module provides two types of integrated FEC: Staircase FEC (SC-FEC) and RS(255,239) FEC. 

The electrical signals are transmitted and received from the host via a standard 38 pin connector described in the QSFP28 MSA (SFF-8679). The electrical interface is compliant to CAUI-4 (IEEE P802.3bm Annex 83E), splitting the 100Gbps signal into four parallel 25 Gbps NRZ streams as well as OTU4 (ITU-T 100G OTN). 

The management interface specification of the module is CMIS. For SFF-8636 compliant version, see p/n: TQ2028-TUNx-SO. 

## TECHNICAL DATA 

|**Parameter**|**Value**|
|---|---|
|Technology|DWDM QSFP28 100GBASE-ZR|
|Transmission media|SM (2x LC)|
|Typical reach, unamplified|80km1)|
|Typical reach, amplified|120km2)|
||300km3)|
|Nominal wavelength|191.35 – 196.10 THz (96ch)|
|Bit rate support|103.12Gbps|
|Protocol support|100GbE/OTU4|
|Dispersion tolerance|±2400ps/nm; ±6000ps/nm3)|
|Power budget|0 – 22dB|
|Power consumption|< 5.5W|
|Operating temperature|0°C to +70°C (TQ2025-TUNC-SO)|
|Storage temperature|-40°C to +85°C|



- 1) Limited by power budget 

- 2) Limited by dispersion compensation 

- 3) Extended mode, set through the host when the transceiver is in Low Power mode. The Extended mode will increase the power consumption of the module by 0.2W. 

- 4) Average power 

- 5) Receiver Sensitivity at unamplified configurations; OSNR >35dB/0.1nm 

- 6) 100G DQPSK SC-FEC 

- 7) 100G DQPSK RS-FEC 

- 8) Extended range; Rx signal input power range over which performance can be guaranteed with <1dB OSNR penalty relative to Rx OSNR tolerance limit 

|**Parameter**|**Value**|
|---|---|
|**Transmitter data:**||
|Output power per lane|Min: -8.0dBm4)|
||Max: -4.0dBm4)|
|Transmit wavelength|191.35 – 196.10 THz|
|**Receiver data:**||
|Minimum input power, unamplified|-30.0dBm4) 5) 6)|
||-24.0dBm4) 5) 7)|
|Minimum input power, amplified|-18dBm4)|
||-22dBm4) 8)|
|Overload (max power)|3.0dBm4)|
|OSNR Tolerance|16.5 dB/0.1nm6)|
||21.5 dB/0.1nm7)|
|Rx power monitor range|Signal power: -21dBm to +3dBm|
||Total power: -21dBm to +6dBm|
|Wavelength range|191.35 – 196.10 THz|
|Misc|Remote Diagnostic Monitoring|
||FlextuneTM|
|MSA compliance|SFF-8665, -8661, -8679|
||CMIS5.2 / OIF C-CMIS-01.2|
|**Media FEC**<br>**Latency [µs]**<br>SC-FEC<br>17<br>RS-FEC<br>3||



## **Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.7 

## APPLICATION MODES 

The below table lists the Host and NTWK modes supported by TQ2025-TUNC-SO 

|**Host framing**|**Network Frame**|**Media code1)**|**FEC**|**MSA format**||
|---|---|---|---|---|---|
|CAUI-4 w/o FEC<br>CAUI-4 with FEC|100GBASE-R|68|SC-FEC|100GBASE-ZR (Clause 154)||
|CAUI-4 w/o FEC||||||
|CAUI-4 with FEC|OTU4|192|SC-FEC|OTU4 Long reach||
|OTL4.4||||||
|CAUI-4 w/o FEC||||||
|CAUI-4 with FEC|OTU4|192|RS(255,239)|OTU4 Short reach||
|OTL4.4||||||



1) The media code is defined through the reference code tables listed in SFF-8024. 

## ORDERING INFORMATION 

|**Ordering code**|**Description**|**Description**||
|---|---|---|---|
|TQ2025-TUNC-SO|QSFP28, 100GBASE-ZR/OTU4 Coh 50GHz Tunable 80km, 22dB, CMIS5.2 LC|||
|GENERAL DEFINITIONS||||
|**Parameter**||**Description**||
|||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
|||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
|Technology||DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
|||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
|||AOC: Active Optical Cable. Optical cable with attached connectors.||
|Transmission Media||Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
|Typical reach||Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
|Bit rate range||Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
|Protocols||Protocols within supported bit rate range.||
|Nominal wavelength||Typical wavelength(s) from transmitter.||
|Interface standards||Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
|Power budget||Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
|Dispersion tolerance/penalty||Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
|||Max operating case temperature range.||
|Temperature range||Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
|||Industrial temperature range (I-temp):-40°C to +85°C (-40°F to +185°F)||
|Power consumption||Worst case power consumption. Will vary over temperature.||
|Transmitter Output power||Average output power. Provided in min and max values.||
|Receiver minimum input power||Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power||Maximum average input power giving a BER, normally 1E-12.||
|DDM||Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

