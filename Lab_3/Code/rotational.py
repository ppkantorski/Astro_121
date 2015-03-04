import numpy as np
import ephem

def main():
	# LST and RA, DEC Test Values
	obs = ephem.Observer()
	obs.lat = ephem.degrees(37.8732*np.pi/180)
	obs.long = ephem.degrees(-122.2573*np.pi/180)
	obs.date = ephem.now()
	LST = float(obs.sidereal_time())
	LAT = float(obs.lat)

	#RA_sun = rl.sunPos()[0]* np.pi/12
	#DEC_sun = rl.sunPos()[1]* np.pi/12

	sun = ephem.Sun()
        sun.compute(obs)

	RA_sun = float(sun.ra)
	DEC_sun = float(sun.dec)


	i = True
	while i == True:

		RA = float(input("Please input RA: "))
		DEC = float(input("Please input DEC: "))

		print(str(RA)+', '+str(DEC))

		rdtoaa(RA, DEC)
		
		go = raw_input("Again? (y/n): ")
		while go != 'y' and go != 'Y' and go != 'N' and go != 'n': 
			go = raw_input("Please enter (y/n): ")

		if go == 'Y' or go == 'y':
			i = True
			print('\n')

		elif go == 'N' or go == 'n':
			i = False
			print('\n')

	print("Test Values for Sun...")
	print("RA: ")
	print sun.ra, float(sun.ra)
	print("DEC: ")
	print sun.dec, float(sun.dec)
	print("AZ: ")
	print sun.az, float(sun.az)
        print("ALT: ")
	print sun.alt, float(sun.alt)


def rect(long_, lat):
# Converting angles to rectangular coordinates.
	x = np.array([0.,0,0])
	x[0] = np.cos(lat) * np.cos(long_)
	x[1] = np.cos(lat) * np.sin(long_)
	x[2] = np.sin(lat)
	return x

def sphere(xp):
	longp = np.arctan2(xp[1], xp[0])
	latp = np.arcsin(xp[2])
	if longp < 0:
		longp = longp + 2*np.pi
	return [longp, latp]


def rdtoaa(ra, dec):

	obs = ephem.Observer()
	obs.lat = ephem.degrees(37.8732*np.pi/180)
	obs.long = ephem.degrees(-122.2573*np.pi/180)
	obs.date = ephem.now()
	LST = float(obs.sidereal_time())
	LAT = float(obs.lat)


	R_rdtohd = np.array([
		[np.cos(LST), np.sin(LST), 0],
		[np.sin(LST), -np.cos(LST), 0],
		[0, 0, 1] ])

	R_hdtoaa = np.array([
		[-np.sin(LAT), 0, np.cos(LAT)],
		[0, -1, 0],
        	[np.cos(LAT), 0, np.sin(LAT)] ])

	x = rect(ra, dec)
	y = np.dot(R_rdtohd, x)
	z = np.dot(R_hdtoaa, y)
	
	k = sphere(z)

	print("\n(RA,DEC) to (AZ, ALT): ")
	print(k)



if __name__ == '__main__':
	main()
