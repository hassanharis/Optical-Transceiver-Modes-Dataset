DATASHEET 

6.1 

## **SFP 1G BiDi 40km** 

## SFP BiDi, 1.0625/1.25Gbps, 1310/1550nm, SM, DDM, 20dB/18dB, 40km, SC 

## TSF087-BxxC-SO 

The TSF087-BxxC-SO is a bi-directional transceiver solution operating directly on a single-fiber without the need for a separate optical filter. This is achieved by having two transceivers that inject different wavelengths into the same single-fiber. The solution thus consists of two transceivers; TSF087-BCOC-SO and TSF087-BOCC-SO, operating at 1310nm and 1550nm respectively. Using a single-fiber solution provides a cost-efficient solution for interconnect and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

The transceiver pair supports 1G Fiberchannel (1G FC) and 1G Ethernet (GbE) services, having an optical performance that provides a bridgeable distance of up to 40km. 

The transceivers provide digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

## TECHNICAL DATA 

|**Parameter**|**Value**<br>BiDi SFP<br>SM (1x SC)<br>40km<br>1310nm/1550nm & 1550nm/1310nm<br>1.0625Gbps / 1.25Gbps<br>GbE<br>1G FC<br>5 – 20dB1)/ 3 – 18dB2)<br>< 1.0W<br>0°C to +70°C<br>-40°C to +85°C|**Parameter**|**Value**|
|---|---|---|---|
|Technology||**Transmitter data:**||
|Transmission media||Output power   TSF087-BCOC-SO<br>TSF007-BOCC-SO|Min: -3.0dBm1) 3)|
|Typical reach|||Max: +2.0dBm1) 3)|
|Nominal wavelength Tx/Rx|||Min: -5.0dBm2) 3)|
|Bit rate support|||Max: +0.0dBm2) 3)|
|Protocol support||Transmit wavelength|1290 – 1330nm1)|
||||1480 – 1580nm2)|
|Power budget||**Receiver data:**||
|Power consumption||Minimum input power|-23.0dBm3) 4)|
|Operating temperature||Overload (max power)|-3.0dBm3) 4)|
|Storage temperature||Wavelength range|1480 – 1580nm1)|
||||1290 – 1330nm2)|
|||LOS Assert|Min -35dBm|
|||LOS De-assert|Max -24dBm|
|||LOS Hysteresis|Min 0.5dB|
|||DDM|Yes|
|||MSA compliance|SFF-8431, -8432, -8472|
|||1)TSF087-BCOC-SO. <br>||



- 2) TSF087-BOCC-SO. 

- 3) Average power. 

4) @ 1.25Gbps, BER  1x10-12, PRBS 27-1, back-to-back. 

## **Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.1 

## POWER BUDGET INFORMATION 


Note that the power budget differs in 1310nm vs 1550nm direction. This has to be taken into account for links with high attenuation. Note also that the fiber attenuation is ~0.4dB/km in the 1310nm region and ~0.25dB/km in the 1550nm region. 

## ORDERING INFORMATION 

|**Ordering code**|**Description**|
|---|---|
|TSF087-BCOC-SO|SFP, BiDi, 1G Ethernet, 1G FC, TX/RX=1310/1550nm, SM, 40km, 18dB, SC|
|TSF087-BOCC-SO|SFP, BiDi, 1G Ethernet, 1G FC, TX/RX=1550/1310nm, SM, 40km, 18dB, SC|



## GENERAL DEFINITIONS 

||**Parameter**|**Description**||
|---|---|---|---|
|||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
|||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
||Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
|||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
|||AOC: Active Optical Cable. Optical cable with attached connectors.||
||Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
||Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual opticalpath loss and dispersionproperties.||
||Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
||Protocols|Protocols within supported bit rate range.||
||Nominal wavelength|Typical wavelength(s) from transmitter.||
||Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
||Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
||Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>agiven bit rate.||
|||Max operating case temperature range.||
||Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
|||Industrial temperature range(I-temp): -40°C to +85°C(-40°F to +185°F)||
||Power consumption|Worst case power consumption. Will vary over temperature.||
||Transmitter Output power|Average output power. Provided in min and max values.||
||Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
||Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
||DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any port ion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof.  The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

