DATASHEET 

6.1 

## **QSFP28 100GE BiDi 10km** 

## QSFP28, BiDi, 100G Ethernet, 1271nm/1331nm, SM, 10km, 6.8dB, LC 

## TQ2020-BXXC-SO 

The TQ2020-BXXC-SO is a bi-directional transceiver solution operating directly on a single-fiber without the need for a separate optical filter. This is achieved by having two transceivers that inject different wavelengths into the same single-fiber. The solution thus consists of two transceivers; TQ2020-BADC-SO and TQ2020-BDAC-SO, operating at transmit wavelengths 1271nm and 1331nm respectively. Using a single-fiber solution provides a cost-efficient solution for interconnect and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

TQ2020-BXXC-SO has an optical performance enabling distances of up to 10km over a SingleMode (SM) G.652 fiber-pair cable. The module includes FEC coding Forward Error Correction (KP4 FEC) to ensure reliable system operation. The host system shall thus not have FEC activated. The optical parameters will provide a bit error ratio (BER) of 2.4 x 10-4. FEC will render in the required BER of better than 1 x 10-12. 

The TQ2020-BXXC-SO transceivers uses a single 1271nm or 1331nm channel/lane @ 50Gbaud using PAM4 modulation to transport the Ethernet signal. The electrical interface is 4x 25.78Gbps and compliant with OIF CEI-28G-VSR. Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|
|Technology|BiDi QSFP28||**Transmitter data:**|||
|Transmission media|SM (1x LC)||Output power|Min: -1.4 dBm5) 6)||
|Typical reach|10km|||Max: +4.5 dBm5) 6)||
|Nominal wavelengths|Tx: 1271nm / Rx: 1331nm1)||Output power, OMA|Min:  +0.7 dBm||
||Tx: 1331nm / Rx: 1271nm2)|||Max: +4.7 dBm||
|Interface standards|100G-LR, 100G Lambda MSA||ER|Min: 3.5dB||
|Bit rate support|106.25Gbps3)|||Typical: 5.3dB7)||
||52.125Gbd4)||Transmit wavelengths|1264.5 – 1277.5nm1)||
|Protocol support|100GbE|||1324.5 – 1337.5nm2)||
|Power budget|0 – 6.8dB||**Receiver data:**|||
|Power consumption|< 4.5W||Receiver sensitivity, OMA|-6.1 dBm8)||
|Operating temperature|0°C to +70°C||Receiver sensitivity, typical|-6.5 dBm5) 7) 8)||
|Storage temperature|-40°C to +85°C||Minimum input power|-7.7 dBm5) 6)||
||||Overload (max power)|4.5 dBm5) 8)||
|1)TQ2020-BADC-SO|||Wavelength range|1324.5 – 1337.5nm1)||
|2)TQ2020-BDAC-SO||||1264.5 – 1277.5nm2)||
|3)Aggregated line rate 100GbE with FEC|||LOS Assert|-12dBm||
|4)Line baud rate|||LOS De-assert|-10dBm||
|5)Average power, per lane|||DDM|Yes||
|6)Average receive power, (min) is informative and not the principal<br>indicator of signal strength. A received power below this value cannot|||MSA compliance|QSFP28 MSA||
|be compliant; however, a value above this does not ensure<br>||||SFF-8472||



- 6) Average receive power, (min) is informative and not the principal indicator of signal strength. A received power below this value cannot be compliant; however, a value above this does not ensure compliance. 

- 7) Typical value, specified as an indicator of strength. Varies between individual components. 

- 8) Specified at BER 2.4x10^-4 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.1 

## **Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQ2020-BADC-SO|QSFP28, BiDi, 100G Eth, Tx/Rx=1271/1331nm, SM, 10km, 6.8dB, LC|
|TQ2020-BDAC-SO|QSFP28, BiDi, 100G Eth, Tx/Rx=1331/1271nm, SM, 10km, 6.8dB, LC|



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
|Optical modulation Amplitude,<br>OMA|Optical Modulation Amplitude is a parameter that, in certain standards, specifies the output power and as receiver sensitivity. To<br>measure the OMA, a oscilloscope with a baud rate corresponding to the transceiver is required. Thus, this parameter cannot be<br>measured using an ordinary optical power meter.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

