states= {
"staat1":{
    "text": """Er was eens een arme \033[1;32mhouthakker\033[0m die samen met zijn \033[1;35mvrouw\033[0m en zijn twee kinderen, \033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m,
in een klein hutje woonde aan de rand van een \033[1;32mGROOT BOS\033[0m.
Er is bijna geen eten meer, en op een avond zegt \033[1;35mde moeder\033[0m: “We hebben niet genoeg voedsel meer.
We moeten de kinderen meenemen \033[1;32mhet bos\033[0m in en ze daar achterlaten.” \033[1;32mDe vader\033[0m twijfelt, maar is wanhopig.
Hij heeft de keuze om ermee in te stemmen of te weigeren en zelf eten te vinden.""",
    "choices": {
        "instemmen": "staat2",
        "weigeren": "staat3"
               }
    }, 
      
"staat2": {
    "text": """De volgende ochtend nemen de ouders \033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m mee \033[1;32mhet bos\033[0m in.
\033[1;34mHans\033[0m heeft stiekem een paar kleine \033[1;37;43mbroodkruimels\033[0m en \033[1;37;46mwitte steentjes\033[0m in zijn zak gestopt, om de weg terug te vinden.""",
    "choices": {
        "broodkruimels": "staat4",
        "steentjes": "staat5"
               }
    }, 

"staat3": {
    "text": """\033[1;32mDe vader\033[0m weigert eerst zijn kinderen achter te laten.
Hij zoekt dagenlang naar eten, maar vindt niets. De honger wordt erger, en \033[1;35mde moeder\033[0m overtuigt \033[1;32mde vader\033[0m uiteindelijk toch om haar plan uit te voeren.
\033[1;32mDe vader\033[0m wilt dat \033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m thuis blijven of \033[1;32mde vader\033[0m stuur ze \033[1;32mhet bos\033[0m in """,
    "choices": {
        "bos": "staat2",
        "thuis": "staat13"
               }
    },

"staat4": {
    "text": """\033[1;34mHans\033[0m laat onderweg broodkruimels vallen.
Wanneer ze later willen teruglopen, merken ze dat de vogels alle \033[1;37;43mbroodkruimels\033[0m hebben opgegeten.
Ze zijn nu helemaal verdwaald.
\033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m twijfelen om te wachten op hun ouders of om samen door te lopen.""",
    "choices": {
        "wachten": "staat6",
        "lopen": "staat7"
               }
    },

"staat5": {
    "text": """ \033[1;34mHans\033[0m laat glanzende steentjes vallen.
’s Nachts, in het \033[1;37;40mmaanlicht\033[0m, vinden ze zo de weg naar huis terug.
\033[1;35mDe moeder\033[0m is woedend en dwingt ze om de volgende dag opnieuw mee te nemen.
\033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m blijven alsnong thuis of ze gaan en \033[1;34mHans\033[0m gebruikt nu \033[1;37;43m de kleine broodkruimels\033[0m.""",
    "choices": {
        "blijven": "staat13",
        "broodkruimels": "staat4"
               }
    },

"staat6": {
    "text": """Ze wachten tot de nacht voorbij is, maar niemand komt.
Ze krijgen honger en \033[1;37;44mkou\033[0m.
’s Ochtends hebben ze de keuzen om verder \033[1;32mhet bos\033[0m in te gaan of om nog langer te wachten.""",
    "choices": {
        "lopen": "staat7",
        "wachten": "staat6"
               }
    },

"staat7": {
    "text": """Na uren lopen ontdekken \033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m een klein huisje, helemaal van koek en snoep gemaakt.
Het ruikt heerlijk!
Ze twijfelen tussen even rondkijken of om van het huis te eten """,
    "choices": {
        "eten": "staat8",
        "rondkijken": "staat9"
               }
    },

"staat8": {
    "text": """Plots gaat de deur open en er verschijnt een oude vrouw.
Ze lijkt vriendelijk en nodigt de kinderen uit binnen te komen, maar ze is eigenlijk \033[1;37;45meen heks\033[0m.
Ze sluit \033[1;34mHans\033[0m op in een kooi en dwingt \033[1;35mGrietje\033[0m voor haar te zorgen.
\033[1;35mGrietje\033[0m gehoorzaamt, maar wacht op een kans om te ontsnappen of \033[1;35mGrietje\033[0m probeert meteen te vluchten.""",
    "choices": {
        "gehoorzaamt": "staat10",
        "vlucht": "staat11"
               }
    },

"staat9": {
    "text": """\033[1;35mGrietje\033[0m merkt rare sporen rond het huis en zegt tegen \033[1;34mHans\033[0m: “Iets klopt hier niet.”
Ze lopen verder en ontmoeten \033[1;31meen jager\033[0m die hun naar huis wilt brengen.
Ze vertrouwen \033[1;31mde jager\033[0m niet en vluchten of ze gaan met \033[1;31mde jager\033[0m mee.""",
    "choices": {
        "mee": "staat6",
        "vluchten": "staat12"
               }
    },

"staat10": {
    "text": """\033[1;37;45mDe heks\033[0m wil \033[1;34mHans\033[0m roosteren en zegt tegen \033[1;35mGrietje\033[0m: “Kijk eens of de oven heet genoeg is!”
\033[1;35mGrietje\033[0m doet alsof ze niet weet hoe dat moet.
\033[1;35mGrietje\033[0m duwt \033[1;37;45mde heks\033[0m in de oven of \033[1;35mGrietje\033[0m pakt \033[1;37;47mde emmer\033[0m met \033[1;37;44mwater\033[0m en dooft \033[1;37;41mhet vuur\033[0m.""",
    "choices": {
        "duwen": "staat11",
        "doven": "staat14"
               }
    },

"staat11": {
    "text": """\033[1;35mGrietje\033[0m probeert te ontsnappen, maar \033[1;37;45mde heks\033[0m  betrapt haar en sluit haar ook op.
\033[1;35mGrietje\033[0m pakt de sleutels naast het hek en ze ontsnappen of ze doet niks en ze blijven in het hok en worden geroosterd op \033[1;37;41mhet vuur\033[0m.""",
    "choices": {
        "sleutels": "staat14",
        "niks": "staat15"
               }
    },

"staat12": {
    "text": """De jager brengt \033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m veilig terug naar hun \033[1;32mvader\033[0m.
\033[1;35mDe moeder\033[0m is verdwenen, en \033[1;32mde vader\033[0m \033[1;37;44mhuilt\033[0m van blijdschap.
Ze leven nog lang en gelukkig.""",
        "choices": {"opnieuw": "staat1",
                "stoppen": "stop"}
               
    },

"staat13": {
    "text": """\033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m blijven thuis en vinden geen eten.
Ze verhongeren!""",
    "choices": {"opnieuw": "staat1",
                "stoppen": "stop"}
    },


"staat14": {
    "text": """Na de dood van \033[1;37;45mde heks\033[0m vinden \033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m een kist vol \033[1;37;43mgoud\033[0m en \033[1;37;46mjuwelen\033[0m.
Ze keren terug naar huis, waar hun \033[1;32mvader\033[0m hen in \033[1;37;44mtranen\033[0m omhelst.
Vanaf dat moment hebben ze nooit meer honger en leven ze gelukkig samen.""",
    "choices": {"opnieuw": "staat1",
                "stoppen": "stop"}
    },

"staat15": {
    "text": """\033[1;37;45mDe heks\033[0m haalt \033[1;34mHans\033[0m en \033[1;35mGrietje\033[0m uit het hok en ze worden geroosterd op \033[1;37;41mhet vuur\033[0m.""",
     "choices": {"opnieuw": "staat1",
                "stoppen": "stop"}
    }
 
}

def inputcheck (inp, keuzes):
    if inp in keuzes:
        return keuzes[inp], True
    else:
        return None, False
    
def FSM(staat):
    while True:
        print(states[staat]["text"])
        if states[staat]["choices"] == {}:
            return None
        print()
        print("Uw keuzes zijn:")
        correctantwoord = False
        while correctantwoord == False:
            try: 
                for keuze in states[staat]["choices"]:
                    print(keuze)
                invoer = input("Wat is uw keuze?")
                staat, correctantwoord = inputcheck(invoer, states[staat]["choices"])
            except:
                pass
        if staat == "stop":
            return None
                            
FSM("staat1")