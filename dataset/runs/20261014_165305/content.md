DATASHEET 

6.1 

## **TQD032-TUNC-SO** 

QSFP-DD OIF 400G-ZR Ethernet Coh Tunable Flexgrid 120km LC D9128-D9612, CMIS5.0 

## OVERVIEW 

The TQD032-TUNC-SO is a QSFP-DD form-factor (type 2) DWDM transceiver for 400 Gbps Ethernet applications. The transceiver is intended for use in interconnect applications between data centers with switches, routers etc. 

TQD032-TUNC-SO supports both the amplified (Application Code 0x01) and the un-amplified (Application Code 0x02) use cases as defined in the OIF 400ZR specification.  Application code 3 is 

The dispersion performance is in accordance with OIF 400ZR for distances up to 120km over a SingleMode (SM) fiber using a single optical carrier at 60Gbaud and 16QAM coherent modulation. The transmitter is tunable over the ITU C-Band at 100 GHz grid (75 GHz grid is optional). 

The electrical interface is according to IEEE 802.3bs 400GAUI-8 enabling SO-TQSFP-DD-4CC-ZR to support 400G transport according to OIF-ZR specification. The 400GAUI-8 client/electrical interface is compatible with IEEE P802.3bs 8 lane 56G PAM-4, as used for “grey” datacenter optical transceivers, for example 400GBASE-DR4. 



This transceiver provides digital diagnostic functions via a 2-wire serial interface and a management interface according to CMIS5.0. 

The transceiver supports the commercial temperature range (C-temp): 0°C to 70°C (32°F to 158°F). 

||**CMIS**<br>**Application**<br>**Code**|<br>**Host format**|**Electrical interface**|**Payload**|**FEC**|**Modulation**|<br>**Line Symbol**<br>**Baud Rate**|**MSA format**|**Media ID**<br>**(hex)**||
|---|---|---|---|---|---|---|---|---|---|---|
||1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x01|0x3E||
||2|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x02|0x3F||
||3|4 × 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x01|0x3E||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.1 

## TECHNICAL DATA 

The optical characteristics are into Generic and Application code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _Application_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|**Parameter**|**Value**|
|---|---|
|Technology|DWDM QSFP-DD type 2a|
|Transmission media|SM (2x LC)|
|Nominal wavelengths|191.3 - 196.1THz (tunable) 6.25GHz Grid|
|Interface standards|OIF 400ZR|
|Operating temperature|+15OC to +75OC1)|
|Storage temperature|-40OC to +85OC|
|DDM functions|Total received power|
||Coherent channel power|
||OSNR, eSNR, PDL, dispersion, DGD|
||Case temperature|



- 1) The module will turn up from cold start at ambient temperature as low as 

- -5C and will reach specifications after self-heating up to min temperature. 

|**Parameter**|**Value**|
|---|---|
|MSA|QSFP-DD MSA’s, CMIS5.0|
|Misc|Sync-E support, LLDP, RMON|
|Power consumption, EOL|17.9W @400G|
|Tx Power|Min -10dBm3)|
|Tx In-band OSNR|Min 34dB/0.1nm|
|Tx Out-Of-Band OSNR|Min 30dB/0.1nm|
|Rx overload|Max: +1dBm|
|Rx_LOS Assert|-28.0dBm4)|
|Receiver turn-up|Max 30ms from warm start|
||Max 120s from cold start|
|Absolute max conditions|Rx signal input power: +13dBm|
||Rx total input power: +15dBm|



- 2) Increasing the CD range with 2x of default range will increase the power consumption by 0.6W. 

- 3) The module transmit power can be provisioned up to the maximum available TX power. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power. The provisional Tx power range of the module is 10dB. 

- 4) Set to comply with 400G modes. Can be changed on individual modules to fully support other modes. 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) 

RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.1 

## OPTICAL SPECIFICATION - APPLICATION CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Appl**<br>**code**|**Line**<br>**rate**|**Host format**|**Tx Power1)**|**Rx sens**<br>**@ OSNR**<br>**> 36dB**|**Rx @ OSNR2)**|**Rx OSNR**<br>**@0.5dB penalty2)**|**Rx OSNR**<br>**@1dB penalty2)**|**Default CDC**<br>**range**|**Maximum CDC**<br>**search range3)**|
|---|---|---|---|---|---|---|---|---|---|
|1|400G|<br>1x 400GAUI-8|<br>-10dBm to -6dBm|-20dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000 ps/nm|
|2|400G|<br>1x 400GAUI-8|<br>-10dBm to -6dBm|-20dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000 ps/nm|
|3|400G|<br>1x 400GAUI-8|<br>-10dBm to -6dBm|-21dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000 ps/nm|



1) Minimum Tx power without attenuation. The module Tx power can be attenuated with 10dB from the maximum available Tx power. If the Tx power is not provisioned by the host, the module Tx power will default to the maximum available power. 

- 2) Specified as [Min OSNR Value @ Min Rx power for the OSNR value]. 

- 3) Maximum provisionable CD search range. Increasing the search range will increase the power consumption of the transceiver. 

## ORDERING INFORMATION 

|**Ordering code**|**Description**|**Latency:**||
|---|---|---|---|
|TQD032-TUNC-SO|QSFP-DD OIF 400ZR Coh Tunable Flexgrid LC, Low power, CMIS5.0|400G CFEC:|8us|



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
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

