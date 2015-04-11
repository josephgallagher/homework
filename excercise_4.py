p_initial = 307357870

def incidents_per_year(incidents_per_second):
	return float( (incidents_per_second)*60*60*24*365 ) #ie: x(incidents/s)*60(s/min)*60(min/hr)*24(hr/day)*365(day/year) = y(incidents/year)   

#By (1.0/7.0) I mean 1 birth every 7 seconds.
births = incidents_per_year(1.0/7.0)
deaths = incidents_per_year(1.0/13.0)
immigrants = incidents_per_year(1.0/35.0)

def population_after(years):
	p_final = p_initial + years * ( (births)-(deaths)+(immigrants) )
	return "New population in %d years will change by %d to be %d." % (years, p_final - p_initial, p_final)


print population_after(0)
print population_after(1)
print population_after(10)
print population_after(100)

