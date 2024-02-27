'''
Copyright (c) 2024 Pyogenics

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

'''
Enums
'''
class ImageFormatEnum:
    NONE = -1
    RGBA8888 = 0
    ABGR8888 = 1
    RGB888 = 2
    BGR888 = 3
    RGB565 = 4
    I8 = 5
    IA88 = 6
    P8 = 7
    A8 = 8
    RGB888_BLUESCREEN = 9
    BGR888_BLUESCREEN = 10
    ARGB8888 = 11
    BGRA8888 = 12
    DXT1 = 13
    DXT3 = 14
    DXT5 = 15
    BGRX8888 = 16
    BGR565 = 17
    BGRX5551 = 18
    BGRA4444 = 19
    DXT1_ONEBITALPHA = 20
    BGRA5551 = 21
    UV88 = 22
    UVWQ8888 = 23
    RGBA16161616F = 24
    RGBA16161616 = 25
    UVLX8888 = 26

class VTFFlagEnum:
    # Flags from the *.txt config file
    POINTSAMPLE = 0x00000001
    TRILINEAR = 0x00000002
    CLAMPS = 0x00000004
    CLAMPT = 0x00000008
    ANISOTROPIC = 0x00000010
    HINT_DXT5 = 0x00000020
    PWL_CORRECTED = 0x00000040
    NORMAL = 0x00000080
    NOMIP = 0x00000100
    NOLOD = 0x00000200
    ALL_MIPS = 0x00000400
    PROCEDURAL = 0x00000800

    # These are automatically generated by vtex from the texture data.
    ONEBITALPHA = 0x00001000
    EIGHTBITALPHA = 0x00002000

    # Newer flags from the *.txt config file
    ENVMAP = 0x00004000
    RENDERTARGET = 0x00008000
    DEPTHRENDERTARGET = 0x00010000
    NODEBUGOVERRIDE = 0x00020000
    SINGLECOPY	= 0x00040000
    PRE_SRGB = 0x00080000

    UNUSED_00100000 = 0x00100000
    UNUSED_00200000 = 0x00200000
    UNUSED_00400000 = 0x00400000

    NODEPTHBUFFER = 0x00800000

    UNUSED_01000000 = 0x01000000

    CLAMPU = 0x02000000
    VERTEXTEXTURE = 0x04000000
    SSBUMP = 0x08000000			

    UNUSED_10000000 = 0x10000000

    BORDER = 0x20000000

    UNUSED_40000000 = 0x40000000
    UNUSED_80000000 = 0x80000000

'''
Data structures
'''
class VTFFlags:
    def __init__(self):
        self.pointSample = False
        self.trilinear = False
        self.clamps = False
        self.clampt = False
        self.anisotropic = False
        self.hint_dxt5 = False
        self.pwl_corrected = False
        self.normal = False
        self.nomip = False
        self.nolod = False
        self.all_mips = False
        self.procedural = False
        
        self.onebitalpha = False
        self.eightbitalpha = False

        self.envmap = False
        self.rendertarget = False
        self.nodebugoverride = False
        self.singlecopy = False
        self.pre_srgb = False
        self.nodepthbuffer = False
        self.clampu = False
        self.vertextexture = False
        self.ssbump = False
        self.border = False

class Header:
    def __init__(self):
        # Not in order of file format
        self.versionMajor = 0
        self.versionMinor = 0
        self.headerSize = 0
        self.flags = VTFFlags()

        self.width = 0
        self.height = 0
        self.format = 0
        self.mimapCount = 0
        self.lowResFormat = 0
        self.lowResWidth = 0
        self.lowResHeight = 0

        self.reflectivity = (0.0, 0.0, 0.0)
        self.bumpMapScale = 0.0

        # 7.2 =<
        self.depth = 0

        # 7.3 =<
        self.resourceCount = 0