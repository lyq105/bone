
import subprocess
import numpy
import scipy
import matplotlib.pyplot as mp

freefem_command = 'FreeFem++-nw'
freefem_out = open('freem.log','wr')
subprocess.call([freefem_command,'bone_remodeling_freefem.edp'],stdout = freefem_out)
#p = subprocess.Popen([freefem_command,'bone_remodeling_freefem.edp'],stdout = freefem_out)
#p.wait()

obj = numpy.loadtxt("objvalue.dat")
print obj

mp.plot(obj[:,0],obj[:,1])
mp.savefig('heloo.pdf')
mp.show()

print "OK!"
