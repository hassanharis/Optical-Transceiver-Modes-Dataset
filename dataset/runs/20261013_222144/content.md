DATASHEET 

6.0 

## **SFP-DD 100G-FR** 

SFP-DD, 100G Ethernet FR, SM, 1x 1311nm, PAM4, 2km, 4.3dB, LC 

## TSD002-S31C-SO 

The TSD002-S31C-SO is a SFP-DD form-factor transceiver for 100 Gbps Ethernet applications. It is intended for use in intra- and interconnect applications within and between data centers between switches, routers, storage equipment etc. 

TSD002-S31C-SO uses a single 1311nm channel/lane @ 50Gbaud using PAM4 modulation to transport the Ethernet signal. The electrical interface is 2x 53.125Gbps PAM4- modulated channels compliant with 100GAUI-2.  Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(544,514). The optical parameters will provide a bit error ratio (BER) of 2.4 x 10-4. 

## TECHNICAL DATA 

|**Parameter**|**Value**|
|---|---|
|Technology|Grey SFP-DD|
|Transmission media|SM (2x LC)|
|Typical reach|2km|
|Nominal wavelength|1x 1311nm|
|Interface standards|100G-FR - 100G Lambda MSA|
|Bit rate support|103.12Gbps1)|
||53.125Gbd2)|
|Protocol support|100GbE|
|Power budget|0 – 4.3dB|
|Power consumption|< 3.5W|
|Operating temperature|0°C to +70°C|
|Storage temperature|-40°C to +85°C|



- 1) Aggregated line rate 100GbE 

- 2) Line baud rate 

- 3) Average launch power (min) is informative and not the principal indicator of signal strength. A transmitter with launch power below this value cannot be compliant; however, a value above this does not ensure compliance. 

|**Parameter**|**Value**|
|---|---|
|**Transmitter data:**||
|Output power, average|Min: -2.4dBm3)|
||Max: +4.0dBm3)|
|Output power, OMA|Min: -0.2dBm|
||Max: +4.2dBm|
|Transmit wavelength|1304.5 – 1317.5nm|
|**Receiver data:**||
|Minimum input power, average|-6.4dBm3)|
|Minimum input power, OMA|-4.5dBm3) 4)|
|Overload (max power)|+4.0dBm3) 4)|
|Wavelength range|1304.5 – 1317.5nm|
|LOS Assert|Min -15dBm|
|LOS De-assert|Max -12dBm|
|LOS Hysteresis|Min 0.5dB|
|DDM|Yes|
|MSA compliance|SFP-DD MSA|
||SFP-DD MIS|



- 4) Specified at BER 2.4x10-4 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.0 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TSD002-S31C-SO|SFP-DD, 100G Ethernet FR, SM, 1x 1311nm, PAM4, 2km, 4.3dB, LC|



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

