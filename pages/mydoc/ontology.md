---
title: Ontology Resources
summary: "The ACT Network is currently using ACT Ontology v4.0, which rolled out to all active ACT sites in May of 2021."
keywords: ontology, ongologies, covid, covid-19, v4.0, LOINC
sidebar: mydoc_sidebar
permalink: ontology.html
folder: mydoc
---

## Current Ontology Version
The ACT Network is currently using ACT Ontology v4.0, which rolled out through all active and staging ACT sites in May 2021. This version includes the LOINC hierarchies for SDoH and vital signs, in addition to additional COVID terms. It also inclues RxNorm by VA class, changing classification codes from NUI to VA Class identifiers. 

## COVID Ontology Information

### ACT COVID Ontology v4.0  Instructions
In order to install this new ontology, please following the following steps:
*	Install the [ACT Ontology v4.0](https://app.box.com/s/kq4opwfbl4nphrf2n9msjo96loap56qt) in production (you may also do this in stage, but production is the priority)
*	Refresh your data to pull in data for new terms 

Please document any issues in the [ACT Network JIRA Project](https://actnetwork.atlassian.net/projects/ACT/summary).

### **Release Notes**
**NEW Ontologies**
* LOINC hierarchy for social determinants of health
* LOINC hierarchy for vital signs (height, weight, BMI, etc.)
* COVID terms (updated LOINC codes, new medications, convalescent plasma and other therapies, COVID-related vaccine hierarchy, etc.) 

**Changed Ontologies**
* RxNorm by VA Class - change classification codes from UI to VA Class identifiers
* Note that the Med VA hierarchy is NOT backward compatible. This means that there will be a break in queries for terms in this hierarchy for sites who do not take the ontology. It is critical that sites take this update and make the necessary changes to ensure queries can complete without interruption across the network. There are also new terms that are only as powerful as the number of sites who add them. 

## Ontology Scripts
**ACT Ontology Modifier Removal:** The Oracle script to remove modifiers can be found [here](https://pitt.box.com/s/zqnavsqx9j01dl2xtue9zsv4es43bh4a).

## Ontology Installation 
All of the ontology installation files can be found in [this repository](https://pitt.box.com/s/qoj5afssw4oz3v27ipmfidhitmgya9nt). The ontology archive and its associated files can be accessed [here](https://pitt.box.com/s/puou2vkwy371gv2mfypadjplymb14gvd).

Installation instructions for the current ontology can be found [here](https://app.box.com/s/kq4opwfbl4nphrf2n9msjo96loap56qt).

## Current Ontology Documentation
* [ETL Guidance](https://docs.google.com/document/d/1sdMsWHUfXMpymO7SHovr0KnDyGLQ9xCUMrz-dWJ_wB4/edit?usp=sharing)
* [ACT Ontology v4.0 Installation Instructions](https://docs.google.com/document/d/1qCfPRdzkCTJZKXYmSIagY63XZGVnz8Py2HJxPOZtJSs/edit) 
* [ACT Ontology v4.0 Files](https://github.com/dbmi-pitt/ACT-Network/tree/master/ontology/ACTOntologyV4.0)

## Data Harmonization
Outputs and work products from the Data Harmonization Workgroup can be found [here](/ACT-Network/data_harmonization.html).

## Ontology Archive
Archived ontology documentation can be found in [this repository](https://pitt.box.com/s/puou2vkwy371gv2mfypadjplymb14gvd).

## Ontology Demo Server
ACT ontology on [i2b2 Web Client ](http://dbmi-ncats-test01.dbmi.pitt.edu/webclient/)

**Username:** demo 

**Password:** demouser 

## Ontology Training Material
[i2b2 Transmart Training Program - Ontology For Beginners](https://www.youtube.com/watch?v=0gF2yt1NBls&feature=youtu.be) - Mike Mendis

## Contact Information
For additional information, please contact Michele Morris at <mim18@pitt.edu>.


{% include links.html %}
