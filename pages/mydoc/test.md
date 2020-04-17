---
title: Test Tier Resources
keywords: test, covid, covid19, covid-19
last_updated: January 2, 2020
summary: "Below is the most up-to-date information regarding current software, network, and technology requirements for sites with a Test node. It also includes additional documentation for the Test nodes, including the participant identification use case."
sidebar: mydoc_sidebar
permalink: test.html
folder: mydoc
---

## Current Software Versions
**i2b2 Version:** 1.7.09c or 1.7.11 

**SHRINE Version:** 2.0 As of October 2019 

**Ontology Version:** 2.0.1 as of March 27, 2019 


## Staging Network Information 
**Hostname:** shrine-act.hms.harvard.edu  

**IP:** 134.174.149.152
 
Port 6443 

## Technology Stacks 
These pages contain all available resources for [i2b2](/ACT-Network/i2b2.html) and [SHRINE](/ACT-Network/help.shrine). This includes installation files, upgrade files, documentation, and release notes.

## Ontology
All ontology resources (including ontology files, ETL, documentation, and release notes) for ontology V2.0.1 can be found [here](/ACT-Network/ontology.html).

## COVID-19 Work
The technical requirements for participating in the ACT Network's COVID-19 are as follows:
*	Twice a week refresh of [COVID subset of patients](https://github.com/shyamvis/covid-phenotyping/blob/master/inclusion-criteria.md) (and more patients if possible)
*	Addition of the [specialized COVID ontology](https://github.com/shyamvis/covid-phenotyping)

If you are having any issues with the ontology, please email Michele Morris. SQLServer flavored DDl and insert statements as provided by Barbara Benoit can be found [here](https://github.com/shyamvis/covid-phenotyping/blob/master/ACT_COVID19_Mart_Ont_SSMS.sql). ETL instructions will be posted on GitHub shortly.

Please refer to this [JIRA Ticket](https://actnetwork.atlassian.net/projects/ACT/issues/ACT-396?filter=addedrecently&orderby=created%20DESC) to replace SHRINE's existing tomcat/webapps/shrine-api/shrine-webclient/index.html. This change add a link to a web page tracking status of cCOVID-19 data available to help researchers interpret the numbers they are seeing.

## Participant Identification Use Case
The test network is being asked to complete a use case for participant identification. The use case can be found [here](https://pitt.box.com/s/m77qy7rmby7iwievb16izltwk64i9scx).

Instructions are as follows:

* Please read the use case and follow the outlined steps.

* Pay close attention to the survey questions. This information is critical for us to understand your process, resources involved, time from ACT query to MRNs, and roadblocks encountered.   

## Site Role Resources
Below are the resources for the various local ACT roles:
* [Project Managers](/ACT-Network/project_managers.html)
* [Data Stewards and Facilitators](/ACT-Network/data_stewards.html)
* [Regulatory/Governance](/ACT-Network/regulatory.html)
* [System Administrators](/ACT-Network/system_administrators.html)
* [Data Curators](/ACT-Network/data_curators.html)

## Help
There are various avenues available for sites looking to seek or provide help. An overview of these resources can be found [here](/ACT-Network/help.html).


{% include links.html %}
