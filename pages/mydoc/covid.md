---
title: ACT COVID-19 Work
keywords: covid, covid-19, covid19
sidebar: mydoc_sidebar
permalink: covid.html
folder: mydoc
---

## Technical Requirements
The technical requirements for participating in the ACT Network's COVID-19 are as follows:
*	Twice a week refresh of [COVID subset of patients](https://github.com/shyamvis/covid-phenotyping/blob/master/inclusion-criteria.md) (and more patients if possible)
*	Addition of the [specialized COVID ontology](https://github.com/shyamvis/covid-phenotyping)

SQLServer flavored DDl and insert statements as provided by Barbara Benoit can be found [here](https://github.com/shyamvis/covid-phenotyping/blob/master/ACT_COVID19_Mart_Ont_SSMS.sql). ETL instructions will be posted on GitHub shortly.

Please refer to this [JIRA Ticket](https://actnetwork.atlassian.net/projects/ACT/issues/ACT-396?filter=addedrecently&orderby=created%20DESC) to replace SHRINE's existing tomcat/webapps/shrine-api/shrine-webclient/index.html. This change add a link to a web page tracking status of cCOVID-19 data available to help researchers interpret the numbers they are seeing.

## COVID-19 Documentation
A folder containing all the ACT COVID-19 Network documentation can be found [here](https://drive.google.com/open?id=1TetKe3JFxpPCjN0DvV7xssZEhCV8_Zu4). If you do not have editing access to this folder and would like to request it, please email Elaina Sendro at <esendro@chartis.com> to be given proper permissions. 

## ACT COVID-19 Ontology
The ACT Network is currently installing the ACT COVID Ontology V3 in production nodes. This is additive to the current production ontology. In order to install this new ontology, please following the following steps:
*	Install the [ACT COVID ontology v3](https://github.com/shyamvis/ACT-COVID-Ontology) in production (you may also do this in stage, but production is the priority)
*	Refresh your data to pull in data for new terms 
*	Start planning for more frequent data refreshes (a web meeting will be scheduled to share tips and recommendations among ACT sites and address questions)
*  Update your status by adding information on [this Google sheet](https://docs.google.com/spreadsheets/d/12M4mKR0qdvPrruFX5qWCcWHAqPB3B5HGxd12l2bQmJY/edit)

A web meeting will be scheduled to share tips and recommendations among ACT sites and address questions. Please document any issues in the [ACT Network JIRA Project](https://actnetwork.atlassian.net/projects/ACT/summary).
 
## Need Help?
If you are having any issues with the ontology, please email Michele Morris, <mim18@pitt.edu>.


{% include links.html %}
