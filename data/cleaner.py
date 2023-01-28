import pandas

#####
# Return dataframe of csv file content.
#####
def read_file(file_name):

    data = pandas.read_csv(file_name)
    
    # Change NaN to NULL.
    for key in data:
        data[key].fillna("NULL", inplace=True)
        

    # Drop duplicates.
    data = data.drop_duplicates(subset=['name'], keep=False)
    print(data)
    return data

def add_und(headers):
    headers = headers.replace(" ", "_")
    return headers


def main():
    supers = read_file("csv/original/Supers_OG.csv")
    powers = read_file("csv/original/Powers_OG.csv")

    # Get intersection of dataframes.
    intersection = pandas.merge(supers, powers, how='inner', on=['name'])

    # Manually add headers (I'm lazy)
    print(add_und("super_id,name,gender,eye_color,race,hair_color,height,publisher,alignment,weight,super_id,agility,accelerated healing,lantern power ring,dimensional awareness,cold resistance,durability,stealth,energy absorption,flight,danger sense,underwater breathing,marksmanship,weapons master,power augmentation,animal attributes,longevity,intelligence,super strength,cryokinesis,telepathy,energy armor,energy blasts,duplication,size changing,density control,stamina,astral travel,audio control,dexterity,omnitrix,super speed,possession,animal oriented powers,weapon-based powers,electrokinesis,darkforce manipulation,death touch,teleportation,enhanced senses,telekinesis,energy beams,magic,hyperkinesis,jump,clairvoyance,dimensional travel,power sense,shapeshifting,peak human condition,immortality,camouflage,element control,phasing,astral projection,electrical transport,fire control,projection,summoning,enhanced memory,reflexes,invulnerability,energy constructs,force fields,self-sustenance,anti-gravity,empathy,power nullifier,radiation control,psionic powers,elasticity,substance secretion,elemental transmogrification,technopath/cyberpath,photographic reflexes,seismic power,animation,precognition,mind control,fire resistance,power absorption,enhanced hearing,nova force,insanity,hypnokinesis,animal control,natural armor,intangibility,enhanced sight,molecular manipulation,heat generation,adaptation,gliding,power suit,mind blast,probability manipulation,gravity control,regeneration,light control,echolocation,levitation,toxin and disease control,banish,energy manipulation,heat resistance,natural weapons,time travel,enhanced smell,illusions,thirstokinesis,hair manipulation,illumination,omnipotent,cloaking,changing armor,power cosmic,biokinesis,water control,radiation immunity,vision - telescopic,toxin and disease resistance,spatial awareness,energy resistance,telepathy resistance,molecular combustion,omnilingualism,portal creation,magnetism,mind control resistance,plant control,sonar,sonic scream,time manipulation,enhanced touch,magic resistance,invisibility,sub-mariner,radiation absorption,intuitive aptitude,vision - microscopic,melting,wind control,super breath,wallcrawling,vision - night,vision - infrared,grim reaping,matter absorption,the force,resurrection,terrakinesis,vision - heat,vitakinesis,radar sense,qwardian power ring,weather control,vision - x-ray,vision - thermal,web creation,reality warping,odin force,symbiote costume,speed force,phoenix force,molecular dissipation,vision - cryo,omnipresent,omniscient"))
    
    intersection.to_csv("csv/fixed/test.csv")
main()