DATASHEET 

6.1 

## **SFP28 25GE BiDi 80km** 

## SFP28, BiDi, 25G Eth, Tx/Rx=1309.14/1295.56nm, SM 80km, 31dB, C-/I-temp, LC 

## TS2015-Bxxy-SO 

The TS2015-Bxxy-SO is a bi-directional transceiver solution operating directly on a single-fiber without the need for a separate optical filter. This is achieved by having two transceivers that inject different wavelengths into the same single-fiber. The solution thus consists of two transceivers; TS2015-BUVI-SO and TS2015-BVUI-SO, operating at transmit wavelengths 1295.56nm and 1309.14nm respectively. Using a single-fiber solution provides a cost-efficient solution for interconnect and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

TQ2015-Bxxy-SO has an optical performance enabling distances of up to 80km over a SingleMode (SM) G.652 single fiber. As stipulated by the 25G Ethernet standards, Forward Error Correction (FEC) is required to be implemented by the host equipment to ensure reliable system operation. 

The electrical interface is 1x 25.78Gbps and compliant with OIF CEI-28G-VSR. Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the SFP28 MSA. 

The transceivers provide digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

TS2015-Bxxy-SO is provided in a C-temp version (TS2015-BxxC-SO) and I-temp version (TS2015-BxxI-SO) 

## TECHNICAL DATA 

|**Parameter**|**Value**<br>BiDi SFP28<br>SM (1x LC)<br>80km<br>Tx: 1295.56nm / Rx: 1309.14nm1)<br>Tx: 1309.14nm / Rx: 1295.56nm2)<br>25GBASE 80km<br>25.78Gbps<br>25GbE<br>8 – 31.0dB<br><2.5W for TS2015-BxxC-SO<br><3.3W for TS2015-BxxI-SO<br>0°C to +70°C (TS2015-BxxC-SO)<br>-40°C to +85°C (TS2015-BxxI-SO)<br>-40°C to +85°C|**Parameter**|**Value**|
|---|---|---|---|
|Technology||**Transmitter data:**||
|Transmission media||Output power|Min: +2dBm3)|
|Typical reach|||Max: +7.0dBm3)|
|Nominal wavelengths||Transmit wavelengths|1294.53 – 1296.59nm1)|
||||1308.09 – 1310.19nm2)|
|Interface standards||**Receiver data:**||
|Bit rate support||Minimum input power|-29.0dBm3) 4)|
|Protocol support||Overload (max power)|-6.0dBm3) 4)|
|Power budget||Wavelength range|1308.09 – 1310.19nm1)|
|Power consumption|||1294.53 – 1296.59nm2)|
|||LOS Assert|Min -32.5dBm|
|Operating temperature||LOS De-assert|Max -29.5dBm|
|||LOS hysteresis|Min 0.5dB|
|Storage temperature||DDM|Yes|
|1)TS2015-BUVy-SO<br>2)TS2015-BVUy-SO<br>3)Average power, per lane||MSA compliance|SFP28 MSA|
||||SFF-8472|
|||||



4) Specified at BER 5x10-5 

**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.1 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TS2015-BUVC-SO|SFP28, BiDi, 25G Eth, Tx/Rx=1295.56/1309.14nm, SM, 80km, 31dB, LC|
|TS2015-BVUC-SO|SFP28, BiDi, 25G Eth, Tx/Rx=1309.14/1295.56nm, SM, 80km, 31dB, LC|
|TS2015-BUVI-SO|SFP28, BiDi, 25G Eth, Tx/Rx=1295.56/1309.14nm, SM, 80km, 31dB, I-temp, LC|
|TS2015-BVUI-SO|SFP28, BiDi, 25G Eth, Tx/Rx=1309.14/1295.56nm, SM, 80km, 31dB, I-temp, LC|



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
|Receiver minimum input power|Minimum average input power at specified BER, normally1x 10-12. Some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally1x10-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

