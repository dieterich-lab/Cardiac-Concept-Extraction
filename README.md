# Supplement: CardioAnno – Towards a German Clinical Corpus Containing Cardiovascular Concepts

## 1. Data
### 1.1. Main Corpus
The base corpus used in this project consists of discharge letters from cardiology domain as binary MS-DOC files. Discharge letters (Arztbriefe) vary a lot in scope and structure between different clinical domains. They are supposed to be short and concise. Next to personal data like the patients name, address and birth date, the notes shall contain past and current diagnoses. In addition patients' clinical history and planned clinical examinations are described. If accomplished, results of laboratory and sensoric examinations are as well part of a discharge letter.\footnote{For more information see: https://de.wikipedia.org/wiki/Arztbrief\#cite_note-1 
    
Length of the discharge letters in our data set vary a lot. The letters contain between half a DIN A4 page to four pages. 
    
All documents share a basic structure. Thus, typical for clinical routine text data, they contain a semi-structure. The majority of the discharge letters contain a header containing contact information, a salutation, a clinical section and a summary. The clinical section typically contains a subset of the following subsections: diagnosis, cardiovascular risk factors, allergies, anamnese, physical examination (Körperlicher Untersuchungsbefund), laboratory data, ECG, MRI and recommended therapy/medication.
The amount of text in each subsection is varying. The subsections contain free unstructured text, sometimes tables, rarely images. 
Occasionally subsections are titled differently, but contain similar information, e.g. therapy/medication. Often terms are abbreviated, e.g. CRF/Cardiovascular risk factors. The letters are concluded by a salutation and the names of the physicians involved. Figure 1 shows a dummy discharge letter:
![Example discharge letters.](misc/dummy_discharge.png)


### 1.2. Sampling Method
To obtain representative samples for annotation from our base corpus, we needed to sample a subset of discharge letters. As a probability sampling plan, to avoid too much bias, we chose stratified sampling. We performed the following steps:
* We divided our base corpus into groups of years 2004-2019. Then we randomly selected letters from each group (strata). We sampled 12 documents per strata in 2004-2012 and 24 documents per strata in 2013-2019. We chose to select twice as much documents per strata for the years 2013-2019, to keep the corpus more up-to-date.
* As our sample size is restricted to anamnese and risk factor sections of each discharge letter we obtain two constraints to our stratified sampling plan.
    * 75% of each strata we randomly selected  discharge letters from the 100 largest anamnese sections (with at least 70 token) from that strata, in order to not choose letters containing too short anamnese and risk factor sections. The longest anamnese section is always included.
    * 25% of each strata we randomly selected from letters  where the anamnese (with at least 45 token) contains the key words NYHA and CSS. This constraint is optional, if the key words are not available in a strata, we choose 100% from first constraint.

In total we sampled 204 discharge letters from the corpus. Following our annotation workflow for redundant annotation we split the corpus into a seed corpus (34 letters) for redundant annotation and a main corpus (170 letters). In addition the main corpus was split into a small subset containing 35 documents to annotate redundantly and a larger set of 135 documents for single annotation.
