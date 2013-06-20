#!/usr/bin/env python

''' Copyright (c) 2013 Potential Ventures Ltd
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of Potential Ventures Ltd nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL POTENTIAL VENTURES LTD BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. '''


"""
    Collection of Ethernet Packet generators to use for testdata generation

    Most generators take the keyword argument "payload" which can be
    used to control the payload contents if required.  Defaults to random data.
"""
import random

from scapy.all import Ether, IP, UDP

from cocotb.decorators import public
from cocotb.generators.byte import *

_default_payload = random_data

def _get_payload(gen, nbytes):
    """Helper function to pull a chunk of bytes from a generator"""
    payload = ""
    while len(payload) < nbytes:
        payload += gen.next()
    return payload


# UDP packet generators
@public
def udp_all_sizes(max_size=1500, payload=_default_payload()):
    """UDP packets of every supported size"""
    header = Ether() / IP() / UDP ()

    for size in range(0, max_size-len(header)):
        yield header / _get_payload(payload, size)

@public
def udp_random_sizes(npackets=100, payload=_default_payload()):
    """UDP packets with random sizes"""
    header = Ether() / IP() / UDP ()
    max_size = 1500 - len(header)

    for pkt in range(npackets):
        yield header / _get_payload(payload, random.randint(0,max_size))

