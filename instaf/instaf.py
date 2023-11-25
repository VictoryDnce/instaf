import pandas as pd

# data access(followers)------------------------------------------------
file = pd.read_json("followers_1.json")
df = pd.DataFrame(file)

bolunmus2 = []
followers = []

# data seperation and cleaning 
for bolunen in range(0,len(file.index)):
    bolunmus = str(file.loc[bolunen]["string_list_data"])
    bolunmus2 = bolunmus.split()
    followers.append(bolunmus2[3])

for i in range(len(followers)):
    followers[i] = followers[i].strip("',")
    # print(followers[i])

# data access(following)------------------------------------------------
file2 = pd.read_json("following.json")
df2 = pd.DataFrame(file2)

bolunmus4 = []
following = []

# data seperation and cleaning -----------------------------------------
for bolunen in range(0,len(file2.index)):
    bolunmusYeni = str(file2.loc[bolunen]["relationships_following"])
    bolunmus4 = bolunmusYeni.split()
    following.append(bolunmus4[8])


for i in range(len(following)):
    following[i] = following[i].strip("',")
    # print(following[i])   

# comparing------------------------------------------------------------
takipEtmeyen = []
takipEdilmeyen = []

def follow(liste1,liste2,liste3):
    for i in liste1:
        if i in liste2: 
            continue
        else:    
            liste3.append(i)
    return
        
takipci = follow(following,followers,takipEtmeyen)
takibim = follow(followers,following,takipEdilmeyen)
takipci2 = pd.DataFrame(takipEtmeyen,columns = ["Takip Etmeyen"])
takibim2 = pd.DataFrame(takipEdilmeyen, columns=["Takip Etmedigim"])
newList = pd.concat([takibim2,takipci2]).fillna(" X ")
print(newList)
print()
giris = input("Sonuçlar gösterilmiştir.")





