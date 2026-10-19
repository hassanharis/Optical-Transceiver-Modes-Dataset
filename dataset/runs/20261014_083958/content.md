DATASHEET 

R6.2 

## **TD8010-TUNC-SO** 

QSFP-DD800 800G OpenROADM/OIF 800ZR Coh Tunable Flexgrid CMIS5.3 LC 

## OVERVIEW 

The TD8010-TUNC-SO is an QSFP-DD form-factor (type 2a) DWDM transceiver conforming to the OpenROAM and OIF 800ZR MSA, for 800Gbps Ethernet applications. The transceiver also supports 400-600Gbps rates with different modulation formats, with proprietary probabilistic constellation shaping (PCS) modulations, resulting in an optimized OSNR performance for the application needs with different channel widths. 

The transceiver provides a flexible solution for operators having routers that not yet have migrated to 800G services. The TD8010-TUNC-SO can as an example be used to combine up to 8x100G/4x200G/2x400G flows to a 800G signal to be transported over an optical network. 

|8x100G|8x100G||||8x100G|8x100G|||||
|---|---|---|---|---|---|---|---|---|---|---|
|||800G||800G|||||||
|The table below lists the||Host and NTWK modes supported by||||TD8010-TUNC-SO.|||||
||**Network**||||**Line**|**Channel**|**Media**||||
|**Host framing 3)**|**Frame**||**Payload**|**Modulation**|<br>**Symbol**|**spacing**|**code1)**|**MSA format**|**NTWK Mode description**||
||**Format**||||**Baud Rate**||||||
|800GAUI-8-S/L|||||||||||
|400GAUI-4-x<br>200GAUI-2-x|OIF 800ZR||800G|DP-16QAM|118.2GBd|150GHz|0x6C|ZR800-16QAM-OS-A|800ZR Power class A||
|100GAUI-1-x|||||||||||
|400GAUI-4-x|||||||||||
|200GAUI-2-x|FlexO-6(e)||600G|PCS-118|118.7GBd|150 GHz|0x6A|FlexO-6e-MPCS118-OS-OR|OpenROADM FlexO-6e-DPO||
|100GAUI-1-x|||||||||||
|400GAUI-4-x<br>200GAUI-2-x<br>100GAUI-1-x|FlexO-6(e)||600G|PCS-118|118.5GBd|150 GHz|0xF2|FlexO-6e-MPCS118-OS-E2)|OpenROADM FlexO-6e-DPO,<br>Enhanced||
|400GAUI-8|||||||||||
|200GAUI-4|||||||||||
|100GAUI-2<br>400GAUI-4-x|FlexO-4(e)||400G|PCS-118|118.2GBd|150GHz|0x64|FlexO-4e-QPSK-OS-OR|OpenROADM FlexO-4e-DO||
|200GAUI-2-x|||||||||||
|100GAUI-1-x|||||||||||
|400GAUI-8|||||||||||
|200GAUI-4|||||||||||
|100GAUI-2<br>400GAUI-4-x|400ZR+||400G|DP-16QAM|60.1GBd|75GHz|0x36|OpenZR400-16QAM-OS-HB|OpenZR+ ZR400-OFEC-<br>16QAMHB||
|200GAUI-2-x|||||||||||
|100GAUI-1-x|||||||||||
|800GAUI-8-x|||||||||||
|400GAUI-4-x<br>200GAUI-2-x|FlexO-8(e)||800G|PCS-131|131.3GBd|150GHz|0x68|FlexO-8e-MPCS131-OS-OR|OpenROADM FlexO-8e-DPO||
|100GAUI-1-x|||||||||||
|800GAUI-8-x|||||||||||
|400GAUI-4-x<br>200GAUI-2-x|FlexO-8(e)||800G|PCS-131|131.3GBd|150GHz|0xF7|FlexO-8e-MPCS131-OS-E2)|OpenROADM FlexO-8e-DPO,<br>Enhanced||
|100GAUI-1-x|||||||||||
|FOIC1.1-RS|FlexO-8||800G|PCS-131|131.4GBd|150GHz|0xF8|FlexO-8-MPCS131-OS-E2)|OpenROADM FlexO-8e-DPO,<br>Enhanced (OTN)||
|400GAUI-4-x|||||||||||
|200GAUI-2-x|FlexO-6(e)||600G|PCS-131|131.2GBd|150GHz|0xF5|FlexO-6e-MPCS131-OS-E2)|600G-PCS-131Gbd||
|100GAUI-1-x|||||||||||
|FOIC1.1-RS|FlexO-6||600G|PCS-131|131.0GBd|150GHz|0xF6|FlexO-6-MPCS131-OS-E2)|600G PCS-131 GBd (OTN)||
|400GAUI-8|||||||||||
|200GAUI-4|||||||||||
|100GAUI-2<br>400GAUI-4-x|FlexO-4(e)||400G|PCS-131|131.3GBd|150GHz|0xEC|FlexO-4e-MPCS131-OS2)|400G PCS-131Gbd||
|200GAUI-2-x|||||||||||
|100GAUI-1-x|||||||||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.2 

|400GAUI-8|||||||||
|---|---|---|---|---|---|---|---|---|
|200GAUI-4|||||||||
|100GAUI-2<br>400GAUI-4-x|FlexO-4(e)|400G|PCS-66|65.7GBd|75GHz|0xC0|FlexO-4e-MPCS066-OS2)|400G PCS-66Gbd|
|200GAUI-2-x|||||||||
|100GAUI-1-x|||||||||
|400GAUI-8|||||||||
|200GAUI-4|||||||||
|100GAUI-2<br>400GAUI-4-x|FlexO-4(e)|400G|PCS-75|75.0GBd|87.5GHz|0xC2|FlexO-4e-MPCS075-OS2)|400G PCS-75Gbd|
|200GAUI-2-x|||||||||
|100GAUI-1-x|||||||||
|400GAUI-8|||||||||
|200GAUI-4|||||||||
|100GAUI-2<br>400GAUI-4-x|FlexO-4(e)|400G|PCS-87|87.4GBd|100GHz|0xC9|FlexO-4e-MPCS087-OS2)|400G PCS-87Gbd|
|200GAUI-2-x|||||||||
|100GAUI-1-x|||||||||
|400GAUI-8|||||||||
|200GAUI-4|||||||||
|100GAUI-2<br>400GAUI-4-x|FlexO-4(e)|400G|PCS-98|97.9GBd|112.5GHz|0xD8|FlexO-4e-MPCS098-OS2)|400G PCS-98Gbd|
|200GAUI-2-x|||||||||
|100GAUI-1-x|||||||||
|400GAUI-8|||||||||
|200GAUI-4|||||||||
|100GAUI-2<br>400GAUI-4-x|FlexO-4(e)|400G|PCS-108|108.5GBd|125GHz|0xE5|FlexO-4e-MPCS108-OS2)|400G PCS-108Gbd|
|200GAUI-2-x|||||||||
|100GAUI-1-x|||||||||
|FOIC1.1-RS<br>FOIC1.2-MFI|FlexO-4|400G|PCS-132|131.7GBd|150GHz|0xED|FlexO-4-MPCS132-OS2)|400G PCS-132Gbd (OTN)|
|FOIC1.1-RS<br>FOIC1.2-MFI|FlexO-4|400G|PCS-79|78.9GBd|87.5GHz|0xC4|FlexO-4-MPCS079-OS2)|400G PCS-79Gbd (OTN)|
|FOIC1.1-RS<br>FOIC1.2-MFI|FlexO-4|400G|PCS-69|69.1GBd|75GHz|0xC1|FlexO-4-MPCS069-OS2)|400G PCS-69Gbd (OTN)|
|FOIC1.1-RS<br>FOIC1.2-MFI|FlexO-4|400G|PCS-87|87.3GBd|100GHz|0xCA|FlexO-4-MPCS087-OS2)|400G PCS-87Gbd (OTN)|
|FOIC1.1-RS<br>FOIC1.2-MFI|FlexO-4|400G|PCS-98|98.6GBd|112.5GHz|0xD9|FlexO-4-MPCS098-OS2)|400G PCS-98Gbd (OTN)|
|FOIC1.1-RS<br>FOIC1.2-MFI|FlexO-4|400G|PCS-111|111.3GBd|125GHz|0xE9|FlexO-4-MPCS111-OS2)|400G PCS-111Gbd (OTN)|



1) The media code is defined through the reference code tables listed in SFF-8024. 

2) Non-MSA compliant code. 

3) “-x” is defined S or / L 

TD8010-TUNC-SO will automatically configure the above via the Host and NTWK modes. For 800G applications, the TD8010TUNC-SO asynchronously (GMP) maps an Ethernet or OTN signal from a switch/router to an intermediate FlexO frame structure, then adapts the frame structure to the selected FEC engine. The encoded signal is subsequently DSP framed and modulated for transmission as a coherent Dual Polarity signal. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.2 

## TECHNICAL DATA 

The optical characteristics are into Generic and Application code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _NTWK/Media_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|**Parameter**|**Value**|
|---|---|
|Technology|DWDM QSFP-DD800 type 2a|
|Transmission media|SM (2x LC)|
|Nominal wavelengths|191.25 - 196.1THz (tunable) 6.25GHz Grid|
|Interface standards|400-800G OpenROADM & OIF 800ZR|
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
|Receiver Acquisition Time|Max 10s from warm start|
|Receiver turn-up, cold start|Max 200s from cold start|
|Absolute max conditions|Rx signal input power: +1dBm|
||Rx total input power: +15dBm|



- 1) The module will turn up from cold start at ambient temperature as low as -5C and will reach specifications after self-heating up to min temperature. 

2) The module transmit power can be provisioned up to the maximum available TX power. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power. The provisional Tx power range of the module is 10dB. 

**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.2 

## OPTICAL SPECIFICATION – NTWK/MEDIA CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Media**<br>**code**|**Line**<br>**rate**|**Network**<br>**frame**|**Modulation**|<br>**Tx**<br>**Power1**<br>**)**|**Rx sens**<br>**@ OSNR >**<br>**36dB**|**Rx @ OSNR2)**|**Rx OSNR**<br>**@1dB penalty2)**|**Default**<br>**CDC range**<br>**[ps/nm]**|**Maximum CDC**<br>**search range**<br>**[ps/nm]3)**|
|---|---|---|---|---|---|---|---|---|---|
|0x6C|800G|<br>OIF 800ZR|<br>DP-16QAM|1dBm|-18.5dBm|26.4dB@ -9dBm|27.4dB@ -13dBm|3 000|58 000|
|0x6A|600G|<br>FlexO-6(e)|PCS-118|1dBm|-23.5dBm|22.8dB@ -9dBm|23.8dB@ -14dBm|29 000|58 000|
|0xF2|600G|<br>FlexO-6(e)|PCS-118|1dBm|-23.5dBm|21.6dB@ -9dBm|22.6dB@ -14dBm|29 000|58 000|
|0x64|400G|<br>FlexO-4(e)|PCS-118|1dBm|-27.0dBm|17.9dB@ -12dBm|18.9dB@ -18dBm|58 000|58 000|
|0x36|400G|<br>400ZR+|DP-16QAM|1dBm|-22.5dBm|23.1dB@ -12dBm|24.1dB@ -18dBm|23 000|175 000|
|0x68|800G|<br>FlexO-8(e)|PCS-131|1dBm|-20.5dBm|25.0dB@ -9dBm|26.0dB@ -13dBm|24 000|47 000|
|0xF7|800G|<br>FlexO-8(e)|PCS-131|1dBm|-20.5dBm|24.7dB@ -9dBm|25.7dB@ -13dBm|24 000|47 000|
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

R6.2 

## ELECTICAL CHARACTERISTICS 

The table below lists the worst-case power consumption for each media code, under the default CD range and worst-case client mapping mode, operating at the FEC threshold. 

|**Media**<br>**code**|**Line**<br>**rate**|**Network**<br>**frame**|**Modulation**|<br>**Worst case power**<br>**consumption**|
|---|---|---|---|---|
|0x6C|800G|<br>OIF 800ZR|<br>DP-16QAM|28.0W|
|0x6A|600G|<br>FlexO-6(e)|PCS-118|28.0W|
|0xF2|600G|<br>FlexO-6(e)|PCS-118|28.0W|
|0x64|400G|<br>FlexO-4(e)|PCS-118|25.0W|
|0x36|400G|<br>400ZR+|DP-16QAM|23.5W|
|0x68|800G|<br>FlexO-8(e)|PCS-131|30.0W|
|0xF7|800G|<br>FlexO-8(e)|PCS-131|30.0W|
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




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.2 

## APPLICATION SELECT TABLE - NORMALIZED APPLICATION DESCRIPTORS 

|**NAD**|**App**<br>**code**|**Host**<br>**code**|**Host MSA code**|**Media**<br>**code**|<br>**Media MSA description**|
|---|---|---|---|---|---|
|NAD_1:Bank_0|1|0x51|800GAUI-8 S C2M (Annex 120G)|0x6C|800ZR Power class A|
|NAD_2:Bank_0|2|0x52|800GAUI-8 L C2M (Annex 120G)|0x6C|800ZR Power class A|
|NAD_3: Bank_0|3|0x4F|400GAUI-4-SC2M (Annex 120G)|0x6C|800ZR Power class A|
|NAD_4:Bank_0|4|0x50|400GAUI-4-LC2M (Annex 120G)|0x6C|800ZR Power class A|
|NAD_5:Bank_0|5|0x4D|200GAUI-2-SC2M (Annex 120G)|0x6C|800ZR Power class A|
|NAD_6:Bank_0|6|0x4E|200GAUI-2-LC2M (Annex 120G)|0x6C|800ZR Power class A|
|NAD_7:Bank_0|7|0x4B|100GAUI-1-SC2M (Annex 120G)|0x6C|800ZR Power class A|
|NAD_8:Bank_0|8|0x4C|100GAUI-1-LC2M (Annex 120G)|0x6C|800ZR Power class A|
|NAD_9:Bank_0|9|0x4F|400GAUI-4-SC2M (Annex 120G)|0x6A|OpenROADM FlexO-6e-DPO|
|NAD_10:Bank_0|<br>10|0x50|400GAUI-4-LC2M (Annex 120G)|0x6A|OpenROADM FlexO-6e-DPO|
|NAD_11:Bank_0|<br>11|0x4D|200GAUI-2-SC2M (Annex 120G)|0x6A|OpenROADM FlexO-6e-DPO|
|NAD_12:Bank_0|<br>12|0x4E|200GAUI-2-LC2M (Annex 120G)|0x6A|OpenROADM FlexO-6e-DPO|
|NAD_13:Bank_0|<br>13|0x4B|100GAUI-1-SC2M (Annex 120G)|0x6A|OpenROADM FlexO-6e-DPO|
|NAD_14:Bank_0|<br>14|0x4C|100GAUI-1-LC2M (Annex 120G)|0x6A|OpenROADM FlexO-6e-DPO|
|NAD_15:Bank_0|<br>15|0x4F|400GAUI-4-SC2M (Annex 120G)|0xF2|OpenROADM FlexO-6e-DPO, Enhanced|
|NAD_1:Bank_1|16|0x50|400GAUI-4-LC2M (Annex 120G)|0xF2|OpenROADM FlexO-6e-DPO, Enhanced|
|NAD_2:Bank_1|17|0x4D|200GAUI-2-SC2M (Annex 120G)|0xF2|OpenROADM FlexO-6e-DPO, Enhanced|
|NAD_3: Bank_1|18|0x4E|200GAUI-2-LC2M (Annex 120G)|0xF2|OpenROADM FlexO-6e-DPO, Enhanced|
|NAD_4:Bank_1|19|0x4B|100GAUI-1-SC2M (Annex 120G)|0xF2|OpenROADM FlexO-6e-DPO, Enhanced|
|NAD_5:Bank_1|20|0x4C|100GAUI-1-LC2M (Annex 120G)|0xF2|OpenROADM FlexO-6e-DPO, Enhanced|
|NAD_6:Bank_1|21|0x4F|400GAUI-4-SC2M (Annex 120G)|0x64|OpenROADM FlexO-4e-DO|
|NAD_7:Bank_1|22|0x50|400GAUI-4-LC2M (Annex 120G)|0x64|OpenROADM FlexO-4e-DO|
|NAD_8:Bank_1|23|0x4D|200GAUI-2-SC2M (Annex 120G)|0x64|OpenROADM FlexO-4e-DO|
|NAD_9:Bank_1|24|0x4E|200GAUI-2-LC2M (Annex 120G)|0x64|OpenROADM FlexO-4e-DO|
|NAD_10:Bank_1|<br>25|0x4B|100GAUI-1-SC2M (Annex 120G)|0x64|OpenROADM FlexO-4e-DO|
|NAD_11:Bank_1|<br>26|0x4C|100GAUI-1-LC2M (Annex 120G)|0x64|OpenROADM FlexO-4e-DO|
|NAD_12:Bank_1|<br>27|0x11|400GAUI-8 C2M (Annex 120E)|0x64|OpenROADM FlexO-4e-DO|
|NAD_13:Bank_1|<br>28|0xF|200GAUI-4 C2M (Annex 120E)|0x64|OpenROADM FlexO-4e-DO|
|NAD_14:Bank_1|<br>29|0xD|100GAUI-2 C2M (Annex 135G)|0x64|OpenROADM FlexO-4e-DO|
|NAD_15:Bank_1|<br>30|0x4E|200GAUI-2-LC2M (Annex 120G)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_1:Bank_2|31|0x4D|200GAUI-2-SC2M (Annex 120G)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_2:Bank_2|32|0x4C|100GAUI-1-LC2M (Annex 120G)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_3:Bank_2|33|0x4B|100GAUI-1-SC2M (Annex 120G)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_4:Bank_2|34|0xF|200GAUI-4 C2M (Annex 120E)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_5:Bank_2|35|0x11|400GAUI-8 C2M (Annex 120E)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_6:Bank_2|36|0xD|100GAUI-2 C2M (Annex 135G)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_7:Bank_2|37|0x4F|400GAUI-4-SC2M (Annex 120G)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_8:Bank_2|38|0x50|400GAUI-4-LC2M (Annex 120G)|0x36|OpenZR+ ZR400-OFEC-16QAMHB|
|NAD_9:Bank_2|39|0x51|800GAUI-8 S C2M (Annex 120G)|0x68|OpenROADM FlexO-8e-DPO|
|NAD_10:Bank_2|<br>40|0x52|800GAUI-8 L C2M (Annex 120G)|0x68|OpenROADM FlexO-8e-DPO|
|NAD_11:Bank_2|<br>41|0x4F|400GAUI-4-SC2M (Annex 120G)|0x68|OpenROADM FlexO-8e-DPO|
|NAD_12:Bank_2|<br>42|0x50|400GAUI-4-LC2M (Annex 120G)|0x68|OpenROADM FlexO-8e-DPO|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.2 

|NAD_13:Bank_2|43|0x4D|200GAUI-2-SC2M (Annex 120G)|0x68|OpenROADM FlexO-8e-DPO|
|---|---|---|---|---|---|
|NAD_14:Bank_2|44|0x4E|200GAUI-2-LC2M (Annex 120G)|0x68|OpenROADM FlexO-8e-DPO|
|NAD_15:Bank_2|45|0x4B|100GAUI-1-SC2M (Annex 120G)|0x68|OpenROADM FlexO-8e-DPO|
|NAD_1:Bank_3|46|0x4C|100GAUI-1-LC2M (Annex 120G)|0x68|OpenROADM FlexO-8e-DPO|
|NAD_2:Bank_3|47|0x51|800GAUI-8 S C2M (Annex 120G)|0xF7|OpenROADM FlexO-8e-DPO, Enhanced|
|NAD_3:Bank_3|48|0x52|800GAUI-8 L C2M (Annex 120G)|0xF7|OpenROADM FlexO-8e-DPO, Enhanced|
|NAD_4:Bank_3|49|0x4F|400GAUI-4-SC2M (Annex 120G)|0xF7|OpenROADM FlexO-8e-DPO, Enhanced|
|NAD_5:Bank_3|50|0x50|400GAUI-4-LC2M (Annex 120G)|0xF7|OpenROADM FlexO-8e-DPO, Enhanced|
|NAD_6:Bank_3|51|0x4D|200GAUI-2-SC2M (Annex 120G)|0xF7|OpenROADM FlexO-8e-DPO, Enhanced|
|NAD_7:Bank_3|52|0x4E|200GAUI-2-LC2M (Annex 120G)|0xF7|OpenROADM FlexO-8e-DPO, Enhanced|
|NAD_8:Bank_3|53|0x4B|100GAUI-1-SC2M (Annex 120G)|0xF7|OpenROADM FlexO-8e-DPO, Enhanced|
|NAD_9:Bank_3|54|0x4C|100GAUI-1-LC2M (Annex 120G)|0xF7|OpenROADM FlexO-8e-DPO, Enhanced|
|NAD_10:Bank_3|55|0x4F|400GAUI-4-SC2M (Annex 120G)|0xF5|600G-PCS-131Gbd|
|NAD_11:Bank_3|56|0x50|400GAUI-4-LC2M (Annex 120G)|0xF5|600G-PCS-131Gbd|
|NAD_12:Bank_3|57|0x4D|200GAUI-2-SC2M (Annex 120G)|0xF5|600G-PCS-131Gbd|
|NAD_13:Bank_3|58|0x4E|200GAUI-2-LC2M (Annex 120G)|0xF5|600G-PCS-131Gbd|
|NAD_14:Bank_3|59|0x4B|100GAUI-1-SC2M (Annex 120G)|0xF5|600G-PCS-131Gbd|
|NAD_15:Bank_3|60|0x4C|100GAUI-1-LC2M (Annex 120G)|0xF5|600G-PCS-131Gbd|
|NAD_1:Bank_4|61|0x4F|400GAUI-4-SC2M (Annex 120G)|0xEC|400G PCS-131Gbd|
|NAD_2:Bank_4|62|0x50|400GAUI-4-LC2M (Annex 120G)|0xEC|400G PCS-131Gbd|
|NAD_3:Bank_4|63|0x4D|200GAUI-2-SC2M (Annex 120G)|0xEC|400G PCS-131Gbd|
|NAD_4:Bank_4|64|0x4E|200GAUI-2-LC2M (Annex 120G)|0xEC|400G PCS-131Gbd|
|NAD_5:Bank_4|65|0x4B|100GAUI-1-SC2M (Annex 120G)|0xEC|400G PCS-131Gbd|
|NAD_6:Bank_4|66|0x4C|100GAUI-1-LC2M (Annex 120G)|0xEC|400G PCS-131Gbd|
|NAD_7:Bank_4|67|0x11|400GAUI-8 C2M (Annex 120E)|0xEC|400G PCS-131Gbd|
|NAD_8:Bank_4|68|0x50|400GAUI-4-LC2M (Annex 120G)|0xC0|400G PCS-66Gbd|
|NAD_9:Bank_4|69|0x50|400GAUI-4-LC2M (Annex 120G)|0xC2|400G PCS-75Gbd|
|NAD_10:Bank_4|70|0x50|400GAUI-4-LC2M (Annex 120G)|0xC9|400G PCS-87Gbd|
|NAD_11:Bank_4|71|0x50|400GAUI-4-LC2M (Annex 120G)|0xD8|400G PCS-98Gbd|
|NAD_12:Bank_4|72|0x50|400GAUI-4-LC2M (Annex 120G)|0xE5|400G PCS-108Gbd|
|NAD_13:Bank_4|73|0x4F|400GAUI-4-SC2M (Annex 120G)|0xC0|400G PCS-66Gbd|
|NAD_14:Bank_4|74|0x4F|400GAUI-4-SC2M (Annex 120G)|0xC2|400G PCS-75Gbd|
|NAD_15:Bank_4|75|0x4F|400GAUI-4-SC2M (Annex 120G)|0xC9|400G PCS-87Gbd|
|NAD_1:Bank_5|76|0x4F|400GAUI-4-SC2M (Annex 120G)|0xD8|400G PCS-98Gbd|
|NAD_2:Bank_5|77|0x4F|400GAUI-4-SC2M (Annex 120G)|0xE5|400G PCS-108Gbd|
|NAD_3:Bank_5|78|0x4E|200GAUI-2-LC2M (Annex 120G)|0xC0|400G PCS-66Gbd|
|NAD_4:Bank_5|79|0x4E|200GAUI-2-LC2M (Annex 120G)|0xC2|400G PCS-75Gbd|
|NAD_5:Bank_5|80|0x4E|200GAUI-2-LC2M (Annex 120G)|0xC9|400G PCS-87Gbd|
|NAD_6:Bank_5|81|0x4E|200GAUI-2-LC2M (Annex 120G)|0xD8|400G PCS-98Gbd|
|NAD_7:Bank_5|82|0x4E|200GAUI-2-LC2M (Annex 120G)|0xE5|400G PCS-108Gbd|
|NAD_8:Bank_5|83|0x4D|200GAUI-2-SC2M (Annex 120G)|0xC0|400G PCS-66Gbd|
|NAD_9:Bank_5|84|0x4D|200GAUI-2-SC2M (Annex 120G)|0xC2|400G PCS-75Gbd|
|NAD_10:Bank_5|85|0x4D|200GAUI-2-SC2M (Annex 120G)|0xC9|400G PCS-87Gbd|
|NAD_11:Bank_5|86|0x4D|200GAUI-2-SC2M (Annex 120G)|0xD8|400G PCS-98Gbd|
|NAD_12:Bank_5|87|0x4D|200GAUI-2-SC2M (Annex 120G)|0xE5|400G PCS-108Gbd|
|NAD_13:Bank_5|88|0x4C|100GAUI-1-LC2M (Annex 120G)|0xC0|400G PCS-66Gbd|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.2 

|NAD_14:Bank_5|89|0x4C|100GAUI-1-LC2M (Annex 120G)|0xC2|400G PCS-75Gbd|
|---|---|---|---|---|---|
|NAD_15:Bank_5|90|0x4C|100GAUI-1-LC2M (Annex 120G)|0xC9|400G PCS-87Gbd|
|NAD_1:Bank_6|91|0x4C|100GAUI-1-LC2M (Annex 120G)|0xD8|400G PCS-98Gbd|
|NAD_2:Bank_6|92|0x4C|100GAUI-1-LC2M (Annex 120G)|0xE5|400G PCS-108Gbd|
|NAD_3:Bank_6|93|0x4B|100GAUI-1-SC2M (Annex 120G)|0xC0|400G PCS-66Gbd|
|NAD_4:Bank_6|94|0x4B|100GAUI-1-SC2M (Annex 120G)|0xC2|400G PCS-75Gbd|
|NAD_5:Bank_6|95|0x4B|100GAUI-1-SC2M (Annex 120G)|0xC9|400G PCS-87Gbd|
|NAD_6:Bank_6|96|0x4B|100GAUI-1-SC2M (Annex 120G)|0xD8|400G PCS-98Gbd|
|NAD_7:Bank_6|97|0x4B|100GAUI-1-SC2M (Annex 120G)|0xE5|400G PCS-108Gbd|
|NAD_8:Bank_6|98|0x11|400GAUI-8 C2M (Annex 120E)|0xC0|400G PCS-66Gbd|
|NAD_9:Bank_6|99|0x11|400GAUI-8 C2M (Annex 120E)|0xC2|400G PCS-75Gbd|
|NAD_10:Bank_6|100|0x11|400GAUI-8 C2M (Annex 120E)|0xC9|400G PCS-87Gbd|
|NAD_11:Bank_6|101|0x11|400GAUI-8 C2M (Annex 120E)|0xD8|400G PCS-98Gbd|
|NAD_12:Bank_6|102|0xF|200GAUI-4 C2M (Annex 120E)|0xEC|400G PCS-108Gbd|
|NAD_13:Bank_6|103|0xF|200GAUI-4 C2M (Annex 120E)|0xC0|400G PCS-66Gbd|
|NAD_14:Bank_6|104|0xF|200GAUI-4 C2M (Annex 120E)|0xC2|400G PCS-75Gbd|
|NAD_15:Bank_6|105|0xF|200GAUI-4 C2M (Annex 120E)|0xC9|400G PCS-87Gbd|
|NAD_1:Bank_7|106|0xF|200GAUI-4 C2M (Annex 120E)|0xD8|400G PCS-98Gbd|
|NAD_2:Bank_7|107|0xD|100GAUI-2 C2M (Annex 135G)|0xEC|400G PCS-108Gbd|
|NAD_3:Bank_7|108|0xD|100GAUI-2 C2M (Annex 135G)|0xC0|400G PCS-66Gbd|
|NAD_4:Bank_7|109|0xD|100GAUI-2 C2M (Annex 135G)|0xC2|400G PCS-75Gbd|
|NAD_5:Bank_7|110|0xD|100GAUI-2 C2M (Annex 135G)|0xC9|400G PCS-87Gbd|
|NAD_6:Bank_7|111|0xD|100GAUI-2 C2M (Annex 135G)|0xD8|400G PCS-98Gbd|
|NAD_7:Bank_7|112|0x11|400GAUI-8 C2M (Annex 120E)|0xE5|400G PCS-108Gbd|
|NAD_8:Bank_7|113|0xF|200GAUI-4 C2M (Annex 120E)|0xE5|400G PCS-108Gbd|
|NAD_9:Bank_7|114|0xD|100GAUI-2 C2M (Annex 135G)|0xE5|400G PCS-108Gbd|
|NAD_10:Bank_7|115|0xC5|FOIC1.1-MFI (ITU-T G.709.5/Y.1331<br>G.Sup58) See CEI112G-VSR-PAM4|0xF8|OpenROADM FlexO-8e-DPO, Enhanced (OTN)|
|NAD_11:Bank_7|116|0xC5|FOIC1.1-MFI (ITU-T G.709.5/Y.1331<br>G.Sup58) See CEI112G-VSR-PAM4|0xF6|600G PCS-131 GBd (OTN)|
|NAD_12:Bank_7|117|0x3C|FOIC1.2-MFI (ITU-T G.709.5/Y.1331<br>G.Sup58) See CEI56G-VSR-PAM4|0xED|400G PCS-132Gbd (OTN)|
|NAD_13:Bank_7|118|0xC5|FOIC1.1-MFI (ITU-T G.709.5/Y.1331<br>G.Sup58) See CEI112G-VSR-PAM4|0xED|400G PCS-132Gbd (OTN)|
|NAD_14:Bank_7|119|0x3C|FOIC1.2-MFI (ITU-T G.709.5/Y.1331<br>G.Sup58) See CEI56G-VSR-PAM4|0xC4|400G PCS-79Gbd (OTN)|
|NAD_15:Bank_7|120|0xC5|FOIC1.1-MFI (ITU-T G.709.5/Y.1331<br>G.Sup58) See CEI112G-VSR-PAM4|0xC4|400G PCS-79Gbd (OTN)|



## ORDERING INFORMATION 

|**Ordering code**|**Item Name**|
|---|---|
|TD8010-TUNC-SO|QSFP-DD800 800G OIF/OpenROADM PCS CMIS5.3|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

R6.2 

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

