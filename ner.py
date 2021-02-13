import spacy
from spacy import displacy
import warnings
warnings.filterwarnings("ignore")


def ner_visualize():
    nlp = spacy.load("en_core_web_sm")

    text = """
    so I'm happy to report we have succeeded in rebooting our Flag ships way ahead of schedule yet again
     this is allowed us to improve I use fees by 90%
     that's nine out of every ten excellent thank you Samuel
     Timothy what's the status with a linear Solutions on the Square project Solutions department has yet again functions at full capacity and we have fulfilled 114% of this month's objectives you can read the handouts for a detailed account but in short Hazard reported last week we decided to use the right angle for the square project not the still some debate as to how big of a right angle is soap with testing currently at 9097 100 and 101 degrees as a great adventure Anderson cross-check the design removing any left angles and doesn't use them in future overall we have very good progress with the design are we on track for the schedule when we were required to stop delivering I'm happy to report that we are ready to start first deliveries tomorrow which is way ahead of the requested delivery schedule we've only just finished system testing the Prototype and only halfway through performance testing
     haven't even released an alfa Vision yet as I said I had very good progress with the design exactly that's three out of every four so we're ready to start shipping tomorrow
     BluePrint juice safe for units. Only shut the first three then when you're finally 100% complete with the design week and then ship the full
     excellent book Timothy you can proceed with the production is a revised delivery schedule so I can share it with a client well thank you everyone this was very pretty again
     """

    doc = nlp(text)
    html = displacy.render(doc, style="ent", page=False)

    with open('templates/NERPage.html', 'a') as html_file:
        html_file.write(html)

