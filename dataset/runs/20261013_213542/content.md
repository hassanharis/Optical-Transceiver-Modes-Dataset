DATASHEET 

R6.0 

## **TOC006-TUNC-SO** 

OSFP800 800G OpenROADM PCS Coh Tunable Flexgrid CMIS5.3 LC 

## OVERVIEW 

The TOC006-TUNC-SO is an OSFP800 form-factor DWDM transceiver conforming to the OpenROAM MSA, for 800Gbps Ethernet applications. The transceiver also supports 400-600Gbps rates with different modulation formats, with proprietary probabilistic constellation shaping (PCS) modulations, resulting in an optimized OSNR performance for the application needs with different channel widths. 

The transceiver provides a flexible solution for operators having routers that not yet have migrated to 800G services. The TOC006-TUNC-SO can as an example be used to combine up to 8x100G/4x200G/2x400G flows to a 800G signal to be transported over an optical network. 


**----- Start of picture text -----**<br>
8x100G 8x100G<br>800G 800G<br>**----- End of picture text -----**<br>




The below table lists the Host and NTWK modes supported by TOC005-TUNC-SO. 

||**Host framing**|**Network**<br>**Frame**|**Payload**|**Modulation**|<br>**Line Symbol**<br>**Baud Rate**|**Channel**<br>**spacing**|**Media**<br>**code1)**|**MSA format**|**NTWK Mode description**|
|---|---|---|---|---|---|---|---|---|---|
||800GAUI-8|||||||||
||400GAUI-4<br>200GAUI-2|FlexO-8(e)|800G|PCS-131|131.3GBd|150GHz|0xF7|FlexO-8e-MPCS131-NOS-E2)|800G PCS-131Gbd|
||100GAUI-1|||||||||
||800GAUI-8|||||||||
||400GAUI-4<br>200GAUI-2|FlexO-8(e)|800G|PCS-131|131.3GBd|150GHz|0x68|FLEXO-8e-DPO-16QAM /<br>FOICe8.8-DPO|OpenROADM 800G 131Gbd|
||100GAUI-1|||||||||
||200GAUI-2<br>100GAUI-1|FlexO-6(e)|600G|PCS-131|131.2GBd|150GHz|0xF5|FlexO-6e-MPCS131-NOS-E2)|600G-PCS-131Gbd|
||400GAUI-4/8|||||||||
||200GAUI-2/4|FlexO-4(e)|400G|PCS-131|131.3GBd|150GHz|0xEC|FlexO-4e-MPCS131-NOS2)|400G PCS-131Gbd|
||100GAUI-1/2|||||||||
||400GAUI-4/8|||||||||
||200GAUI-2/4|FlexO-4(e)|400G|PCS-66|65.7GBd|75GHz|0xC0|FlexO-4e-MPCS066-OS2)|400G PCS-66Gbd|
||100GAUI-1/2|||||||||
||400GAUI-4/8|||||||||
||200GAUI-2/4|FlexO-4(e)|400G|PCS-75|75.0GBd|87.5GHz|0xC2|FlexO-4e-MPCS075-OS2)|400G PCS-75Gbd|
||100GAUI-1/2|||||||||
||400GAUI-4/8|||||||||
||200GAUI-2/4|FlexO-4(e)|400G|PCS-87|87.4GBd|100GHz|0xC9|FlexO-4e-MPCS087-OS2)|400G PCS-87Gbd|
||100GAUI-1/2|||||||||
||400GAUI-4/8|||||||||
||200GAUI-2/4|FlexO-4(e)|400G|PCS-108|108.5GBd|125GHz|0xE5|FlexO-4e-MPCS108-OS2)|400G PCS-108Gbd|
||100GAUI-1/2|||||||||



- 1) The media code is defined through the reference code tables listed in SFF-8024. 

- 2) Non-MSA compliant code. 

TOC006-TUNC-SO will automatically configure the above via the Host and NTWK modes. For 800G applications, the TOC006TUNC-SO asynchronously (GMP) maps an Ethernet signal from a switch/router to an intermediate FlexO frame structure, then adapts the frame structure to the selected FEC engine. The encoded signal is subsequently DSP framed and modulated for transmission as a coherent Dual Polarity signal. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.0 

## TECHNICAL DATA 

The optical characteristics are into Generic and Application code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _NTWK/Media_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|**Parameter**|**Value**|
|---|---|
|Technology|DWDM OSFP800 type 2a|
|Transmission media|SM (2x LC)|
|Nominal wavelengths|191.25 - 196.1THz (tunable) 6.25GHz Grid|
|Interface standards|400-800G OpenROADM|
|Operating temperature|+15OC to +75OC1)|
|Storage temperature|-40OC to +85OC|
|DDM functions|Total received power|
||Coherent channel power|
||OSNR, eSNR, PDL, dispersion, DGD|
||Case temperature|



|**Parameter**|**Value**|
|---|---|
|MSA|OSFP800 MSA’s, CMIS5.3|
|Misc|Sync-E support, LLDP, RMON|
|Power consumption, EOL|See Section below.|
|Tx Power|Min 1dBm2)|
|Tx In-band OSNR|37dB|
|Tx Out-Of-Band OSNR|36dB|
|Receiver turn-up|Max 30ms from warm start|
||Max 125s from cold start|
|Absolute max conditions|Rx signal input power: +1dBm|
||Rx total input power: +15dBm|



- 1) The module will turn up from cold start at ambient temperature as low as -5C and will reach specifications after self-heating up to min temperature. 

- 2) The module transmit power can be provisioned up to the maximum available TX power. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power. The provisional Tx power range of the module is 10dB. 

**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.0 

## OPTICAL SPECIFICATION – NTWK/MEDIA CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Media**<br>**code**|**Line**<br>**rate**|**Network**<br>**frame**|**Modulation**|<br>**Tx**<br>**Power1**<br>**)**|**Rx sens**<br>**@ OSNR >**<br>**36dB**|**Rx @ OSNR2)**|**Rx OSNR**<br>**@~1dB penalty2)**|**Default**<br>**CDC range**<br>**[ps/nm]**|**Maximum**<br>**CDC search**<br>**range**|
|---|---|---|---|---|---|---|---|---|---|
|0xF7|800G|<br>FlexO-8(e)|PCS-131|1dBm|-20.5dBm|24.7dB@ -9dBm|25.5dB@ -17dBm|24 000|47 000|
|0x68|800G|<br>FlexO-8(e)|PCS-131|1dBm|-20.5dBm|25.4dB@ -9dBm|26.2dB@ -17dBm|24 000|47 000|
|0xF5|600G|<br>FlexO-6(e)|PCS-131|1dBm|-24.0dBm|21.3dB@ -9dBm|22.2dB@ -20dBm|24 000|47 000|
|0xEC|400G|<br>FlexO-4(e)|PCS-131|1dBm|-27.0dBm|18.0dB@ -12dBm|18.9dB@ -22dBm|24 000|47 000|
|0xC0|400G|<br>FlexO-4(e)|PCS-66|1dBm|-24.5dBm|21.2dB@ -12dBm|22.0dB@ -20dBm|75 000|150 000|
|0xC2|400G|<br>FlexO-4(e)|PCS-75|1dBm|-24.0dBm|20.6dB@ -12dBm|21.4dB@ -20dBm|66 000|125 000|
|0xC9|400G|<br>FlexO-4(e)|PCS-87|1dBm|-26.0dBm|19.5dB@ -12dBm|20.3dB@ -21dBm|47 000|94 000|
|0xE5|400G|<br>FlexO-4(e)|PCS-108|1dBm|-26.5dBm|18.7dB@ -12dBm|19.6dB@ -22dBm|29 000|57 000|



- 1) Minimum Tx power without attenuation. The module Tx power can be attenuated with 10dB from the maximum available Tx power. If the Tx power is not provisioned by the host, the module Tx power will default to the maximum available power. 

- 2) Specified as [Min OSNR Value @ Min Rx power for the OSNR value]. 

- 3) maximum provisionable CD search range. Increasing the search range will increase the power consumption of the transceiver. 

## ELECTICAL CHARACTERISTICS 

The table below lists the worst case power consumption for each media code. The power consumption will also increase based on the host interface 

|**Media**<br>**code**|**Line**<br>**rate**|**Network**<br>**frame**|**Modulation**|<br>**Worst case power**<br>**consumption**|
|---|---|---|---|---|
|0xF7|800G|<br>FlexO-8(e)|PCS-131|30.0W|
|0x68|800G|<br>FlexO-8(e)|PCS-131|30.0W|
|0xF5|600G|<br>FlexO-6(e)|PCS-131|29.0W|
|0xEC|400G|<br>FlexO-4(e)|PCS-131|28.5W|
|0xC0|400G|<br>FlexO-4(e)|PCS-66|25.0W|
|0xC2|400G|<br>FlexO-4(e)|PCS-75|25.5W|
|0xC9|400G|<br>FlexO-4(e)|PCS-87|26.5W|
|0xE5|400G|<br>FlexO-4(e)|PCS-108|27.0W|



1) The power consumption figures are listed with the transceiver multiplexing the host streams. If the transceiver is running a 400GBASE-R stream, the transceiver shall remove the power consumption according to the numbers listed in the table.. 

- 2) The power consumption figures are listed with the default chromatic dispersion compensation range. For maximum dispersion compensation, the transceiver shall add the power consumption figures according to the numbers listed in the table. 

## ORDERING INFORMATION 

|**Ordering code**|**Item Name**|
|---|---|
|TOC006-TUNC-SO|OSFP800 800G OpenROADM PCS CMIS5.3|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.0 

## GENERAL DEFINITIONS 

||**Parameter**|**Description**||
|---|---|---|---|
|||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
||Technology|CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.<br>DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.||
|||BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
||Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
||Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
||Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
||Protocols|Protocols within supported bit rate range.||
||Nominal wavelength|Typical wavelength(s) from transmitter.||
||Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
||Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
||Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
|||Max operating case temperature range.||
||Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
|||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
||Power consumption|Worst case power consumption. Will vary over temperature.||
||Transmitter Output power|Average output power. Provided in min and max values.||
||Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
||Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
||DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

