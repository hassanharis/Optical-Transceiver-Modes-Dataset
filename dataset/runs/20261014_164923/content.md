DATASHEET 

6.2 

## **QSFP28 100GE BiDi 40km** 

## QSFP28, BiDi, 100G Ethernet, 1304nm/1309nm, SM, 40km, 18.3dB, LC 

## TQ2024-BXXC-SO 

The TQ2024-BXXC-SO is a bi-directional transceiver solution operating directly on a single-fiber without the need for a separate optical filter. This is achieved by having two transceivers that inject different wavelengths into the same single-fiber. The solution thus consists of two transceivers; TQ2024-BWVC-SO and TQ2024-BVWC-SO, operating at transmit wavelengths 1304nm and 1309nm respectively. Using a single-fiber solution provides a cost-efficient solution for interconnect and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

TQ2024-BXXC-SO has an optical performance enabling distances of up to 40km over a SingleMode (SM) G.652 fiber-pair cable. The module includes FEC coding Forward Error Correction (KP4 FEC) to ensure reliable system operation. The host system shall thus not have FEC activated. The optical parameters will provide a bit error ratio (BER) of 2.4 x 10-4. FEC will render in the required BER of better than 1 x 10-12. 

The TQ2024-BXXC-SO transceivers uses a single 1304nm or 1309nm channel/lane @ 50Gbaud using PAM4 modulation to transport the Ethernet signal. The electrical interface is 4x 25.78Gbps and compliant with OIF CEI-28G-VSR. Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

The transceivers provide digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|BiDi QSFP28||**Transmitter data:**||
|Transmission media|SM (1x LC)||Output power, per lane|Min: +3.7dBm5)|
|Typical reach|40km|||Max: +7.1dBm5)|
|Nominal wavelengths|Tx: 1304nm / Rx: 1309nm1)||Transmit wavelengths|1304.06 – 1305.10nm1)|
||Tx: 1309nm / Rx: 1304nm2)|||1308.61 – 1309.66nm2)|
|Interface standards|100G ER1-40||**Receiver data:**||
|Bit rate support|106.25Gbps3)||Minimum input power|-14.6dBm5) 6)|
||52.125Gbd4)||Overload (max power)|-3.4dBm5) 6)|
|Protocol support|100GbE||Wavelength range|1308.61 – 1309.66nm1)|
|Power budget|10.5 – 18.3dB|||1304.06 – 1305.10nm2)|
|Power consumption|< 4.5W||LOS Assert|-26dBm|
|Operating temperature|0°C to +70°C||LOS De-assert|-17dBm|
|Storage temperature|-40°C to +85°C||DDM|Yes|
||||MSA compliance|QSFP28 MSA|
|1)TQ2024-BWVC-SO||||SFF-8472|
|2)TQ2024-BVWC-SO|||||
|3)Aggregated line rate 100GbE with FEC|||||
|4)Line baud rate|||||
|5)Average power, per lane|||||
|4)Specified at BER 2.4x10^-4|||||
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||




Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.2 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQ2024-BWVC-SO|QSFP28, BiDi, 100G Eth, Tx/Rx=1304/1309nm, SM, 40km, 18.3dB, LC|
|TQ2024-BVWC-SO|QSFP28, BiDi, 100G Eth, Tx/Rx=1309/1304nm, SM, 40km, 18.3dB, LC|



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

