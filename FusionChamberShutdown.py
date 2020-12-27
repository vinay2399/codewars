# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4
def burner(c,h,o):
    # code here
    h2=int(h/2)
    if o>=h2:
        water=h2
        h-=water*2
        o=o-water
    else:
        water=o
        o=0
        h-=water*2
    o2=int(o/2)
    if c<=o2:
        co2=c
        c=0
        o-=co2*2
    else:
        co2=o2
        c-=co2
        o-=co2
    h4=int(h/4)
    if c<=h4:
        methane=c
        c-=methane
        h-=methane*4
    else:
        methane=h4
        c-=methane
        h-=methane*4
    return water,co2,methane
