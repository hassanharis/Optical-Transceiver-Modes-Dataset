DATASHEET 

6.1 

## **QSFP-DD 400GBASE-ER4 LITE, CMIS4.0** QSFP-DD 400G-ER4 Lite Ethernet, PAM4 CMIS4.0, 1296/1300/1305/1309nm, 30km 15.5dB 

## TQD023-SL4C-SO 

The TQD023-SL4C-SO is a QSFP-DD form-factor transceivers for 400Gbps Ethernet applications. The intended use is data center interconnect for optical distances up to 30km over a SingleMode (SM) fiber cable. 

The electrical interface consists of eight 53.125G signals (400GAUI-8) that are converted to four PAM4-modulated channels/lanes to transport the Ethernet signal. The transceiver can also be set in 4x100GAUI-2 mode to enable 400G to 4x 100G break-out configurations. Digital diagnostics functions are available via an I2C interface, as specified by the QSFP-DD MSA. 

Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 2.4 x 10-4. TQD023-SL4C-SO also allows an onboard FEC, P-FEC, through application code 3 to allow better performance. 

The TQD023-SL4C-SO is compliant with Common Management Interface Specification CMIS4.0. 

## TECHNICAL DATA 

|**Parameter**||**Value**||**Parameter**|**Value**|
|---|---|---|---|---|---|
|Technology||Grey QSFP-DD||**Transmitter data:**||
|Transmission media||SM (2xLC)||Output power, per lane|Min: +0.4dBm3)|
|Typical reach||30km|||Max: +6.5dBm|
|Nominal wavelength||1296/1300/1305/1309nm||Output power, OMA, per lane|Min: +3.4dBm|
|Interface standards||400G ER4 Lite|||Max: +9.0dBm|
|Electrical interfaces||400GAUI-8 or 4x100GAUI-2||ER|Min: 6dB|
|Bit rate support||425Gbps1)||Transmit wavelengths|1294.53 – 1296.59nm|
|||53.125Gbd2)|||1299.02 – 1301.09nm|
|Protocol support||400GbE, 4x100GbE|||1303.54 – 1305.63nm|
|Power budget||3.8 – 15.5dB|||1308.09 – 1310.19nm|
|Power consumption||< 12W||**Receiver data:**||
|Operating temperature||0°C to +70°C||Receiver sensitivity, OMA, per<br>lane|-12.1dBm4)|
|Storage temperature||-40°C to +85°C||Minimum input power, per<br>lane|-15.1dBm3) 4)|
|||||Overload (max power), per<br>lane|-3.4dBm|
|1)Aggregated line rate 400GbE||||Receive wavelengths range|1294.53 – 1296.59nm|
|2)Line baud rate|||||1299.02 – 1301.09nm|
|3)Average receive power, (min) is informative and not the principal<br>indicator of signal strength. A received power below this value cannot|||||1303.54 – 1305.63nm|
|be compliant; however, a value above this does not ensure<br>compliance.|||||1308.09 – 1310.19nm|
|4)Specified at BER 2.4x10-4||||LOS Assert|Min -30dBm|
|5)Typical value, specified as an indicator<br>individual components.||of strength. Varies between||LOS De-assert|Max -14dBm|
|**Safety/regulatory compliance:**||||LOS Hysteresis|Min 0.5dB|
|TUV/UL/FDA (contact Smartoptics for|latest certification information)|||DDM|Yes|
|RoHS compliance||||MSA compliance|QSFP-DD MSA, CMIS4.0|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.1 

## APPLICATION CODE LIST 

|**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**|**MSA**||
|---|---|---|---|---|---|---|
|1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|RS-FEC|400G ER4||
|2|4 x 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|RS-FEC|100G ER1-30||
|3|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|P-FEC|400G ER4, with P-FEC||



## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQD023-SL4C-SO|QSFP-DD 400G-ER4 Lite 30km CMIS4.0|



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

