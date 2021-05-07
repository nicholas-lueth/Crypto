# Mathamatical cryptography Final
## Problem 1: (BONUS) Did you solve the steganographic message hidden throughout our recorded lectures? What was the message and how was it encoded?
No I did not.

## Problem 2: (Shift) You are sitting outside on a park bench, when a paper airplane hits you on the shoulder. You unfold the paper to discover the following mysterious message. Decipher this message, and identify the author. For a bonus point: what is the special characteristic of the source text of this message?
```
nkdtz ymymw tzlmt zyfqq mnxyt wdmfi mfifh mfrun tsytx yfsiz uktwn yytxm tbfit zgyns lbtwq iymfy fhmnq ihfsy mnspf siutx xngqd itnyu wfhyn hfqqd dtzbt zqisy htsxy fsyqd wzsfh
wtxxk tqpxy tifdb mthqf nrymf yfhmn qiits ypstb fsdym nslfh mnqix gwfns xyfwy xkzsh yntsn slfyg nwymf simfx frtsl xynyx rfsdn skfsy htsat qzynt sxymt zxfsi xtkit wrfsy fytrx
nsytb mnhml timfx uzyfr dxynh utxxn gnqny dktws tynhn slfsf izqyx fhyfs iknlz wnslt zynyx uzwut wy
```
For this problem, I created a python script to loop through all 26 possible keys and was able to read through the results to see which one looked like the plaintext. After running CaesarCipher.py I see that there is some recognizable text under key 21:
```
Key (21):
IFYOU THTHR OUGHO UTALL HISTO RYHAD HADAC HAMPI ONTOS TANDU PFORI TTOSH OWADO UBTIN GWORL DTHAT ACHIL 
DCANT HINKA NDPOS SIBLY DOITP RACTI CALLY YOUWO ULDNT CONST ANTLY RUNAC ROSSF OLKST ODAYW HOCLA IMTHA TACHI LDDON TKNOW 
ANYTH INGAC HILDS BRAIN START SFUNC TIONI NGATB IRTHA NDHAS AMONG STITS MANYI NFANT CONVO LUTIO NSTHO USAND SOFDO RMANT 
ATOMS INTOW HICHG ODHAS PUTAM YSTIC POSSI BILIT YFORN OTICI NGANA DULTS ACTAN DFIGU RINGO UTITS PURPO RT
``` 
If I space out this text properly I get the following message: <br>
"IF YOUTH THROUGHOUT ALL HISTORY HAD HAD A CHAMPION TO STAND UP FOR IT TO SHOW A DOUBTING WORLD THAT A CHILD CAN THINK AND POSSIBLY DO IT PRACTICALLY YOU WOULDNT CONSTANTLY RUN ACROSS FOLKS TODAY WHO CLAIM THAT A CHILD DONT KNOW ANYTHING A CHILDS BRAIN STARTS FUNCTIONING AT BIRTH AND HAS AMONGST ITS MANY INFANT CONVOLUTIONS THOUSANDS OF DORMANT ATOMS INTO WHICH GOD HAS PUT A MYSTIC POSSIBILITY FOR NOTICING AN ADULTS ACT AND FIGURING OUT ITS PURPORT" <br>
Which is a quote from the book Gadsby by Ernest Vincent Wright.

## Problem 3: (affine) A few days later, you are sitting at your computer with an open terminal. Suddenly, the cursor starts moving and the following message appears on your screen: "OPAMKNYIBYTXYPOBYNYTTYLCITTXYYVHMPTXOCEYCCIGYICHOGOTCT\\\\XYAGOBYAMKIVKEZYLAMKSONNVYYHNITYLMVZGHHX" <br>Moments later, you receive a Signal message from an untraceable number: the first two letters are "if" Crack the code.
For this problem we are going to need to a little bit of ,ath: first we need to develope 2 equations out of the chatacters that we know. We do this by associating the letters with number equivalents between 0 and 25. So 0 would be equivalent to A. <br>
I(8) -> O(14) <br>
F(5) -> P(15) <br>
