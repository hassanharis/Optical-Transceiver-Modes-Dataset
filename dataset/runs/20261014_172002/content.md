DATASHEET 

6.13 

## **QSFP-DD 100GE DP-QPSK 450KM ETH/OTN** 

QSFP-DD 100G Ethernet/OpenROADM Coherent Tunable SM 450km, Encryption, CMIS5.0, LC 

## OVERVIEW 

The TQD011-TUNC-SO is an QSFP-DD form-factor (type 2a) DWDM transceiver for 100Gbps Ethernet, OTN and OpenROADM applications. The transceiver is intended for use in interconnect applications between data centers with switches, routers etc. having QSFP-DD support but where the services are limited to 100Gbps. 

TQD011-TUNC-SO conforms to both the 100G option of OpenZR+ and the OpenROADM 3.0/4.0, using the powerful Open Forward Error Correction (oFEC) scheme giving a Net Coding Gain (NCG) of 11.6dB at a pre-FEC BER of 2.0x10[-2] . TQD011TUNC-SO also supports the OpenROADM 2.0 with the media format OTU4 and SC-FEC giving a Net Coding Gain (NCG) of 9.4dB at a pre-FEC BER of 4.5x10[-3] 

The Chromatic Dispersion Compensation (CDC) limit of TQD011-TUNC-SO is 8600ps/nm providing an operating range of 450km in amplified links. 

TQD011-TUNC-SO also allows AES-256 encryption through I[2] C. 

The transceiver is managed via I[2] C interface and according to CMIS 5.0. 

The TQD011-TUNC-SO supports the following CMIS application codes: 

|**CMIS**<br>**Application**<br>**code**|**Host format**|**Payload**|**Media**<br>**Format**|**FEC**|**Modulation**|**Media Symbol**<br>**Baud rate**|**Operating**<br>**range**|**Encryption**<br>**support**||
|---|---|---|---|---|---|---|---|---|---|
|1|CAUI4|100G|OpenZR+|oFEC|DP-QPSK|30.1Gbd|450km|No||
|2|CAUI4 KR4 FEC|100G|OpenZR+|oFEC|DP-QPSK|30.1Gbd|450km|No||
|3|100GAUI-2 KP4 FEC|<br>100G|OpenZR+|oFEC|DP-QPSK|30.1Gbd|450km|No||
|4|CAUI4|100G|FlexO-1|oFEC|DP-QPSK|31.6Gbd|450km|Yes||
|5|CAUI4 KR4 FEC|100G|FlexO-1|oFEC|DP-QPSK|31.6Gbd|450km|Yes||
|6|100GAUI-2 KP4 FEC|<br>100G|FlexO-1|oFEC|DP-QPSK|31.6Gbd|450km|Yes||
|7|OTL4.4|100G|FlexO-1|oFEC|DP-QPSK|31.6Gbd|450km|Yes||
|8|CAUI4|100G|OTU4|SC-FEC|DP-DQPSK|28.0Gbd|450km|No||
|9|CAUI4 KR4 FEC|100G|OTU4|SC-FEC|DP-DQPSK|28.0Gbd|450km|No||
|10|100GAUI-2 KP4 FEC|<br>100G|OTU4|SC-FEC|DP-DQPSK|28.0Gbd|450km|No||
|11|OTL4.4|100G|OTU4|SC-FEC|DP-DQPSK|28.0Gbd|450km|No||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.13 

## TECHNICAL DATA 

The optical characteristics are divided into _Generic_ and _Application_ code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _Application_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|**Parameter**|**Value**<br>DWDM QSFP-DD type 2a<br>SM (2x LC)<br>Unamplified: 130km<br>Dispersion limited: 450km<br>Tunable C-band<br>OpenZR+ and OpenROADM<br>100GBASE-R<br>SyncE<br>17.0W (Class 8)<br>0°C to +75°C<br>-40°C to +85°C|**Parameter**|**Value**|
|---|---|---|---|
|Technology||Transmit VOA dynamic range|0 - 10dB|
|Transmission media||Transmit wavelengths|191.275 - 196.125THz|
|Typical reach|||in minimum 6.25GHz steps|
|||Tx In-Band OSNR|Min 34dB/0.1nm|
|Nominal wavelengths||Tx Out-Of-Band OSNR|Min 30dB/0.1nm|
|Interface standards||Rx Overload1)|Signal power: 13dBm|
|Protocol support|||Total power: 15dBm|
|||Wavelength switch time|Max 86s channel to channel|
|Power consumption||DDM|Yes|
|Operating temperature||MSA compliance|QSFP-DD MSA|
|Storage temperature|||OpenZR+ MSA, OpenROADM<br>MSA, CMIS 5.0|



1) Specified to be within the pre-FEC BER range of the selected application code. Rx damage threshold is located at 16dBm. 

**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.13 

## OPTICAL SPECIFICATION - APPLICATION CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Appl**<br>**mode**|**Line**<br>**rate**|**Host format**|**Maximum, Tx**<br>**Power1)**|**Rx sens**<br>**@ high**<br>**OSNR2)**|**Rx**<br>**@ OSNR**|**Rx OSNR**<br>**@0.5dB penalty**|**Rx OSNR**<br>**@1dB penalty**|**CDC range**<br>**@0.5dB**<br>**OSNR**<br>**penalty**|
|---|---|---|---|---|---|---|---|---|
|1|100G|<br>CAUI4|-5.0dBm to 0dBm|-32dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|2|100G|<br>CAUI4 KR4 FEC|-5.0dBm to 0dBm|-32dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|3|100G|<br>100GAUI-2 KP4 FEC|<br>-5.0dBm to 0dBm|-32dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|4|100G|<br>CAUI4|-5.0dBm to 0dBm|-32dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|5|100G|<br>CAUI4 KR4 FEC|-5.0dBm to 0dBm|-32dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|6|100G|<br>100GAUI-2 KP4 FEC|<br>-5.0dBm to 0dBm|-32dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|7|100G|<br>OTL4.4|-5.0dBm to 0dBm|-32dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|8|100G|<br>CAUI4|-5.0dBm to 0dBm|-30dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|9|100G|<br>CAUI4 KR4 FEC|-5.0dBm to 0dBm|-30dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|10|100G|<br>100GAUI-2 KP4 FEC|<br>-5.0dBm to 0dBm|-30dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|
|11|100G|<br>OTL4.4|-5.0dBm to 0dBm|-30dBm|15.5dB@-20dBm|16.0dB@-23dBm|16.5dB@-25dBm|8 600 ps/nm|



1) The module transmit power can be provisioned up to the maximum available TX power which is somewhere in the range between -5.0 to 0dBm. The Tx power can be provisioned with up to 10dB below the maximum available power level. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power. 

2) Rx sensitivity is specified at a OSNR > 36dB, 

|**FEC modes**|**Latency [µs]**|**Encryption**<br>**Enabled [µs]**||
|---|---|---|---|
|oFEC|11|13.5||
|SC-FEC|20|22.5||



## ORDERING INFORMATION 

|**Ordering code**|**Description**|
|---|---|
|TQD011-TUNC-SO|QSFP-DD 100G Ethernet/OTN/OpenROADM, Coherent Tuneable SM 450km Encryption CMIS5.0 LC|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.13 

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
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

