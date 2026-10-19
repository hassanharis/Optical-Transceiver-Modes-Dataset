DATASHEET 

R6.1 

## **TD8006-TUNC-SO** 

QSFP-DD800 800G OpenROADM PCS Coh Tunable Flexgrid CMIS5.3 LC 

## OVERVIEW 

The TD8006-TUNC-SO is an QSFP-DD form-factor (type 2a) DWDM transceiver conforming to the OpenROAM MSA, for 800Gbps Ethernet applications. The transceiver also supports 400-600Gbps rates with different modulation formats, with proprietary probabilistic constellation shaping (PCS) modulations, resulting in an optimized OSNR performance for the application needs with different channel widths. 

The transceiver provides a flexible solution for operators having routers that not yet have migrated to 800G services. The TD8006-TUNC-SO can as an example be used to combine up to 8x100G/4x200G/2x400G flows to a 800G signal to be transported over an optical network. 


**----- Start of picture text -----**<br>
8x100G 8x100G<br>800G 800G<br>**----- End of picture text -----**<br>




The table below lists the Host and NTWK modes supported by TD8006-TUNC-SO. 

|**Host framing**|**Network**<br>**Frame**|**Payload**|**Modulation**|<br>**Line Symbol**<br>**Baud Rate**|**Channel**<br>**spacing**|**Media**<br>**code1)**|**MSA format**|**NTWK Mode description**||
|---|---|---|---|---|---|---|---|---|---|
|800GAUI-8||||||||||
|400GAUI-4<br>200GAUI-2|FlexO-8(e)|800G|PCS-131|131.3GBd|150GHz|0xF7|FlexO-8e-MPCS131-NOS-E2)|800G PCS-131Gbd||
|100GAUI-1||||||||||
|800GAUI-8||||||||||
|400GAUI-4<br>200GAUI-2|FlexO-8(e)|800G|PCS-131|131.3GBd|150GHz|0x68|FLEXO-8e-DPO-16QAM /<br>FOICe8.8-DPO|OpenROADM 800G 131Gbd||
|100GAUI-1||||||||||
|FOIC1.1|FlexO-8|800G|PCS-131|131.4GBd|150GHz|0xF8|FlexO-8-MPCS131-NOS-E2)|800G PCS-131Gbd (OTN)||
|200GAUI-2<br>100GAUI-1|FlexO-6(e)|600G|PCS-131|131.2GBd|150GHz|0xF5|FlexO-6e-MPCS131-NOS-E2)|600G-PCS-131Gbd||
|FOIC1.1|FlexO-6|600G|PCS-131|131.0GBd|150GHz|0xF6|FlexO-6-MPCS131-NOS-E2)|600G PCS-131 (OTN)||
|400GAUI-4/8||||||||||
|200GAUI-2/4|FlexO-4(e)|400G|PCS-131|131.3GBd|150GHz|0xEC|FlexO-4e-MPCS131-NOS2)|400G PCS-131Gbd||
|100GAUI-1/2||||||||||
|400GAUI-4/8||||||||||
|200GAUI-2/4|FlexO-4(e)|400G|PCS-66|65.7GBd|75GHz|0xC0|FlexO-4e-MPCS066-OS2)|400G PCS-66Gbd||
|100GAUI-1/2||||||||||
|400GAUI-4/8||||||||||
|200GAUI-2/4|FlexO-4(e)|400G|PCS-75|75.0GBd|87.5GHz|0xC2|FlexO-4e-MPCS075-OS2)|400G PCS-75Gbd||
|100GAUI-1/2||||||||||
|400GAUI-4/8||||||||||
|200GAUI-2/4|FlexO-4(e)|400G|PCS-87|87.4GBd|100GHz|0xC9|FlexO-4e-MPCS087-OS2)|400G PCS-87Gbd||
|100GAUI-1/2||||||||||
|400GAUI-4/8||||||||||
|200GAUI-2/4|FlexO-4(e)|400G|PCS-98|97.9GBd|112.5GHz|<br>0xD8|FlexO-4e-MPCS098-OS2)|400G PCS-98Gbd||
|100GAUI-1/2||||||||||
|400GAUI-4/8||||||||||
|200GAUI-2/4|FlexO-4(e)|400G|PCS-108|108.5GBd|125GHz|0xE5|FlexO-4e-MPCS108-OS2)|400G PCS-108Gbd||
|100GAUI-1/2||||||||||
|FOIC1.1/1.2|FlexO-4|400G|PCS-132|131.7GBd|150GHz|0xED|FlexO-4-MPCS132-OS2)|400G PCS-132Gbd (OTN)||
|FOIC1.1/1.2|FlexO-4|400G|PCS-79|78.9GBd|87.5GHz|0xC4|FlexO-4-MPCS079-OS2)|400G PCS-79Gbd (OTN)||
|FOIC1.1/1.2|FlexO-4|400G|PCS-69|69.1GBd|75GHz|0xC1|FlexO-4-MPCS069-OS2)|400G PCS-69Gbd (OTN)||
|FOIC1.1/1.2|FlexO-4|400G|PCS-87|87.3GBd|100GHz|0xCA|FlexO-4-MPCS087-OS2)|400G PCS-87Gbd (OTN)||
|FOIC1.1/1.2|FlexO-4|400G|PCS-98|98.6GBd|112.5GHz|<br>0xD9|FlexO-4-MPCS098-OS2)|400G PCS-98Gbd (OTN)||
|FOIC1.1/1.2|FlexO-4|400G|PCS-111|111.3GBd|125GHz|0xE9|FlexO-4-MPCS111-OS2)|400G PCS-108Gbd (OTN)||



- 1) The media code is defined through the reference code tables listed in SFF-8024. 

2) Non-MSA compliant code. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.1 

TD8006-TUNC-SO will automatically configure the above via the Host and NTWK modes. For 800G applications, the TD8006TUNC-SO asynchronously (GMP) maps an Ethernet or OTN signal from a switch/router to an intermediate FlexO frame structure, then adapts the frame structure to the selected FEC engine. The encoded signal is subsequently DSP framed and modulated for transmission as a coherent Dual Polarity signal. 

## TECHNICAL DATA 

The optical characteristics are into Generic and Application code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _NTWK/Media_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|GENERIC||||
|---|---|---|---|
|**Parameter**|**Value**<br>DWDM QSFP-DD800 type 2a<br>SM (2x LC)<br>191.25 - 196.1THz (tunable) 6.25GHz Grid<br>400-800G OpenROADM<br>+15OC to +75OC1)<br>-40OC to +85OC<br>Total received power<br>Coherent channel power<br>OSNR, eSNR, PDL, dispersion, DGD<br>Case temperature|**Parameter**|**Value**|
|Technology||MSA|OSFP800 MSA’s, CMIS5.3|
|Transmission media||Misc|Sync-E support, LLDP, RMON|
|Nominal wavelengths||Power consumption, EOL|See Section below.|
|Interface standards||Tx Power|Min 1dBm2)|
|Operating temperature||Tx In-band OSNR|37dB|
|Storage temperature||Tx Out-Of-Band OSNR|36dB|
|DDM functions||Receiver turn-up|Max 30ms from warm start|
||||Max 125s from cold start|
|||Absolute max conditions|Rx signal input power: +1dBm|
||||Rx total input power: +15dBm|



- 1) The module will turn up from cold start at ambient temperature as low as 

- -5C and will reach specifications after self-heating up to min temperature. 

- 2) The module transmit power can be provisioned up to the maximum available TX power. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power. The provisional Tx power range of the module is 10dB. 

**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.1 

## OPTICAL SPECIFICATION – NTWK/MEDIA CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Media**<br>**code**|**Line**<br>**rate**|**Network**<br>**frame**|**Modulation**|<br>**Tx**<br>**Power1**<br>**)**|**Rx sens**<br>**@ OSNR >**<br>**36dB**|**Rx @ OSNR2)**|**Rx OSNR**<br>**@1dB penalty2)**|**Default**<br>**CDC range**<br>**[ps/nm]**|**Maximum**<br>**CDC search**<br>**range**|
|---|---|---|---|---|---|---|---|---|---|
|0xF7|800G|<br>FlexO-8(e)|PCS-131|1dBm|-20.5dBm|24.7dB@ -9dBm|25.7dB@ -13dBm|24 000|47 000|
|0x68|800G|<br>FlexO-8(e)|PCS-131|1dBm|-20.5dBm|25.4dB@ -9dBm|26.4dB@ -13dBm|24 000|47 000|
|0xF8|800G|<br>FlexO-8|PCS-131|1dBm|-20.0dBm|26.4dB@ -14dBm|27.4dB@ -18dBm|24 000|47 000|
|0xF5|600G|<br>FlexO-6(e)|PCS-131|1dBm|-24.0dBm|21.3dB@ -9dBm|22.3dB@ -14dBm|24 000|47 000|
|0xF6|600G|<br>FlexO-6|PCS-131|1dBm|-23.5dBm|22.0dB@ -14dBm|23.0dB@ -19dBm|24 000|47 000|
|0xEC|400G|<br>FlexO-4(e)|PCS-131|1dBm|-27.0dBm|18.0dB@ -12dBm|19.0dB@ -18dBm|24 000|47 000|
|0xC0|400G|<br>FlexO-4(e)|PCS-66|1dBm|-24.5dBm|21.2dB@ -12dBm|22.2dB@ -18dBm|75 000|150 000|
|0xC2|400G|<br>FlexO-4(e)|PCS-75|1dBm|-24.0dBm|20.6dB@ -12dBm|21.6dB@ -18dBm|66 000|125 000|
|0xC9|400G|<br>FlexO-4(e)|PCS-87|1dBm|-26.0dBm|19.5dB@ -12dBm|20.5dB@ -18dBm|47 000|94 000|
|0xD8|400G|<br>FlexO-4|PCS-98|1dBm|-26.5dBm|19.2dB@ -12dBm|20.2dB@ -18dBm|42 000|84 000|
|0xE5|400G|<br>FlexO-4(e)|PCS-108|1dBm|-26.5dBm|18.7dB@ -12dBm|19.7dB@ -18dBm|29 000|57 000|
|0xED|400G|<br>FlexO-4|PCS-132|1dBm|-26.5dBm|18.5dB@ -14dBm|19.5dB@ -20dBm|24 000|47 000|
|0xC4|400G|<br>FlexO-4|PCS-79|1dBm|-25.0dBm|20.5dB@ -14dBm|21.5dB@ -20dBm|63 000|125 000|
|0xC1|400G|<br>FlexO-4|PCS-69|1dBm|-24.0dBm|21.5dB@ -14dBm|22.5dB@ -20dBm|72 000|125 000|
|0xCA|400G|<br>FlexO-4|PCS-87|1dBm|-25.5dBm|20.1dB@ -14dBm|21.1dB@ -20dBm|47 000|94 000|
|0xD9|400G|<br>FlexO-4|PCS-98|1dBm|-26.0dBm|19.7dB@ -14dBm|20.7dB@ -20dBm|42 000|84 000|
|0xE9|400G|<br>FlexO-4|PCS-111|1dBm|-26.5dBm|19.1dB@ -14dBm|20.1dB@ -20dBm|28 000|56 000|



1) Minimum Tx power without attenuation. The module Tx power can be attenuated with 10dB from the maximum available Tx power. If the Tx power is not provisioned by the host, the module Tx power will default to the maximum available power. 

2) Specified as [Min OSNR Value @ Min Rx power for the OSNR value]. 

3) maximum provisionable CD search range. Increasing the search range will increase the power consumption of the transceiver. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.1 

## ELECTICAL CHARACTERISTICS 

The table below lists the worst-case power consumption for each media code, under the default CD range and Muxponder mode. The power consumption will also increase based on the host interface. 

|**Media**<br>**code**|**Line**<br>**rate**|**Network**<br>**frame**|**Modulation**|<br>**Worst case power**<br>**consumption**|
|---|---|---|---|---|
|0xF7|800G|<br>FlexO-8(e)|PCS-131|30.0W|
|0x68|800G|<br>FlexO-8(e)|PCS-131|30.0W|
|0xF8|800G|<br>FlexO-8|PCS-131|30.0W|
|0xF5|600G|<br>FlexO-6(e)|PCS-131|29.5W|
|0xF6|600G|<br>FlexO-6|PCS-131|29.5W|
|0xEC|400G|<br>FlexO-4(e)|PCS-131|28.5W|
|0xC0|400G|<br>FlexO-4(e)|PCS-66|26.0W|
|0xC2|400G|<br>FlexO-4(e)|PCS-75|26.5W|
|0xC9|400G|<br>FlexO-4(e)|PCS-87|27.5W|
|0xD8|400G|<br>FlexO-4|PCS-98|28.0W|
|0xE5|400G|<br>FlexO-4(e)|PCS-108|28.5W|
|0xED|400G|<br>FlexO-4|PCS-132|29.5W|
|0xC4|400G|<br>FlexO-4|PCS-79|26.5W|
|0xC1|400G|<br>FlexO-4|PCS-69|26.5W|
|0xCA|400G|<br>FlexO-4|PCS-87|27.5W|
|0xD9|400G|<br>FlexO-4|PCS-98|28.0W|
|0xE9|400G|<br>FlexO-4|PCS-111|28.5W|



1) The power consumption figures are listed with the transceiver multiplexing the host streams. If the transceiver is running a 800GBASE-R stream, the transceiver shall remove the power consumption according to the numbers listed in the table.. 

2) The power consumption figures are listed with the default chromatic dispersion compensation range. For maximum dispersion compensation, the transceiver shall add the power consumption figures according to the numbers listed in the table. 

## ORDERING INFORMATION 

|**Ordering code**|**Item Name**|
|---|---|
|TQD006-TUNC-SO|QSFP-DD800 800G OpenROADM PCS CMIS5.3|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.1 

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

