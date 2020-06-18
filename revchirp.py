""" Reverse chirping waveform model using IMRPhenomD as a a base
"""

# Notes on style:
#
# For example purposes only of how to advertise a waveform model to PyCBC
# Function should take kwargs only, and must accept abitrary kwargs.
# 'newparam' is an example of adding a new argument.
def reverse_chirp_fd(newparam=0.0, **kwds):
    from pycbc.waveform import get_fd_waveform

    if 'approximant' in kwds:
        kwds.pop("approximant")
    hp, hc = get_fd_waveform(approximant="IMRPhenomD", **kwds)

    return hp*1.0j, hc*1.0j + newparam

def reverse_chirp_td(**kwds):
    import numpy
    from pycbc.waveform import get_td_waveform

    if 'approximant' in kwds:
        kwds.pop("approximant")
    hp, hc = get_td_waveform(approximant="IMRPhenomD", **kwds)

    return ((hp.to_frequencyseries()*1.0j).to_timeseries(),
           (hp.to_frequencyseries()*1.0j).to_timeseries())
