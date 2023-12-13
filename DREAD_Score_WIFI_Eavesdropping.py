# -----------------------------------#
""" Version 1.0
    13/12:23
    Author:Userhonest

"""

damage_potential = 7
reproducibility = 9
exploitability = 7
affected_users = 6
discoverability = 4

# Calculate the average DREAD score
average_dread_score = (damage_potential + reproducibility + exploitability + affected_users + discoverability) / 5

print ("DREAD Score for WIFI Eavesdropping")
print (average_dread_score)


# end of file # 
