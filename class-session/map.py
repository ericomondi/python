blogs = [
    {"id":1, "tittle":"PCI", "descreption":"Start from...", "status": 0},
    {"id":2, "tittle":"ACI", "descreption":"Start from...", "status": 0},
    {"id":3, "tittle":"BCE", "descreption":"Start from...", "status": 1},
    {"id":4, "tittle":"BCG", "descreption":"Start from...", "status": 0},
    {"id":5, "tittle":"TET", "descreption":"Start from...", "status": 1}
]

#  filter in the list only active blogs and change title to title case
# use only maps and comprehension

act_blogs = [ blogs for blogs in blogs if blogs["status"] == 1]



def to_tittle_case(x):
        w= x["tittle"].title()
        x["tittle"] = w

        return x
    

result = list(map(to_tittle_case, act_blogs))
print(result)
  
