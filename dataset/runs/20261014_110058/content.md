DATASHEET 

6.8 

## **TQD013-TUNC-SO** 

QSFP-DD, OIF 400ZR, OpenZR+, Coh Tunable, High-power, CMIS5.0, LC 

## OVERVIEW 

The TQD013-TUNC-SO is an QSFP-DD form-factor (type 2a) DWDM transceiver conforming to the OIF 400ZR for 400Gbps as well as the OpenZR+ MSA for 100Gbps to 400Gbps Ethernet applications. 

The output power of 0dBm unlocks the potential for the module to transmit 400G signals in already existing, 100GHz spacing, ROADM architectures. 

The OpenZR+ MSA provides a flexible solution for operators having routers that not yet have migrated to 400G services. The TQD013-TUNC-SO can as an example be used in the Smartoptics DCP-404 Muxponder to combine up to 4x 100G flows to a 100G/200G/300G/400G OpenZR+ signal to be transported over an optical network. 


The below table lists the OIF 400ZR and OpenZR+ modes supported by TQD013-TUNC-SO. 

|**CMIS**<br>**Application**<br>**Code**|<br>**Host format**|**Electrical interface**|**Payload**|**FEC**|**Modulation**|<br>**Line Symbol**<br>**Baud Rate**|**MSA format**||
|---|---|---|---|---|---|---|---|---|
|1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x01||
|2|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x02||
|3|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA||
|4|2 × 200GBASE-R|2x 200GAUI-4 (2x 200G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA||
|5|4 × 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA||
|6|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA, Enhanced||
|7|2 × 200GBASE-R|2x 200GAUI-4 (2x 200G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA, Enhanced||
|8|4 × 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA, Enhanced||
|9|2 × 100GBASE-R|2x 100GAUI-2 (2x 50G)|200G|oFEC|DP-QPSK|60.1GBd|OpenZR+ MSA||
|10|1 × 100GBASE-R|1x 100GAUI-2 (2x 50G)|100G|oFEC|DP-QPSK|30.1GBd|OpenZR+ MSA||
|11|3 × 100GBASE-R|3x 100GAUI-2 (2x 50G)|300G|oFEC|DP-8QAM|60.1GBd|OpenZR+ MSA||
|12|3 × 100GBASE-R|3x 100GAUI-2 (2x 50G)|300G|oFEC|DP-8QAM|60.1GBd|OpenZR+ MSA, Enhanced||
|13|4 × 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|CFEC|DP-16QAM|59.8GBd|OIF400ZR app code 0x01||
|14|2 × 100GBASE-R|2x 100GAUI-2 (2x50G)|200G|oFEC|DP-16QAM|30.1GBd|OpenZR+ MSA, Enhanced||
|15|100GBASE-R|1x CAUI-4 w/o FEC|100G|oFEC|DP-QPSK|30.1GBd|OpenZR+ MSA||



TQD013-TUNC-SO will automatically configure the above via the Application modes. For 400G applications, the TQD013-TUNCSO asynchronously (GMP) maps an Ethernet signal from a switch/router to an intermediate 400ZR frame structure, then adapts the frame structure to the selected FEC engine. The encoded signal is subsequently DSP framed and modulated for transmission as a coherent Dual Polarity signal. 

Note! CMIS application codes 6, 7, 8 and 12 are not interoperable with the OpenZR+ MSA. These modes have been enhanced in to increase the optical performance on the Media side. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.8 

## TECHNICAL DATA 

The optical characteristics are into Generic and Application code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _Application_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|**Parameter**|**Value**|
|---|---|
|Technology|DWDM QSFP-DD type 2a|
|Transmission media|SM (2x LC)|
|Nominal wavelengths|191.3 - 196.1THz (tunable) 6.25GHz Grid|
|Interface standards|OIF 400ZR / OpenZR+|
|Operating temperature|+15OC to +75OC1)|
|Storage temperature|-40OC to +85OC|
|DDM functions|Total received power|
||Coherent channel power|
||OSNR, eSNR, PDL, dispersion, DGD|
||Case temperature|



- 1) The module will turn up from cold start at ambient temperature as low as 

- -5C and will reach specifications after self-heating up to min temperature. 

- 2) Increasing the CD range with 2x of default range will increase the power consumption by 0.6W. 

- 3) The module transmit power can be provisioned up to the maximum available TX power. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power. The provisional Tx power range of the module is 10dB. 

|**Parameter**|**Value**|
|---|---|
|MSA|QSFP-DD MSA’s, CMIS5.0|
|Misc|Sync-E support, LLDP, RMON|
|Power consumption, EOL<br>@ Default CD Range2)|23.1W @400G|
||23.4W @300G|
||21.9W @200G|
||18.0W @100G|
|Tx Power|Min 1dBm3)|
|Tx In-band OSNR|Min 38dB/0.1nm|
|Tx Out-Of-Band OSNR|Min 42dB/0.1nm|
|Rx_LOS Assert|-28.0dBm4)|
|Receiver turn-up|Max 30ms from warm start|
||Max 120s from cold start|
|Absolute max conditions|Rx signal input power: +13dBm|
||Rx total input power: +15dBm|



- 4) Set to comply with 400G modes. Can be changed on individual modules to fully support other modes. 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) 

RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.8 

## OPTICAL SPECIFICATION - APPLICATION CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Appl**<br>**code**|**Line**<br>**rate**|**Host format**|**Tx**<br>**Power1**<br>**)**|**Rx sens**<br>**@ OSNR >**<br>**36dB**|**Rx @ OSNR2)**|**Rx OSNR**<br>**@0.5dB penalty2)**|**Rx OSNR**<br>**@1dB penalty2)**|**Default CDC**<br>**range**|**Maximum CDC**<br>**search range**|
|---|---|---|---|---|---|---|---|---|---|
|1|400G|<br>1x 400GAUI-8|1dBm|-20dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000 ps/nm|
|2|400G|<br>1x 400GAUI-8|1dBm|-20dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000 ps/nm|
|3|400G|<br>1x 400GAUI-8|1dBm|-21dBm|23.4dB@-12dBm|23.9dB@-14dBm|24.4dB@-16dBm|13 000 ps/nm|<br>52 000 ps/nm|
|4|400G|<br>2x 200GAUI-4|1dBm|-21dBm|23.4dB@-12dBm|23.9dB@-14dBm|24.4dB@-16dBm|13 000 ps/nm|<br>52 000 ps/nm|
|5|400G|<br>4x 100GAUI-2|1dBm|-21dBm|23.4dB@-12dBm|23.9dB@-14dBm|24.4dB@-16dBm|13 000 ps/nm|<br>52 000 ps/nm|
|6|400G|<br>1x 400GAUI-8|1dBm|-21dBm|23.1dB@-12dBm|23.6dB@-14dBm|24.1dB@-16dBm|13 000 ps/nm|<br>52 000 ps/nm|
|7|400G|<br>2x 200GAUI-4|1dBm|-21dBm|23.1dB@-12dBm|23.6dB@-14dBm|24.1dB@-16dBm|13 000 ps/nm|<br>52 000 ps/nm|
|8|400G|<br>4x 100GAUI-2|1dBm|-21dBm|23.1dB@-12dBm|23.6dB@-14dBm|24.1dB@-16dBm|13 000 ps/nm|<br>52 000 ps/nm|
|9|200G|<br>2x 100GAUI-2|1dBm|-29dBm|14.8dB@-18dBm|15.3dB@-20dBm|15.8dB@-22dBm|50 000 ps/nm|<br>100 000 ps/nm|
|10|100G|<br>1x 100GAUI-2|1dBm|-32dBm|11.5dB@-20dBm|12.0dB@-23dBm|12.5dB@-25dBm|80 000 ps/nm|<br>100 000 ps/nm|
|11|300G|<br>3x 100GAUI-2|1dBm|-22dBm|20.3dB@-15dBm|20.8dB@-17dBm|20.5dB@-19dBm|50 000 ps/nm|<br>100 000 ps/nm|
|12|300G|<br>3x 100GAUI-2|1dBm|-23dBm|19.5dB@-15dBm|20.0dB@-17dBm|21.3dB@-19dBm|50 000 ps/nm|<br>100 000 ps/nm|
|13|400G|<br>4x 100GAUI-2|1dBm|-20dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000 ps/nm|
|14|200G|<br>2x 100GAUI-2|1dBm|-24dBm|19.3dB@-15dBm|19.8dB@-18dBm|20.3dB@-20dBm|21 000 ps/nm|<br>85 000 ps/nm|
|15|100G|<br>1x CAUI-4 w/o FEC|1dBm|-32dBm|11.5dB@-20dBm|12.0dB@-23dBm|12.5dB@-25dBm|80 000 ps/nm|<br>160 000 ps/nm|



1) Minimum Tx power without attenuation. The module Tx power can be attenuated with 10dB from the maximum available Tx power. If the Tx power is not provisioned by the host, the module Tx power will default to the maximum available power. 

2) Specified as [Min OSNR Value @ Min Rx power for the OSNR value]. 

3) maximum provisionable CD search range. Increasing the search range will increase the power consumption of the transceiver. 

|ORDERING|INFORMATION|**Latency:**||
|---|---|---|---|
|||400G CFEC:|8us|
|**Ordering code**|**Item Name**|400G OFEC:|5us|
|||300G OFEC:|6us|
|TQD013-TUNC-SO|<br>QSFP-DD OpenZR+ HPow Coh-T SM CMIS5.0|200G OFEC:|7us|
|||100G OFEC:|11us|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.8 

## GENERAL DEFINITIONS 

|**Parameter**|**Description**||
|---|---|---|
||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
|Technology|CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.<br>DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.||
||BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
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

