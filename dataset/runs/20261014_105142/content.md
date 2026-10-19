DATASHEET 

6.4 

**QSFP-DD OPENROADM 400G HIGH POWER, ENC** QSFP-DD, 400G, OpenROADM, Coh Tunable, High Tx power, Flexgrid, Encryption, CMIS5.0, LC 

## OVERVIEW – TQD017-TUNC-SO 

The TQD017-TUNC-SO is an QSFP-DD form-factor (type 2a) DWDM transceiver conforming to the OpenROADM MSA. The module is also encryption capable, using AES-256. 

The output power of 0dBm unlocks the potential for the module transmit 400G signals in already existing, 100GHz spacing, ROADM architectures. 

The OpenZR+ MSA provides a flexible solution for operators having routers that not yet have migrated to 400G services. The TQD017-TUNC-SO can as an example be used in the Smartoptics DCP-404 Muxponder to combine 4x 100G flows to a 400G OpenZR+ signal to be transported over an optical network. 



OpenROADM application codes will allow the module to run over ROADM (Reconfigurable Add/Drop Multiplexer) compliant to the OpenROADM 2.0 and 5.0 MSA. 

The below table lists the OpenROADM mode supported by TQD017-TUNC-SO. 

|**CMIS**<br>**Application**<br>**Code**|<br>**Host format**|**Electrical interface**|**Payload**|**FEC**|**Modulation**|**Line Symbol**<br>**Baud Rate**|**MSA format**||
|---|---|---|---|---|---|---|---|---|
|1|4x100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|oFEC|DP-16QAM|63.1 GBd|OpenROADM 5.0||
|2|3x100GBASE-R|3x 100GAUI-2 (2x 50G)|300G|oFEC|DP-8QAM|63.1 GBd|OpenROADM 5.0||
|3|2x100GBASE-R|2x 100GAUI-2 (2x 50G)|200G|oFEC|DP-QPSK|63.1 GBd|OpenROADM 5.0||
|3|2x100GBASE-R|2x 100GAUI-2 (2x 50G)|200G|oFEC|DP-16QAM|31.6 GBd|OpenROADM 5.0||
|5|100GBASE-R|100GAUI-2 (2x 50G)|100G|oFEC|DP-QPSK|31.6 GBd|OpenROADM 5.0||
|6|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|oFEC|DP-16QAM|63.1 GBd|OpenROADM 5.0||
|7|200GBASE-R|200GAUI-4 (2x 200G)|200G|oFEC|DP-QPSK|63.1 GBd|OpenROADM 5.0||
|8|200GBASE-R|200GAUI-4 (2x 200G)|200G|oFEC|DP-16QAM|31.6 GBd|OpenROADM 5.0||
|9|100GBASE-R|CAUI-4 w/o FEC (4x 25G)|100G|oFEC|DP-QPSK|31.6 GBd|OpenROADM 5.0||
|10|100GBASE-R|CAUI-4 with FEC (4x 25G)|100G|oFEC|DP-QPSK|31.6 GBd|OpenROADM 5.0||
|11|100GBASE-R|CAUI-4 w/o FEC (4x 25G)|100G|SC-FEC|DP-DQPSK|31.6 GBd|OpenROADM 2.0||
|12|100GBASE-R|CAUI-4 with FEC (4x 25G)|100G|SC-FEC|DP-DQPSK|31.6 GBd|OpenROADM 2.0||
|13|OTU4|OTL4.4 (4x 28G)|100G|SC-FEC|DP-DQPSK|31.6 GBd|OpenROADM 2.0||



The SO-TQD017-TUNC-SO will automatically configure the above via the Application modes. The TQD017-TUNC-SO operates as an OTN transceiver/transponder, maps Ethernet signal(s) to an intermediate ODUFlex,OTUCn/FlexO-x frame structure, then adapts the frame structure with SC-FEC or oFEC. The encoded signal is subsequently DSP framed and modulated for transmission as a coherent Dual Polarity mQAM, QPSK or DQPSK signal. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.4 

## TECHNICAL DATA 

The optical characteristics are separated into Generic and Application code specific sections. The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|**Parameter**|**Value**|
|---|---|
|Technology|DWDM QSFP-DD type 2a|
|Transmission media|SM (2x LC)|
|Nominal wavelengths|191.3 - 196.1THz (tunable) 100GHz|
|Interface standards|OpenROADM|
|Operating temperature|+15OC to +75OC1)|
|Storage temperature|-40OC to +85OC|
|DDM functions|Total received power|
||Coherent channel power|
||OSNR, eSNR, PDL, dispersion, DGD|
||Case temperature|



- 1) The module will turn up from cold start at ambient temperature as low as 

- -5C and will reach specifications after self-heating up to min temperature. 

- 3) The module transmit power can be provisioned up to the maximum available TX power. 

If the TX power is not provisioned by the host, the module TX power will default to the maximum available power, which can be any power level in the specified 10dB range. 

|**Parameter**|**Value**|
|---|---|
|MSA|QSFP-DD MSA’s, CMIS5.0|
|Misc|Sync-E support, LLDP, RMON, Encryption|
|Power consumption, EOL|24.7W @400G|
||24.1W @300G|
||22.6W @200G|
||19.6W @100G|
|Tx Power|Min 0dBm3)|
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

6.4 

## OPTICAL SPECIFICATION - APPLICATION CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Appl**<br>**mode**|**Line**<br>**rate**|**Host format**|**Line**<br>**Modulation**|<br>**Tx Power1)**|**Rx sens**<br>**@ OSNR >36dB**|<br>**Rx**<br>**@ OSNR**|**Rx OSNR**<br>**@1dB penalty**|**Default CDC**<br>**range**|**Maximum**<br>**CDC Search**<br>**range2)**|
|---|---|---|---|---|---|---|---|---|---|
|1|400G|<br>4x 100GAUI-2|DP-16QAM|<br>1dBm|-20dBm|23.5dB@ -14dBm|25.0dB@ -16dBm|12 000 ps/nm|<br>48 000 ps/nm|
|2|300G|<br>3x 100GAUI-2|DP-8QAM|1dBm|-23dBm|20.5dB@ -16dBm|21.5dB@ -20dBm|48 000 ps/nm|<br>96 000 ps/nm|
|3|200G|<br>2x 100GAUI-2|DP-QPSK|1dBm|-28dBm|14.8dB@ -18dBm|15.8dB@ -28dBm|48 000 ps/nm|<br>96 000 ps/nm|
|4|200G|<br>2x 100GAUI-2|DP-16QAM|<br>1dBm|-23dBm|20.5dB@ -16dBm|21.5dB@-18dBm|30 000 ps/nm|<br>77 000 ps/nm|
|5|100G|<br>1x 100GAUI-2|DP-QPSK|1dBm|-32dBm|11.8dB@ -20dBm|12.8@ -25dBm|77 000 ps/nm|<br>154 000 ps/nm|
|6|400G|<br>1x 400GAUI-8|DP-16QAM|<br>1dBm|-20dBm|23.5dB@ -14dBm|25.0dB@ -16dBm|12 000 ps/nm|<br>48 000 ps/nm|
|7|200G|<br>1x 200GAUI-4|DP-QPSK|1dBm|-28dBm|14.8dB@ -18dBm|15.8dB@ -28dBm|48 000 ps/nm|<br>96 000 ps/nm|
|8|200G|<br>1x 200GAUI-4|DP-16QAM|<br>1dBm|-23dBm|20.5dB@ -16dBm|21.5dB@-18dBm|30 000 ps/nm|<br>77 000 ps/nm|
|9|100G|<br>CAUI-4 w/o FEC|DP-QPSK|1dBm|-32dBm|11.8dB@ -20dBm|12.8@ -25dBm|77 000 ps/nm|<br>154 000 ps/nm|
|10|100G|<br>CAUI-4 with FEC|DP-QPSK|1dBm|-32dBm|11.8dB@ -20dBm|12.8@ -25dBm|77 000 ps/nm|<br>154 000 ps/nm|
|11|100G|<br>CAUI-4 w/o FEC|DP-DQPSK|<br>1dBm|-30dBm|14.5dB@ -19dBm|15.5dB@ -24dBm|80 000 ps/nm|<br>115 000 ps/nm|
|12|100G|<br>CAUI-4 with FEC|DP-DQPSK|<br>1dBm|-30dBm|14.5dB@ -19dBm|15.5dB@ -24dBm|80 000 ps/nm|<br>115 000 ps/nm|
|13|100G|<br>OTU4|DP-DQPSK|<br>1dBm|-30dBm|14.5dB@ -19dBm|15.5dB@ -24dBm|80 000 ps/nm|<br>115 000 ps/nm|



1) Minimum Tx power without attenuation. The module Tx power can be attenuated with 10dB from the maximum available Tx power. If the Tx power is not provisioned by the host, the module Tx power will default to the maximum available power. 

- 2) Maximum provisionable CD search range. Increasing the search range will increase the power consumption of the transceiver. 

## ORDERING INFORMATION 

**Ordering code Description** TQD017-TUNC-SO QSFP-DD OTN High Tx Power Coh Tunable Flexgrid Encryption CMIS5.0 **Latency:             w/o encryption        With encryption** 400G CFEC: 8us - 400G OFEC: 5us 7.5us 300G OFEC: 6us 8.5us 200G OFEC: 7us 9.5us 100G OFEC: 11us 13.5us 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.4 

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

