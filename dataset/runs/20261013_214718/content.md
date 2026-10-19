DATASHEET 

6.2 

## **QSFP28 100GE O-BAND DWDM 25km** QSFP28, O-Band DWDM, 100G Ethernet, SM, 25km, 15dB, LC 

## TQ2026-OXXC-SO 

TQ2026-OXXC-SO is a QSFP28 form-factor O-Band DWDM transceiver for 100 Gbps Ethernet applications. It is intended for use in intra- and interconnect applications within and between data centers between switches, routers, storage equipment etc. 

The transceiver is provided in 16 channel versions with 200GHz spacing. The optical performance enables distances of up to 25km over a SingleMode (SM) G.652 fiber-pair cable. 

The module includes FEC coding Forward Error Correction (KP4 FEC) to ensure reliable system operation. The host system shall thus not have FEC activated. The optical parameters will provide a bit error ratio (BER) of 2.4 x 10-4. FEC will render in the required BER of better than 1 x 10-12. 

The TQ2026-OXXC-SO transceivers uses a single lane carrier @ 50Gbaud with PAM4 modulation to transport the Ethernet signal. The electrical interface is 4x 25.78Gbps and compliant with OIF CEI-28G-VSR. Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

The transceivers provide digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

## TECHNICAL DATA 

|**Parameter**|**Value**<br>O-Band DWDM QSFP28<br>SM (2x LC)<br>25km<br>228.4 - 231.4 THz (16ch)<br>100GBASE<br>106.25Gbps1)<br>53.125Gbd2)<br>100GbE<br>8.6 – 15dB<br>< 5.5W<br>0°C to +70°C<br>-40°C to +85°C|**Parameter**|**Value**|
|---|---|---|---|
|Technology||**Transmitter data:**||
|Transmission media||Output power, per lane|Min: +0.0dBm3)|
|Typical reach|||Max: +5.6dBm3)|
|Nominal wavelengths||Transmit wavelengths|228.4 – 231.4 THz (16ch)|
|Interface standards||**Receiver data:**||
|Bit rate support||Minimum input power|-15.0dBm3) 4)|
|||Overload (max power)|-3.0dBm3) 4)|
|Protocol support||Wavelength range|1290-1325nm|
|Power budget||LOS Assert|-18dBm|
|Power consumption||LOS De-assert|-15dBm|
|Operating temperature||DDM|Yes|
|Storage temperature||MSA compliance|QSFP28 MSA|
||||SFF-8636|



- 1) Aggregated line rate 100GbE with FEC 

- 2) Line baud rate 

- 3) Average power, per lane 

- 4) Specified at BER 2.4x10^-4 

**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.2 

## ORDERING INFORMATION 

|**Ordering number**|<br>**Freq. THz**|**nm**|**Ordering number**|<br>**Freq. THz**|**nm**|
|---|---|---|---|---|---|
|TQ2026-O55C-SO|<br>228.4|1312.58|<br>TQ2026-O39C-SO|<br>230.0|1303.45|
|TQ2026-O53C-SO|<br>228.6|1311.43|<br>TQ2026-O37C-SO|<br>230.2|1302.31|
|TQ2026-O51C-SO|<br>228.8|1310.28|<br>TQ2026-O35C-SO|<br>230.4|1301.18|
|TQ2026-O49C-SO|<br>229.0|1309.14|<br>TQ2026-O33C-SO|<br>230.6|1300.05|
|TQ2026-O47C-SO|<br>229.2|1308.00|<br>TQ2026-O31C-SO|<br>230.8|1298.93|
|TQ2026-O45C-SO|<br>229.4|1306.85|<br>TQ2026-O29C-SO|<br>231.0|1297.80|
|TQ2026-O43C-SO|<br>229.6|1305.72|<br>TQ2026-O27C-SO|<br>231.2|1296.68|
|TQ2026-O41C-SO|<br>229.8|1304.58|<br>TQ2026-O25C-SO|<br>231.4|1295.56|



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

