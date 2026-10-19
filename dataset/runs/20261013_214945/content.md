DATASHEET 

6.2 

## **QSFP28 100GE O-BAND DWDM 40km** QSFP28, O-Band DWDM, 100G Ethernet, SM, 40km, 18.5dB, LC 

## TQ2030-OXXC-SO 

TQ2030-OXXC-SO is a QSFP28 form-factor O-Band DWDM transceiver for 100 Gbps Ethernet applications. It is intended for use in intra- and interconnect applications within and between data centers between switches, routers, storage equipment etc. 

The transceiver is provided in 8 channel versions with 200GHz spacing. The optical performance enables distances of up to 40km over a SingleMode (SM) G.652 fiber-pair cable. 

The module includes FEC coding Forward Error Correction (P-FEC) to ensure reliable system operation. The host system shall thus not have FEC activated. The optical parameters will provide a corrected bit error ratio (BER) after FEC to be better than 1 x 10-12. 

The TQ2030-OXXC-SO transceivers uses a single lane carrier @ 50Gbaud with PAM4 modulation to transport the Ethernet signal. The electrical interface is 4x 25.78Gbps and compliant with OIF CEI-28G-VSR. Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

The transceivers provide digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

## TECHNICAL DATA 

|**Parameter**|**Value**<br>O-Band DWDM QSFP28<br>SM (2x LC)<br>40km<br>228.4 – 229.8 THz (8ch)<br>100GBASE<br>112.5Gbps1)<br>56.25Gbd2)<br>100GbE<br>9.5 – 18.5dB<br>< 6.0W<br>0°C to +70°C<br>-40°C to +85°C|**Parameter**|**Value**|
|---|---|---|---|
|Technology||**Transmitter data:**||
|Transmission media||Output power, per lane|Min: +2.0dBm3)|
|Typical reach|||Max: +7.1dBm3)|
|Nominal wavelengths||Transmit wavelengths|228.4 – 229.8 THz (8ch)|
|Interface standards||**Receiver data:**||
|Bit rate support||Minimum input power|-16.5dBm3) 4)|
|||Overload (max power)|-2.4dBm3) 4)|
|Protocol support||Wavelength range|1290-1325nm|
|Power budget||LOS Assert|-26dBm|
|Power consumption||LOS De-assert|-17dBm|
|Operating temperature||DDM|Yes|
|Storage temperature||MSA compliance|QSFP28 MSA|
||||SFF-8636|



- 1) Aggregated line rate 100GbE with FEC 

- 2) Line baud rate 

- 3) Average power, per lane 

- 4) Specified at BER 1.0x10^-12 

**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.2 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|**Freq. THz**|**nm**|
|---|---|---|---|
|TQ2030-O55C-SO|QSFP28 100GE O-DWDM O284/1312nm 40km 18.5dB|228.4|1312.58|
|TQ2030-O53C-SO|QSFP28 100GE O-DWDM O286/1311nm 40km 18.5dB|228.6|1311.43|
|TQ2030-O51C-SO|QSFP28 100GE O-DWDM O288/1310nm 40km 18.5dB|228.8|1310.28|
|TQ2030-O49C-SO|QSFP28 100GE O-DWDM O290/1309nm 40km 18.5dB|229.0|1309.14|
|TQ2030-O47C-SO|QSFP28 100GE O-DWDM O292/1308nm 40km 18.5dB|229.2|1308.00|
|TQ2030-O45C-SO|QSFP28 100GE O-DWDM O294/1306nm 40km 18.5dB|229.4|1306.85|
|TQ2030-O43C-SO|QSFP28 100GE O-DWDM O296/1305nm 40km 18.5dB|229.6|1305.72|
|TQ2030-O41C-SO|QSFP28 100GE O-DWDM O298/1304nm 40km 18.5dB|229.8|1304.58|



Note: The above channels represent the center channels defined in the CW-WDM MSA. 

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
||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally1x 10-12. Some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally1x10-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

