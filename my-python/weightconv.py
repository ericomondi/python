weight = float(input("Weight: "))
unit = input(" (K)kg  , (L)bs: ")
if unit == "k":
    converted = weight / 0.45
    print(" Weight in Kg: " + str(converted))
else:
    converted = weight * 0.45
    print( "Weight in Lb: " + str(converted))
print("Done")

