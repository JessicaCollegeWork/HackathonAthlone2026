def rbcount():
    outputs = ''
    #red blood cell count per mililitre
    #x10^9 refers to number of red blood cells per 1ml of blood sample taken.
    #This function compares pre-flight data (rbPre) on red blood cells per 1ml of blood to in-flight levels of red blood cells (rbTest) per 1ml of blood.
    rbPre = float(input("Enter your preflight red blood cell count test in x10^9/mL(ex. 4.5): ")) 
    rbTest = float(input("Enter red blood cell count as of last test in x10^9/mL(ex. 4.5): "))
    ceDaily = float(input("Enter daily Carbon Elemination test results (ex. 1800): "))
    if rbTest <= rbPre*0.9:
        outputs = outputs + "Warning: red blood cell count low, Space Anemia possible. Consult your medical officer.\n"
    elif rbTest > rbPre*1.15:
        outputs = outputs +  "Red blood cells exceeding acceptable levels.\n"
    #ceDaily is the data on Carbon Elimination taken from daily breath tests and compares the data to normal levels of Carbon Elimination (1705) within the safe range <54% elevated levels.
    if ceDaily >= 1705+1705*0.54:
        outputs = outputs + "Warning: Carbon Elimination exceeding acceptable levels. Proceed to your medical officer.\n"
    if outputs != '':
        print(outputs)
    else:
        print("Red Blood Cell count is normal\n")
    
def bloodLab(sex):
    outData = ''
    vitALow = 32.5#μg/dL
    vitAUp = 78.0#pg/mL
    vitBLow = 200.0#pg/mL
    vitBUp = 800.0#pg/mL
    vitCLow = 0.4#mg/dL
    vitCUp = 1.5#mg/dL
    #vitamin D
    dihyLow = 15.0#pg/mL
    dihyUp = 60.0#pg/mL
    hydroLow = 30.0#ng/mL
    hydroUp = 60.0#ng/mL
    vitELow = 5.5#mg/L
    vitEUp = 17.0#mg/L
    
    ALTLo = 10#U/L
    ALTHi = 40#U/L
    AlbuLo = 3.5#g/dL
    AlbuHi = 5.5#g/dL
    ALPLo = 30#U/L
    ALPHi = 120#U/L
    AmmoniaLo = 40#μg/dL
    AmmoniaHi = 70#μg/dL
    AmylaseLo = 25#U/L
    AmylaseHi = 125#U/L
    ASTLo = 10#U/L
    ASTHi = 40#U/L
    BiliruDirLo = 0.1#mg/dL
    BiliruDirHi = 0.3#mg/dL
    BiliruTotLo = 0.3#mg/dL
    BiliruTotHi = 1#mg/dL
    BUNLo = 8#mg/dL
    BUNHi = 20#mg/dL
    CalciumIonLo = 1.16#mmol/L
    CalciumIonHi = 1.31#mmol/L
    CalciumTotLo = 8.6#mg/dL
    CalciumTotHi = 10.2#mg/dL
    CO2VenLo = 23#mEq/L
    CO2VenHi = 30#mEq/L
    CILo = 98#mEq/L
    CIHi = 106#mEq/L
    CRPLo = 1#mg/L
    CRPHi = 3#mg/L
    CKLoFem = 30#U/L
    CKHiFem = 135#U/L
    CKLoMasc = 55#U/L
    CKHiMasc = 170#U/L
    SCrLoFem = 0.5#mg/dL
    SCrHiFem = 1.1#mg/dL
    SCrLoMasc = 0.7#mg/dL
    SCrHiMasc = 1.3#mg/dL
    CrClLo = 90#mL/minute/1.73 m^2
    CrCHi = 140#mL/minute/1.73 m^2
    FerrLoFem = 24#ng/mL
    FerrHiFem = 307#ng/mL
    FerrLoMasc = 24#ng/mL
    FerrHiMasc = 336#ng/mL
    γGtpLoFem = 8#U/L
    γGtpHiFem = 40#U/L
    γGtpLoMasc = 9#U/L
    γGtpHiMasc = 50#U/L
    GlucoseLow = 70#mg/dL
    GlucoseUp = 99#mg/dL
    HemoglobinLow = 4#%
    HemologinUp = 5.6#%
    LDHLow = 80#U/L
    LDHUp = 225#U/L
    LipaseLow = 10#U/L
    LipaseUp = 140#U/L
    MagnesiumLow = 1.6#mEq/L
    MagnesiumUp = 2.6#mEq/L
    OsmolatityLow = 275#mOsm/kg
    OsmolatityUp = 295#mOsm/kg
    PhosphorusLow = 3#mg/dL
    PhosphorusUp = 4.5#mg/dL
    PotassiumLow = 3.5#mEq/L
    PotassiumUp = 5.0#mEq/L
    PrealbuminLow = 16#mg/dL
    PrealbuminUp = 30#mg/dL
    SodiumLow = 136#mEq/L
    SodiumUp = 145#mEq/L
    UricAcidLow = 3#mg/dL
    UricAcidUp = 7#mg/dL
    HctFLow = 37#%
    HctFUp = 47#%
    HctMLow = 42#%
    HctMUp = 50#%
    HgbFLow = 12#g/dL
    HgbFUp = 16#g/dL
    HgbMLow = 14#g/dL
    HgbMUp = 18#g/dL
    MCHLow = 28#pg/cell
    MCHUp = 32#pg/cell
    MCHCLow = 33#g/dL
    MCHCUp = 36#g/dL
    MCVLow = 80#fL/cell
    MCVUp = 98#fL/cell
    PTTLow = 25#seconds
    PTTUp = 35#seconds
    PltLow = 0.15#× 10^9cells/mL
    PltUp = 0.45#× 10^9cells/mL
    PTLow = 11#seconds
    PTUp = 13#seconds
    RpRBCLow = 0.5#%
    RpRBCUp = 1.5#%
    WBCLow = 4.0#× 10^6 cells/mL
    WBCUp = 11.0#× 10^6 cells/mL
    Dopamine = 30#pg/mL
    Serotonin = 230#ng/mL
    EstradiolFLow = 10#pg/mL
    EstradiolFUp = 300#pg/mL
    EstradiolMLow = 20#pg/mL
    EstradiolMUp = 50#pg/mL
    ProgesteroneFLow = 0.02#ng/mL
    ProgesteroneFUp = 30#ng/mL
    ProgesteroneMLow = 0.12#ng/mL
    ProgesteroneMUp = 0.3#ng/mL
    TestosteroneFLow = 18#ng/dL
    TestosteroneFUp = 54#ng/dL
    TestosteroneMLow = 291#ng/dL
    TestosteroneMUp = 1100#ng/dL
    ZincLow = 75#μg/dL
    ZincUp = 140#μg/dL

    inALT = float(input("Enter most recent Alanine aminotransferase test results (ex. 27.5): "))
    inAlbu = float(input("Enter most recent Albuim test results (ex. 4.25): "))
    ALP = float(input("Enter most recent Alkaline phosphatase test results (ex. 75): "))
    inAmmonia = float(input("Enter most recent Ammonia test results (ex. 55): "))
    inAmylase = float(input("Enter most recent Amylase test results (ex. 85): "))
    inAST = float(input("Enter most recent Aspartate aminotransferase test results (ex. 30): "))
    inBiliruDir = float(input("Enter most recent Bilirubin Direct test results (ex. 0.2): "))
    inBiliruTot = float(input("Enter most recent Bilirubin Total test results (ex. 0.65): "))
    inBUN = float(input("Enter most recent Blood urea nitrogen test results (ex. 14): "))
    inCalciumIon = float(input("Enter most recent Calcium Ionized test results (ex. 1.2): "))
    inCalciumTot = float(input("Enter most recent Calcium Total test results (ex. 9.1): "))
    inCO2Ven = float(input("Enter most recent Carbon Dioxide (venous) test results (ex. 25.5): "))
    inCl = float(input("Enter most recent Chloride test results (ex. 100): "))
    inCRP = float(input("Enter most recent C-reactive protein test results (ex. 2.0): "))
    inCK = float(input("Enter most recent Creatinine kinase test results (ex. 100): "))
    inSCr = float(input("Enter most recent Creatinine (serum) test results (ex. 0.90): "))
    inCrCl = float(input("Enter most recent Creatinine (clearence) test results (ex. 115): "))
    inFerr = float(input("Enter most recent Ferritin test results (ex. 164): "))
    inγGtp = float(input("Enter most recent γ-Glutamyl transpeptidase test results (ex. 35): "))
    inGlucose = float(input("Enter most recent Glucose (serum) test results (ex. 84): "))
    inHemoglobin = float(input("Enter most recent Hemoglobin A1C percent test results (ex. 150): "))
    inLDH = float(input("Enter most recent Lactate dehydrogenase test results (ex. 140): "))
    inLipase = float(input("Enter most recent Lipase test results (ex. 80): "))
    inMagnesium = float(input("Enter most recent Magnesium test results (ex. 2.1): "))
    inOsmolatity = float(input("Enter most recent Osmolality test results (ex. 280): "))
    inPhosphorus = float(input("Enter most recent Phosphorus test results (ex. 3.75): "))
    inPotassium = float(input("Enter most recent Potassium test results (ex. 4.25): "))
    inPrealbumin = float(input("Enter most recent Prealbumin test results (ex. 23): "))
    inSodium = float(input("Enter most recent Sodium test results (ex. 140): "))
    inUricAcid = float(input("Enter most recent Uric acid test results (ex. 5): "))
    inHct = float(input("Enter most recent Hematocrit test results (ex. 42): "))
    inHgb = float(input("Enter most recent Hemoglobin test results (ex. 14): "))
    inMCH = float(input("Enter most recent Mean corpuscular hemoglobin test results (ex. 30): "))
    inMCHC = float(input("Enter most recent Mean corpuscular hemoglobin concentration test results (ex. 34): "))
    inMCV = float(input("Enter most recent Mean corpuscular volume test results (ex. 86): "))
    inPTT = float(input("Enter most recent Partial thromboplastin time test results (ex. 30): "))
    inPlt = float(input("Enter most recent Platelet count test results (ex. 0.3): "))
    inPT = float(input("Enter most recent Prothrombin time test results (ex. 12): "))
    inRpRBC = float(input("Enter most recent Reticulocyte percent of red blood cells test results (ex. 1): "))
    inWBC = float(input("Enter most recent White blood cell count test results (ex. 7): "))
    inDopamine = float(input("Enter most recent Dopamine test results (ex. <30): "))
    inSerotonin = float(input("Enter most recent Serotonin test results (ex. <230): "))
    inEstradiol = float(input("Enter most recent Estradiol test results (ex. Women ~150, Men ~35): "))
    inProgesterone = float(input("Enter most recent Progesterone test results (ex. Women ~15, Men ~0.2): "))
    inTestosterone = float(input("Enter most recent Testosterone test results (ex. Women ~35, Men ~500): "))
    inZinc = float(input("Enter most recent Zinc test results (ex. 100): "))
    
    
    inVitA = float(input("Enter most recent Vitamin A test results(ex. 52.3): "))
    inVitB = float(input("Enter most recent Vitamin B test results(ex. 500): "))
    inVitC = float(input("Enter most recent Vitamin C test results(ex. 1.1): "))
    inDihy = float(input("Enter most recent Vitamin D Dihydroxyvitamin test results(ex. 4.5): "))
    inHydro = float(input("Enter most recent Vitamin D Hydroxyvitamin test results(ex. 45): "))
    inVitE = float(input("Enter most recent Vitamin E test results(ex. 11.5): "))
    
    if inVitA < vitALow:
        outData = outData + 'Vitamin A Levels low.\n'
    elif inVitA > vitAUp:
        outData = outData + 'Vitamin A Levels high.\n'
    if inVitB < vitBLow:
        outData = outData + 'Vitamin B Levels low.\n'
    elif inVitB > vitBUp:
        outData = outData + 'Vitamin B Levels high.\n'
    if inVitC < vitCLow:
        outData = outData + 'Vitamin C Levels low.\n'
    elif inVitC > vitCUp:
        outData = outData + 'Vitamin C Levels high.\n'
    if inDihy < dihyLow:
        outData = outData + 'Vitamin Vitamin D Dihydroxyvitamin Levels low.\n'
    elif inDihy > dihyUp:
        outData = outData + 'Vitamin Vitamin D Dihydroxyvitamin Levels high.\n'
    if inHydro <  hydroLow:
        outData = outData + 'Vitamin Vitamin D Hydroxyvitamin Levels low.\n'
    elif inHydro >  hydroUp:
        outData = outData + 'Vitamin Vitamin D Hydroxyvitamin Levels high.\n'
    if inVitE < vitELow:
        outData = outData + 'Vitamin E Levels low.\n'
    elif inVitE < vitEUp:
        outData = outData + 'Vitamin E Levels high.\n'
    if inALT < ALTLo:
        outData = outData + 'Alanine aminotransferase (ALT) Levels low.\n'
    elif inALT > ALTHi:
        outData = outData + 'Alanine aminotransferase (ALT) Levels high.\n'        
    if inAlbu < AlbuLo:
        outData = outData + 'Albumin Levels low.\n'
    elif inAlbu > AlbuHi:
        outData = outData + 'Albumin Levels high.\n'        
    if ALP < ALPLo:
        outData = outData + 'Alkaline phosphatase (ALP) Levels low.\n'
    elif ALP > ALPHi:
        outData = outData + 'Alkaline phosphatase (ALP) Levels high.\n'        
    if inAmmonia < AmmoniaLo:
        outData = outData + 'Ammonia Levels low.\n'
    elif inAmmonia > AmmoniaHi:
        outData = outData + 'Ammonia Levels high.\n'
    if inAmylase < AmylaseLo:
        outData = outData + 'Amylase Levels low.\n'
    elif inAmylase > AmylaseHi:
        outData = outData + 'Amylase Levels high.\n'       
    if inAST < ASTLo:
        outData = outData + 'Aspartate aminotransferase (AST) Levels low.\n'
    elif inAST > ASTHi:
        outData = outData + 'Aspartate aminotransferase (AST) Levels high.\n'       
    if inBiliruDir < BiliruDirLo:
        outData = outData + 'Bilirubin, direct Levels low.\n'
    elif inBiliruDir > BiliruDirHi:
        outData = outData + 'Bilirubin, direct Levels high.\n'
    if inBiliruTot < BiliruTotLo:
        outData = outData + 'Bilirubin, total Levels low.\n'
    elif inBiliruTot > BiliruTotHi:
        outData = outData + 'Bilirubin, total Levels high.\n'
    if inBUN < BUNLo:
        outData = outData + 'Blood urea nitrogen (BUN) Levels low.\n'
    elif inBUN > BUNHi:
        outData = outData + 'Blood urea nitrogen (BUN) Levels high.\n'        
    if inCalciumIon < CalciumIonLo:
        outData = outData + 'Calcium, ionized Levels low.\n'
    elif inCalciumIon > CalciumIonHi:
        outData = outData + 'Calcium, ionized Levels high.\n'
    if inCalciumTot < CalciumTotLo:
        outData = outData + 'Calcium, total serum Levels low.\n'
    elif inCalciumTot > CalciumTotHi:
        outData = outData + 'Calcium, total serum Levels high.\n'
    if inCO2Ven < CO2VenLo:
        outData = outData + 'Carbon dioxide (venous) (CO2) Levels low.\n'
    elif inCO2Ven > CO2VenHi:
        outData = outData + 'Carbon dioxide (venous) (CO2) Levels high.\n'
    if inCl < CILo:
        outData = outData + 'Chloride (Cl) Levels low.\n'
    elif inCl > CIHi:
        outData = outData + 'Chloride (Cl) Levels high.\n'
    if inCRP < CRPLo:
        outData = outData + 'C-reactive protein (CRP) Levels low.\n'
    elif inCRP > CRPHi:
        outData = outData + 'C-reactive protein (CRP) Levels high.\n'
    if inCrCl < CrClLo:
        outData = outData + 'Creatinine (clearance) (CrCl) Levels low.\n'
    elif inCrCl > CrCHi:
        outData = outData + 'Creatinine (clearance) (CrCl) Levels high.\n'             
    if inGlucose < GlucoseLow:
        outData = outData + 'Glucose, serum Levels low.\n'
    elif inGlucose > GlucoseUp:
        outData = outData + 'Glucose, serum Levels high.\n'
    if inHemoglobin < HemoglobinLow:
        outData = outData + 'Hemoglobin A1C percent of total hemoglobin Levels low.\n'
    elif inHemoglobin > HemologinUp:
        outData = outData + 'Hemoglobin A1C percent of total hemoglobin Levels high.\n'
    if inLDH < LDHLow:
        outData = outData + 'Lactate dehydrogenase (LDH) Levels low.\n'
    elif inLDH > LDHUp:
        outData = outData + 'Lactate dehydrogenase (LDH) Levels high.\n'
    if inLipase < LipaseLow:
        outData = outData + 'Lipase Levels low.\n'
    elif inLipase > LipaseUp:
        outData = outData + 'Lipase Levels high.\n'
    if inMagnesium < MagnesiumLow:
        outData = outData + 'Magnesium Levels low.\n'
    elif inMagnesium > MagnesiumUp:
        outData = outData + 'Magnesium Levels high.\n'        
    if inOsmolatity < OsmolatityLow:
        outData = outData + 'Osmolality, serum Levels low.\n'
    elif inOsmolatity > OsmolatityUp:
        outData = outData + 'Osmolality, serum Levels high.\n'        
    if inPhosphorus < PhosphorusLow:
        outData = outData + 'Phosphorus Levels low.\n'
    elif inPhosphorus > PhosphorusUp:
        outData = outData + 'Phosphorus Levels high.\n'
    if inPotassium < PotassiumLow:
        outData = outData + 'Potassium Levels low.\n'
    elif inPotassium > PotassiumUp:
        outData = outData + 'Potassium Levels high.\n'
    if inPrealbumin < PrealbuminLow:
        outData = outData + 'Prealbumin Levels low.\n'
    elif inPrealbumin > PrealbuminUp:
        outData = outData + 'Prealbumin Levels high.\n'        
    if inSodium < SodiumLow:
        outData = outData + 'Sodium Levels low.\n'
    elif inSodium > SodiumUp:
        outData = outData + 'Sodium Levels high.\n'        
    if inUricAcid < UricAcidLow:
        outData = outData + 'Uric acid, serum Levels low.\n'
    elif inUricAcid > UricAcidUp:
        outData = outData + 'Uric acid, serum Levels high.\n'            
    if inMCH < MCHLow:
        outData = outData + 'Mean corpuscular hemoglobin (MCH) Levels low.\n'
    elif inMCH > MCHUp:
        outData = outData + 'Mean corpuscular hemoglobin (MCH) Levels high.\n'        
    if inMCHC < MCHCLow:
        outData = outData + 'Mean corpuscular hemoglobin concentration (MCHC) Levels low.\n'
    elif inMCHC > MCHCUp:
        outData = outData + 'Mean corpuscular hemoglobin concentration (MCHC) Levels high.\n'        
    if inMCV < MCVLow:
        outData = outData + 'Mean corpuscular volume (MCV) Levels low.\n'
    elif inMCV > MCVUp:
        outData = outData + 'Mean corpuscular volume (MCV) Levels high.\n'
    if inPTT < PTTLow:
        outData = outData + 'Partial thromboplastin time (PTT) Levels low.\n'
    elif inPTT > PTTUp:
        outData = outData + 'Partial thromboplastin time (PTT) Levels high.\n'        
    if inPlt < PltLow:
        outData = outData + 'Platelet count (Plt) Levels low.\n'
    elif inPlt > PltUp:
        outData = outData + 'Platelet count (Plt) Levels high.\n'        
    if inPT < PTLow:
        outData = outData + 'Prothrombin time (PT) Levels low.\n'
    elif inPT > PTUp:
        outData = outData + 'Prothrombin time (PT) Levels high.\n'        
    if inRpRBC < RpRBCLow:
        outData = outData + 'Reticulocyte percent of red blood cells Levels low.\n'
    elif inRpRBC > RpRBCUp:
        outData = outData + 'Reticulocyte percent of red blood cells Levels high.\n'        
    if inWBC < WBCLow:
        outData = outData + 'White blood cell count (WBC) Levels low.\n'
    elif inWBC > WBCUp:
        outData = outData + 'White blood cell count (WBC) Levels high.\n'        
    if inDopamine > Dopamine:
        outData = outData + 'Dopamine Levels high.\n'
    if inSerotonin > Serotonin:
        outData = outData + 'Serotonin Levels high.\n'   
    if inZinc < ZincLow:
        outData = outData + 'Zinc Levels low.\n'
    elif inZinc > ZincUp:
        outData = outData + 'Zinc Levels high.\n'
    if sex == 'f':
        if inProgesterone < ProgesteroneFLow:
            outData = outData + 'Progesterone Levels low.\n'
        elif inProgesterone > ProgesteroneFUp:
            outData = outData + 'Progesterone Levels high.\n'               
        if inTestosterone < TestosteroneFLow:
            outData = outData + 'Testosterone Levels low.\n'
        elif inTestosterone > TestosteroneFUp:
            outData = outData + 'Testosterone Levels high.\n'
        if inEstradiol < EstradiolFLow:
            outData = outData + 'Estradiol Levels low.\n'
        elif inEstradiol > EstradiolFUp:
            outData = outData + 'Estradiol Levels high.\n'   
        if inHct < HctFLow:
            outData = outData + 'Hematocrit (Hct) Levels low.\n'
        elif inHct > HctFUp:
            outData = outData + 'Hematocrit (Hct) Levels high.\n'
        if inHgb < HgbFLow:
            outData = outData + 'Hemoglobin (Hgb) Levels low.\n'
        elif inHgb > HgbFUp:
            outData = outData + 'Hemoglobin (Hgb) Levels high.\n'
        if inCK < CKLoFem:
            outData = outData + 'Creatinine kinase (CK) Levels low.\n'
        elif inCK > CKHiFem:
            outData = outData + 'Creatinine kinase (CK) Levels high.\n'
        if inSCr < SCrLoFem:
            outData = outData + 'Creatinine, serum (SCr) Levels low.\n'
        elif inVitC > SCrHiFem:
            outData = outData + 'Creatinine, serum (SCr) Levels high.\n'
        if inFerr < FerrLoFem:
            outData = outData + 'Ferritin Levels low.\n'
        elif inFerr > FerrHiFem:
            outData = outData + 'Ferritin Levels high.\n'
        if inγGtp < γGtpLoFem:
            outData = outData + 'γ-Glutamyl transpeptidase Levels low.\n'
        elif inγGtp > γGtpHiFem:
            outData = outData + 'γ-Glutamyl transpeptidase Levels high.\n'

    if sex == 'm':
        if inProgesterone < ProgesteroneMLow:
                outData = outData + 'Progesterone Levels low.\n'
        elif inProgesterone > ProgesteroneMUp:
                outData = outData + 'Progesterone Levels high.\n' 
        if inTestosterone < TestosteroneMLow:
            outData = outData + 'Testosterone Levels low.\n'
        elif inTestosterone > TestosteroneMUp:
            outData = outData + 'Testosterone Levels high.\n'
        if inEstradiol < EstradiolMLow:
            outData = outData + 'Estradiol Levels low.\n'
        elif inEstradiol > EstradiolMUp:
            outData = outData + 'Estradiol Levels high.\n'
        if inHct < HctMLow:
            outData = outData + 'Hematocrit (Hct) Levels low.\n'
        elif inHct > HctMUp:
            outData = outData + 'Hematocrit (Hct) Levels high.\n'
        if inHgb < HgbMLow:
            outData = outData + 'Hemoglobin (Hgb) Levels low.\n'
        elif inHgb > HgbMUp:
            outData = outData + 'Hemoglobin (Hgb) Levels high.\n'
        if inSCr < SCrLoMasc:
            outData = outData + 'Creatinine, serum (SCr) Levels low.\n'
        elif inVitC > SCrHiMasc:
            outData = outData + 'Creatinine, serum (SCr) Levels high.\n'
        if inCK < CKLoMasc:
            outData = outData + 'Creatinine kinase (CK) Levels low.\n'
        elif inCK > CKHiMasc:
            outData = outData + 'Creatinine kinase (CK) Levels high.\n'
        if inFerr < FerrLoMasc:
            outData = outData + 'Ferritin Levels low.\n'
        elif inFerr > FerrHiMasc:
            outData = outData + 'Ferritin Levels high.\n' 
        if inγGtp < γGtpLoMasc:
            outData = outData + 'γ-Glutamyl transpeptidase Levels low.\n'
        elif inγGtp > γGtpHiMasc:
            outData = outData + 'γ-Glutamyl transpeptidase Levels high.\n'
    if outData != '':
        print(outData)
    else:
        print("Blood Lab is clear\n")
    
def radExpo(inSpace):
    outputs = ''
    rLNuke =  55#microsieverts per day
    rLGCRpl = 0.9#milisieverts
    rLGCRsp = 1.3#milisieverts
    nukeExpo = float(input("What has been your daily exposre to Nuclear Technology Radiation in microsieverts(ex. 30): "))
    gcrExpo = float(input("What has been your daily exposre to Galactic Cosmic Radiation in millisiverts(ex. 0.9): "))
    if nukeExpo > rLNuke:
        outputs = outputs + 'Nuclear technology radiation exposer exceedes recommended safe levels\n'
    if inSpace == True:
        if gcrExpo > rLGCRsp:
            outputs = outputs + 'Galactic Cosmic Radiation exposer exceedes recommended safe levels\n'
    elif inSpace == False:
         if gcrExpo > rLGCRpl:
             outputs = outputs + 'Galactic Cosmic Radiation exposer exceedes recommended safe levels\n'
    if outputs != '':
        print(outputs)
    else:
        print("Radiation Levels are within safe levels\n")
        
def boneDens(months):
    outputs = ''
    avgBoneDensLow = 1892.0#g/cm^2
    avgBoneDensUp = 3844.0#g/cm^2
    bdTest = float(input("Enter bone density in float value from most recent test(ex. 2500): "))
    if months >= 6:
        denseLoss = 0.10
        if bdTest < avgBoneDensLow - avgBoneDensLow*denseLoss:
            outputs = outputs + 'Bone Density is below expected range\n'
        elif bdTest > avgBoneDensUp - avgBoneDensUp*denseLoss:
            outputs = outputs + 'Bone Density is above expected range\n'
    elif months <6:
        denseLoss = 0
        for x in range(months):
            denseLoss += 0.015
        if bdTest < avgBoneDensLow - avgBoneDensLow*denseLoss:
            outputs = outputs + 'Bone Density is below expected range\n'
        elif bdTest > avgBoneDensUp - avgBoneDensUp*denseLoss:
            outputs = outputs + 'Bone Density is above expected range\n'
    if outputs != '':
        print(outputs)
    else:
        print("Bone density is within expected range\n")
    
def vision():
    outputs = ''
    print("The following questions will be used to determin the likely hood of vision impairment(SANS)")
    tempAns1 = input("Have you had swelling in your optic nerve(y/n): ")
    tempAns2 = input("Have you observed folding in your retina(y/n): ")
    tempAns3 = input("Have been feeling pressure/stress in the back of the eye(y/n): ")
    tempAns4 = input("Do you feel pressure/stress/swelling in the brain(y/n): ")
    
    if tempAns1 == 'y' or tempAns2 == 'y' or tempAns3 == 'y' or tempAns4 == 'y':
        outputs = outputs + 'Speak to crew medical officer about risk of SANS\n'
    if outputs != '':
        print(outputs)
    else:
        print("All questions clear you are not currently at risk of SANS.")
        
def muscleAtrophy():
    outputs = ''
    preWeight = float(input("Enter pre-flight body weight(ex. 75kg: "))
    deadLift = float(input("Enter current dead lift capability: "))
    benchPress = float(input("Enter current bench press capability: "))
    print("\n")
    exer1 = input("Have you used your daily advanced resistive exercise device(ARED) weight lifting system(y/n): ")
    exer2 = input("Have you used your daily second gen treadmill(T2)(y/n): ")
    exer3 = input("Have you used your cycle erometer with vibration, isolation and stabilisation system(CEVIS) cycling machine(y/n): ")
    
    if exer1 != 'y' or exer2 != 'y'  or exer3 != 'y':
        exercisesDone = False 
    else:
        exercisesDone = True
    if deadLift < 0.8*1.6*preWeight:
        outputs = outputs + 'Risk of muscle atrophy as dead lift capability is less than 80% of preflight weight\n'
        check = True
    if benchPress < 0.8*preWeight:
        outputs = outputs + 'Risk of muscle atrophy as bench press capability is less than 80% of preflight weight\n'
        check = True
    if check == True:
        if exercisesDone == False:
            outputs = outputs + 'Muscle atrophy risk may be due to lack of exercise equipment use\n'
    if outputs != '':
        print(outputs)
    else:
        print("You are not currently at risk of muscle atrophy")    
    
def main():
    run = True
    print("Welcome to health monitor system\nFirst need you to answer some basic information")
    sex = input("Enter sex: ")
    days = int(input("Enter total days on mission: "))
    months = int(input("Enter total months on mission: "))
    tempAns = int(input("Are you on Planet Surface(1) or in free Space(2): "))
    if tempAns == 1:
        inSpace = False
    if tempAns == 2:
        inSpace = True
    while run == True:
        print("\nPlease select what test/system you would like to run")
        print("1. Vision Questionnaire\n2. Red Blood Cell count\n3. Bone Density\n4. Blood Lab\n5. Muscle Atrophy test\n6. Radiation Exposure\n")
        select = int(input("Select option(1-6) 0r enter 0 to exit: "))
        print("")
        if select == 1:
            vision()
        elif select == 2:
            rbcount()
        elif select == 3:
            boneDens(months)
        elif select == 4:
            bloodLab(sex)
        elif select == 5:
            muscleAtrophy()
        elif select == 6:
            radExpo(inSpace)
        elif select == 0:
            run = False
        else:
            print("Invalid input please select 1-6 or 0 to exit")
    print("Thank You for using the health monitor")

if __name__ == '__main__':
    main()
