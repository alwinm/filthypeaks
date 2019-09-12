# testing functions
import numpy as n
import pylab as p
import filthypeaks.peaks as fp

def white_noise(length):
    amps = n.random.normal(size=length)
    angles = 2*n.pi*n.random.random(size=length)
    noise = n.fft.fft(amps*n.cos(angles)+n.complex(0,1)*amps*n.sin(angles))
    noise = noise.real/n.max(n.abs(noise.real))
    return noise

def gen_sine(length,npeaks=10):
    # generate sine wave
    signal = n.sin(npeaks*2*n.pi*n.linspace(0,1,length))
    return signal

def gen_delta(length,npeaks=10):
    # generate delta function peaks
    signal = n.zeros(length)
    signal[list((n.random.random(npeaks)*length).astype(int))] += 1.0
    return signal

def gen_dino(length,npeaks=10):
    # generate dinosaur tail 
    signal = (1.2+n.sin(npeaks*2*n.pi*n.linspace(0,1,length))) * n.exp(-0.5*n.linspace(0,1,length))
    return signal

def alltests(length,iters,function=fp.extremum_iterate,show=False,save=''):
    noise1 = white_noise(length)
    noise2 = 0.5*n.random.normal(size=length)
    sine = gen_sine(length)
    delta = gen_delta(length)
    dino = gen_dino(length)
    signals = [sine,delta,dino]
    noises = [noise1,noise2]
    # snames = ['Sine','Delta','Dino']
    # nnames = ['White','Normal']
    nh = iters
    nw = len(signals)*len(noises)
    ns = 4
    fig,axs = p.subplots(nh,nw,sharey=True,sharex=True,figsize=(ns*nw,ns*nh))
    for i in range(len(signals)):
        signal = signals[i]
        for j in range(len(noises)):
            noise = noises[j]
            column = i*len(noises) + j
            working_array = signal+noise
            working_points = n.arange(len(working_array))
            # sname = snames[i]
            # nname = nnames[j]
            for k in range(iters):
                ni = k*nw + column
                ax = axs[k][column]
                ax.plot(signal+noise,alpha=0.5)
                ax.plot(signal)
                working_array,working_points = function(working_array,working_points)
                ax.plot(working_points,working_array,'ko')
                if column == 0:
                    ax.set_ylabel('Iteration {}'.format(k+1))
    if show:
        p.show()
    if len(save) > 0:
        p.savefig(save)
        

if __name__ == "__main__":
    alltests(1000,3,function=fp.iterate,save='peaks.png')
    alltests(1000,3,save='extremum.png')

