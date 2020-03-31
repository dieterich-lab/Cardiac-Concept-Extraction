# Supplement: Cardiac Concept Extraction from German Discharge Letters to Prefill Structured Reporting Forms

Table 1: Translation of cardiac entities German-English and xml field name

|German entity name|English entity name|XML field name|
|---|---|---|
|Kardiomyopathie|Cardiomyopathy|gopl_kardiomyopathie|
|Diabetes Mellitus|Diabetes mellitus|gopl_diabetes_mellitus|
|Arterielle Hypertonie|Arterial hypertension|gopl_arterielle_hypertonie|
|Niereninsuffizeinz|Kidney failure|gopl_niereninsuffizienz|
|Zustand nach Myokardinfarkt|Condition after myocardial infarction|gopl_zustand_myokardinfarkt|
|Zustand nach Dekompensation|Condition after decompensation|gopl_zustand_nach_dekompensation|
|Vorhofflimmern|Atrial fibrillation|gopl_vorhofflimmern_flattern|
|Herzklappenerkrankung|Heart valve desease|gopl_herzklappenerkrankung|
|Koronare Bypass Operation|Coronary bypass surgery|gopl_koronare_bypass_operation|
|Dislipidämie|Dyslipidemia|gopl_dyslipidaemie|
|Familienanamnese|(Medical) Family History|gopl_familienanamnese_kardiovaskulaere_ereignisse|
|Interventionelle koronare Revaskularisation|Coronary revascularization|gopl_interventionelle_koronare_revaskularisation|
|Kardiale Kontraktilitätsmodulation (CCM)|Cardiac Contractility Modulation (CCM)|gopl_ccm|
|Racuher|Smoker|gdrp_raucher|
|NYHA Klasse|NYHA Class|gdrp_nyha_klasse_derzeit|
|Typ Kardiomyopathie|Type cardiomyopathy|gdrp_einteilungmitkardiomyopathie|
|Körpergröße|Body height|gtfe_koerpergroesse|
|Körpergewicht|Body weight|gtfe_gewicht|
|Raucher - Menge|Smoking - amount|gtfe_pack_years|
|Raucher - Ex seit|Smoking - Ex since|gtfe_ex_raucher|


Table 2: Extraction method and rule per binary cardiac entity

|XML Field|Extraction Method|Rules|
|---|---|---|
|gopl_kardiomyopathie|Substring matching|"myopathie" and not ("ischämische kar" in string (Diagnosis)|
|gopl_diabetes_mellitus|Substring matching|"diabetes" or "iddm" or "DM" in string.lower (Cvrf)|
|xml: gopl_arterielle_hypertonie|Substring matching|"hyperton" in string.lower (Cvrf)|
|gopl_niereninsuffizienz|Substring matching|"nierenins" in string.lower (Diagnosis)|
|gopl_zustand_myokardinfarkt|Substring matching|'myokardinfarkt' or 'wandinfarkt' or 'STEM' in string.lower (Diagnosis)|
|gopl_zustand_nach_dekompensation|Substring matching|"dekompensation" in string.lower (Anamnese, Diagnosis)|
|gopl_vorhofflimmern_flattern|Substring matching|"vorhof" and ("flimmern" or "flattern") in string.lower (Diagnosis)|
|gopl_herzklappenerkrankung|Substring matching|"klappe" and 'insuf') or (("mitral" or "aorten" or "pulmonal" or "trikuspi" or "bikuspi") and insuf in string.lower (Diagnosis)|
|gopl_koronare_bypass_operation|Substring matching|"bypass" or "ACB" in stirng.lower (Diagnosis)|
|gopl_dyslipidaemie|Substirng matching|cholester" or "dyslip" or "hyperlip" in string.lower (Cvrf)|
|gopl_familienanamnese_kardiovaskulaere_ereignisse|Substring matching|"familienanamnese" and not "leer" and not "negativ" and not     "unauffällig" in string.lower (Cvrf, FA)|
|gopl_interventionelle_koronare_revaskularisation|Substring matching|"stent" or "ballon" or "ptca" in string.lower (Diagnosis)|
|gopl_ccm|Regular Expression|"\bCCM\b"|

Table 3: Extraction method and rule per multiclass cardiac entity

|XML Field|Extraction Method|Rules|Classes|
|---|---|---|---|
|gdrp_raucher|Majority Vote (four labeling functions using regular expression and pattern matching)|see predict_smoking.py|Yes, no, unknown|
|gdrp_nyha_klasse_derzeit|Regular expression|(?<=NYHA)\s?(Stadium)?(\sI-II\|\sII-III\|\sIII-IV\|\sI{1,3}\|\sIV)|I, II, III|
|gdrp_einteilungmitkardiomyopathie|Substirng matching|("hypertroph" or "HCM") or ("compaction" or "NCCM") or ("dilatativ" or "DCM") or ("arrhythmogen" or "ARVCM" or "ARVC") or ("inflammatorisch") in string.lower|DCM, HCM, NCCM, ARVC, inflammatorisch, unknown|

Table 4: Extraction method and rule per numeric cardiac entity

|XML Field|Extraction Method|Rules|
|---|---|---|
|gtfe_koerpergroesse|Regular expression|'(\d{3}\s?cm)\|([12][\,\.][0-9]{2}\s?m)'|
|gtfe_gewicht|Regular expression|'\d{2,3}\s?kg'|
|gtfe_pack_years|Regular expression|'\d+\s+\|pack\-?years)'|
|gtfe_ex_raucher|Regular expression|'[12][9012][0-9][0-9]'|

Table 5: Human baseline evaluation per field

|Cardiac Entity|F1-score in %|
|---|---|
|Hypertonie|98.8|
|Diabetes Mellitus|98.4|
|Niereninsuffizienz|90|
|Zustand nach Myokardinfarkt|95.4|
|Zustand nach Dekompensation|92.7|
|Vorhofflimmern|98.9|
|Herzklappeninsuffizienz|86.9|
|Kardiomyopathie|98.6|
|Koronarer Bypass Operation|100|
|CCM|100|
|Dyslipidämie|98.4|
|Familienanamnese|100|
|Interventionelle koronare Revaskularisation|100|
|Raucher|98.6|
|NYHA|94.4|
|Typ Kardiomyopathie|100|

Table 6a: Multiclass extractions - Raucher
||precision|recall|f1|support|
|---|---|---|---|---|
|Ex|100|98|99|55|
|Ja|100|100|100|18|
|Unbekannt|99|100|99|94|
|macro avg|100|99|100|167|
|weighted avg|99|99|99|167|

Table 6b: Multiclass extractions - NYHA
||precision|recall|f1|support|
|---|---|---|---|---|
|I|98|92|95|66|
|II|98|88|93|69|
|III|81|100|89|25|
|nicht erhoben|50|86|63|7|
|macro avg|82|92|85|167|
|weighted avg|94|92|92|167|

Table 6c: Multiclass extractions - Typ Kardiomyopathie
||precision|recall|f1|support|
|---|---|---|---|---|
|ARVC|100|100|100|2|
|DCM|96|100|98|70|
|HCM|86|95|90|20|
|NCCM|100|80|89|5|
|inflammatorische|100|100|100|1|
|nicht erhoben|100|94|97|69|
|macro avg|97|95|96|167|
|weighted avg|97|96|96|167|

Table 7: Types of Cardiomyopathy
|Abbreviation|Description|
|---|---|
|ARVC|Arrhythmogene rechtsventrikuläre Kardiomyopathie|
|DCM|Dilatative Kardiomyopathie|
|HCM|Hypertrophe Kardiomyopathie|
|NCCM|Non-Compaction-Kardiomyopathie|


Figure 1
![Figure 1](https://github.com/dieterich-lab/Cardiac-Concept-Extraction/blob/master/docx2dpdf.PNG)
