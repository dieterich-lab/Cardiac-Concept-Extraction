    # Rules for extracting Smoker information from German Discharge Letters. 
    # JA (smoker), EX (ex-smoker), NA (no information available) 
    
    @labeling_function()
    def lf1(sample):
        if not "bis" in sample.Text.lower() and not re.search(r"z\s\s?n", sample.Text.lower()) and \
            not re.search(r"ex\s\s?", sample.Text.lower()) and not "früher" in sample.Text.lower() and \
            not "ehemalig" in sample.Text.lower() and not "karent" in sample.Text.lower() and \
            not "krent" in sample.Text.lower() and not "sistiert" in sample.Text.lower():
            if "aktiver" in sample.Text.lower() and "nikotin" in sample.Text.lower():
                return JA
            elif "fortgeführter" in sample.Text.lower() and "nikotin" in sample.Text.lower():
                return JA
            elif "fortgesetzter" in sample.Text.lower() and "nikotin" in sample.Text.lower():
                return JA
            elif "gelegentlicher" in sample.Text.lower() and "nikotin" in sample.Text.lower():
                return JA
            elif "stattgehabter" in sample.Text.lower() and "nikotin" in sample.Text.lower():
                return JA
            elif "anhaltend" in sample.Text.lower() and "nikotin" in sample.Text.lower():
                return JA
            elif "zigarette" in sample.Text.lower():
                return JA
            else:
                return ABSTAIN
        else:
            return ABSTAIN
    
    @labeling_function()
    def lf2(sample):
        if "nikotin" in sample.Text.lower() and not "bis" in sample.Text.lower() and \
            not re.search(r"z\s\s?n", sample.Text.lower()) and \
            not re.search(r"ex\s\s?", sample.Text.lower()) and not "früher" in sample.Text.lower() and \
            not "ehemalig" in sample.Text.lower() and not "karent" in sample.Text.lower() and \
            not "krent" in sample.Text.lower() and not "sistiert" in sample.Text.lower():
            return JA
        elif "raucher" in sample.Text.lower() and not "bis" in sample.Text.lower() and \
            not re.search(r"z\s\s?n", sample.Text.lower()) and \
            not re.search(r"ex\s\s?", sample.Text.lower()) and not "früher" in sample.Text.lower() and \
            not "ehemalig" in sample.Text.lower() and not "karent" in sample.Text.lower() and \
            not "krent" in sample.Text.lower() and not "sistiert" in sample.Text.lower():
            return JA
        else:
            return ABSTAIN

    @labeling_function()
    def lf3(sample):
        if  "p y" in sample.Text.lower() and re.search(r"z\s\s?n", sample.Text.lower()):
            return EX
        elif "%dpy" in sample.Text.lower() and re.search(r"z\|?\s?n", sample.Text.lower()):
            return EX
        elif "packyears" in sample.Text.lower() and re.search(r"z\s\s?n", sample.Text.lower()):
            return EX
        elif re.search(r"z\s\s?n", sample.Text.lower()) and "nikotin" in sample.Text.lower():
            return EX
        elif re.search(r"ex\s\s?", sample.Text.lower()) and "nikotin" in sample.Text.lower():
            return EX
        elif re.search(r"ex\s\s?", sample.Text.lower()) and "raucher" in sample.Text.lower():
            return EX
        elif "früher" in sample.Text.lower() and "nikotin" in sample.Text.lower():
            return EX
        elif "ehemalig" in sample.Text.lower() and "nikotin" in sample.Text.lower():
            return EX
        elif "karent" in sample.Text.lower() and "nikotin" in sample.Text.lower():
            return EX
        elif "krent" in sample.Text.lower() and "nikotin" in sample.Text.lower():
            return EX
        elif "sistiert" in sample.Text.lower() and "nikotin" in sample.Text.lower():
            return EX
        elif "bis" in sample.Text.lower() and "nikotin" in sample.Text.lower():
            return EX
        else:
            return ABSTAIN

    @labeling_function()
    def lf4(sample):
        if re.search(r"nikotin[a-z]+\s\s?nie", sample.Text.lower()):
            return NA
        elif re.search(r"nikotin[a-z]+\s\s?wird\sverneint", sample.Text.lower()):
            return NA
        elif "früher" in sample.Text.lower() and "verneint" in sample.Text.lower() and \
            ("raucher" in sample.Text.lower() or "nikotin" in sample.Text.lower()):
            return NA
        elif len(sample.Text.split(" ")) < 5:
            return NA
        elif "kardiovaskuläre risikofaktoren keine bekannt" in sample.Text.lower() or \
            "kardiovaskuläre risikofaktoren keine" in sample.Text.lower()  or "keine bekannt" in sample.Text.lower():
            return NA
        elif not "raucher" in sample.Text.lower() and not "nikotin" in sample.Text.lower():
            return NA
        else:
            return ABSTAIN
