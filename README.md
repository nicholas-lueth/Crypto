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
Since I'm on a time crunch I'm going to unfortunatley skip this question, but I think this would be a really cool cipher to try and decode and implement in python.

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
I don't know what the fourth character is, but I can still figure this out. I started by using the index of coincidence to try and identify the key length. What that sentence does tell us is that the keyword is 4 charcters or longer. I made a, you guess it, a python script to do this for me. It's called Coincidence.py<br>
When I ran the script I found that every 6 characters the coincidence would increase to a little over 6% which is about a 2-3% increase over the others. With this information we can assume the keylength is 6. <br>
The next step is to separate each letter into 6 bins, in this example we would but the first character in the first bin the second character in the second and so on and so forth. Then once we have all of the characters group we will use a freqency analysis to identify what that letter in the key is. I made 2 more python scripts for this. (BinSort.py and FrequencyAnalysis.py) and fed the results from the bin sort to the frequency analysis. I get the following bins: <br>
```
Bin 1:
EGYLFXZAAYKWODFMJWLALEJSFDWWJUTLMKTAFGKSSZLDKKSSGOGWTGZAFILXWJLGWDLHIGDLJSKSLLWWVVWYGJTHKJFFVYGGMKUJVHSOJHEFKDWDWEELKWSMWWFXUMLMGJAQQZOCDGDSAJKSGZKFHWOWDWKWWDLZKZZFADLYKWFWKVLJEWLWUWKGWZQEZGOXEJHKDFJJMAWSWFMESCVDXGSFZLGZLGFLLWSKZSSTMFLSWWFZFYDWMGLLJHVFVWZSQVWFDJXVJWFWYVEXWGWVMAWSDUVSAZZJLUJAUWAFDX

Bin 2:
GRDWXIDCCTQGXSTHTGACPTPATQICKRJAIIACSKLHGXWPWHCHJPUVGJXHAJXDTTGCSDWLJMPWDOBCWXSBRXKXSTJXAISIEGUGCTXATIVGHPTTTDGDGHPLXPRGLGRGDQXCHXUPQXATPSTGCJIUZIWVGIPCSHRLGNTIATIVCTWPXITPIAWTNDWDJGTBGTNTJJXDTTXJNDTTICGHNDCTIXIAIKITIWJTGUIIWIGLPECTRPKAPAHTDTGTRJWWWASITITISXLTSHPIIAVADDTPSCTXAGCHTGQCCTIDXATCJGBITX

Bin 3:
DOCMVPXIKWZQBJJMEGMMVIKTIMPQMIBMPMMMUMQQOAMEWULBAABZQAKBIIMZZKCLCVMIIWKBVMIMMUWITVMBLMBKGPWIPIUTLLVAAXMITBLALEMXGGZWFDSMVAQMUTWOAVBLTVIBKJASSJIMAQQIWGXBKWCAAXLQQBPZOAMAVPATCWMKAZMNAAKMMZWVVBVZJAVLWNUITOIQEBLWTVPIPMALCMAAIUPWMPUPLXKQPVMCVMQUBVCUPVMBICMPXAQAWVIAMBNWBTBTVWIKZWTNBKBPAICMOAMDWILLAEXDVX

Bin 4:
HRWPJLQOKIRQFHHWDOEVBQWBWIHQUUODLQEVRUIQHEUWSDVKHRKLFHKHUQVHDRFDSGVVUIHKWGOVGHRLRWQVLWVLDHZLRSRHUGJQFDVSLHLFBSQHIDNDLBIVXRHQLLQDDJRLXDFRNRRLDEPZZWQWSDSORIUSEUZWNRHRWDWMVHZZUZURVIVWWWXUHYXZJWGDHOJGUDDJRJOIHLVIDGHUHUWUSLWDFXHPLHHLWHHQZGUDGJGGDHORDWUKQQHHRRUWGVBKUDUVKJKKWUQXLIZIWXLRVFWYDOVRQWEWWLXLF

Bin 5:
VMMSPWSPELXPSHGLWMYWXHMRESIKPIMFWWYWVLIGSVMLAPSIMRSQOWIHKXFXSRXASSLEIEAIKMPMEXVRWLMXWPYSNAGRXLVWIEKSVGMTORGPIEZWPRIRRFMEQJRGGGWGWEHRIFEJAXJRRITFMPXMVJECTSIEEMMPIVKYMRAIMTIERIJRESELSLWWMIRLELSXJMMIQQXISIPXVRWXWLGWMGYMXVERIHFSVVRGLESKSRCFXWIMWVIJGIAIHKTWGJGLKMWSJWEXISIYLFWVFWEMSQXTPOSIXMXGMXILSXHVI

Bin 6:
CEEIVJDPIZYRLFRVMKJRZGTFCIMDFUKFFZJRVZNYWFEVRCNYKVJPYNOZVZVYWJZEEEFJSGZWCEGEPYIVVVEFTPJLRZFVFJVJJEZEZBEVVKZFCGVMZUUUYCXWSRKYGRYIKJIXTFJSFKDXUIJFKVZDZVIFZSEGUEKVKTFJKUFKURIPVZFFBIBVDVKNKIXFSVNZFGEEVFLSBEPYVWFYKRFFIFIXFDTUJFFWEXKYVIWDIFMCYZKURRJDTZZZJVZZBKFVVUFLZZZRSZSEVPFMSKJTTMNVPVWEKXGRKVYVDYVLX
```
In the first bin W is most likely = E based on the frequency analysis of the english language. Based on this information the distance between these two letters (22 - 4 = 18) or as a letter "S". If I do this for every bin I get a guess of what the key is. At the end I get:
W(22) = E(4) <br>
22 - 4 = 18 = S <br>
T(19) = E(4) <br>
19 - 4 = 15 = P <br>
M(12) = E(4) <br>
12 - 4 = 8 = I <br>
H(7) = E(4) <br>
7 - 4 = 3 = D <br>
I(8) = E(4) <br>
8 - 4 = 4 = E <br>
V(21) = E(4) <br>
21 - 4 = 17 = R <br>
Key = SPIDER <br>
Using this newly found key we can crack the code and we get the following:
```
MR VERLOC GOING OUT IN THE MORNING LEFT HIS SHOP NOMINALLY IN CHARGE OF HIS BROTHER IN LAW IT COULD BE DONE BECAUSE THERE WAS VERY 
LITTLE BUSINESS AT ANYTIME AND PRACTICALLY NONE AT ALL BEFORE THE EVENING MR VERLOC CARED BUT LITTLE ABOUT HIS OSTENSIBLE BUSINESS 
AND MORE OVER HIS WIFE WAS IN CHARGE OF HIS BROTHER IN LAW THE SHOP WAS SMALL AND SO WAS THE HOUSE IT WAS ONE OF THOSE GRIMY BRICK 
HOUSES WHICH EXISTED IN LARGE QUANTITIES BEFORE THE ERA OF RECONSTRUCTION DAWNED UPON LONDON THE SHOP WAS A SQUARE BOX OF A PLACE 
WITH THE FRONT GLAZED IN SMALL PANES IN THE DAYTIME THE DOOR REMAINED CLOSED IN THE EVENING IT STOOD DISCREETLY BUT SUSPICIOUSLY
AJAR THE WINDOW CONTAINED PHOTOGRAPHS OF MORE OR LESS UNDRESSED DANCING GIRLS NONDESCRIPT PACKAGES IN WRAPPERS LIKE PATENT MEDICINES 
CLOSED YELLOW PAPER ENVELOPES VERY FLIMSY AND MARKED TWO AND SIX IN HEAVY BLACK FIGURES A FEW NUMBERS OF ANCIENT FRENCH COMIC 
PUBLICATIONS HUNG ACROSS A STRING AS IF TO DRY A DINGY BLUE CHINA BOWL A CASKET OF BLACK WOOD BOTTLES OF MARKING INK AND RUBBER
STAMPS A FEW BOOKS WITH TITLES HINTING AT IMPROPRIETY A FEW APPARENTLY OLD COPIES OF OBSCURE NEWSPAPERS BADLY PRINTED WITH TITLES LIKE
THE TORCH THE GONG ROUSING TITLES AND THE TWO GAS JETS INSIDE THE PANES WERE ALWAYS TURNED LOW EITHER FOR ECONOMYS SAKE OR FOR THE
SAKE OF THE CUSTOMERS THESE CUSTOMERS WERE EITHER VERY YOUNG MEN WHO HUNG ABOUT THE WINDOW FOR A TIME BEFORE SLIPPING IN SUDDENLY OR
MEN OF A MORE MATURE AGE BUT LOOKING GENERALLY AS IF THEY WERE NOT IN FUNDS SOME OF THAT LAST KIND HAD THE COLLARS OF THEIR OVERCOATS
TURNED RIGHT UP TO THEIR MOUSTACHES AND TRACES OF MUD ON THE BOTTOM OF THEIR NETHER GARMENTS WHICH HAD THE APPEARANCE OF BEING MUCH 
WORN AND NOT VERY VALUABLE AND THE LEGS INSIDE THEM DID NOT AS A GENERAL RULE SEEM OF MUCH ACCOUNT EITHER WITH THEIR HANDS PLUNGED
DEEP IN THE SIDE POCKETS OF THEIR COATS THEY DODGED IN SIDEWAYS ONE SHOULDER FIRST AS IF AFRAID TO START THE BELL GOING THE BELL HUNG
ON THE DOOR BY MEANS OF A CURVED RIBBON OF STEEL WAS DIFFICULT TO CIRCUMVENT IT WAS HOPELESSLY CRACKED BUT OF AN EVENING AT THE
SLIGHTEST PROVOCATION IT CLATTERED BEHIND THE CUSTOMER WITH IMPUDENT VIRULENCE GFIP
```
This the first few paragraphs in the book "The Secret Agent a Simple Tale - Joseph Conrad"

## Problem 6: (Substitution) One morning, your radio starts reading a string of random letters. You jot them down (it takes quite a while) and begin to decrypt. For a bonus point, identify the secret message hidden in the permutation itself. For another bonus point, identify the source of this text.
```
RCXQN AIXPC FQFEF IKFJX RMJMQ RMTSQ QCXPX NPXQX KRQFK MIAMS QKMWA MSQFK AJFGV CALCX UXPYM KXCFQ RXKQR MLPSQ CSKIX PTMMR FHFAK QRRCA QQSJJ FPYUX PIALR
RCXME QXPUX PQXRQ RCXEX FQRQA KISQR PYARQ RFGXK RFQFV XFUXP ARQVA GAKXQ QAKRC XLCFQ XARQR PFHAL KSNRA FGQFK IMRCX PLCFP FLRXP AQRAL QMTHP XFRAK RXPXQ
RYXQR CXQNA IXPAQ VXGGV MPRCQ RSIYA KHFNF PRTPM JFKYQ LAXKR ATALP XFQMK QESRQ CXAQQ FAIRM EXNMA QMKMS QFKIR CFRAQ CXPLP AJXFK IRCXN PAJFP YLFSQ XMTRC
XPXNS HKFKL XVCXP XVARC QCXAK QNAPX QSQNM AQMKM SQAFH PXXAT EYRCF RVXSK IXPQR FKIRC FRRCX FKAJF GAQFP JXIVA RCRVM TFKHQ VCALC LFSQX RCXAJ JXIAF RXIXF
RCMTR CXGAR RGXUA LRAJQ VCALC ARLFR LCXQE SRRCX PXAQF VAIXI ATTXP XKLXE XRVXX KDAGG AKHFJ AIHXF KICFP JAKHF JFKCM VXUXP AJJXI AFRXA KARQX TTXLR QSNMK
RCXAK QXLRX KRFKH GXIAK RCXTF RFGVX ERCXQ NAIXP QNMAQ MKAQK MRQXP AMSQT MPSQF KILFS QXQGX QQAKL MKUXK AXKLX RCFKF HKFRE ARXRC FRFRG XFQRA QVCFR VXLFK
QFTXG YQFYF QPXHF PIQRC XHPXF RJFBM PARYM TRCXQ NAIXP QMTMS PPXHA MKQKX UXPRC XGXQQ FTXVF PXRME XTXFP XIFKI TMPXJ MQRFJ MKHRC XQXAQ RCXJF GJAHK FRRXR
CXRXP PMPMT RCXLM PQALF KNXFQ FKRPY ACFUX QXXKC XPQXR RGXAK RCXTS PPMVQ GFYMS RCXPV XEFKI PSQCE MGIGY FRAKQ XLRQG FPHXP RCFKC XPQXG TACFU XFIJA PXICX
PHFPE MTEGF LDUXG UXRQN XLDGX IVARC LFPJA KXPXI FEMUX FGGAC FUXCX FPIJM QRIAQ OSAXR AKHQR MPAXQ RMGIF EMSRC XPFPM SKIFB FLLAM FKIEM KATFL AMCXP EARXA
QPXNS RXIUX PYIFK HXPMS QQMJX RAJXQ JMPRF GRCXL MSKRP YJFKI XLGFP XQRCA QTMPF TFLRF KIRCX IMLRM PIMXQ KMRFG VFYQI FPXIX KYARA KRCXK XAHCE MSPCM MIMTN
SBFSI KMRTF PTPMJ FUAHK MKRCX CFPUX QRXPQ QNXFD VARCI PXFIM TRCXP AIAMK GSHSE PXTAP QRMEQ XPUXI EYGXM KISTM SPAKR CXLFR FGMKA FKJMS KRFAK QFLLM PIAKH
RMRCX JCXPE ARXVM SGIGX FIRMQ XPAMS QFLLA IXKRQ RCXAR FGAFK QCFUX EXQRM VXIFE FIPXN SRFRA MKMKR CXRFP FKRSG FVCMN PMISL XQLMK USGQA MKQFK ITPXK ZAXII
FKLXQ AKRCX NXPQM KQRSK HEYCX PRMLM NXVAR CRFPF KRAQJ RCXKF JXHAU XKRMR CXIAQ XFQXR CFRTM GGMVQ MKRCX EARXM TRCXA RFGAF KQNAI XPYMS JSQRC FUXPX LMSPQ
XRMJS QALRC XMKGY XTTAL FLAMS QPXJX IYQMR CXYRX GGSQQ NXLAF GRSKX QCFUX EXXKK MRXIR CMQXO SALDX QRRMF TTMPI PXGAX TRCXP XAQJX IALFG LCMPX MHPFN CYJXI
ALFGJ SQALF KICFU XVXKM RRCXR FPXKR XGGFF GAUXG YFKIK AJEGX IFKLX EXOSX FRCXI RMSQN XPCFN QEYRC XCXFG AKHFP RMTRC XLFGF EPAFK NXFQF KRJSQ RVXRF DXRCX
QXOSX XPRCA KHQQX PAMSQ GYMPG FSHCF RRCXJ TPMJR CXGAR RGXRC FRACF UXQXX KACXQ ARFRX RMNPM KMSKL XFKMN AKAMK KMRCA KHRXG GQSQR CFRRC XEARX MTRCX RFPFK
RSGFJ FYKMR NPMUM DXAKV XFDFK IUXPY AJNPX QQAMK FEGXN XMNGX FKXPU MSQIA QMPIX PVCAL CJSQA LVAGG PXGAX UXKMR CAKHR XGGQS QRCFR FNPMT SQXNX PQNAP FRAMK
PXQSG RAKHT PMJFU XPYXK XPHXR ALIFK LXAQK MRGAD XGYRM IAJAK AQCRC XIAQL MJTMP REYIA JAKAQ CAKHR CXLFS QXMTR CXFAG JXKRQ MTFPT PMJGF SHCAK HAPXT GXLRF
KIXKO SAPXV CXKRC XLFGF EPAFK NXFQF KRRFG DQRMJ XMTCA QRFPF KRSGF RCXNS BFSIP XFNXP MTCAQ RCXPA IAMKG SHSEP XRCXL MPQAL FKCSQ EFKIJ FKMTC AQJFG JAHKF
RRXRC MQXQN AIXPQ JAHCR XFQAG YIXQX PUXFR GXFQR NFPRG YRCXA PRXPP AEGXP XNSRF RAMK
```
This one is acutally relatively easy to solve. All we need to do is do a frequency analysis with the script that we used for the last problem and compare the analysis to the English Language frequency analysis. <br>
  488 <br>
X 320 <br>
R 238 <br>
F 215 <br>
A 189 <br>
Q 184 <br>
K 159 <br>
P 156 <br>
M 154 <br>
C 140 <br>
I 89 <br>
G 87 <br>
S 80 <br>
L 71 <br>
J 59 <br>
T 55 <br> 
N 44 <br>
H 41 <br>
E 40 <br>
V 35 <br>
Y 35 <br>
U 32 <br>
D 10 <br>
O 5 <br> 
B 4 <br>
W 1 <br>
Z 1 <br>
Eventually after a while of trial and error, comparing this text's analysis to the english language I get the key of "IZHKBALGDMNCOPJRSTUFVWXEYQ". This key gives us the following plaintext when plugged into my substitution cipher decryption script in python (Substitution.py)
```
THE SPIDER HAS A BAD NAME TO MOST OF US SHE REPRESENTS AN ODIOUS NOXIOUS ANIMAL WHICH EVERY ONE HASTENS TO CRUSH UNDER FOOT AGAINST THIS 
SUMMARY VERDICT THE OBSERVER SETS THE BEASTS INDUSTRY ITS TALENT AS A WEAVER ITS WILINESS IN THE CHASE ITS TRAGIC NUPTIALS AND OTHER 
CHARACTERISTICS OF GREAT INTEREST YES THE SPIDER IS WELL WORTH STUDYING APART FROM ANY SCIENTIFIC REASONS BUT SHE IS SAID TO BE POISONOUS 
AND THAT IS HER CRIME AND THE PRIMARY CAUSE OF THE REPUGNANCE WHEREWITH SHE INSPIRES US POISONOUS I AGREE IF BY THAT WE UNDERSTAND THAT 
THE ANIMAL IS ARMED WITH TWO FANGS WHICH CAUSE THE IMMEDIATE DEATH OF THE LITTLE VICTIMS WHICH IT CATCHES BUT THERE IS A WIDE DIFFERENCE 
BETWEEN KILLING A MIDGE AND HARMING A MAN HOWEVER IMMEDIATE IN ITS EFFECTS UPON THE INSECT ENTANGLED IN THE FATAL WEB THE SPIDERS POISON 
IS NOT SERIOUS FOR US AND CAUSES LESS INCONVENIENCE THAN A GNATBITE THAT AT LEAST IS WHAT WE CAN SAFELY SAY AS REGARDS THE GREAT MAJORITY 
OF THE SPIDERS OF OUR REGIONS NEVERTHELESS A FEW ARE TO BE FEARED AND FOREMOST AMONG THESE IS THE MALMIGNATTE THE TERROR OF THE CORSICAN 
PEASANTRY I HAVE SEEN HER SETTLE IN THE FURROWS LAY OUT HER WEB AND RUSH BOLDLY AT INSECTS LARGER THAN HERSELF I HAVE ADMIRED HER GARB OF 
BLACK VELVET SPECKLED WITH CARMINERED ABOVE ALL I HAVE HEARD MOST DISQUIETING STORIES TOLD ABOUT HER AROUND AJACCIO AND BONIFACIO HER BITE 
IS REPUTED VERY DANGEROUS SOMETIMES MORTAL THE COUNTRYMAN DECLARES THIS FOR A FACT AND THE DOCTOR DOES NOT ALWAYS DARE DENY IT IN THE 
NEIGHBOURHOOD OF PUJAUD NOT FAR FROM AVIGNON THE HARVESTERS SPEAK WITH DREAD OF THERIDION LUGUBRE 1 FIRST OBSERVED BY LEON DUFOUR IN THE 
CATALONIAN MOUNTAINS ACCORDING TO THEM HER BITE WOULD LEAD TO SERIOUS ACCIDENTS THE ITALIANS HAVE BESTOWED A BAD REPUTATION ON THE 
TARANTULA WHO PRODUCES CONVULSIONS AND FRENZIED DANCES IN THE PERSON STUNG BY HER TO COPE WITH TARANTISM THE NAME GIVEN TO THE DISEASE 
THAT FOLLOWS ON THE BITE OF THE ITALIAN SPIDER YOU MUST HAVE RECOURSE TO MUSIC THE ONLY EFFICACIOUS REMEDY SO THEY TELL US SPECIAL TUNES 
HAVE BEEN NOTED THOSE QUICKEST TO AFFORD RELIEF THERE IS MEDICAL CHOREOGRAPHY MEDICAL MUSIC AND HAVE WE NOT THE TARENTELLA A LIVELY AND 
NIMBLE DANCE BEQUEATHED TO US PERHAPS BY THE HEALING ART OF THE CALABRIAN PEASANT MUST WE TAKE THESE QUEER THINGS SERIOUSLY OR LAUGH AT 
THEM FROM THE LITTLE THAT I HAVE SEEN I HESITATE TO PRONOUNCE AN OPINION NOTHING TELLS US THAT THE BITE OF THE TARANTULA MAY NOT PROVOKE 
IN WEAK AND VERY IMPRESSIONABLE PEOPLE A NERVOUS DISORDER WHICH MUSIC WILL RELIEVE NOTHING TELLS US THAT A PROFUSE PERSPIRATION RESULTING 
FROM A VERY ENERGETIC DANCE IS NOT LIKELY TO DIMINISH THE DISCOMFORT BY DIMINISHING THE CAUSE OF THE AILMENT SO FAR FROM LAUGHING I REFLECT 
AND ENQUIRE WHEN THE CALABRIAN PEASANT TALKS TO ME OF HIS TARANTULA THE PUJAUD REAPER OF HIS THERIDION LUGUBRE THE CORSICAN HUSBANDMAN OF 
HIS MALMIGNATTE THOSE SPIDERS MIGHT EASILY DESERVE AT LEAST PARTLY THEIR TERRIBLE REPUTATION
```
These are the first few paragraphs in the book "The Life of the Spider - J. Henri Fabre"

## problem 7: (RSA) Ages ago, you posted a public key to an anonymous message board, but you've lost the link. Out of the blue, you receive a cryptic, anonymous message <br> R1: 13512408<br> R2: 16662049<br> that you believe was encrypted with that key. You can remember that n =  35808247 = 5981 * 5987, but have forgotten your encryption exponent. Fortunately, it seems that the same person sent you the encryption exponent in one of the earlier clues! Decrypt this message. You should get four numbers (hint: remember we use 8-bit ASCII...)
