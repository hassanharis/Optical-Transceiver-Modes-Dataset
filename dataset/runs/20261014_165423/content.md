DATASHEET 

6.1 

## **TQD033-TUNC-SO** 

QSFP-DD OIF 400G OpenZR+ Coh Tunable Flexgrid LC D9128-D9612, Low power, CMIS5.0 

## OVERVIEW 

The TQD033-TUNC-SO is a QSFP-DD form-factor (type 2a) DWDM transceiver conforming to the OIF 400ZR for 400Gbps as well as the OpenZR+ MSA for 100Gbps to 400Gbps Ethernet applications. 

The OpenZR+ MSA provides a flexible solution for operators having routers that not yet have migrated to 400G services. The TQD033-TUNC-SO can as an example be used in the Smartoptics DCP-404 Muxponder to combine 4x 100G flows to a 400G OpenZR+ signal to be transported over an optical network. 



OpenZR+ is currently only defined for amplified line systems. OIF 400ZR is defined for both amplified as well as un-amplified configurations. The Application Mode 2 (OIF app code 0x02) corresponds to the un-amplified OIF 400ZR configuration. 

The below table lists the OIF 400ZR and OpenZR+ modes supported by TQD033-TUNC-SO. 

|**CMIS**<br>**Application**<br>**Code**|<br>**Host format**|**Electrical interface**|**Payload**|**FEC**|**Modulation**|<br>**Line Symbol**<br>**Baud Rate**|**MSA format**|**Media ID**<br>**(hex)**||
|---|---|---|---|---|---|---|---|---|---|
|1|400GBASE-R|1x 400GAUI-8 (8x 50G)|<br>400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x01|0x3E||
|2|400GBASE-R|1x 400GAUI-8 (8x 50G)|<br>400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x02|0x3F||
|3|4 × 100GBASE-R|4x 100GAUI-2 (2x 50G)|<br>400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x01|0x3E||
|4|400GBASE-R|1x 400GAUI-8 (8x 50G)|<br>400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA, (small<br>PMD)|0xC5||
|5|400GBASE-R|1x 400GAUI-8 (8x 50G)|<br>400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA|0xC0||
|6|4 × 100GBASE-R|4x 100GAUI-2 (2x 50G)|<br>400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA|0xC0||
|7|3 × 100GBASE-R|3x 100GAUI-2 (2x 50G)|<br>300G|oFEC|DP-8QAM|60.1GBd|OpenZR+ MSA|0xC1||
|8|400GBASE-R|1x 400GAUI-8 (8x 50G)|<br>400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA,<br>Enhanced mode1|0xCE||
|9|4 × 100GBASE-R|4x 100GAUI-2 (2x 50G)|<br>400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA<br>Enhanced mode1|0xCE||
|10|3 × 100GBASE-R|3x 100GAUI-2 (2x 50G)|<br>300G|oFEC|DP-8QAM|60.1GBd|OpenZR+ MSA<br>Enhanced mode1|0xCF||
|11|2x 100GBASE-R|2x 100GAUI-2 (2x 50G)|<br>200G|oFEC|DP-QPSK|60.1GBd|OpenZR+ MSA|0xC2||
|12|2x 100GBASE-R|2 x CAUI4 (4x 25G)<br>w/o FEC|200G|oFEC|DP-QPSK|60.1GBd|OpenZR+ MSA|0xC2||
|13|1x 100GBASE-R|1x 100GAUI-2 (2x 50G)|<br>100G|oFEC|DP-QPSK|30.1GBd|OpenZR+ MSA|0xC4||
|14|1x 100GBASE-R|1 x CAUI4 (4x 25G)<br>w/o FEC|100G|oFEC|DP-QPSK|30.1GBd|OpenZR+ MSA|0xC4||



1) Enhanced mode grants better optical performance but is not fully interoperable with OpenZR+. 

The TQD033-TUNC-SO will automatically configure the above via the Application modes. The TQD033-TUNC-SO asynchronously (GMP) maps an Ethernet signal from a switch/router to an intermediate 400ZR frame structure, then adapts the frame structure to the selected FEC engine. The encoded signal is subsequently DSP framed and modulated for transmission as a coherent Dual Polarity coherent signal. 


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
|Nominal wavelengths|191.275 - 196.125THz (tunable) 6.25GHz|
|Interface standards|OIF 400ZR / OpenZR+|
|Operating temperature|+15OC to +75OC1)|
|Storage temperature|-40OC to +85OC|
|DDM functions|Total received power|
||Coherent channel power|
||OSNR, eSNR, PDL, dispersion, DGD|
||Case temperature|



- 1) The module will turn up from cold start at ambient temperature as low as 

- -5C and will reach specifications after self-heating up to min temperature. 

- 2) See full power consumption data listed in the table in the section “Electrical characteristics”. 

- 3) Set to comply with 400G modes. Can be changed on individual modules to fully support other modes. 

|**Parameter**|**Value**|
|---|---|
|MSA|QSFP-DD MSA’s, CMIS5.0|
|Misc|Sync-E support, LLDP, RMON|
|Power consumption2)|Worst case 21.6W @400G|
||Worst case 21.8W @300G|
||Worst case 21.4W @200G|
||Worst case 17.3W @100G|
|Tx In-band OSNR|Min 42dB/0.1nm|
|Tx Out-Of-Band OSNR|Min 42dB/0.1nm|
|Rx_LOS Assert|-28.0dBm3)|
|Rx Overload|Max: +1dBm|
|Receiver turn-up|Max 30ms from warm start|
||Max 120s from cold start|
|Absolute max conditions|Rx signal input power: +13dBm|
||Rx total input power: +15dBm|



**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.1 

## OpenZR+ 

There are 11 OpenZR+ modes that can be set. The table below lists the primary optical parameters. 

|**Appl**<br>**mode**|**Line**<br>**rate**|**Host format**|**Tx Power1)**|**Rx sens**<br>**@ OSNR**<br>**>36dB**|**Rx @ OSNR2)**|**Rx OSNR**<br>**@0.5dB penalty**|**Rx OSNR**<br>**@1dB penalty**|**Default CDC**<br>**range**|**Maximum**<br>**CDC range3)**|
|---|---|---|---|---|---|---|---|---|---|
|1|400G|<br>1x 400GAUI-8|-10dBm to -6dBm|-20dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000ps/nm|
|2|400G|<br>1x 400GAUI-8|-10dBm to -6dBm|-20dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000ps/nm|
|3|400G|<br>1x 400GAUI-8|-10dBm to -6dBm|-21dBm|26dB@-12dBm|26.5dB@-14dBm|27.0dB@-15dBm|4 000 ps/nm|4 000ps/nm|
|4|400G|<br>1x 400GAUI-8|-10dBm to -6dBm|-20dBm|23.9dB@-12dBm|<br>24.2dB@-14dBm|24.7dB@-16dBm|13 000 ps/nm|<br>52 000ps/nm|
|5|400G|<br>1x 400GAUI-8|-13dBm to -9dBm|-21dBm|23.4dB@-12dBm|<br>23.9dB@-14dBm|24.4dB@-16dBm|13 000 ps/nm|<br>52 000ps/nm|
|6|400G|<br>4x 100GAUI-2|-13dBm to -9dBm|-21dBm|23.4dB@-12dBm|<br>23.9dB@-14dBm|24.4dB@-16dBm|13 000 ps/nm|<br>52 000ps/nm|
|7|300G|<br>3x 100GAUI-2|-12dBm to -8dBm|-22dBm|20.3dB@-15dBm|<br>20.8dB@-17dBm|21.3dB@-19dBm|26 000 ps/nm|<br>100 000ps/nm|
|8|400G|<br>1x 400GAUI-8|-13dBm to -9dBm|-21dBm|23.1dB@-12dBm|<br>23.6dB@-14dBm|24.1dB@-16dBm|13 000 ps/nm|<br>52 000ps/nm|
|9|400G|<br>4x 100GAUI-2|-13dBm to -9dBm|-21dBm|23.1dB@-12dBm|<br>23.6dB@-14dBm|24.1dB@-16dBm|13 000 ps/nm|<br>52 000ps/nm|
|10|300G|<br>3x 100GAUI-2|-12dBm to -8dBm|-23dBm|19.5dB@-15dBm|<br>20.0dB@-17dBm|20.5dB@-19dBm|26 000 ps/nm|<br>100 000ps/nm|
|11|200G|<br>2x 100GAUI-2|-10.5dBm to -6.5dBm|<br>-29dBm|15dB@-18dBm|15.5dB@-20dBm|16dB@-22dBm|50 000 ps/nm|<br>100 000ps/nm|
|12|200G|<br>2x CAUI4 w/o FEC|<br>-10.5dBm to -6.5dBm|<br>-29dBm|15dB@-18dBm|15.5dB@-20dBm|16dB@-22dBm|50 000 ps/nm|<br>100 000ps/nm|
|13|100G|<br>1x 100GAUI-2|-6dBm to -2dBm|-32dBm|11.8dB@-20dBm|<br>12.3dB@-23dBm|12.8dB@-25dBm|80 000 ps/nm|<br>160 000ps/nm|
|14|100G|<br>1x CAUI4 w/o FEC|<br>-6dBm to -2dBm|-32dBm|11.8dB@-20dBm|<br>12.3dB@-23dBm|12.8dB@-25dBm|80 000 ps/nm|<br>160 000ps/nm|



1) The module transmit power can be provisioned up to the maximum available TX power. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power, which can be any power level in the specified 4dB range. Based on the maximum available power, the host can attenuate the Tx power with up to 10dB. 

2) Specified as [Min OSNR Value @ Min Rx power for the OSNR value]. 3) Maximum provisionable CD search range. Increasing the search range will increase the total power consumption. 

**Latency:** 

400G CFEC: 8us 400G OFEC: 5us 300G OFEC: 6us 200G OFEC: 7us 100G OFEC: 11us 

## ELECTICAL CHARACTERISTICS 

The table below lists the worst case power consumption for each media code. The power consumption will also increase based on the host interface and Chromatic dispersion 

|**Appl**<br>**mode**|**Line**<br>**rate**|**Host format**|**Worst case power**<br>**consumption**|<br>**Addition**<br>**Muxponder mode1)**|**Additional Max**<br>**CD range2)**|
|---|---|---|---|---|---|
|1|400G|<br>1x 400GAUI-8|17.5|-|0.6|
|2|400G|<br>1x 400GAUI-8|17.5|-|0.6|
|3|400G|<br>1x 400GAUI-8|17.5|-|0.6|
|4|400G|<br>1x 400GAUI-8|20.3|-|0.6|
|5|400G|<br>1x 400GAUI-8|20.6|-|0.6|
|6|400G|<br>4x 100GAUI-2|20.6|0.4|0.6|
|7|300G|<br>3x 100GAUI-2|20.8|0.4|0.6|
|8|400G|<br>1x 400GAUI-8|20.6|-|0.6|
|9|400G|<br>4x 100GAUI-2|20.6|0.4|0.6|
|10|300G|<br>3x 100GAUI-2|20.8|0.4|0.6|
|11|200G|<br>2x 100GAUI-2|19.6|0.2|0.6|
|12|200G|<br>2x CAUI4 w/o FEC|<br>19.6|0.2|0.6|
|13|100G|<br>1x 100GAUI-2|16.7|-|0.6|
|14|100G|<br>1x CAUI4 w/o FEC|<br>16.7|-|0.6|



1) The power consumption figures are listed with the transceiver without multiplexing the host streams. If the transceiver is not running a 400GBASE-R stream, the transceiver will increase the power consumption according to the numbers listed in the table. 

2) The power consumption figures are listed with the default chromatic dispersion compensation range. If the dispersion range is configured above 2x default dispersion compensation, the transceiver shall add the power consumption figures according to the numbers listed in the table. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.1 

## ORDERING INFORMATION 

||**Ordering code**|**Description**|
|---|---|---|
||TQD033-TUNC-SO|QSFP-DD OIF 400G OpenZR+ Coh Tunable Flexgrid LC, Low power, CMIS5.0|
||GENERAL DEFINITIONS||
||**Parameter**|**Description**|
|||Grey; Transceiver type for non-WDM applications. Electrical or optical.|
||Technology|CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.<br>DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.|
|||BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.|
||Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).|
||Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.|
||Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).|
||Protocols|Protocols within supported bit rate range.|
||Nominal wavelength|Typical wavelength(s) from transmitter.|
||Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.|
||Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.|
||Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.|
|||Max operating case temperature range.|
||Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)|
|||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)|
||Power consumption|Worst case power consumption. Will vary over temperature.|
||Transmitter Output power|Average output power. Provided in min and max values.|
||Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.|
||Receiver max input power|Maximum average input power giving a BER, normally 1E-12.|
||DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.|



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

