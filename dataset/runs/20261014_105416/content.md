DATASHEET 

R5.2 

## **TQD029-TUNC-SO** 

QSFP-DD 400G Ultra Long Haul Coh Tunable Flexgrid CMIS5.3 LC 

## OVERVIEW 

The TQD029-TUNC-SO is an QSFP-DD form-factor (type 2a) DWDM transceiver conforming to the OpenZR+ and OpenROADM MSA for 400Gbps Ethernet applications. The transceiver has the option to transport 400Gbps with a DP-QPSK modulated signal, resulting in a better OSNR performance compared to DP-16QAM modulated signals. The transceiver also has options to modulate the signal with a proprietary probabilistic constellation shaping (PCS). 

While the 400G DP-QSPSK signal results in a better optical performance it also increases the optical bandwidth (FWHM) to 113GHz making it compatible with 150GHz spaced filters. 

The OpenZR+ MSA provides a flexible solution for operators having routers that not yet have migrated to 400G services. The TQD029-TUNC-SO can as an example be used in the Smartoptics DCP-404 Muxponder to combine up to 4x100G/2x200G/1x400G flows to a 400G OpenZR+ signal to be transported over an optical network. 


The below table lists the Host and NTWK modes supported by TQD029-TUNC-SO. 

||**Host framing**|**Network**<br>**Frame**|**Payload**|**Modulation**|**Line Symbol**<br>**Baud Rate**|**Channel**<br>**spacing**|**Media**<br>**code1)**|**MSA format**|**NTWK Mode description**||
|---|---|---|---|---|---|---|---|---|---|---|
||1x 400GAUI-8||||||||||
||2x 200GAUI-4|<br>FlexO-4(e)|400G|DP-QPSK|118.2GBd|150GHz|0x64|FLEXO-4e-DO-QPSK|OpenROADM 400G QPSK||
||4x 100GAUI-2||||||||||
||1x 400GAUI-8||||||||||
||2x 200GAUI-4|<br>FlexO-4(e)|400G|PCS-66|65.7GBd|75GHz|0xC0|FlexO-4e-MPCS066-OS2)|400G PCS-66||
||4x 100GAUI-2||||||||||
||1x 400GAUI-8||||||||||
||2x 200GAUI-4|<br>FlexO-4(e)|400G|PCS-75|75.0GBd|87.5GHz|0xC2|FlexO-4e-MPCS075-OS2)|400G PCS-75||
||4x 100GAUI-2||||||||||
||1x 400GAUI-8||||||||||
||2x 200GAUI-4|<br>FlexO-4(e)|400G|PCS-87|87.4GBd|100GHz|0xC9|FlexO-4e-MPCS087-OS2)|400G PCS-87||
||4x 100GAUI-2||||||||||
||1x 400GAUI-8||||||||||
||2x 200GAUI-4|<br>FlexO-4(e)|400G|PCS-98|97.9GBd|112.5GHz|<br>0xD8|FlexO-4e-MPCS098-OS2)|400G PCS-98||
||4x 100GAUI-2||||||||||
||4xFOIC1.2|FlexO-4|400G|PCS-101|100.8GBd|125GHz|0xDC|FlexO-4-MPCS101-OS2)|400G PCS-101 (OTN)||
||4xFOIC1.2|FlexO-4|400G|PCS-79|78.9GBd|87.5GHz|0xC4|FlexO-4-MPCS079-OS2)|400G PCS-79 (OTN)||
||4xFOIC1.2|FlexO-4|400G|PCS-69|69.1GBd|75GHz|0xC1|FlexO-4-MPCS069-OS2)|400G PCS-69 (OTN)||
||4xFOIC1.2|FlexO-4|400G|PCS-87|87.3GBd|100GHz|0xCA|FlexO-4-MPCS087-OS2)|400G PCS-87 (OTN)||
||1x 400GAUI-8<br>2x 200GAUI-4<br>4x 100GAUI-2|<br> <br> <br>OpenZR400|<br>400G|DP-16QAM|60.1GBd|75GHz|0xC6|OpenZR+, MSA, Enhanced|OpenZR+ 400G 16QAM<br>(Enhanced mode)||
||1x 400GAUI-8||||||||||
||2x 200GAUI-4|<br>OpenZR400|<br>400G|DP-16QAM|60.1GBd|75GHz|0x46|ZR400-OFEC-16QAM|OpenZR+ 400G 16QAM||
||4x 100GAUI-2||||||||||
||1x 400GAUI-8||||||||||
||2x 200GAUI-4|<br>OpenZR400|<br>400G|DP-16QAM|60.1GBd|75GHz|0x36|ZR400-OFEC-16QAM-HB|OpenZR+ 400G 16QAM-HB||
||4x 100GAUI-2||||||||||
||1) The media code|is defined through|the reference code tables listed in SFF-8024.||||||||



- 2) Non-MSA compliant code. 

TQD029-TUNC-SO will automatically configure the above via the Host and NTWK modes. For 400G applications, the TQD029TUNC-SO asynchronously (GMP) maps an Ethernet signal from a switch/router to an intermediate 400ZR/FlexO frame structure, then adapts the frame structure to the selected FEC engine. The encoded signal is subsequently DSP framed and modulated for transmission as a coherent Dual Polarity signal. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R5.2 

## TECHNICAL DATA 

The optical characteristics are into Generic and Application code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _NTWK/Media_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|**Parameter**|**Value**|
|---|---|
|Technology|DWDM QSFP-DD type 2a|
|Transmission media|SM (2x LC)|
|Nominal wavelengths|191.25 - 196.1THz (tunable) 6.25GHz Grid|
|Interface standards|400G OpenZR+/OpenROADM|
|Operating temperature|+15OC to +75OC1)|
|Storage temperature|-40OC to +85OC|
|DDM functions|Total received power|
||Coherent channel power|
||OSNR, eSNR, PDL, dispersion, DGD|
||Case temperature|



|**Parameter**|**Value**|
|---|---|
|MSA|QSFP-DD MSA’s, CMIS5.3|
|Misc|Sync-E support, LLDP, RMON|
|Power consumption, EOL|See Section below.|
|Tx Power|Min 1dBm2)|
|Tx In-band OSNR|37dB|
|Tx Out-Of-Band OSNR|TBD|
|Receiver turn-up|Max 30ms from warm start|
||Max 125s from cold start|
|Absolute max conditions|Rx signal input power: +1dBm|
||Rx total input power: 15dBm|



- 1) The module will turn up from cold start at ambient temperature as low as 

- -5C and will reach specifications after self-heating up to min temperature. 

2) The module transmit power can be provisioned up to the maximum available TX power. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power. The provisional Tx power range of the module is 10dB. 

**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R5.2 

## OPTICAL SPECIFICATION – NTWK/MEDIA CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Media**<br>**code**|**Line**<br>**rate**|**Network**<br>**frame**|**Modulation**|<br>**Tx**<br>**Power1**<br>**)**|**Rx sens**<br>**@ OSNR >**<br>**36dB**|**Rx @ OSNR2)**|**Rx OSNR**<br>**@~1dB penalty2)**|**Default**<br>**CDC range**<br>**[ps/nm]**|**Maximum**<br>**CDC search**<br>**range**|
|---|---|---|---|---|---|---|---|---|---|
|0x64|400G|<br>FlexO-4(e)|DP-QPSK|1dBm|-27.0dBm|17.9dB@ -12dBm|18.7dB@ -18dBm|58 000|58 000|
|0xC0|400G|<br>FlexO-4(e)|PCS-66|1dBm|-24.5dBm|21.2dB@ -12dBm|22.0dB@ -18dBm|42 000|150 000|
|0xC2|400G|<br>FlexO-4(e)|PCS-75|1dBm|-25.5dBm|20.6dB@ -12dBm|21.4dB@ -18dBm|37 000|125 000|
|0xC9|400G|<br>FlexO-4(e)|PCS-87|1dBm|-25.5dBm|19.5dB@ -12dBm|20.3dB@ -18dBm|52 000|100 000|
|0xD8|400G|<br>FlexO-4(e)|PCS-98|1dBm|-26.0dBm|19.2dB@ -12dBm|20.0dB@ -18dBm|35 000|70 000|
|0xDC|400G|<br>FlexO-4|PCS-101|1dBm|-26.0dBm|19.7dB@ -14dBm|20.4dB@ -20dBm|34 000|68 000|
|0xC4|400G|<br>FlexO-4|PCS-79|1dBm|-25.0dBm|20.5dB@ -14dBm|21.2dB@ -20dBm|58 000|100 000|
|0xC1|400G|<br>FlexO-4|PCS-69|1dBm|-24.0dBm|21.5dB@ -14dBm|22.2dB@ -20dBm|80 000|150 000|
|0xCA|400G|<br>FlexO-4|PCS-87|1dBm|-25.5dBm|20.1dB@ -14dBm|20.8dB@ -20dBm|52 000|100 000|
|0xC6|400G|<br>OpenZR400|<br>DP-16QAM|1dBm|-22.5dBm|22.9dB@ -12dBm|23.6dB@ -18dBm|23 000|175 000|
|0x46|400G|<br>OpenZR400|<br>DP-16QAM|1dBm|-22.5dBm|23.1dB@ -12dBm|23.8dB@ -18dBm|23 000|175 000|
|0x36|400G|<br>OpenZR400|<br>DP-16QAM|1dBm|-22.5dBm|23.1dB@ -12dBm|23.8dB@ -18dBm|23 000|175 000|



1) Minimum Tx power without attenuation. The module Tx power can be attenuated with 10dB from the maximum available Tx power. If the Tx power is not provisioned by the host, the module Tx power will default to the maximum available power. 

- 2) Specified as [Min OSNR Value @ Min Rx power for the OSNR value]. 

- 3) maximum provisionable CD search range. Increasing the search range will increase the power consumption of the transceiver. 

## ELECTICAL CHARACTERISTICS 

The table below lists the worst case power consumption for each media code. The power consumption will also increase based on the host interface 

|**Media**<br>**code**|**Line**<br>**rate**|**Network**<br>**frame**|**Modulation**|<br>**Worst case power**<br>**consumption**|<br>**If non-Muxponder**<br>**mode1)**|<br>**Additional Max**<br>**CD range2)**|
|---|---|---|---|---|---|---|
|0x64|400G|<br>FlexO-4(e)|DP-QPSK|24.0W|TBD|TBD|
|0xC0|400G|<br>FlexO-4(e)|PCS-66|23.5W|TBD|TBD|
|0xC2|400G|<br>FlexO-4(e)|PCS-75|24.0W|TBD|TBD|
|0xC9|400G|<br>FlexO-4(e)|PCS-87|24.0W|TBD|TBD|
|0xD8|400G|<br>FlexO-4(e)|PCS-98|25.0W|TBD|TBD|
|0xDC|400G|<br>FlexO-4|PCS-101|24.5W|TBD|TBD|
|0xC4|400G|<br>FlexO-4|PCS-79|24.0W|TBD|TBD|
|0xC1|400G|<br>FlexO-4|PCS-69|23.5W|TBD|TBD|
|0xCA|400G|<br>FlexO-4|PCS-87|24.5W|TBD|TBD|
|0xC6|400G|<br>OpenZR400|<br>DP-16QAM|22.5W|TBD|TBD|
|0x46|400G|<br>OpenZR400|<br>DP-16QAM|22.5W|TBD|TBD|
|0x36|400G|<br>OpenZR400|<br>DP-16QAM|22.5W|TBD|TBD|



- 1) The power consumption figures are listed with the transceiver multiplexing the host streams. If the transceiver is running a 400GBASE-R stream, the transceiver shall remove the power consumption according to the numbers listed in the table.. 

- 2) The power consumption figures are listed with the default chromatic dispersion compensation range. For maximum dispersion compensation, the transceiver shall add the power consumption figures according to the numbers listed in the table. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R5.2 

## APPLICATION SELECT TABLE - NORMALIZED APPLICATION DESCRIPTORS 

|**NAD**|**App**<br>**code**|**Host code**|**Host MSA code**|**Media code**|<br>**Media MSA description**|
|---|---|---|---|---|---|
|NAD_1:Bank_0|1|0x11|400GAUI-8 C2M (Annex 120E)|0x64|FLEXO-4e-DO-QPSK|
|NAD_2:Bank_0|2|0x0F|200GAUI-4 C2M (Annex 120E)|0x64|FLEXO-4e-DO-QPSK|
|NAD_3: Bank_0|3|0x0D|100GAUI-2 C2M (Annex 135G)|0x64|FLEXO-4e-DO-QPSK|
|NAD_4:Bank_0|4|0x11|400GAUI-8 C2M (Annex 120E)|0xC0|FlexO-4e-MPCS066-OS|
|NAD_5:Bank_0|5|0x0F|200GAUI-4 C2M (Annex 120E)|0xC0|FlexO-4e-MPCS066-OS|
|NAD_6:Bank_0|6|0x0D|100GAUI-2 C2M (Annex 135G)|0xC0|FlexO-4e-MPCS066-OS|
|NAD_7:Bank_0|7|0x11|400GAUI-8 C2M (Annex 120E)|0xC2|FlexO-4e-MPCS075-OS|
|NAD_8:Bank_0|8|0x0F|200GAUI-4 C2M (Annex 120E)|0xC2|FlexO-4e-MPCS075-OS|
|NAD_9:Bank_0|9|0x0D|100GAUI-2 C2M (Annex 135G)|0xC2|FlexO-4e-MPCS075-OS|
|NAD_10:Bank_0|10|0x11|400GAUI-8 C2M (Annex 120E)|0xC9|FlexO-4e-MPCS087-OS|
|NAD_11:Bank_0|11|0x0F|200GAUI-4 C2M (Annex 120E)|0xC9|FlexO-4e-MPCS087-OS|
|NAD_12:Bank_0|12|0x0D|100GAUI-2 C2M (Annex 135G)|0xC9|FlexO-4e-MPCS087-OS|
|NAD_13:Bank_0|13|0x11|400GAUI-8 C2M (Annex 120E)|0xD8|FlexO-4e-MPCS098-OS|
|NAD_14:Bank_0|14|0x0F|200GAUI-4 C2M (Annex 120E)|0xD8|FlexO-4e-MPCS098-OS|
|NAD_15:Bank_0|15|0x0D|100GAUI-2 C2M (Annex 135G)|0xD8|FlexO-4e-MPCS098-OS|
|NAD_1:Bank_1|16|0x11|400GAUI-8 C2M (Annex 120E)|0xC6|OpenZR+, MSA, Enhanced|
|NAD_2:Bank_1|17|0x0F|200GAUI-4 C2M (Annex 120E)|0xC6|OpenZR+, MSA, Enhanced|
|NAD_3: Bank_1|18|0x0D|100GAUI-2 C2M (Annex 135G)|0xC6|OpenZR+, MSA, Enhanced|
|NAD_4:Bank_1|19|0x11|400GAUI-8 C2M (Annex 120E)|0x46|ZR400-OFEC-16QAM|
|NAD_5:Bank_1|20|0x0F|200GAUI-4 C2M (Annex 120E)|0x46|ZR400-OFEC-16QAM|
|NAD_6:Bank_1|21|0x0D|100GAUI-2 C2M (Annex 135G)|0x46|ZR400-OFEC-16QAM|
|NAD_7:Bank_1|22|0x11|400GAUI-8 C2M (Annex 120E)|0x36|ZR400-OFEC-16QAM-HB|
|NAD_8:Bank_1|23|0x0F|200GAUI-4 C2M (Annex 120E)|0x36|ZR400-OFEC-16QAM-HB|
|NAD_9:Bank_1|24|0x0D|100GAUI-2 C2M (Annex 135G)|0x36|ZR400-OFEC-16QAM-HB|
|NAD_10:Bank_1|25|0x3C|FOIC1.2-MFI (ITU-T G.709.5/Y.1331 G.Sup58)|0xDC|FlexO-4-MPCS101-OS|
|NAD_11:Bank_1|26|0x3C|FOIC1.2-MFI (ITU-T G.709.5/Y.1331 G.Sup58)|0xC4|FlexO-4-MPCS079-OS|
|NAD_12:Bank_1|27|0x3C|FOIC1.2-MFI (ITU-T G.709.5/Y.1331 G.Sup58)|0xC1|FlexO-4-MPCS069-OS|
|NAD_13:Bank_1|28|0x3C|FOIC1.2-MFI (ITU-T G.709.5/Y.1331 G.Sup58)|0xCA|FlexO-4-MPCS087-OS|



## ORDERING INFORMATION 

|**Ordering code**|**Item Name**|
|---|---|
|TQD029-TUNC-SO|QSFP-DD 400G ULH Coh-T SM C5.3|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R5.2 

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
||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

