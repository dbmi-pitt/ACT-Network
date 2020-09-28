---
title: Ontology Resources
summary: "The ACT Network is currently using ACT Ontology 2.0.1, which rolled out through all active and staging ACT sites to better meet the needs of clinical investigators and CTSA hubs. In June 2020, the ACT COVID Ontology V3 was also released, which contains the new COVID-19 ontology."
keywords: ontology, ongologies, covid, covid-19, v3
sidebar: mydoc_sidebar
permalink: ontology.html
folder: mydoc
---

## Current Ontology Version
The ACT Network is currently using ACT Ontology 2.0.1, which rolled out through all active and staging ACT sites in 2019. This new version provides a substantial increase in the available data elements, including CPT, HCPCS, ICD10 procedures, a full set of LOINC codes and additional medications. 

A summary overview of the changes made can be found [here](https://www.actnetwork.us/Global/FileLib/PDFs/ACT_ONTOLOGY_V2.0.1_final.pdf).

Currently the ACT Network is upgrading to ACT COVID Ontology V3, which includes the new COVID-19 ontology. This is additive to the current production ontology. All information related to this ontology can be found below.

## COVID Ontology Information

### Technical Requirements for ACT COVID Oncology V3
The technical requirements for participating in the ACT Network's COVID-19 are as follows:
*	Twice a week refresh of [COVID subset of patients](https://github.com/shyamvis/covid-phenotyping/blob/master/inclusion-criteria.md) (and more patients if possible)
*	Addition of the [specialized COVID ontology](https://github.com/shyamvis/covid-phenotyping)

SQLServer flavored DDl and insert statements as provided by Barbara Benoit can be found [here](https://github.com/shyamvis/covid-phenotyping/blob/master/ACT_COVID19_Mart_Ont_SSMS.sql). ETL instructions will be posted on GitHub shortly.

Please refer to this [JIRA Ticket](https://actnetwork.atlassian.net/projects/ACT/issues/ACT-396?filter=addedrecently&orderby=created%20DESC) to replace SHRINE's existing tomcat/webapps/shrine-api/shrine-webclient/index.html. This change add a link to a web page tracking status of cCOVID-19 data available to help researchers interpret the numbers they are seeing.

### ACT COVID Ontology V3 Documentation
A folder containing all the ACT COVID-19 Network documentation can be found [here](https://drive.google.com/open?id=1TetKe3JFxpPCjN0DvV7xssZEhCV8_Zu4). If you do not have editing access to this folder and would like to request it, please email Elaina Sendro at <esendro@chartis.com> to be given proper permissions. 

### ACT COVID Ontology V3  Instructions
In order to install this new ontology, please following the following steps:
*	Install the [ACT COVID ontology v3](https://github.com/shyamvis/ACT-COVID-Ontology) in production (you may also do this in stage, but production is the priority)
*	Refresh your data to pull in data for new terms 
*	Start planning for more frequent data refreshes (a web meeting will be scheduled to share tips and recommendations among ACT sites and address questions)
*  Update your status by adding information on [this Google sheet](https://docs.google.com/spreadsheets/d/12M4mKR0qdvPrruFX5qWCcWHAqPB3B5HGxd12l2bQmJY/edit)

Please document any issues in the [ACT Network JIRA Project](https://actnetwork.atlassian.net/projects/ACT/summary).

### **Release Notes**
**NEW Ontologies**
* CPT Procedures - UMLS 2018AA (Remember only sites that have valid CPT licenses are permitted to use CPT ontology) 
* HCPCS Procedures - UMLS 2018AA 
* ICD10 PCS Procedures - UMLS 2018AA 
* ICD10 CM Diagnosis - UMLS 2018AA 
* Labs LOINC Provisional - Full LOINC tree - UMLS 2018AA LOINC V2.63 
* Medications by Ingredient - Hybrid UMLS 2018AA RxNorm? files and RxNav? 

**Updated Ontologies**
* ICD9 Diagnosis - UMLS 2018AA modified format. Ordered by code. 
* ICD9 Procedures - UMLS 2018AA modified format. Ordered by code. 
* Medication by VA Class - RxNav? NDFRT and RxNorm? APIs updated to September 2018 
* Demographics - Added Adult >= 18 and Child < 18 terms 

**Unchanged**
* ICD10/ICD9 Integrated - Curated UMLS 2015AB 
* Visit Details 
* Lab - Curated Approx. 300 Labs 

**Other Updated Files** 
* Schemes 
* Table Access 
* SHRINE Adapter Mapping 

**Breakdown** (coming soon) 

## Ontology Scripts
**ACT Ontology Modifier Removal:** The Oracle script to remove modifiers can be found [here](https://pitt.box.com/s/zqnavsqx9j01dl2xtue9zsv4es43bh4a).

## Ontology Installation 
All of the ontology installation files can be found in [this repository](https://pitt.box.com/s/qoj5afssw4oz3v27ipmfidhitmgya9nt). The ontology archive and its associated files can be accessed [here](https://pitt.box.com/s/puou2vkwy371gv2mfypadjplymb14gvd).

Installation instructions for the current ontology can be found [here](https://pitt.box.com/s/jf2mupczvclzzxtmfvdd6pn1bytg1z1v).

## COVID-19 Ontology
Links to the COVID-19 ontology and other information related to the ACT Network's COVID-19 project can be found [here](https://dbmi-pitt.github.io/ACT-Network/test.html#covid-19-ontology).

## Current Ontology Documentation
* [ACT Common Data Model V1.7](https://pitt.box.com/s/nuoueqadkcuhq6oqxbg3rsmg0kcaqcyo)
* [ACT SHRINE Query Ontology Specification](https://pitt.box.com/s/ovkqhwhg6hhqv83hqp522wix0hsysr2k) 
* [ACT ETL Quick Reference](https://pitt.box.com/s/eg528mhbwb20fnp5mntgf5une8rv7zcp)

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
