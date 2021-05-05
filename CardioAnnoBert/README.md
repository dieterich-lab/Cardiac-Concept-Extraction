# Supplement: CardioAnnoBert - Automatic Extraction of Twelve Cardiovascular Concepts from German Discharge Letters using Pre-trained Language Models

## 1. Data
### 1.1. Main Corpus
The base corpus used in this project consists of discharge letters from cardiology domain as binary MS-DOC files. Discharge letters (Arztbriefe) vary a lot in scope and structure between different clinical domains. They are supposed to be short and concise. Next to personal data like the patients name, address and birth date, the notes shall contain past and current diagnoses. In addition patients' clinical history and planned clinical examinations are described. If accomplished, results of laboratory and sensoric examinations are as well part of a discharge letter. For more information see: https://de.wikipedia.org/wiki/Arztbrief\#cite_note-1
    
Length of the discharge letters in our data set vary a lot. The letters contain between half a DIN A4 page to approximately four pages. 
    
All documents share a basic structure. Thus, typical for clinical routine text data, they contain a semi-structure. The majority of the discharge letters contain a header containing contact information, a salutation, a clinical section and a summary. The clinical section typically contains a subset of the following subsections: diagnosis, cardiovascular risk factors, allergies, anamnese, physical examination (Körperlicher Untersuchungsbefund), laboratory data, ECG, MRI and recommended therapy/medication.
The amount of text in each subsection is varying. The subsections contain free unstructured text, sometimes tables, rarely images. 
Occasionally subsections are titled differently, but contain similar information, e.g. therapy/medication. Often terms are abbreviated, e.g. CRF/Cardiovascular risk factors. The letters are concluded by a salutation and the names of the physicians involved. Figure 1 shows a dummy discharge letter:

![Example discharge letters.](../misc/dummy_discharge.png)
Figure 1: Example discharge letter.

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

## 3. Baseline Classifier

### CRF Classifier

Feature functions CRF:

| Feature | Description | Value | Example token, Value |
|--|--|--|--|
| isLowerCase* | Token is lower-cased | binary | 'pektangiöse', True |
| lastThreeChars | Last three characters of token | string | 'pektangiöse', 'öse' |
| lastTwoChars | Last two characters of token | string | 'pektangiöse', 'se' |
| isUpperCased* | Token is upper-cased | binary | 'pektangiöse', False |
| firstCharCapitalized* | First character is capitalized | binary | 'Angina', True |
| isDigit | Token is integer value | binary | '15', True |
| POSTag* | Part-of-speech-tags generated using SpaCy's *de_core_news_md* model  | Universal POS tags | 'Angina', 'NOUN' |
| POSTagLastTwoCharacters* | Last two characters of POS tag | string | 'Angina', 'UN' |
| EndOfSentence | token is end of sentence | binary | '.', True |
| BeginningOfSentence | token is beginning of sentence | binary | 'Der', True |

*\* Feature is used as well for context token (+1: subsequent token, -1: preceding token)*

Details CRF:

1. Library: sklearn-crfsuite==0.3.6
2. Algorithm: lbfgs
3. Hapyerparameters: c1=0.01, c2=0.5, max_iterations=100, all_possible_transitions=False

### LSTM Classifier

Architecture LSTM classifier:

1. An embedding layer using 850B Glove embeddings with dimension 300.
2. A bidirectional LSTM layer with dimension 128.
3. A 0.25 dropout layer
4. A dense layer with dimension 64
5. A final crf layer

Hyperparamters LSTM classifier:

1. Batchsize: 64
2. Epochs: 30
3. Early stopping after five epoechs on validation loss
4. Validation split 10%
5. maximum sequence length: 512

## 4. Results

### Precision/Recall and F1-score per model per concept

4-fold cross validation per model. Floating point numbers in *support* column due to summing up results of all folds and division by four.

#### CRF
Table 2: 4-foild cross validation of CRF model. Scores per concept.

||precision|recall|f1-score|support|
|--|--|--|--|--|
|AnginaPectoris|0.855|0.5825|0.6875|186.75|
|Hypertonie|0.895|0.8975|0.895|102.5|
|Cholesterin/Lipide|0.9045|0.87|0.885|35.75|
|Dyspnoe|0.8025|0.6224|0.6975|99.5|
|Schwindel|0.95|0.8|0.8674|43.75|
|Synkope|0.965|0.795|0.87|51.5|
|Palpitation|0.9325|0.7025|0.7975|45|
|Familienanamnese|0.92|0.765|0.83|23.5|
|Oedeme|0.865|0.425|0.57|62.75|
|Nikotinkonsum|0.9199|0.7975|0.855|30.25|
|Nykturie|1|0.95|0.9725|19.25|
|DiabetesMellitus|0.8825|0.9025|0.885|37.5|
|micro avg|0.885|0.7025|0.7825|738|
|macro avg|0.9075|0.76|0.8175|738|
|weighted avg|0.8875|0.7025|0.775|738|

#### LSTM
Table 3: 4-foild cross validation of LSTM model. Scores per concept.

||precision|recall|f1-score|support|
|--|--|--|--|--|
|AnginaPectoris|0.87|0.62|0.725|186.75|
|Hypertonie|0.8925|0.9075|0.8975|102.5|
|Cholesterin/Lipide|0.9045|0.85|0.885|35.75|
|Dyspnoe|0.815|0.6525|0.717|99.5|
|Schwindel|0.97|0.795|0.87|43.75|
|Synkope|0.9425|0.7725|0.85|51.5|
|Palpitation|0.865|0.665|0.735|45|
|Familienanamnese|0.85|0.7175|0.765|23.5|
|Oedeme|0.9525|0.6775|0.785|62.75|
|Nikotinkonsum|0.9725|0.7925|0.87|30.25|
|Nykturie|1|0.85|0.9175|19.25|
|DiabetesMellitus|0.9025|0.905|0.8975|37.5|
|micro avg|0.895|0.7275|0.8|738|
|macro avg|0.9125|0.7675|0.825|738|
|weighted avg|0.9|0.7275|0.7975|738|

#### BERTscratch
Table 4: 4-foild cross validation of BERTscratch model. Scores per concept.

| Entity Class | F1-Score | Precision | Recall | Support |
|--|--|--|--|--|
|AnginaPectoris|0.783|0.821|0.762|186.75|
|Cholesterin/Lipide|0.891|0.877|0.909|35.75|
|DiabetesMellitus|0.908|0.900|0.925|37.5|
|Dyspnoe|0.698|0.758|0.653|99.5|
|Familienanamnese|0.798|0.842|0.787|23.5|
|Hypertonie|0.915|0.897|0.934|102.5|
|Nikotinkonsum|0.939|0.944|0.938|30.25|
|Nykturie|0.972|1.000|0.950|19.25|
|Oedeme|0.842|0.878|0.815|62.75|
|Palpitation|0.774|0.769|0.813|45.0|
|Schwindel|0.915|0.935|0.908|43.75|
|Synkope|0.879|0.922|0.848|51.5|
|macro avg|0.860|0.879|0.854|738.0|
|micro avg|0.832|0.852|0.815|738.0|
|weighted avg|0.830|0.860|0.815|738.0|

#### BERTbase
Table 5: 4-foild cross validation of BERTbase model. Scores per concept.

| Entity Class | F1-Score | Precision | Recall | Support |
|--|--|--|--|--|
|AnginaPectoris|0.831|0.847|0.819|186.75|
|Cholesterin/Lipide|0.916|0.892|0.944|35.75|
|DiabetesMellitus|0.893|0.877|0.927|37.5|
|Dyspnoe|0.739|0.746|0.747|99.5|
|Familienanamnese|0.817|0.845|0.819|23.5|
|Hypertonie|0.928|0.916|0.942|102.5|
|Nikotinkonsum|0.916|0.919|0.918|30.25|
|Nykturie|0.972|0.987|0.960|19.25|
|Oedeme|0.910|0.942|0.882|62.75|
|Palpitation|0.792|0.820|0.796|45.0|
|Schwindel|0.952|0.964|0.943|43.75|
|Synkope|0.884|0.928|0.849|51.5|
|macro avg|0.879|0.890|0.879|738.0|
|micro avg|0.861|0.869|0.853|738.0|
|weighted avg|0.860|0.876|0.853|738.0|

#### BERTfine
Table 5: 4-foild cross validation of BERTfine model. Scores per concept.

| Entity Class | F1-Score | Precision | Recall | Support |
|--|--|--|--|--|
|AnginaPectoris|0.819|0.845|0.805|186.75|
|Cholesterin/Lipide|0.909|0.898|0.925|35.75|
|DiabetesMellitus|0.911|0.904|0.929|37.5|
|Dyspnoe|0.740|0.746|0.743|99.5|
|Familienanamnese|0.817|0.825|0.830|23.5|
|Hypertonie|0.925|0.921|0.931|102.5|
|Nikotinkonsum|0.919|0.932|0.907|30.25|
|Nykturie|0.962|0.969|0.960|19.25|
|Oedeme|0.900|0.903|0.899|62.75|
|Palpitation|0.815|0.829|0.816|45.0|
|Schwindel|0.956|0.954|0.961|43.75|
|Synkope|0.895|0.941|0.854|51.5|
|macro avg|0.881|0.889|0.880|738.0|
|micro avg|0.859|0.868|0.851|738.0|
|weighted avg|0.859|0.874|0.851|738.0|

### Precision/Recall Balance

![Example discharge letters.](../misc/prec_rec_balance_CardioBert.PNG)
Figure 2: Balance between precision and recall per concept of the two baseline models and the BERT models. Each data point in the scatter plots represents a cardiovascular concept. Defining the regression line with y = b + ax, an optimal result would be: r2=1, a slope coefficient of a=1 and a bias b=0.

### Significance test

![Example discharge letters.](../misc/sign_tests_CardioBERT.PNG)
Figure 3: Cardiovascular concepts per fold per model achieving p-value>0.5 using F1-score and approximate randomization (Yeh 2000, Pado 2006). E.g. Comparing the models difference of F1-score performance between BERTbase and CRF the concepts *AP*, *Oedeme*, *Palpitation* and *Schwindel* achieve a significance level p-value>0.5 in fold 1.

