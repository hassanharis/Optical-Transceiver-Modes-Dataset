DATASHEET 

6.0 

## **SFP28 ZR 80km** 

## SFP28, 25G Ethernet ZR, 1300nm, SM, 80km, 30dB, LC, C-temp, I-temp 

## TS2014-S30x-SO 

The TS2014-S30x-SO is an SFP+ form-factor transceiver for 25Gbps Ethernet applications. It is intended for use in interconnect applications between data centers with switches, routers, storage equipment etc. The optical performance supports distances up to 80km over a SingleMode (SM) fiber. 

TS2014-S30x-SO uses a single 1300nm channel to transport a 25G Ethernet signal. As stipulated by the 25G Ethernet standards, Forward Error Correction (FEC) is required to be implemented by the host equipment to ensure reliable system operation. The optical parameters below will provide a bit error ratio (BER) of 5 x 10[-5 ] for 25G Ethernet. FEC will provide the required quality for secure service. 

The electrical interface is according to 25GAUI specifications per IEEE 802.3cc. 

TS2014-S30x-SO is provided in a C-temp version (TS2014-S30C-SO) and an I-temp version (TS2014-S30I-SO). 

Digital diagnostics functions are available via an I2C interface, as specified by the SFF-8472 MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|
|Technology|Grey SFP28||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Output power|Min: +2.0dBm1)||
|Typical reach|80km|||Max: +7.0dBm||
|Nominal wavelength|1x 1300.05nm||Output power, OMA|Min: +3.7dBm||
|Bit rate support|25.78Gbps|||Max: +7.8dBm||
|Protocol support|25GE||ER|8dB||
|Power budget|13 – 30.2dB||Transmit wavelength|1299.02 – 1301.09nm||
|Dispersion penalty|< 3.0dB||**Receiver data:**|||
|Power consumption|< 2.5W @ 0°C to +70°C||Receiver sensitivity, OMA|-26.5dBm2)||
||< 3.5W @ -40°C to +85°C||Receiver Sensitivity|-31dBm1)||
|Operating temperature|0°C to +70°C (TS2014-S30C-SO)||Minimum input power, typical|-28.1dBm1) 2)||
||-40°C to +85°C (TS2014-S30I-SO)||Overload (max power)|-6.0dBm||
|Storage temperature|-40°C to +85°C||Wavelength range|1299.02 – 1301.09nm||
||||LOS De-assert|Max -29.5dBm||
|1)Average power, (min) is informative and not the principal indicator|||LOS Assert|Min -40dBm||
|of signal strength. A received power below this value cannot be||||||
|compliant; however, a value|above this does not ensure compliance.||LOS Hysteresis|Min 0.5dB||
|2)Typical value, specified as<br>individual components|an indicator of strength. Varies between||DDM|Yes||
|3)at 25.78Gbps (25GE) and BER 5x10-5|||MSA compliance|SFF-8402, SFF-8472||
|||||SFF-8419||



**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 






Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.0 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TS2014-S30C-SO|SFP28, 25G ZR, 1300.05nm, SM, 80km, 30dB, LC|
|TS2014-S30I-SO|SFP28, 25G ZR, 1300.05nm, SM, 80km, 30dB, LC, I-temp|



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
|Optical modulation Amplitude,<br>OMA|Optical Modulation Amplitude is a parameter that, in certain standards, specifies the output power and receiver sensitivity. To<br>measure the OMA, a oscilloscope with a baud rate corresponding to the transceiver is required. Thus, this parameter cannot be<br>measured using an ordinary optical power meter.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

