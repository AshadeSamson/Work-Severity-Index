# Get RIs for Personal factors
print("Enter the RIs for the following personal factors (1 - 3)")
ri_age = float(input("1: enter the RI for age: \n"))
ri_we = float(input("2: enter the RI for work experience: \n"))
ri_bmi = float(input("3: enter the RI for body mass index: \n"))

# Get RIs for Task factors
print("Enter the RIs for the following task factors (4 - 7)")
ri_wo = float(input("4: enter the RI for weight of object: \n"))
ri_hc = float(input("5: enter the RI for hand coupling: \n"))
ri_wp = float(input("6: enter the RI for work posture: \n"))
ri_dur = float(input("7: enter the RI for duration: \n"))

# Get RIs for environmental factors
print("Enter the RIs for the following environmental factors (8 - 10)")
ri_temp = float(input("8: enter the RI for ambient temperature: \n"))
ri_noise = float(input("9: enter the RI for noise level: \n"))
ri_vib = float(input("10: enter the RI for vibration: \n"))



# Compute the TRIs 
tri_personal = (0.46 * ri_we) + (0.23 * ri_bmi) + (0.32 * ri_age)
tri_task = (0.24 * ri_wo) + (0.39 * ri_hc) + (0.29 * ri_wp) + (0.08 * ri_dur)
tri_env = (0.71 * ri_temp) + (0.23 * ri_noise) + (0.06 * ri_vib)


# TRIs table
d = {
    1: [tri_personal, tri_task, tri_env]
}
print("{:<8}   {:<15}   {:<10}   {:<10}".format("S/N","TRI (personal)","TRI (task)","TRI (environment)"))
for k, v in d.items():
    tri_personal, tri_task, tri_env = v
    print("{:<8}   {:<15.2f}   {:<10.2f}   {:<10.2f}".format(k, tri_personal, tri_task, tri_env))


# Function to calculate the WSI
def calculateWSI(x, y, z):

    wsi = (0.33*x) + (0.38*y) + (0.29*z)
    if(wsi <= 8):
        print("The Work Severity Index (WSI) is {:.2f} and is categorised as Low-Risk".format(wsi))
        return wsi
    elif(wsi >= 9 and wsi <= 15):
        print("The Work Severity Index (WSI) is {:.2f} and is categorised as Medium-Risk".format(wsi))
        return wsi
    else:
        print("The Work Severity Index (WSI) is {:.2f} and is categorised as High-Risk".format(wsi))
        return wsi
    

calculateWSI(tri_personal, tri_task, tri_env)




