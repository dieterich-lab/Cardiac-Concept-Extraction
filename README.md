# Supplement: CardioAnno – Towards a German Clinical Corpus Containing Cardiovascular Concepts

## 1. Data
### 1.1. Main Corpus
The base corpus used in this project consists of discharge letters from cardiology domain as binary MS-DOC files. Discharge letters (Arztbriefe) vary a lot in scope and structure between different clinical domains. They are supposed to be short and concise. Next to personal data like the patients name, address and birth date, the notes shall contain past and current diagnoses. In addition patients' clinical history and planned clinical examinations are described. If accomplished, results of laboratory and sensoric examinations are as well part of a discharge letter. For more information see: https://de.wikipedia.org/wiki/Arztbrief\#cite_note-1
    
Length of the discharge letters in our data set vary a lot. The letters contain between half a DIN A4 page to four pages. 
    
All documents share a basic structure. Thus, typical for clinical routine text data, they contain a semi-structure. The majority of the discharge letters contain a header containing contact information, a salutation, a clinical section and a summary. The clinical section typically contains a subset of the following subsections: diagnosis, cardiovascular risk factors, allergies, anamnese, physical examination (Körperlicher Untersuchungsbefund), laboratory data, ECG, MRI and recommended therapy/medication.
The amount of text in each subsection is varying. The subsections contain free unstructured text, sometimes tables, rarely images. 
Occasionally subsections are titled differently, but contain similar information, e.g. therapy/medication. Often terms are abbreviated, e.g. CRF/Cardiovascular risk factors. The letters are concluded by a salutation and the names of the physicians involved. Figure 1 shows a dummy discharge letter:

![Example discharge letters.](misc/dummy_discharge.png)
Figure 1: Example discharge letters.

### 1.2. Sampling Method
To obtain representative samples for annotation from our base corpus, we needed to sample a subset of discharge letters. As a probability sampling plan, to avoid too much bias, we chose stratified sampling. We performed the following steps:
* We divided our base corpus into groups of years 2004-2019. Then we randomly selected letters from each group (strata). We sampled 12 documents per strata in 2004-2012 and 24 documents per strata in 2013-2019. We chose to select twice as much documents per strata for the years 2013-2019, to keep the corpus more up-to-date.
* As our sample size is restricted to anamnese and risk factor sections of each discharge letter we obtain two constraints to our stratified sampling plan.
    * 75% of each strata we randomly selected  discharge letters from the 100 largest anamnese sections (with at least 70 token) from that strata, in order to not choose letters containing too short anamnese and risk factor sections. The longest anamnese section is always included.
    * 25% of each strata we randomly selected from letters  where the anamnese (with at least 45 token) contains the key words NYHA and CSS. This constraint is optional, if the key words are not available in a strata, we choose 100% from first constraint.

In total we sampled 204 discharge letters from the corpus. Following our annotation workflow for redundant annotation we split the corpus into a seed corpus (34 letters) for redundant annotation and a main corpus (170 letters). In addition the main corpus was split into a small subset containing 35 documents to annotate redundantly and a larger set of 135 documents for single annotation.

## 2. Cardiovascular Concepts

Table 1: Cardiovascular Concepts including ICD-10 code (if available) and description. 

| Cardiovascular Concept | ICD-10 | Description |
|--|--|--|
|	Angina Pectoris | I20 | describes a chest pain or preassure. It is graded using the CCS classification. Value range is 1-4, while ranges like "2-3" can be used for annotation. |   
|        Cholesterine/Lipide |  E78.* | This describes all appearances of cholesterols or lipids, mostly expressed as cardiovascular risk factors. It is not graded.    |
|        Diabetes Mellitus    |  E10-14 |  Diabetes Mellitus is a metabolic disorder characterized by high blood sugar level. It is graded with the value range 1-2.    |
|        Dyspnoe    |   R06.0 | Dyspnoe describes a feeling of not being able to breathe sufficiently.It is graded using the NYHA classification. Value range is 1-4, while ranges like "2-3" can be used for annotation.    |
|        Familienanamnese   | None |    Familial anamnesis is a kind of anamnesis, which gives information about specific disease of family members. It is not graded.    |
|        Hypertonie    |  I10.*  | Hypertension describes the disease when blood pressure in the arteries is persistently elevated. It is not graded.    |
|        Nikotinkonsum    | F17.* |  Describes a state of dependence of nicotine. It is graded if the amount of pack years is expressed in the document.     |
|        Nykturie    | R35 | Nocturia describes the need of a patient to wake up in the night to urinate. It is graded if the amount of times, the patient needs to get up in the night is expressed in the document.    |
|        Ödeme    |    R60 | Edema is the swelling of body tissue due to fluid retention. Value range of grading is 1-2.    |
|        Palpitation    |    R00.2 | Palpitation describe the conscious awareness of your own heartbeat. It is not graded.    |
|        Schwindel    |   H81-82  | Vertigo describes the feeling of turning or swaying. It is not graded.    |
|        Synkope    |  R55 | Syncopes describes the sudden loss of consciousness. It is not graded.|

![Distribution of sequence length per concept.](misc/heatmap.png)
Figure 2: Distribution of sequence length per concept.

Table 2: Inter annotator agreement per concept per corpus split including average seed.

|Concept | Seed1 | Seed2 | Seed3 | Avg. Seed | Main35 |
|--|--|--|--|--|--|
|AP|72.1|80.6|93.9|82.2|78|
|Cholesterin|94.1|94.7|100|96.2|95.2|
|Diabetes|100|100|88.9|96.3|96|
|Dyspnoe|92.3|91.7|62.5|81.1|82.5|
|FA|57.1|80|94.7|77.1|95.2|
|Hyp|100|95.7|100|98.5|98.1|
|Nikotin|93.3|92.3|100|95.2|97|
|Nykturie|88.8|90.9|100|93.2|100|
|Oedeme|80|95.2|93.3|89.5|97.6|
|Palpitation|92.3|100|66.7|86.3|84.8|
|Schwindel|83.3|88.8|100|90.7|90|
|Synkope|100|83.3|92.3|91.9|100|

## 3. Inter Annotator Agreement

Table 3: Examples for evaluating entity-wise exact and partial IAA.

|A | B | Exact | Partial | Type
|--|---|--|--|--|
|17,4-17,5 Hyp | = | TP | TP | exact range match |
|17,8 FA | = | TP | TP | exact single match|
|17,12-17,16 FA | X | FN | FN | no annotation in B|
|20,43 Palpitation | X | FN | FN | no annotation in B|
|20,67 Dyspnoe | = | TP | TP | exact single matc|
|20,70 Schwindel | = | TP | TP | exact single matc|
|20,106 Dyspnoe | = | TP | TP | exact single match|
|X | 20,110-20,111 Dyspnoe | FP | FP | no annotation in A|
|20,119-20,120 AP | = | TP | TP | exact range match|
|20,128 Palpitation | = | TP | TP | exact single match|
|20,133 Schwindel | = | TP | TP | exact single match|
|20,141 Synkope | = | TP | TP | exact single match|
|20,162-20,164 Ödeme | 20,162-20,163 Ödeme | FP | TP | range token with partial overlap, same class, same start token|
|21,210 Synkope | 21,210 Hyp | FP | FP | single token match different class|
|21,220-224 Dyspnoe | 21,221-222 Dyspnoe | FP | TP | range token partial overlap, same class, different start and end token|
|21,225-226 FA | 21,225-226 Schwindel | FP | FP | range token exact match different class|
|21,231 Schwindel | 21,230-232 Schwindel | FP | TP | single token vs range token same class|
|21,246-248 Synkope | 21,246 Schwindel | FP | FP | range token vs single token different class | 

Table 3 contains the annotation of annotator A, column two the annotation of annotator B. Column three and four contain the evaluation using IAA entitywise exact and partial match. The last column contains further descriptions.

Entitywise exact match IAA score results in: 

*Precision = tp/fp+tp = 10 / 7 + 10 = 0.59*

*Recall = tp/fn + tp = 10 / 2 + 10 = 0.83*

*F1 = 0.69*

Entitywise partial match IAA score results in: 

*Precision = tp/fp+tp = 12 / 7 + 12 = 0.63*

*Recall = tp/fn + tp = 12 / 2 + 12 = 0.86*

*F1 = 0.73*

