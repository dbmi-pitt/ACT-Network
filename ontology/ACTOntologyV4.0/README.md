# ACT Ontology V4.0 Installation 

- Installation instructions can be found at https://docs.google.com/document/d/1qCfPRdzkCTJZKXYmSIagY63XZGVnz8Py2HJxPOZtJSs/edit?usp=sharing
- Files may be downloaded here (if you have GIt LFS installed) otherwise download from the Box https://pitt.box.com/s/kq4opwfbl4nphrf2n9msjo96loap56qt


# ACT Ontology V4.0 Release Notes

## Demographics
Added Data Completeness folder with six total patient counts by visit, by patient in patient_dimension, and the equivalent of top level folders for meds, labs, procedures, and diagnosis

## Social Determinants of Health
(Courtesy of UAB and USC)
- New LOINC hierarchy

## Vital Signs
(Courtesy of UAB and USC)
- New LOINC hierarchy (height, weight, BMI, systolic, diastolic, temperature, heart rate, oxygen saturation) (Thanks UAB and USC)


## COVID-19
- Added new COVID-19 test LOINC codes
- Relabelled Nucleic and Antibody tests
- Added new COVID-19 related ICD-10-CM and MS-DRG
- Added new COVID-19 related Vaccine hierarchy including CPT-4, RxNorm, NDC, ICD-10-PCS and CVX codes
- Added convalescent plasma
- Added experimental treatment medications including monoclonal antibody treatments ICD-10-PCS ( Courtesy of Mayo )
- Corrected mechanical ventilation ICD10 hierarchies - added missing codes

## Diagnosis 
### ICD-9-CM
- Historical codes UMLS 2004AA - 2018AA
- New Codes UMLS 2018AB - 2020AB
### ICD-10-CM
- Historical codes UMLS 2004AA - 2018AA
- New Codes UMLS 2018AB - 2020AB

## Procedures
### ICD-9-Proc
- Historical codes UMLS 2004AA - 2018AA
- New Codes UMLS 2018AB - 2020AB
### ICD-10-PCS
- Historical codes UMLS 2004AA - 2018AA
- New Codes UMLS 2018AB - 2020AB
### CPT-4
- Historical codes UMLS 2004AA - 2018AA
- New Codes UMLS 2018AB - 2020AB
- Removed retired branch. Retired codes are now integrated into the main CPT-4 hierarchy.
### HCPCS
- Historical codes UMLS 2004AA- 2018AA
- New Codes UMLS 2018AB - 2020AB
- Removed obsolete branches
- Removed never active codes
- Removed Dental Procedures *No data in the network.

## Labs
### Labs (Small; manually curated) 
(Courtesy of Mayo and Malar)
- Added Drug Doses
- Added Drug/Tox
- Added 193 common LOINCs
- Moved Virus to a child of Microbiology.
- Moved Urinalysis Protein tests to a folder under Urinalysis
### Labs (Provisional; uses the LOINC hierarchy)
- No Change

## Medications
### RxNorm by alphabet
- Historical codes UMLS 2004AA - 2018AA
- New Codes UMLS 2018AB - 2020AB
### RxNorm by VA Class *This hierarchy is not backward compatible*
- Changed classification codes from NUI to VA Class identifiers
- Class ingredients match RxClass associations, no longer inferring ingredients to class mapping.
- Historical codes UMLS 2004AA - 2018AA
- New Codes UMLS 2018AB - 2020AB

## Visit Details
- Added new visit types
   - Tele-Health (T)
   - Long Term Care (LTC)
- Added Length of Stay equal to 0 days
- Modification of age at visit to improve performance of query ( Courtesy of Darren Henderson UKy)




## ACT i2b2/OMOP Ontology
Release Expected May 28, 2021


Thanks to all who contributed including the ACT Data Harmonization team:
- Sendro, Elaina
- Visweswaran, Shyam
- Philip_Trevvett
- Wyatt, Matthew C
- Vangala, Uma Maheswara Reddy
- Lin.Woon Tzu, Michael
- Vodislav, Carmen G.
- Phillip Reeder
- Ramkiran Gouripeddi 
- Wang, Amy Y
- Curtis Kieler 
- Daniel Popham
- Malarkodi Jebathilagam Samayamuthu 
- Abajian, Mark
- griffin_weber
- Cagan, Andrew 
- Gainer, Vivian S. 
- Benoit, Barbara
- Samayamuthu, Malarkodi Jebathilag
- Zhu, Wenhong
- Thorson.Stacy
- Ottmar, Paige

Testers
- Vallejos, Andrew
- Henderson, Darren
