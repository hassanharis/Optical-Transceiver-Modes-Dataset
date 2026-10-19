DATASHEET 

6.0 

## **QSFP28 100G ER1 40KM** QSFP28, 100G Ethernet ER1, SM 1x 1310nm, 40km, 18.5dB, LC 

## TQ2023-S31C-SO 

The TQ2023-S31C-SO is a QSFP28 form-factor transceiver for 100 Gbps Ethernet applications. It is intended for use in intra- and interconnect applications within and between data centers between switches, routers, storage equipment etc. 

TQ2023-S31C-SO has an optical performance enabling distances of up to 40km over a SingleMode (SM) G.652 fiber-pair cable. The module includes FEC coding Forward Error Correction (KP4 FEC) to ensure reliable system operation. The host system shall thus not have FEC activated. The optical parameters will provide a bit error ratio (BER) of 2.4 x 10[-4] . FEC will render in the required BER of better than 1 x 10[-12] . 

TQ2023-S31C-SO uses a single 1311nm channel/lane @ 50Gbaud using PAM4 modulation to transport the Ethernet signal. The electrical interface is 4x 25.78Gbps and compliant with OIF CEI-28G-VSR.  Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|
|Technology|Grey QSFP28||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Output power|Min: +1.7dBm3) 4)||
|Typical reach|40km|||Max: +7.1dBm3)||
|Nominal wavelength|1x 1311nm||Output power, OMA|Min: +4.7dBm||
|Interface standards|100G-ER1 MSA|||Max: +7.9dBm||
|Bit rate support|103.12Gbps1)||ER|Min: 5dB||
||53.125Gbd2)|||Typical: 5.5 dB5)||
|Protocol support|100GbE||Transmit wavelength|1307 – 1313nm||
|Power budget|10.1 – 18.5dB||**Receiver data:**|||
|Power consumption|< 4W||Receiver sensitivity, OMA|-13.8dBm6)||
|Operating temperature|0°C to +70°C||Receiver sensitivity, typical|-14.5dBm3) 5) 6)||
|Storage temperature|-40°C to +85°C||Minimum input power|-16.0dBm3) 4)||
||||Overload (max power)|-3.0dBm3) 6)||
|1)Aggregated line rate 100GbE|||Wavelength range|1307 – 1313nm||
|2)Line baud rate|||LOS Assert|Min -30dBm||
|3)Average power|||LOS De-assert|Max -10dBm||
|4)Average receive power, (min) is informative and not the principal<br>indicator of signal strength. A received power below this value cannot|||LOS Hysteresis|Min 0.5dB||
|be compliant; however, a value above this does not ensure<br>compliance.|||DDM|Yes||
|5)Typical value, specified as an indicator of strength. Varies between<br>individual components|||MSA compliance|QSFP28 MSA||
|6)Specified at BER 2.4x10-4||||SFF-8636, SFF-8679, SFF-8661||



- 6) Specified at BER 2.4x10-4 

Safety/regulatory compliance: 

**TUV/UL/FDA (contact Smartoptics for latest certification information)** RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.0 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQ2023-S31C-SO|QSFP28, 100G Ethernet ER1, SM 1x 1310nm, 40km, 18.5dB, LC|



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
|Optical modulation Amplitude,<br>OMA|Optical Modulation Amplitude is a parameter that, in certain standards, specifies the output power and as reciever sensitivity. To<br>measure the OMA, a oscilloscope with a baud rate corresponding to the transceiver is required. Thus, this parameter cannot be<br>measured using an ordinary optical power meter.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

