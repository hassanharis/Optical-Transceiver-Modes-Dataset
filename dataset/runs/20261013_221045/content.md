DATASHEET 

6.0 

## **QSFP-DD 400GBASE-SR8 MPO, CMIS4.0** QSFP-DD 400GBASE-SR8, 8x50G-SR, PAM4 CMIS4.0, 8x850 nm 100m 2.0dB MPO APC 

## TQD024-M85C-SO 

The TQD024-M85C-SO is a QSFP-DD form-factor transceivers for 400Gbps Ethernet applications. It is intended for use in interand intra-connect applications within data centers between switches, routers, storage equipment etc. The optical performance is in accordance with the 400GBASE-SR8 IEEE 802.3cd standard, i.e. for optical distances up to 100m over a MultiMode (MM) OM4grade ribbon fiber. 

The electrical interface consists of eight 53.125G signals (400GAUI-8) that are converted to eight PAM4-modulated channels/lanes to transport the Ethernet signal. The transceiver can also be set in 8x50GAUI-1 mode to enable 400G to 8x 50G optical break-out configurations. Digital diagnostics functions are available via an I2C interface, as specified by the QSFP-DD MSA. The optical interface to the transceiver is an angled polished (APC) MPO16 connector. 

Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 2.4 x 10-4. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey QSFP-DD||**Transmitter data:**||
|Transmission media|MM (MPO-16 APC)||Output power, per lane|Min: -6.5dBm3)|
|Typical reach|70m @ OM3, 100m @ OM4|||Max: +4.0dBm|
|Nominal wavelength|8x 850nm||Output power, OMA outer,<br>per lane|Min: -4.5dBm|
|Interface standards|400GBASE-SR8|||Max: +3.0dBm|
|Electrical interfaces|400GAUI-8 or 4x100GAUI-2||ER|Min: 3dB|
|Bit rate support|425Gbps1)||Transmit wavelength|840 – 860nm|
||53.125Gbd2)||**Receiver data:**||
|Protocol support|400GbE, 8x50GbE||Receiver sensitivity, OMA, per<br>lane|-6.5dBm4)|
|Power budget|0 – 2.0dB||Minimum input power, per<br>lane|-8.5dBm3)|
|Power consumption|< 8W||Overload (max power), per<br>lane|+4.0dBm|
|Operating temperature|0°C to +70°C||Wavelength range|840 – 860nm|
|Storage temperature|-40°C to +85°C||LOS Assert|Min -30dBm|
||||LOS De-assert|Max -9dBm|
|1)Aggregated line rate 400GbE|||LOS Hysteresis|Min 0.5dB|
|2)Line baud rate|||DDM|Yes|
|3)Average receive power, (min) is informative and not the principal<br>indicator of signal strength. A received power below this value cannot|||MSA compliance|QSFP-DD MSA|
|be compliant; however, a value above this does not ensure<br>||||CMIS4.0|



- 3) Average receive power, (min) is informative and not the principal indicator of signal strength. A received power below this value cannot be compliant; however, a value above this does not ensure compliance. 

- 4) Specified at BER 2.4x10-4 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.0 

## APPLICATION CODE LIST 

|**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**|**MSA**||
|---|---|---|---|---|---|---|
|1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|RS-FEC|400GBASE-SR8||
|2|8 x 50GBASE-R|8x 50GAUI-1 (1x 50G)|400G|RS-FEC|50GBASE-SR||
|3|4 x 100GBASE-R|4x 100GAUI-2 (4x 100G)|400G|P-FEC|100GBASE-SR2||



## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQD024-M85C-SO|QSFP-DD 400G SR8 100m CMIS4.0 MPO|



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

DATASHEET 

6.0 



Subject to change without notice. For more information visit smartoptics.com. 

