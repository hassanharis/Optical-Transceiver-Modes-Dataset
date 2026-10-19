DATASHEET 

6.0 

## **QSFP56 200G SR4** 

QSFP56 200GBASE-SR4 Ethernet, 850nm, 1.9dB@OM4, MPO12 

## TQ5001-M85C-SO 

The TQ5001-M85C-SO is a QSFP56 form-factor transceiver for 200 Gbps Ethernet (200GBASE-SR4) applications. It is intended for use in inter- and intra-connect applications within data centers between switches, routers, storage equipment etc. The optical performance is in accordance with the 100GBASE-SR IEEE 802.3bm standard, i.e. for optical distances up to 100m over a MultiMode (MM) OM4-grade ribbon fiber. 

The module has 4 independent electrical input/output channels operating at 26.5625GBd per channel. This transceiver uses four PAM4 modulated lanes operating at 850nm. The transceiver requires that the host system uses Forward Error Correction (FEC). 

The electrical interface is compliant with the 200GAUI-4 interface as defined by IEEE 802.3bs. 

Digital diagnostics functions are available via an I[2] C interface, as specified by the QSFP56 MSA using CMIS4.0. 

## TECHNICAL DATA 

|**Parameter**|**Value**<br>Grey QSFP56<br>MM (1x MPO-12)<br>100m @ OM4<br>4x 850nm<br>200GBAS-SR4<br>InfiniBand HDR<br>212.5Gbps1)<br>26.5625Gbd (PAM4)2)<br>200GbE<br>0 –1.9dB<br>< 5.0W<br>0°C to +70°C<br>-40°C to +85°C|**Parameter**|**Value**|
|---|---|---|---|
|Technology||**Transmitter data:**||
|Transmission media||Output power, per lane|Min: -6.5dBm|
|Typical reach|||Max: +4.0dBm|
|Nominal wavelengths||Transmit wavelengths|840 – 860nm|
|Interface standards||**Receiver data:**||
|||Minimum input power per lane|-8.4dBm3)|
|Bit rate support||Overload (max power) per lane|+4.0dBm3)|
|||Wavelength range|840 – 860nm|
|Protocol support||LOS Assert|Min 17dBm|
|Power budget||LOS De-Assert|Max -12dBm|
|Power consumption||LOS Hysteresis|Min 0.5dBm|
|Operating temperature||DDM|Yes|
|Storage temperature||MSA compliance|QSFP56 MSA, CMIS4.0|



- 1) Aggregated line rate 200GbE 2) Line rate per lane 3) Specified at BER 2x10-4 



**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.0 

## APPLICATION CODE LIST 

|**CMIS**|**Application**|**Code**|**Host format**|**Electrical interface**|**Host**<br>**Electrical ID**|**Payload**|**FEC**|**MSA**|**Media ID**||
|---|---|---|---|---|---|---|---|---|---|---|
||1||200GBASE-R|200GAUI-4 (4x 50G)|0x0F|200G|RS-FEC|200GBASE-SR4|<br>0x0E||
||2||4 x 50GBASE-R|4x 50GAUI-1 (4x 50G)|0x0A|200G|RS-FEC|50GBASE-SR|0x07||
||3||IB HDR|IB HRR|0x31|200G|-|200GBASE-SR4|<br>0x0E||



## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQ5001-M85C-SO|QSFP28, 100G Eth SR4, MM 4x 850nm, 100m, 1.9dB, MPO|



## GENERAL DEFINITIONS 

|**Parameter**|**Description**||
|---|---|---|
||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
|Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
||AOC: Active Optical Cable. Optical cable with attached connectors.||
|Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
|Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
|Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
|Protocols|Protocols within supported bit rate range.||
|Nominal wavelength|Typical wavelength(s) from transmitter.||
|Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
|Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
|Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
||Max operating case temperature range.||
|Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
||Industrial temperature range (I-temp):-40°C to +85°C (-40°F to +185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

