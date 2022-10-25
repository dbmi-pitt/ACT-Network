---
title: ETL
keywords: etl
permalink: etl.html
sidebar: mydoc_sidebar
folder: mydoc
---

## Calculating and Populating the c_totalnum Field
A set of scripts for calculating and populating the c_totalnum field of the metadata tables can be found [here](https://github.com/i2b2/i2b2-data/tree/master/edu.harvard.i2b2.data/Release_1-7/NewInstall/Metadata/scripts/procedures).

These scripts are written for SQLServer and calculate patient counts across the entire local i2b2 instance. While not required, it is generally recommended that you populate the c_totalnum field for query performance reasons. Be sure to read the README file before running the scripts. These scripts were previously sent via email on Feb 19; the scripts posted above are identical. 

## Resources
For EPIC ETL help, please contact Jeff Klann at <jeff.klann@mgh.harvard.edu>.

{% include links.html %}
