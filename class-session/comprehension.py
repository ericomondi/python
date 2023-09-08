blogs = [
    {"id":1, "tittle":"PCI", "descreption":"Start from...", "status": 0},
    {"id":2, "tittle":"ACI", "descreption":"Start from...", "status": 0},
    {"id":3, "tittle":"BCE", "descreption":"Start from...", "status": 1},
    {"id":4, "tittle":"BCG", "descreption":"Start from...", "status": 0},
    {"id":5, "tittle":"TET", "descreption":"Start from...", "status": 1}
]

lsc = [ blogs for blogs in blogs if blogs["status"] == 1]
print(lsc)