DATASHEET 

6.1 

## **QSFP28 100GE BiDi 70km** QSFP28, BiDi, 100G Eth, 4LAN-WDM, SM, 70km, 27dB, LC 

## TQ2034-BXXY-SO 

The TQ2034-BXXy-SO is a bi-directional transceiver solution operating directly on a single-fiber without the need for a separate optical filter. This is achieved by having two transceivers that each inject four LAN-WDM wavelengths into the same single-fiber. The solution thus consists of two transceivers; TQ2034-BWXC-SO transmitting at the lower wavelengths 1274/1278/1282/1287nm and TQ2034-BXWy-SO transmitting at the high wavelengths 1296/1300/1305/1309nm. Using a single-fiber solution provides a cost-efficient solution for interconnect and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

TQ2034-BXXy-SO has an optical performance enabling distances of up to 70km over a SingleMode (SM) G.652 fiber-pair cable. Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 5 x 10-5. FEC will render in the required BER of better than 1 x 10-12. 

Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. The transceiver is available in two temperature range options, one being the Extended temperature range (E-temp): -20°C to 85°C (-20°F to 185°F). 

## TECHNICAL DATA 

||**Parameter**|**Value**|
|---|---|---|
||**Transmitter data:**||
||Output power, per lane|Min: +1.0dBm5)|
|||Max: +7.0dBm5)|
||Output power, OMA|Min: +3.0dBm|
|||Max: +8.8dBm|
||Extinction Ration|Min: 8dB|
||Transmit wavelengths|1274/1278/1282/1287nm1)|
|||1296/1300/1305/1309nm2)|
||**Receiver data:**||
||Receiver sensitivity, OMA|-24dBm6)|
||Minimum input power|-26.0dBm5)|
||Overload (max power), average<br>power per lane|-5.0dBm6)|
||Receiver wavelengths|1296/1300/1305/1309nm1)|
|||1296/1300/1305/1309nm2)|
||LOS Assert|-40dBm|
||LOS De-assert|-26dBm|
||LOS Hysteresis|Min: 0.5dB, Max: 5.0dB|
||DDM|Yes|
||MSA Compliance|QSFP28 MSA, SFF-8636|
||1)<br>2)||
||||




Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.1 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQ2034-BWXC-SO|QSFP28 BiDi 100G 4WL Tx 1282nm 70km|
|TQ2034-BXWC-SO|QSFP28 BiDi 100G 4WL Tx 1305nm 70km|
|TQ2034-BWXE-SO|QSFP28 BiDi 100G 4WL Tx 1282nm 70km-E|
|TQ2034-BXWE-SO|QSFP28 BiDi 100G 4WL Tx 1305nm 70km-E|



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
|Optical modulation Amplitude,<br>OMA|Optical Modulation Amplitude is a parameter that, in certain standards, specifies the output power and receiver sensitivity. To<br>measure the OMA, a oscilloscope with a baud rate corresponding to the transceiver is required. Thus, this parameter cannot be<br>measured using an ordinary optical power meter.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

