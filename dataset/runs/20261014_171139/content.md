## **Data sheet Cisco public** 


Cisco 400G Digital Coherent Optics QSFP-DD Optical Modules 

© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 1 of 12 

|Contents||
|---|---|
|Product overview|4|
|Features and benefits|5|
|**Multivendor interoperability**|**6**|
|**Flexible modulation**|**6**|
|Specification|7|
|**Transmitter specifications**|**7**|
|**Rx parameter specifications**|**8**|
|**Rx Optical Polarization specifications**|**9**|
|**Rx Multichannel Interaction specifications**|**9**|
|**Physical**|**10**|
|Ordering information|10|
|Cisco environmental sustainability|11|
|Cisco Capital|11|
|Document history|12|



© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 2 of 12 

Cisco offers a comprehensive range of pluggable optical modules in the Cisco[®] pluggables portfolio. The wide variety of modules gives you flexible and cost-effective options for all types of interfaces. Cisco offers a range of GBIC, SFP, XFP, SFP+, CXP, CFP, Cisco CPAK, and QSFP+ pluggable modules. These small, modular optical interface transceivers offer a convenient and cost-effective solution for an array of applications in the data center, campus, metropolitan-area access and ring network, storage area network, and long-haul network. In recent times, with longer strides of innovation, Cisco has introduced analog DWDM CFP2 interfaces to the market. The latest addition to the Cisco portfolio pushes this boundary further with the introduction of the 400G DIGITAL COHERENT QSFP-DD PLUGGABLE OPTICAL MODULE. 


**Figure 1.** From Discrete components to Integrated Coherent Pluggable. 

© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 3 of 12 

## Product overview 

Cisco now offers a range of all new 400G Digital Coherent QSFP-DD transceivers. Cisco already offers a range of Digital Coherent CFP2 transceivers capable of supporting up to a 200-Gbps wavelength. Thanks to the miniaturization of the technology with a 7-nm manufacturing procedure and innovation in silicon photonic technology, it is now possible to squeeze a 400G-capable Digital Coherent WDM interface within a QSFP-DD form factor. 

Two product variants are available: 

1. ZR variant 

2. ZR Plus variant 

## **QDD ZR overview** 

The QSFP-DD ZR variant complies with OIF MSA, allowing to provide compatibility with the equivalent component compliant with the same MSA standard. The key application for the ZR standard is allowing the transmission of a 400G wavelength in point-to-point topology up to a distance of 120 km with the Mux/Demux and Amplifier as depicted the below. 


**Figure 2.** QSFP DD ZR Application. 

In this product variant, the pluggable can support both a 400GE and 4x 100GE interface with the host card. 

## **QDD ZR Plus overview** 

The QSFP-DD ZR Plus variant complies with OpenZR+ MSA, allowing to cope for distances going from regional to long haul with multiple amplification sites between the end point. This variant is also providing multiple configuration options in terms of Modulation scheme, TX filter shaping, and baud rates on top of what OpenZR+ MSA defines. 

This variant is also the one capable of reaching the longest transmission distance thanks to the high-performing O-FEC algorithm. 

It is able to support an ~60G baud rate, QPSK, and 8-QAM and 16-QAM modulation scheme to cope with a 200G (QPSK), 300G (8-QAM), and 400G (16-QAM) per wavelength transmission capacity. 

It is also capable of supporting 100G signals leveraging QPSK modulation scheme at ~30G baud as well as 200G signal at 16-QAM (~30Gbaud) and 8-QAM (~40 Gbaud). 

From the signal shaping mode of view, two different configurations are supported (with or without Tx shaping) to cope with different filtering requirements. 

© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 4 of 12 

## Features and benefits 

As line card ports become universal, it is possible to design new line cards optimized for 400G, knowing that by simply replacing the pluggable, the port can support bitrates down to 100G to guarantee backward compatibility with previous-generation routers. In addition, the IPoDWDM options, available by simply using the 400G ZR/ZR+ optics, provides, for the first time, the same density of grey line cards, eventually solving the usual dilemma of having to choose between the benefits of integration and maximizing the throughput of router line cards. 

Some network operators chose to take a different approach at 400G upon recognizing the lessons learned from the efforts at 100G. In late 2016, these network operators and a few vendors identified 400G as an intersection point for the industry to support coherent optics in the same form factors as emerging high-volume client optics, such as QSFP-DD. In less than one year, the OIF defined most of the 400ZR interface technical details, which helped motivate increased industry investment in pluggable, interoperable coherent interfaces. 

A key requirement was to accommodate hyperscale DCI links beyond 120 km, while maintaining the same QSFP-DD/OSFP form factors. A survey of 400G standardization efforts pointed to elements of OpenROADM that could provide a standard-based, high-performance addition to the 400ZR standard. Thus, the industry began looking at the next logical step, which would be to combine these vetted specifications and achieve the goal of addressing 400G Ethernet-centric solutions beyond 120 km. This would enable the extension of hyperscale DCIs beyond the edge to regional distances, and expand the addressable market for module suppliers, providing greater economies of scale that benefit the entire distribution chain. This combination of the 400ZR standard with elements of OpenROADM became known as OpenZR+. 


**Figure 3.** OpenZR+ is the logical combination of two industry standardization efforts that enables high-performance DCI pluggable modules supporting multivendor interoperability. 

© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 5 of 12 

As illustrated in Figure 1, OpenZR+ is a combination of two industry standardization efforts created to maintain the simple Ethernet-only host interface of 400ZR while adding support for features such as: (1) higher coding gain using oFEC from the OpenROADM standard, which extends the reach capability; (2) multirate Ethernet, which enables the multiplexing of 100GbE and 200GbE clients over the line-side link, providing optimization options for the switch/router equipment to channelize the traffic over the transport link; (3) adjustable 100G, 200G, 300G, or 400G line-side transport links (using QPSK, 8QAM, or 16QAM modulation), which enables reach/capacity optimization over various fiber links; and (4) higher dispersion tolerance. All of these enhanced capabilities would exist in a QSFP-DD designed to utilize OpenZR+, supporting reaches well beyond the 120 km supported by 400ZR. 

The table below summarizes the benefits of modules designed to use OpenZR+, compared to 400ZR and OpenROADM. 

||**400ZR**|**OpenROADM**|**OpenZR+**|
|---|---|---|---|
|**Target Application**|Edge DCI|Carrier Metro/LH|Regional DCI|
|**Client Traffic**|400GbE only|100-400GbE & OTN|100-400GbE Multirate|
|**Reach**|≤120km|>120km*|>120km*|
|**Form Factor**|QSFP-DD/OSFP|CFP2 or other|QSFP-DD/OSFP|
|**SD-FEC**|CFEC|oFEC|oFEC|



* Distance depending on adopted WDM Transport system 

## **Multivendor interoperability** 

Extensive system-level testing and unmatched technical expertise enable Cisco optics to be successfully used across Cisco as well as multivendor platforms. The strategic supply chain diversity and service capabilities provide the high network availability and peace of mind. 

## **Flexible modulation** 

As in the case of QSFP+, QSFP56-DD will provide the capability to support lower bitrates, via 4x 100G pluggables. In addition, this pluggable supports the downsize to the port to 200G (or 2x 100G). This one pluggable fit’s all type of approach provides great benefits to both vendors and customers, as it enables a simplification in the IP router portfolio and, as a consequence, a simplification in network planning and spare parts. 

© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 6 of 12 

## Specification 

## **Transmitter specifications** 

Both QDD ZR and ZR+ supports full C band tune ability. Tx parameter specifications are showed in the table below. 

|**Product ID**|**Max Transmit Power**|**Symbol Rate**|**Modulation**|**FEC**|**OOB**|**OIB**|
|---|---|---|---|---|---|---|
|||**(+/-20ppm)**|**(Payload)**||**OSNR**|**OSNR**|
||||||||
|**QDD-400G-ZR-S**|Without TX Shaping:|59,843,750,000|16-QAM (400G)|C-FEC|30 dB|34 dB|
||-8.5 (Typ)||||||
||-10 (Worst case)||||||
|**QDD-400G-ZRP-S**|Without TX Shaping:|60,138,546,798|16-QAM (400G)|OFEC|42 dB|42 dB|
||-8.0 (Typ)||||||
||-10.0 (Worst case)||||||
||With TX Shaping:||||||
||-11.0 (Typ)||||||
||-13.0 (Worst case)||||||
||Without TX Shaping:|60,138,546,798|8-QAM (300G)|OFEC|42 dB|42 dB|
||-8.6 (Typ)||||||
||-10.2 (Worst case)||||||
||With TX Shaping:||||||
||-10.4 (Typ)||||||
||-11.9 (Worst case)||||||
||Without TX Shaping:|60,138,546,798|QPSK (200G)|OFEC|42 dB|42 dB|
||-6.2 (Typ) -7.7||||||
||(Worst case)||||||
||With TX Shaping:||||||
||-9.0 (Typ)||||||
||-10.5 (Worst case)||||||
||TX shaping only:|40,092,364,532|8-QAM (200G)|OFEC|42 dB|42 dB|
||-9.0 (Typ)||||||
||-11 (Worst case)||||||
||TX shaping only:|30,069,273,399|16-QAM (200G)|OFEC|42 dB|42 dB|
||-8.0 (Typ)||||||
||-10 (Worst case)||||||
||Without TX shaping|30,069,273,399|QPSK (100G)|OFEC|42 dB|42 dB|
||only:||||||
||||||||
||-5.9 (Typ)||||||



© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 7 of 12 

|**Product ID**|**Max Transmit Power**|**Max Transmit Power**||**Symbol Rate**|**Symbol Rate**|**Modulation**|**Modulation**|**FEC**|**FEC**|**OOB**|**OOB**|**OIB**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||**(+/-20ppm)**||**(Payload)**||||**OSNR**||**OSNR**|
||||||||||||||
||-7.5 (Worst case)||||||||||||
|**Rx parameter specifications**|||||||||||||
|**Product ID**|**Modulation**|**RX OSNR**|**RX**||**Extended**||**RX Power**||**Max Rx**||**CD Robustness**||
||**(Payload)**|**Sensitivity**|**Sensitivity**||**Range RX**||**Sensitivity (No**||**Power**||**(ps/nm)**||
|||<br>**(dB)**|<br>**Optimal**||<br>**Sensitivity**||<br>**ASE Noise)**||||||
||||||<br>**(1dB OSNR**||||||||
||||||<br>**Penalty)**||||||||
|**QDD-400G-ZR-S**|16-QAM|26|-12dBm||-15dBm||-20dBm||13dBm||+/-2400||
||(400G)||||||||||||
||||||||||||||
|**QDD-400G-ZRP-S**|16-QAM|Without|-12dBm||-16dBm||Without TX||13dBm||Default: +/-||
||(400G)|TX|||||Shaping:||||13,000||
|||<br>Shaping:|||||<br>-20dBm||||||
||||||||||||Configurable up||
|||23.7|||||||||||
||||||||With TX Shaping:||||<br>to: +/-52,000||
|||With TX|||||<br>-21dBm||||||
||||||||||||||
|||Shaping:|||||||||||
||||||||||||||
|||23.1|||||||||||
||8-QAM|Without|-15dBm||-19dBm||Without TX||13dBm||Default: +/-||
||(300G)|TX|||||Shaping:||||26,000||
||||||||||||||
|||Shaping:|||||-22dBm||||||
|||<br>20.8|||||||||Configurable up||
||||||||With TX Shaping:||||<br>to: +/- 100,000||
|||With TX|||||<br>-23dBm||||||
|||<br>Shaping:|||||||||||
||||||||||||||
|||19.5|||||||||||
||QPSK|Without|-18dBm||-22dBm||-28dBm||13dBm||Default: +/-||
||(200G)|TX|||||||||50,000||
||||||||||||||
|||Shaping:|||||||||||
|||<br>15.3|||||||||Configurable up||
||||||||||||to: +/- 100,000||
|||With TX|||||||||||
|||<br>Shaping:|||||||||||
|||15.0|||||||||||
||8-QAM|17.4 (Only|-16dBm||-20dBm||-28dBm||13dBm||Default: +/-||
||(200G)|TX|||||||||26,000||
||||||||||||||
|||shaping|||||||||||
||||||||||||Configurable up||
|||supported)|||||||||||
||||||||||||to: +/-100,000||
||||||||||||||
||16-QAM|19.3 (Only|-15dBm||-20dBm||-24dBm||13dBm||Default: +/-||
||(200G)|TX|||||||||21,000||
||||||||||||||
|||shaping|||||||||||
||||||||||||Configurable up||
|||supported)|||||||||||
||||||||||||to: +/- 85,000||
||||||||||||||
||QPSK|11.8 (No|-20dBm||-25dBm||-28dBm||13dBm||Default: +/-||
||(100G)|Tx|||||||||80,000||
|||shaping)|||||||||||
||||||||||||Configurable up||
||||||||||||<br>to: +/-160,000||



© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 8 of 12 

## **Rx Optical Polarization specifications** 

|**Product ID**|**Modulation**|**State of**|**State of**|**State of**|**DGD Robustness**|
|---|---|---|---|---|---|
||**(Payload)**|**Polarization**|**Polarization**|**Polarization**|**(ps)**|
|||**Change rate w/**|**Change rate w/**|**Change rate w/**||
|||<br>**0.5dB of OSNR**|<br>**1dB of OSNR**|<br>**2dB of OSNR**||
|||**penalty**|**penalty**|**penalty**||
|**QDD-400G-ZR-S**|16-QAM (400G)|50 rad/ms|50 rad/ms|50 rad/ms|33|
|**QDD-400G-ZRP-S**|16-QAM (400G)|80 rad/ms|150 rad/ms|200 rad/ms|60|
||8-QAM (300G)|120 rad/ms|200 rad/ms|300 rad/ms|60|
||QPSK (200G)|800 rad/ms|1000 rad/ms|1400 rad/ms|60|
||8-QAM (200G)|70 rad/ms|100 rad/ms|150 rad/ms|60|
||16-QAM (200G)|50 rad/ms|100 rad/ms|150 rad/ms|60|
||QPSK (100G)|400 rad/ms|500 rad/ms|800 rad/ms|80|



## **Rx Multichannel Interaction specifications** 

|**Product ID**|**Modulation (Payload)**|**Multichannel Xtalk tolerance by**|**Multichannel Xtalk OSNR penalty**|
|---|---|---|---|
|||**15 additional channels**|**induced by 2 adjacent channels**|
|||||
|**QDD-400G-ZR-S**|16-QAM (400G)|15db with OSNR oenalty ≤ 1dB|0.5 dB ( adjacent chs at 75Ghz)|
|**QDD-400G-ZRP-S**|16-QAM (400G)|15db with OSNR oenalty ≤ 0.5dB|0.5 dB ( adjacent chs at 75Ghz)|
||8-QAM (300G)|15db with OSNR oenalty ≤ 0.3dB|0.3 dB ( adjacent chs at 75Ghz)|
||QPSK (200G)|15db with OSNR oenalty ≤ 0.3dB|0.2 dB ( adjacent chs at 75Ghz)|
||8-QAM (200G)|15db with OSNR oenalty ≤ 0.3dB|0.7 dB ( adjacent chs at 50Ghz)|
||16-QAM (200G)|15db with OSNR oenalty ≤ 0.3dB|0.8 dB ( adjacent chs at 50Ghz)|
||QPSK (100G)|17db with OSNR oenalty ≤ 0.35dB|0.6 dB ( adjacent chs at 37.5Ghz)|



© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 9 of 12 

## **Physical** 

|**Product ID**|**Temp Range**|**MTBF**|**Roundtrip Latency**|
|---|---|---|---|
|**QDD-400G-ZR-S**|Operating Case Temperature|442,477 hrs|400GE: 7.9 microsec|
||range: 15 to +75°C|||
||||4x100GE: 8.2 microsec|
||Short term operating case|||
|**QDD-400G-ZRP-S**|<br>temperature range +80°C.|442,477 hrs|400GE: 4.7 microsec|
||Note: a short term condition is|||
||present for a period of not||4x100GE: 5.2 microsec|
||more than 96 consecutive|||
||hours and a total of not more<br>||3x100GE: 6.0 microsec|
||than 15 days in 1 year. This||2x100GE: 6.9 microsec|
||refers to a total of 360 hours in|||
||any given year, but no more|||
||than 15 occurrences during|||
||that 1-year period.|||
||Note: the module turn up from|||
||cold start at ambient|||
||temperature as low as -5°C|||
||and it will warm up with a case|||
||temperature higher than the|||
||ambient temperature, but it will|||
||meet optical performance|||
||specs only with case|||
||temperature within the range|||
||defined above.|||



## Ordering information 

QSFP Double-Density Digital Coherent Optical Modules 400G 

|**Product ID**|**Product Description**|
|---|---|
|**QDD-400G-ZR-S**|QSFP-DD transceiver module, coherent DCO, 400G-ZR|
|**QDD-400G-ZRP-S**|QSFP-DD transceiver module, coherent DCO, 400G-ZR+|



© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 10 of 12 

## Cisco environmental sustainability 

Information about Cisco’s environmental sustainability policies and initiatives for our products, solutions, operations, and extended operations or supply chain is provided in the “Environment Sustainability” section of Cisco’s Corporate Social Responsibility (CSR) Report. 

Reference links to information about key environmental sustainability topics (mentioned in the “Environment Sustainability” section of the CSR Report) are provided in the following table: 

|**Sustainability topic**|**Reference**|
|---|---|
|**Information on product material content laws and regulations**|Materials|
|**Information on electronic waste laws and regulations, including products, batteries, and packaging**|WEEE compliance|



Cisco makes the packaging data available for informational purposes only. It may not reflect the most current legal developments, and Cisco does not represent, warrant, or guarantee that it is complete, accurate, or up to date. This information is subject to change without notice. 

## Cisco Capital 

## **Flexible payment solutions to help you achieve your objectives** 

Cisco Capital makes it easier to get the right technology to achieve your objectives, enable business transformation and help you stay competitive. We can help you reduce the total cost of ownership, conserve capital, and accelerate growth. In more than 100 countries, our flexible payment solutions can help you acquire hardware, software, services and complementary third-party equipment in easy, predictable payments. Learn more. 

© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 11 of 12 

## Document history 

**Table 1.** Document history 

|**New or Revised Topic**|**Described In**|**Date**|
|---|---|---|
|**01**|First Version||
|**02**|Provided additional Optical parameterlist||




Printed in USA 

C78-744377-01 10/21 

© 2021 Cisco and/or its affiliates. All rights reserved. 

Page 12 of 12 

