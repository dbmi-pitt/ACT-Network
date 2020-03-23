---
title: Example Use Cases
keywords: use case
last_updated: January 3, 2020
summary: "Below are four example use cases utilizing the ACT Network."
sidebar: mydoc_sidebar
permalink: use_cases.html
folder: mydoc
---

## Use Case 1: Rheumatoid Arthritis
Clinical trial to evaluate safety and efficacy of a novel biologic in early rheumatoid arthritis inadequate responders to methotrexate. 
### Inclusion Criteria:
**Diagnosis**
* Rheumatoid arthritis (ICD-9 714.0) 
* Duration of disease: <2 years 
* Active disease: CRP >1.2x ULN or ESR >30 mm/hr (note: clinical findings generally required for enrollment, but would not be in structured data) 

**Demographics**
* Age: Between 18 and 75 years 
* Sex: No criteria 

**Medications**
* Methotrexate >3 months at >7.5 mg/week 
* Currently on Prednisone <10 mg/day or not on prednisone 
* No current biologic (etanercept, golimumab, adalimiumab, infliximab, certulizumab, anakinra, rituximab) or JAK inhibitor (tofacitinib)

**Laboratory**
* Hgb >10 g/dl, ALT and AST <ULN 
* and T bili <ULN, Creatinine <ULN 

### Exclusion Criteria
* Active tuberculosis 
* Hepatitis B 
* Hepatitis C 
* HIV 
* Pregnancy 
* Enrolled in another clinical trial 

### Pseudocode 
```
Age between 18 and 75 years
AND Rheumatoid arthritis diagnosis
AND NOT [Tuberculosis, Hepatitis B, Hepatitis C, or HIV diagnosis]

AND methotrexate order
AND NOT [prednisone >10 mg/day orders, tanercept, golimumab, adalimumab, infliximab, 
certolizumab, anakinra, rituximab, or tofacitinib orders] since 1 January 2014

AND NOT [Hemoglobin ≤10 g/dL, ALT ≥55 U/L, AST ≥48 U/L, Total bilirubin ≥1.0 mg/dL, 
or Creatinine ≥1.3 mg/dL] since 1 January 2014
```
## Use Case 2: Hepatitis C
Identification of subjects with early stage fibrosis secondary to Hepatitis C infection.
### Inclusion Criteria
**Diagnosis**
* Hepatitis C ICD9 code 070.54 
* HCV RNA positive 

**Demographics**
* Age: 18 to 64 
* Sex: No criteria

**Laboratory**
* AST available 
* ALT available 
* Platelet count available 

### Exclusion Criteria
* Prior treatment with interferon 

### Pseudocode 
```
Age between 18 and 64 years
AND Hepatitis C (ICD9 070.54) diagnosis 

AND positive Hepatitis C RNA test or Hepatitis C virus Ab or Hepatitis C virus IgG Ab
AND has Platelet measurement
AND has ALT measurement
AND has AST measurement

AND NOT [interferon order]
```
## Use Case 3: Multiple Sclerosis
### Inclusion Criteria:
**Diagnosis**
* Diagnosed with or suspected relapsing remitting multiple sclerosis optic neuritis ,transverse myelitis, cerebral or brainstem demyelinating event, neuromyelitis optica, migraine with abnormal MRI, CNS demyelinating event 
* Duration of disease: no restriction 
* Active disease: evidence by brain or spinal cord MRI, oligoclonal banding 

**Demographics**
* Age: Between 18 and 65 years inclusive 
* Sex: No criteria 

**Medications**
* Steroids currently or anytime in the last 6 months 
* Anti-coagulation or anti-platelet therapy (e.g. Coumadin, Pradaxa, Plavix, heparin) 
* Use of interferon beta 1a, interferon beta 1b, glatiramer acetate, natalizumab, teroflunomide, dimethyl fumarate, fingolimod, mitoxantrone, rituximab, cyclophosphamide, IVIG) in past 6 months 

**Laboratory**
* IgG Index any level 
* White blood cell count 
* Negative VDRL 
* Myelin basic protein 

### Exclusion Criteria
* History of Hepatitis B or C 
* HIV 
* History of lymphoma 
* History of bone marrow transplant 

  
## Use Case 4: Biliary atresia
Rare pediatric disease use case (contributed by Ronald J. Sokol, Colorado Clinical and Translational Sciences Institute) 

Proposed Clinical Trial: Clinical trial of new anti-fibrosis medication for children with biliary atresia who have undergone hepatic portoenterostomy and have evidence of portal hypertension but have not yet had liver transplant. 

### Inclusion criteria
**Diagnosis**
* Diagnosis of biliary atresia (ICD-9-CM 751.61) 
* Status post Kasai hepatic portoenterostomy (ICD-9-CM 51.37 or CPT code 47701, 47765, or 47785) 
* Presence of portal hypertension (572.3), or as defined by either platelet count < 100,000 or WBC < 4,000 or presence of esophageal varices (ICD-9 CM 456.0, 456.1, 456.20, 456.21) 

**Demographics**
* Age: 2 years through 18 years 
* Gender: No critera 
* Race/Ethnicity: Any race or ethnic group

### Exclusion criteria
* Having undergone a liver transplantation (CPT – 47135, 47136) 
* Serum creatinine > 1.5 mg/dl 
* Asthma (ICD-9-CM 493.0, 493.1, 493.2, 493.8, 493.9) 

{% include links.html %}
