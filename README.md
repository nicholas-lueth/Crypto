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
I(8) --> O(14) <br>
F(5) --> P(15) <br>
14 mod 26 = (a * 8 + b) mod 26 <br>
15 mod 26 = (a * 5 + b) mod 26 <br>
The easiest way to solve these equations is by subtracting them. <br>
((a * 8 + b) mod 26) - ((a * 5 + b) mod 26)  <br>
25 = a * 3 + 0 <br>
a = 25/3 <br>
a = 25 * 3^-1 <br>
Since now I need to find the modular inverse of 3, I created a program to do the work for me with ModularInverse.py. With the program we get the modular inverse of 9. <br>
a = (25 * 9) mod 26 = 17 <br>
We can now solve for b in one of our previous equations. <br>
14 mod 26 = (17 * 8 + b) mod 26 <br>
14 - 17 * 8 mod 26 = b = 8 <br>
a = 17 <br>
b = 8 <br>
If we plug these values into the python script I made for decoding affine ciphers (AffineCipher.py) then we get the following message: <br>
"IF YOU LEAVE THE FIVE LETTERS AT THE END OF THIS MESSAGE AS DIGITS THEY GIVE YOU A NUMBER YOU WILL NEED LATER ON BGDDH" <br>
And the number we will need later on is 16337

## Problem 4: (SDES) You wake up to an annoying flashing light outside your window. Paying attention to the rhythm of the flashes, you figure out that it is repeating the message: 10010011 <br>After you write it down, a new pattern begins: 001011011001 <br>8-bit and 12-bit blocks... sounds like an SDES message and its key! Decrypt the message.
Since I'm on a time crunch I'm going to unfortunatley skip this question, but I think this would be a really cool cipher to try and decode and implement in python. I used another persons program to get the following, so I should not recieve credit for this question. I don't even necessarily know if the information is right.<br>
First key: 00101101<br>
Second key: 11110010<br>
IP: 00011101<br>
Fk: 01111101<br>
SW: 11010111<br>
Fk: 10110111<br>
IP^-1: 11101011<br>

## Problem 5: (Vigenere) Another paper airplane, another mysterious message. Identify the source of this message for one bonus point. Hint: the fourth character of the keyword has already been sent to you...
```
EGDHV CGROR MEYDC WMELW MPSIF XVJPV XIPLW JZDXQ SDACI OPPAC KKEIY TWILZ KQZRX YWGQQ PROXB FSLDS JHHFF TJHGR MHMWL VJTED WMWGG OMKLA MEYJA CMVWR 
LPVBX ZETIQ HGJPK WMTSA TBRFF TIWEC DQMIS IWIPH IMWCQ QKDJK MUPFU RIUIU TJBOM KLAMD FFMIP LWFKI MQWZT AMEYJ ACMVW RFSUR VVGKM ULZKL QIINS HQQGY 
SGOHS WZXAE VFLWM UMEDP EWLVK WWSAR KHUDP CSCLV SNSHB KIYGJ AHMKO PARRV GUBKS JWVZL QPTGQ FOYGJ AHWNZ XKKIO AHBHH ZFAIU KVIJI QXZLX MVFVX DZHXY 
WTZDS WJTKR RJLGC FXZGC LDAEW SCSSE DDVGS ELWMV LFHLI VEJIJ IUISG MWIEG DPKHA ZLWBK IWJDV WKCSO MGMEK BIOPG SCMVM ELWMG EPLXU HXYWS WRVIW BILRV 
VRTRW VVXVW LVWKM QMEYX BVXFG SLLWT JTMWP PTJBV YJHXK LSLKA GDNRJ IPHAZ FSWZG FFIIL RVVEP RXFYG ISLJG UURVV GGTHW JMCLU IJKTL GEEUX VJKZJ AAQSE 
VTAFV ZHIXD GBSVM VMEOG ISTVJ HTLOV HPBHR KETLL GZFTA FPFKT LBICD DESEG WGMQZ VDDXH WMWGG IPZEH GDRUE PZNIU LLWDR UKXFL RYWPD BFCSR SIMXM GMVEW 
WLVXQ SWGAR JRFRQ HRKXG MQGYU DULGG MQTLG RLXWQ WYMCO DGIGH ADWKJ XVJEJ AUBRH IQPLL RXQQT XITZX VDFFO AIFEJ CTBRJ SDPKN AFGSJ RXKDT ARJDS GSLRX 
ACSDR UJJJE IIKII PTJSU MZFFG ZAZMK ZIQWP VKWQQ XZFVI WMDHG WSVZW IGDJV OPXSE IWCBO CFDSK RTZWH WISSK RCUIE WLASE GWGAE EUDNX UMELT LZMKZ IQWPV 
KAQNI KZTBR VTZIP HKFFV ZRYJA COWMK DTADR ULWMW AFYPA MIKKX VVMUW IPHTR FTAZI IWPTZ EPKIC URVVA WZIZL WMUJF JTKRR FENAV EBWDZ ISILW MVEBW DNWLV 
UJAWS DWGAW LVKTK XWKGB MUWNW GMHMK ZTZYI IQNWX RXETV ZLFZJ VJESG JBWLV OXVGS NXDZD XZETJ HJFJT AOMGH XVJME KJLGI EDNWU QVFDN DQFJT UDXLJ TIJIS 
MITRS BACOJ IEWGI OPPSH QIXYW NEHVV FDBLR WMCLV WFETW IXYSI TDWKC XVGLR VIPHG FDAIU WFXIP HMIGK MUGFS IAWYI FTLUM XZICS XFLWM LVDGJ AWETZ TADRU 
LGIFI JGUUX HFFIP HFFLI WPSWL WMLVE WIPHV XSGUH RKKLP LGYZP LWLVS EXHEI SCKHS WTTQQ KDMRP ZSIFP VGRFL KMUCM SACDF CWPVG XYWAM JWZFH QGIKZ TUGMU 
FDBDW RYTVH VRDGC OIJWT URJDM RPDGT GJVWI ZLWMU AZLWB KIZJW IQHJH ACQKV VSMHT ZFIPH WZVTX RGBWI ARJKZ TQUGF SIAWL VQSWG KVVXV VMUWL IBWFF TAKSL 
DSMUJ ZJHBD WZXPN UEZVI WVXRJ IBKIS WATJS ZFVBK ISWAT KYEYD VWLVV DWUFP ETIQW FXPKX VMWSZ LFSGC WIWKW TTZEJ VXNIM TMABW STAGK XQMWC BLXNS HPRTV 
DTAVP PUGIF OVVQC WSWSC MYIEA CODXK ZTAOM XZIMV XGJDD RGRLX WQMKU AIWXV JTLEI YACLW LVUJA WSDWG ELXYA BXXHV FIDLV LDTVF IXXXX
```
I don't know what the fourth character is, but I can still figure this out. I started by using the index of coincidence to try and identify the key length. What that sentence does tell us is that the keyword is 4 charcters or longer. <br>
