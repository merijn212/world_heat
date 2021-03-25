#!/usr/bin/env python
# coding: utf-8

# # Assignment Netwerkanalyse

# ## Notebook made by
# 
# 
# |Naam|Studentnummer|
# |-|-|
# |Merijn van der Leek|12870862 |
# | | |
# | | |
# | | |
# 
# ## Peerreview
# 
# * Vul onderstaande dict/tabel in en run de cel. Klopt het? Zijn jullie het er allemaal mee eens?
#     * Verander `1,2,3,4` door jullie studentnummers
#     * `1: {1:.2,2:.3,3:.3,4:.2}` betekent dat student 1 zijn punt zo over de 4 studenten verdeelt
#     * Let op, per student moeten de punten optellen tot 1!
#     * De gegeven punten staan in de tabel op de rijen, de ontvangen punten in de kolommen.
#     * met `cijfer_per_student` kan je bepalen welk cijfer ieder krijgt bij een gegeven groepscijfer.

# In[3]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

def cijfer_per_student(weging,cijfer=7):
    return round(weging*cijfer,1)

weging= {
        12870862: {12870862:.25,2:.25,3:.25,4:.25},
        2: {12870862:.25,2:.3,3:.3,4:.15},
        3: {12870862:.2,2:.2,3:.4,4:.2},
        4: {12870862:.1,2:.5,3:.2,4:.2}
        }
# verander hier niks aan
df= pd.DataFrame(weging).T
assert all((df.sum(1)==1).values) # per student moeten de gewichten optellen tot 1
df.sum().plot(kind='barh', title='Weging per student');
print("Cijfer per student:\n",cijfer_per_student(df.sum()))
df


# ## Toelichting
# 
# * De meeste opgaven worden automatisch nagekeken. Bij vrijwel alle opdrachten staan er een paar tests onder de opdracht, dit is voornamelijk om te zorgen dat je de juiste type output geeft. Dit zijn dus *NIET* alle tests, die komen er bij het graden nog bij.
# * Elke vraag is 1 punt waard, tenzij anders aangegeven. Soms is die punt onderverdeeld in deelpunten, maar niet altijd. 
# 
# ## Voor het inleveren!
# 
# * Pas niet de cellen aan, vooral niet die je niet kunt editen. Dit levert problemen op bij nakijken. Twijfel je of je per ongeluk iets hebt gewijzigd, kopieer dan bij inleveren je antwoorden naar een nieuw bestand, zodat het niet fout kan gaan.
# 
# * Zorg dat de code goed runt van boven naar beneden, verifieer dat door boven in Kernel -> Restart & Run All uit te voeren
# 
# ## Na het inleveren!
# 
# * Het gebeurt erg vaak dat mensen een "leeg bestand" inleveren. Vaak een andere versie van de opgave die nog ergens op je computer rondslingerde. Zonde van al je werk toch!
# * Dus, lever **minstens een half uur voor tijd in**. Download dan wat je hebt ingeleverd op Canvas. Geef het een andere naam om verwarring te voorkomen. En draai alle cellen, en bekijk het. Geen syntax fouten? Alle vragen gemaakt? Dan zit het vast wel goed, en hoef je niet in de zenuwen te zitten.

# # Linked Data project
# 
# Maak een notebook met een end-to-end project gebaseerd op wikidata, en neem bijvoorbeeld deze als inspiratie:
# * Mooie tutorial van begin tot eind met goede video: <https://media.ed.ac.uk/media/Wikidata+Sparql+Query+Tutorial/1_7v9v6s04> (Vrouwen educated in university of edinburg)
# * Leuke tutorial met notebooks beschikbaar: <https://towardsdatascience.com/where-do-mayors-come-from-querying-wikidata-with-python-and-sparql-91f3c0af22e2>
# * [Deze pagina](https://www.wikidata.org/wiki/Wikidata:WikiProject_every_politician/Netherlands/data/House/All_Members) over Nederlandse politici bevat een mooi begin, waar je nog heel wat moois van kan maken. 
# * Of [deze](https://www.wikidata.org/wiki/Wikidata:WikiProject_Netherlands_Public_Libraries/Branches/By_Organisation) over bibliotheken. Ook hier kan je zowel het spreadsheet veel rijker maken, als natuurlijk op basis daarvan een geweldige interface maken.
#     * Maar er is al een hoop mee gedaan hoor: zie bijvoorbeeld <https://www.wikidata.org/wiki/Wikidata:WikiProject_Netherlands_Public_Libraries/Maps#Country>
# * <https://www.wikidata.org/wiki/Wikidata:WikiProject_COVID-19>
# 
# 
# ## Vereisten
# 
# 1. Leuk probleem, goed uitgewerkt en gemotiveerd. Origineel, maar kan natuurlijk gebaseerd zijn op eerder werk.
#     * Wees heel eerlijk met je inspiratiebronnen, en noem ze, en benoem exact waar jij verder bent gegaan (wat zijn jullie toevoegingen?)
# 2. Het moet gaan over **Nederlandse** data, of data over Nederland. 
#     * Natuurlijk mag er ook een verband met het buitenland zijn.
# 2. Een dataset die je met SPARQL uit wikidata haalt, en die je netjes beschrijft, en aangeeft dat de data "klopt" met jouw probleem.
#     * je dataset moet wel echt wat body hebben: dus flink wat rijen (items), en kolommen (eigenschappen)
#     * je kan je data in spreadsheet formaat of SQL formaat of zelfs JSON formaat opslaan, en er dan later mee verder werken in Python-Pandas, SQL, of direct met python dicts.
# 3. Je laat nu op een aansprekende manier zien hoe jouw data jouw probleem oplost.
#     * Dit kan prima in een jupyter notebook. Het is een **functioneel prototype** voor een mogelijke webapplicatie. 
#     * Je kan [python widgets](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20Basics.html) gebruiken voor interactie met gebruiker
#     * of plotly en dash voor gave interactieve plots en visuals (of seaborn als je het saai statisch wilt houden)
# 4. Schrijf een reflectie.
# 5. Jouw hele "blogpost/tutorial" is een Jupyter notebook die standalone perfect draait. (mits verbonden met het web).
# 6. Je plaatst je notebook op een publiek github adres, of ergens op Google colab. Met gedraaide output. Het is belangrijk dat anderen jouw notebook 
#     * heel makkelijk kunen lezen
#     * heel makkelijk kunnen downloaden, en runnen.
#         * dus als je niet standaard modules gebruikt zet je in een aparte uitgecommentarieerde cel de `pip install commands`
# 7. En levert hem natuurlijk ook weer in via Canvas.
# 
# ### Grading
# 
# * Ook hier weer via peer review binnen je groep.
# * Plus een expert review van je tutor.
# * Maak er wat moois, leerzaams, gaafs, en verrassends van! 

# # Tutorial 
# 
# ## Ons probleem
# Wij willen graag het volgende onderzoeken: Wat zijn de demografische verschillen tussen de verschillende stromingen van de schilderijen in het Rijksmuseum?
# 
# ## Het Rijksmuseum en haar schilderijen
# 
# Het Rijksmuseum in Amsterdam is opgericht op 19 november 1798. De collectie biedt een overzicht van vooral Nederlandse kunst en geschiedenis met onder andere werken van 17e-eeuwse Nederlandse meesters als Rembrandt, Vermeer en Hals. Daarnaast bevat de collectie ook enkele kunst met oorsprongen elders uit de wereld. Het museum is sinds 1885 gevestigd in het Rijksmuseumgebouw dat ontworpen werd door de Nederlandse architect Pierre Cuypers. 
# 
# ![rijksmuseum](https://images.arcadis.com/media/6/6/8/%7B66844D25-A8FF-46FB-BBF6-E5855A6087E3%7DRijksmuseumAmsterdam-main.jpg?width=1920&height=0&mode=crop&anchor=top)
# 
# Het Rijksmuseum beschikt over duizenden kunststukken, gemaakt door vele verschillende kunstenaars en kunstenaressen. Deze kunststukken zijn door de jaren heen verzameld waardoor er een gevarieerde collectie is ontstaan. Het jaar van creatie van ieder stuk en de woonplaats van de kunstenaar zijn beide bekend in de data. Daarom is het interessant om uit te zoeken of de kunsstroming kan worden gekoppeld aan het jaar van creatie en de woonplaats van de kunstenaar. Dit zal met SPARQL worden gedaan.
# 
# 
# ### Wat is SPARQL? 
# 
# SPARQL is een query taal die gebruikt wordt om gegevens op te vragen die zijn opgeslagen als RDF (Resource Description Framework). Dit wordt gedaan door middel van zoekopdrachten (queries), met deze zoektaal is het mogelijk om informatie op te vragen voor applicaties op het semantisch web. Wij gebruiken Wikidata om een gerichte database te zoeken, Wikidata is een centrale opslagruimte waartoe iedereen toegang kan krijgen. De Wikidata-database bestaat voornamelijk uit items, met elk een label, een beschrijving en een of meerdere alternatieve namen.
# 
# Als voorbeeld nemen we bijvoorbeeld het schilderij 'De Nachtwacht' wat bijna iedereen wel kent. 
# 
# ![DeNachtwacht](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/The_Night_Watch_-_HD.jpg/1200px-The_Night_Watch_-_HD.jpg)
# 
# 
# [![Schermafbeelding-2021-03-22-om-22-01-51.png](https://i.postimg.cc/bvL2JrQM/Schermafbeelding-2021-03-22-om-22-01-51.png)](https://postimg.cc/2qb59z9F)
# 
# 
# [![Schermafbeelding-2021-03-22-om-22-07-57.png](https://i.postimg.cc/0yh9Cs9Q/Schermafbeelding-2021-03-22-om-22-07-57.png)](https://postimg.cc/3kCMKz45)
# 
# ### Een voorbeeld
# 
# * Een **item** wordt geidentificeerd door een Q met daaropvolgend een nummer. Bij de nachtwacht is dit *Q219831*, dat is te zien rechts naast de naam. 
# 
# * Vervolgens heb je **statements**. Statements beschrijven gedetailleerde eigenschappen van een item en bestaan uit een eigenschap en een waarde. **Eigenschappen** in Wikidata hebben een P gevolgd door een nummer, zoals bijvoorbeeld bij de Nachtwacht, *movement  P135*
# 
# Voor ons probleem zouden we graag alle schilderijen willen krijgen die in het Rijksmuseum hangen. Met de volgende query laten we zien hoe je die kan opvragen.
# 
# [![Schermafbeelding-2021-03-23-om-22-02-25.png](https://i.postimg.cc/3WQWdDyB/Schermafbeelding-2021-03-23-om-22-02-25.png)](https://postimg.cc/dZnJf3jk)
# 
# * Met SELECT definieer je de variabelen die je wilt verkijgen (voor de variabele moet een vraagteken). 
# 
# * Met WHERE stel je beperkingen, die worden in de vorm van een triple geschreven. Het statement ?painting wdt:P195 wd:Q190804 geeft alle schilderijen die in het Rijksmuseum hangen. Items worden aangeduid met de wd en properties met wdt.
# 
# * Als laatste zie je SERVICE wikibase:label {bd:serviceParam wikibase:language "nl".} staan. Dit is verantwoordelijk voor het ophalen van labels voor de verzamelde items in een extra variabele met Label postfix in de opgegeven taal (in dit geval Nederlands). Bij ons voorbeeld is dat bijvoorbeeld voor ?paintingLabel
# 
# ### Probeer het eens zelf! 
# 
# Maak een query die alleen de schilderijen weergeeft die door een vrouwelijke kunstenaar is gemaakt. Onderaan deze notebook kan je het antwoordt vinden! 

# In[4]:


# Geef hier je antwoordt


# Door middel van verschillende tussenstappen komen we bij ons uiteindelijke probleem. 

# ### Het antwoordt 
# 
# [![Schermafbeelding-2021-03-25-om-12-28-50.png](https://i.postimg.cc/zBRM6W3q/Schermafbeelding-2021-03-25-om-12-28-50.png)](https://postimg.cc/S2kDznWP)

# In[5]:


from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
# From https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Cats
sparql.setQuery("""
SELECT ?paintingLabel ?creatorLabel ?geslachtLabel ?stromingLabel ?geboortejaar ?creatiedatumLabel ?landLabel 
WHERE
{
    ?painting wdt:P195 wd:Q190804 .
    ?painting wdt:P170 ?creator .
    ?creator wdt:P21 ?geslacht .
    ?creator wdt:P135 ?stroming .
    ?creator wdt:P569 ?geboortejaar .
    ?painting wdt:P571 ?creatiedatum .
    ?creator wdt:P27 ?land .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
results_df = pd.io.json.json_normalize(results['results']['bindings'])
results_df.rename(columns = {'paintingLabel.value' : 'Schilderijen', 'creatorLabel.value' : 'Schilders', 
                             'geslachtLabel.value' : 'Geslacht', 'stromingLabel.value' : 'Stroming',
                            'geboortejaar.value' : 'Geboortejaar', 'creatiedatumLabel.value' : 'Creatie Datum',
                            'landLabel.value' : 'Land'}, inplace = True)
print("Dit is de hele collectie van schilderijen die in het Rijksmuseum hangen")
results_df['Geboortejaar'] = results_df['Geboortejaar'].str[:4]
results_df['Creatie Datum'] = results_df['Creatie Datum'].str[:4]

results_df[['Schilderijen', 'Creatie Datum', 'Schilders', 'Geslacht', 'Geboortejaar', 'Stroming', 'Land']].head(100)


# ## Dataset moderniseren
# Helaas zijn de verschillende landen in de dataset wel heel accuraat. Wij hebben handmatig alles gemoderniseerd om hem overeen te laten komen met de moderne landnamen. Hiervoor hebben wij soms wat keuzes moeten maken die historici niet altijd zouden goedkeuren (zo is het _Holy Roman Empire_ nu Duitsland omdat daar het meeste oppervlak zat).

# In[12]:


results_df['Land'] = results_df['Land'].replace(['Austria-Hungary'],'austria')
results_df['Land'] = results_df['Land'].replace(['United States of America'],'United States')
results_df['Land'] = results_df['Land'].replace(['Spanish Netherlands', 'County of Holland','Seventeen Provinces','Habsburg Netherlands', 'Dutch Republic', 'Duchy of Brabant', 'Austrian Netherlands', 'Burgundian Netherlands', 'County of Flanders', 'United Kingdom of the Netherlands','Kingdom of the Netherlands'],'Netherlands')
results_df['Land'] = results_df['Land'].replace(['Duchy of Bavaria','Kingdom of Prussia', 'Holy Roman Empire','German Empire'],'Germany')
results_df['Land'] = results_df['Land'].replace(['Duchy of Brabant', 'West Flanders','Southern Netherlands'],'Belgium')
results_df['Land'] = results_df['Land'].replace(['Duchy of Lorraine', 'Kingdom of France'],'France')
results_df['Land'] = results_df['Land'].replace(['Duchy of Milan', 'Republic of Florence', 'Republic of Genova','Republic of Venice', 'Papal States', 'Lombardy', 'Kingdom of Italy'],'Italy')
results_df['Land'] = results_df['Land'].replace(['Great Britain', 'United Kingdom','United Kingdom of Great Britain and Ireland' ],'England')
results_df['Land'] = results_df['Land'].replace(['Dutch East Indies'],'Indonesia')
results_df['Land'] = results_df['Land'].replace(['Polish–Lithuanian Commonwealth'],'Poland')
results_df['Land'] = results_df['Land'].replace(['Russian Empire'],'Russia')


# ## Stromingen per schilder
# Laten we allereerst kijken naar de meest populaire stroming onder schilders in het rijksmuseum. Uit de grafiek hieronder kunnen we zien dat dit _baroque_ is.

# In[13]:


schilders_per_stroming = results_df.groupby('Stroming')['Schilders'].nunique()
plot = schilders_per_stroming.plot.pie(y='mass', figsize=(32, 32),label='', title= 's', fontsize= 11)


# ## Stromingen per land
# We gaan nu kijken naar welk land de meeste stromingen kent. Dit geven we weer in de tabel hieronder:

# In[14]:


sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
# From https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Cats
sparql.setQuery("""
SELECT ?stromingLabel  ?landLabel
WHERE
{
    ?painting wdt:P195 wd:Q190804 .
    ?painting wdt:P170 ?creator .
    ?creator wdt:P135 ?stroming .
    ?painting wdt:P571 ?creatiedatum .
    ?creator wdt:P27 ?land .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
""")
sparql.setReturnFormat(JSON)
stroming = sparql.query().convert()
stroming_df = pd.io.json.json_normalize(stroming['results']['bindings'])
stroming_df.rename(columns = {
                              'stromingLabel.value' : 'Stroming',
                              'landLabel.value' : 'Land'}, inplace = True)
print("Dit is de hele collectie van schilderijen die in het Rijksmuseum hangen")

stroming_df['Land'] = stroming_df['Land'].replace(['Austria-Hungary'],'austria')
stroming_df['Land'] = stroming_df['Land'].replace(['United States of America'],'United States')
stroming_df['Land'] = stroming_df['Land'].replace(['Spanish Netherlands', 'County of Holland','Seventeen Provinces','Habsburg Netherlands', 'Dutch Republic', 'Duchy of Brabant', 'Austrian Netherlands', 'Burgundian Netherlands', 'County of Flanders', 'United Kingdom of the Netherlands','Kingdom of the Netherlands'],'Netherlands')
stroming_df['Land'] = stroming_df['Land'].replace(['Duchy of Bavaria','Kingdom of Prussia', 'Holy Roman Empire','German Empire'],'Germany')
stroming_df['Land'] = stroming_df['Land'].replace(['Duchy of Brabant', 'West Flanders','Southern Netherlands'],'Belgium')
stroming_df['Land'] = stroming_df['Land'].replace(['Duchy of Lorraine', 'Kingdom of France'],'France')
stroming_df['Land'] = stroming_df['Land'].replace(['Duchy of Milan', 'Republic of Florence', 'Republic of Genova','Republic of Venice', 'Papal States', 'Lombardy', 'Kingdom of Italy'],'Italy')
stroming_df['Land'] = stroming_df['Land'].replace(['Great Britain', 'United Kingdom','United Kingdom of Great Britain and Ireland' ],'England')
stroming_df['Land'] = stroming_df['Land'].replace(['Dutch East Indies'],'Indonesia')
stroming_df['Land'] = stroming_df['Land'].replace(['Polish–Lithuanian Commonwealth'],'Poland')
stroming_df['Land'] = stroming_df['Land'].replace(['Russian Empire'],'Russia')
stromingen_per_land = results_df.groupby('Land')['Stroming'].nunique()
stromingen_per_land = stromingen_per_land.to_frame()
stromingen_per_land['COUNTRY'] = stromingen_per_land.index
stromingen_per_land = stromingen_per_land.rename(columns={"Stroming": "count"})
plot_bar = stromingen_per_land.plot.bar()


# Geen slecht begin en het is zeker duidelijk dat in het rijksmuseum het meeste schilderijen met verschillende stromingen uit Nederland komen. Maar zo'n plot kan natuurlijk een stuk mooier, de mogelijkheden zijn bijna eindeloos. Je kan zelf met de verschillende variabelen knutselen maar er staan ook een aantal goeie templates online. Neem bijvoorbeeld de volgende style gevonden op:<br/>
# https://scentellegher.github.io/visualization/2018/10/10/beautiful-bar-plots-matplotlib.html

# In[17]:


import matplotlib.pyplot as plt
# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'


# we first need a numeric placeholder for the y axis
my_range=list(range(1,len(stromingen_per_land.index)+1))

fig, ax = plt.subplots(figsize=(5,3.5))
plt.hlines(y=my_range, xmin=0, xmax=stromingen_per_land['count'], color='#007acc', alpha=0.2, linewidth=5)

# create for each expense type a dot at the level of the expense percentage value
plt.plot(stromingen_per_land['count'], my_range, "o", markersize=5, color='#007ACC', alpha=0.6)

# set labels
ax.set_xlabel('count', fontsize=15, fontweight='black', color = '#333F4B')
ax.set_ylabel('')

# set axis
ax.tick_params(axis='both', which='major', labelsize=12)
plt.yticks(my_range, stromingen_per_land.index)

# add an horizonal label for the y axis 
fig.text(-0.23, 0.96, 'Transaction Type', fontsize=15, fontweight='black', color = '#333F4B')

# change the style of the axis spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# ## Voorwoord heatmap
# Laten we nu eens een heatmap maken van al onze data. <br/>
# Om te beginnen moeten we een aantal libraries downloaden: Pandas, Geopandas, Matplotlib en Seaborn. Pandas wordt gebruikt om de data in tabellen te krijgen, Geopandas om onze wereld te kunnen lezen en Matplotlib en Seaborn zijn voornamelijk voor de plots zelf.
# Ook wij hebben de komende vaardigheden ergens van moeten leren dus daarom willen wij ook de benodigde credits geven aan de volgende site die alles heel goed uitlegt: 
# https://medium.com/@m_vemuri/create-a-geographic-heat-map-of-the-city-of-toronto-in-python-cd2ae0f8be55

# In[16]:


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Inladen van de geografische data
# Van enorm veel landen en steden zijn shapefiles te vinden. Dit zijn mapjes met een aantal bestand die samen een kaart met berwerkbare data vormen. Om te kunnen laten zien wat voor data dit precies is gebruiken wij geopandas. Geopandas lijkt eigenlijk heel veel op Pandas maar richt zich specifiek op geografische data. Namen van landen kunnen nogal verschillen per dataset en om mogelijke errors te voorkomen halen wij meteen alle hoofdletters uit de namen. De dataset ziet er dan alsvolgt uit:<br />
# **Tip**: zorg er altijd voor dat alle data die je download in dezelfde map zit, anders kan Geopandas het niet inladen.

# In[41]:


nb = 'world_heat/World_Countries.shp'
regions = gpd.read_file(nb)
regions['COUNTRY'] = regions['COUNTRY'].str.lower()
data = stromingen_per_land
data['COUNTRY'] = data['COUNTRY'].str.lower()
regions.sample(10)


# ## Plotten van de kaart
# Laat we eerst even kijken hoe onze wereldkaart er precies uit ziet zonder dat wij daar iets aan toevoegen. Dit kan daar de kaart simpelweg te plotten, het ziet er dan alsvolgt uit:

# In[19]:


regions.plot(figsize=(40,20))
plt.show()


# ## Data samenvoegen
# Het is nu belangrijk dat de twee datasets worden samengevoegd. Gelukkig heeft Pandas hier de functie _join_ voor. Wij moeten dan natuurlijk wel de gemeenschappelijke collumn aangeven waarme we de data gaan samenvoegen, bij ons zijn dit de landen. Maar er zijn natuurlijk genoeg landen die niet in onze dataset zitten maar wel in die van alle landen die counters kunnen we niet zomaar weglaten. Hiervoor vullen we al deze rijen met het getal 0 en vervolgens plotten we de collumen die wij willen. Vijf rijen van de complete dataset zien er dan zo uit:

# In[25]:


merged = regions.set_index('COUNTRY').join(data.set_index('COUNTRY'))
merged = merged.reset_index()
merged = merged.fillna(0)
merged[['COUNTRY', 'geometry', 'count']].sample(5)


# ## De heatmap plotten
# Nu we een complete dataset hebben hoeven we deze eigenlijk alleen nog weer te geven. Dit doen we met de volgende code die er misschien intimiderend uit ziet maar eigenlijk best logisch is. Eerst maken we een simpele plot aan zonder _axis_. Dit zorgt ervoor dat het er niet als een grafiek uitziet wat wij een stuk mooier vinden bij heatmap. Vervolgens geven het plot een titel en kleurenschema. Er zijn tientallen opties voor kleuren zelf hebben wij voor de standaard oranje/rode kleuren gekozen omdat dit het meest typerend is voor een heatmap maar je kan van alles proberen. Nu komt een het ingewikkelde gedeelte, het normaliseren van de data in een kleur. Gelukkig is hier een functie voor die iedere waarde op een schaal zet met een bijbehorende kleur het enige wat jij moet doen is de minimale en maximale waarde van je counter aangeven. Dit kan handmatig maar je het handigste is om de _max_ en _min_ functies van Pandas te gebruiken, zo werken ze op iedere dataset.
# Na het plotten ziet de heatmap er als volgt uit:

# In[26]:


fig, ax = plt.subplots(1, figsize=(40, 20))
ax.axis('off')
ax.set_title('Aantal stromingen per land', fontdict={'fontsize': '40', 'fontweight' : '3'})
color = 'Oranges'
sm = plt.cm.ScalarMappable(cmap=color, norm=plt.Normalize(vmin=merged['count'].min(), vmax=merged['count'].max()))
cbar = fig.colorbar(sm)
cbar.ax.tick_params(labelsize=20)
merged.plot('count', cmap=color, linewidth=0.8, ax=ax, edgecolor='0.8', figsize=(40,20))


# ## Bonus: Namen toevoegen
# Helaas zijn de topografische vaardigheden van mensen nogal verschillend. Het kan dus waardevol zijn om ook de namen van alle landen toe te voegen. Dit doen we door een regel op het einde van de code toe te voegen die de namen van alle landen op de juiste plek zet doormiddel van de geometrische gegevens uit de dataset. Zo kan de code de namen precies in het midden van ieder land zetten. Dit was verbazingwekkend moeilijk om te doen en ik heb daarom de hulp gebruikt van de volgende Stackoverflow thread: <br />
# https://stackoverflow.com/questions/13151514/matplotlib-plot-window-wont-appear <br />
# Hier onder staat het eindresultaat. Het kan op sommige plekken wat moeilijk te lezen zijn omdat er behoorlijk wat kleine landen op een aantal vierkante meter zitten.

# In[30]:


fig, ax = plt.subplots(1, figsize=(40, 20))
ax.axis('off')
ax.set_title('Aantal stromingen per land met namen', fontdict={'fontsize': '40', 'fontweight' : '3'})
color = 'Oranges'
sm = plt.cm.ScalarMappable(cmap=color, norm=plt.Normalize(vmin=merged['count'].min(), vmax=merged['count'].max()))
cbar = fig.colorbar(sm)
cbar.ax.tick_params(labelsize=20)
merged.plot('count', cmap=color, linewidth=0.8, ax=ax, edgecolor='0.8', figsize=(40,20))
merged.apply(lambda x: ax.annotate(s=x.COUNTRY, xy=x.geometry.centroid.coords[0], ha='center'),axis=1);


# In[ ]:




