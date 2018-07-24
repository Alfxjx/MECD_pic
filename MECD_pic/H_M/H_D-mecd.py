import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def H_M(D_W, D_N=0.7,fi=0.0667):
	D_tmp = D_N/(D_W*np.cos(fi))
	H_M = -0.5*D_W*np.cos(fi)*(cosh_1(D_tmp)-cosh_1(1/np.cos(fi)))
	return H_M
def cosh_1(f):
	fi = 1.00/(np.cosh(f))
	return fi
if __name__ == '__main__':
	#print("Height of the meniscus is: %0.4f mm" % H_D0(0.7))
	list= []
	for i in range(0,700):
		i0= i/1000
		print(H_M(i0))
		list.append(H_M(i0))
	with open('H_M.txt','w')  as f:
		for num in list:
			f.write(str(num)+'\n')
		f.close()

	mpl.rcParams['xtick.labelsize'] = 24
	mpl.rcParams['ytick.labelsize'] = 24
	D_W = np.linspace(0.0, 0.7, 700)
	plt.figure('H_M')
	plt.plot(D_W/0.7, H_M(D_W)/0.7)
	plt.savefig('H_M.png')
	plt.show()
	print(cosh_1(1/np.cos(0.0667)))
