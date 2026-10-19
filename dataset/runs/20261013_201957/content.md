**Data sheet Cisco public** 


## Cisco Digital CFP2-DCO Coherent Optical Module 

© 2020 Cisco and/or its affiliates. All rights reserved. 

Page 1 of 8 

## Contents 

|Contents||
|---|---|
|Introduction|3|
|Product overview|3|
|Features and benefits|3|
|Product variants|4|
|Physical specifications|7|
|Ordering information|7|
|Cisco environmental sustainability|7|
|Cisco Capital|8|



© 2020 Cisco and/or its affiliates. All rights reserved. 

Page 2 of 8 

## Introduction 

Cisco offers a comprehensive range of pluggable optical modules in the Cisco ONS pluggables portfolio. The wide variety of modules gives you flexible and cost-effective options for all types of interfaces. Cisco offers a range of GBIC, SFP, XFP, SFP+, CXP, CFP, Cisco CPAK, and QSFP+ pluggable modules. These small, modular optical interface transceivers offer a convenient and cost-effective solution for an array of applications in the data center, campus, metropolitan-area access and ring network, storage area network, and long-haul network. In recent times, with longer strides of innovation, Cisco has introduced analog DWDM CFP2 interfaces to the market. The latest addition to the Cisco portfolio pushes this boundary further with the introduction of the DIGITAL CFP2 PLUGGABLE OPTICAL MODULE. 

## Product overview 

Cisco now offers a range of all new Digital CFP2 transceivers. Cisco already offers a range of analog CFP2 transceivers. With the analog version, the DSP (Digital Signal Processor) chip resided on the line card and was therefore custom to it, while the pluggable module only had transceiver capabilities. With the digital version of the same, both the DSP and the transceiver module reside in the pluggable itself. Therefore, this digital CFP2 pluggable that is more complete and compact, could be used across all platforms with the CFP2 interface. 


**Figure 1.** Difference between analog and digital CFP2 Modules 

## Features and benefits 

This is a standard DWDM pluggable that adds on a myriad of values, each of which are listed below. 

- The line rate and modulation scheme associated with the same are both software settable on the pluggable. One could choose between 100G QPSK, 200G 8-QAM, 200G 16-QAM on the same pluggable module by software actuation. This allows one to adopt different reach as required. 

   - QPSK schemes could offer up to 2000km of reach on standard G.652 Single mode fiber. 

   - 16-QAM schemes could offer up to 400km of reach on standard G.652 Single mode fiber. 

© 2020 Cisco and/or its affiliates. All rights reserved. 

Page 3 of 8 

- The module does support different FEC algorithms to best match customer needs. This includes a 100G Staircase-FEC mode (SC-FEC) that enables interoperability with other, non CFP2-DCO based IPoDWDM products. 

- The compact pluggable formfactor itself allows you to leverage a pay-as-you-grow-model. Also noteworthy is the fact that, contrary to a analog CFP2 where one has to depend on the line card to accommodate the DSP, the digital CFP2 carries the same onboard and allows complete independence in the pay-as-you-grow model. 

- Cisco also offers a pay-as-you-grow solution on the pluggable itself by licensing its capabilities. The base pluggable comes with an automatic 100G offering alone. Then you can procure a separate license for 200G at a later point in time as required. This brings down the cost of the pluggable day one and allows customer to purchase additional features only when required. 

- When operated in 200G mode the pluggable consumes around 19W of power. This is state of the art in terms of power consumption specifications. Consequently, this offers considerable savings in OPEX. 


**Figure 2.** Digital CFP2 Optical Module 

## Product variants 

Cisco offers different versions of the Digital CFP2. Table 1 lists a PID for a product that contains what is known as a “Tunable Optical Filter (TOF)”. Table 2 lists a PID that is exactly the same module as the previous one in Table 1, except that this version does not have a TOF. The presence of the TOF in the module is attached to the application it will be used in. The TOF allows the pluggable to be used in long reach amplified DWDM systems. Removal of the TOF module from the pluggable allows for cost reduction while the application shall be limited to dark fiber systems. While customer networks require either support for DWDM or not, Cisco offers both versions allowing you to pick what is needed as per the network requirements. This is again a salient feature of the Cisco Digital CFP2 offering that distinguishes itself with the customer requirements as the prime focus. 

**Table 1.** Digital CFP2 Modules with TOF 

|**Product ID**|**Product Description**|
|---|---|
|**CFP2-WDM-DETS-1HL=**|200G, 100G, WDM Digital CFP2 pluggable Licensed for 100G only – TOF|



© 2020 Cisco and/or its affiliates. All rights reserved. 

Page 4 of 8 

**Table 2.** Digital CFP2 Modules without TOF 

|**Product ID**|**Product Description**|
|---|---|
|**CFP2-WDM-DS-1HL=**|200G, 100G, WDM Digital CFP2 pluggable Licensed 100G only - NON TOF version|



## Specifications 

It is important to note that 200G version in table 1 with TOF and the 200G version in table 2 without TOF, both have the same technical specifications, except that the without-TOF version has a lesser out-of-band OSNR specification. Therefore, the below specifications will be detailed for the 200G+100G version. It is implied that the specification of those in table 2 are exactly the same except for the out-of-band OSNR specification. 

**Table 3.** Transmitter specifications 

|**Product ID**|**Transmit Power**|**Output out-of-band**|**Output in-band**|**Optical output return**|
|---|---|---|---|---|
||**Range (dBm)**|**OSNR (dB @0.1nm)**|**OSNR (dB @0.1nm)**|**loss (dB)**|
||||||
|**CFP2-WDM-DETS-1HL=**|-10 to +1|45|100G QPSK: 37|27|
||||200G 16QAM: 34.3||
||||200G 8QAM: 32.3||
|**CFP2-WDM-DS-1HL=**|-5 to +1|25|100G QPSK: 37|27|
||-10 to -5|20|200G 16QAM: 34.3||
||||200G 8QAM: 32.3||



The transmitter has a cold restart timing specification of 50-90 seconds. Cold restart means that the DCO is in a Low_Power mode. The maximum Tx turn-up time is counted from de-assert of the Low_power pin and Tx_disable pin to full Tx turn-up. 

The transmitter has a warm restart timing specification of 4 seconds. Warm restart means that the DCO is in Ready state. The maximum transmitter turn-up time is counted from de-assert of the Tx_disable Pin to full Tx turn-up. 

The transmitter also has the ability to grid-less tune to any channel in the C-band spectrum. Typical of this is the 96 channel 50GHz spaced tuning that is adopted by many users. The tunability switching time in such a case where you shift from one optical frequency to another including the Tx turn off and turn on time, is 60 seconds. During the tuning period, the Tx power stays at -40dBm. 

© 2020 Cisco and/or its affiliates. All rights reserved. 

Page 5 of 8 

**Table 4.** Receiver specifications 

|**Product ID**|**Receiver Power Range**|**Maximum**|**Back to back OSNR (dB**|**Chromatic**|
|---|---|---|---|---|
||<br>**(dBm) – Single Channel**|**Optical input**|**@0.1nm)**|**Dispersion**|
|||<br>**power (dBm)**||<br>**Tolerance (dB)**|
||||||
|**CFP2-WDM-DETS-1HL=**<br>**CFP2-WDM-DS-1HL=**|**100G QPSK**<br>Without OSNR penalty: -<br>18 to 0<br>With 0.3dB OSNR penalty<br>-22 to +1<br>Differential with 7% FEC ,<br>15% SD-FEC and SC-FEC:<br>-29 to 0<br>100G QPSK Non-<br>Differential with SD-FEC: -<br>30 to 0|13|**100G QPSK**<br>SD-FEC (diff): 13.5<br>SD-FEC (non-diff): 12.3<br>Staircase-FEC: 14.5|100G QPSK: 0.5<br>|CD|<=<br>40000ps/nm|
||**200G 16QAM**<br>Without OSNR penalty: -<br>13 to 0<br>With 0.5dB OSNR penalty:<br>-18 to 0<br>With 1dB OSNR penalty: -<br>21 to 0<br>With SD-FEC: -22 to 0|13|**200G 16QAM**<br>SD-FEC Non-Diff: 21.5|200G 16QAM:<br>0.5<br>|CD|<=<br>16000ps/nm|
||**200G 8QAM**<br>Without OSNR penalty: -<br>18 to 0<br>With 0.5dB OSNR penalty:<br>-21 to 0<br>With SD-FEC: -24 to 0|13|**200G 8QAM**<br>15% SD-FEC Non-Diff: 20|200G 8QAM: 0.5<br>|CD|<=<br>20000ps/nm|



© 2020 Cisco and/or its affiliates. All rights reserved. 

Page 6 of 8 

## Physical specifications 

**Table 5.** Digital CFP2 Modules 

|**Product ID**|**Maximum Power**|**Connector Type**|**Cable Type**|**Temperature**|
|---|---|---|---|---|
||**Consumption (W)**|||**Range (°C)**|
||||||
|**CFP2-WDM-DETS-1HL=**|100G QPSK: 17|LC-LC|LC|0 to +70|
|**CFP2-WDM-DS-1HL=**|200G 16QAM: 19.5||||
||200G 8QAM: 20.5||||



## Ordering information 

**Table 6.** Digital CFP2 Modules 100G/200G 

|**Product ID**|**Product Description**|
|---|---|
|**CFP2-WDM-DETS-1HL=**|200G, 100G, WDM Digital CFP2 pluggable Licensed for 100G only – TOF|
|**CFP2-WDM-DS-1HL=**|200G, 100G, WDM Digital CFP2 pluggable Licensed 100G only - NON TOF version|
|**CFP2-LIC-UPG-200G**|License for WDM Digital CFP2 enabling 200G - physical|



The above listed optical modules come per default with 100G license. The 200G capability is an add-on that can be procured as a license shown in the above table. 

## Cisco environmental sustainability 

Information about Cisco’s environmental sustainability policies and initiatives for our products, solutions, operations, and extended operations or supply chain is provided in the “Environment Sustainability” section of Cisco’s Corporate Social Responsibility (CSR) Report. 

Reference links to information about key environmental sustainability topics (mentioned in the “Environment Sustainability” section of the CSR Report) are provided in the following table: 

|**Sustainability topic**|**Reference**|
|---|---|
|**Information on product material content laws and regulations**|Materials|
|**Information on electronic waste laws and regulations, including products, batteries, and packaging**|WEEE compliance|
|||



Cisco makes the packaging data available for informational purposes only. It may not reflect the most current legal developments, and Cisco does not represent, warrant, or guarantee that it is complete, accurate, or up to date. This information is subject to change without notice. 

© 2020 Cisco and/or its affiliates. All rights reserved. 

Page 7 of 8 

## Cisco Capital 

## **Flexible payment solutions to help you achieve your objectives** 

Cisco Capital makes it easier to get the right technology to achieve your objectives, enable business transformation and help you stay competitive. We can help you reduce the total cost of ownership, conserve capital, and accelerate growth. In more than 100 countries, our flexible payment solutions can help you acquire hardware, software, services and complementary third-party equipment in easy, predictable payments. Learn more. 


Printed in USA 

C78-743732-00 05/20 

© 2020 Cisco and/or its affiliates. All rights reserved. 

Page 8 of 8 

