select 'ACT_CPT4_PX_V4' table_name, count(*) local_rowcount, '16564' rowcount from ACT_CPT4_PX_V4
union select 'ACT_DEM_V4' table_name, count(*) local_rowcount, '172' rowcount from ACT_DEM_V4
union select 'ACT_HCPCS_PX_V4' table_name, count(*) local_rowcount, '9186' rowcount from ACT_HCPCS_PX_V4
union select 'ACT_ICD10PCS_PX_V4' table_name, count(*) local_rowcount, '244334' rowcount from ACT_ICD10PCS_PX_V4
union select 'ACT_ICD9CM_DX_V4' table_name, count(*) local_rowcount, '17753' rowcount from ACT_ICD9CM_DX_V4
union select 'ACT_ICD9CM_PX_V4' table_name, count(*) local_rowcount, '4676' rowcount from ACT_ICD9CM_PX_V4
union select 'ACT_LOINC_LAB_PROV_V4' table_name, count(*) local_rowcount, '142860' rowcount from ACT_LOINC_LAB_PROV_V4
union select 'ACT_LOINC_LAB_V4' table_name, count(*) local_rowcount, '547' rowcount from ACT_LOINC_LAB_V4
union select 'ACT_MED_ALPHA_V4' table_name, count(*) local_rowcount, '1059167' rowcount from ACT_MED_ALPHA_V4
union select 'ACT_MED_VA_V4' table_name, count(*) local_rowcount, '1244825' rowcount from ACT_MED_VA_V4
union select 'ACT_SDOH_V4' table_name, count(*) local_rowcount, '22' rowcount from ACT_SDOH_V4
union select 'ACT_VITAL_SIGNS_V4' table_name, count(*) local_rowcount, '85' rowcount from ACT_VITAL_SIGNS_V4
union select 'ACT_COVID_V4' table_name, count(*) local_rowcount, '66451' rowcount from ACT_COVID_V4
union select 'ACT_ICD10CM_DX_V4' table_name, count(*) local_rowcount, '96366' rowcount from ACT_ICD10CM_DX_V4
union select 'ACT_ICD10_ICD9_DX_V4' table_name, count(*) local_rowcount, '128152' rowcount from ACT_ICD10_ICD9_DX_V4
union select 'ACT_VISIT_DETAILS_V4' table_name, count(*) local_rowcount, '164' rowcount from ACT_VISIT_DETAILS_V4;