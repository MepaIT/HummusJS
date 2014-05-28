{
    'targets': [
        {
            'target_name': 'freetype',
            'type': 'static_library',
            'defines': [
                'FT2_BUILD_LIBRARY=1'
            ],
            'include_dirs': [
             './include',
             './include',
             './include/freetype/config',
             './include/src',
             './include/freetype/internal',
             './include/freetype/internal/services'
            ],
            'sources': [
                './src/base/ftbbox.c',
                './src/base/ftgxval.c',
                './src/base/ftlcdfil.c',
                './src/base/ftmm.c',
                './src/base/ftotval.c',
                './src/base/ftpatent.c',
                './src/base/ftpfr.c',
                './src/base/ftsynth.c',
                './src/base/fttype1.c',
                './src/base/ftwinfnt.c',
                './src/base/ftxf86.c',
                './src/pcf/pcf.c',
                './src/pfr/pfr.c',
                './src/psaux/psaux.c',
                './src/pshinter/pshinter.c',
                './src/psnames/psmodule.c',
                './src/raster/raster.c',
                './src/sfnt/sfnt.c',
                './src/truetype/truetype.c',
                './src/type1/type1.c',
                './src/type42/type42.c',
                './src/cid/type1cid.c',
                './src/winfonts/winfnt.c',
                './src/autofit/autofit.c',
                './src/bdf/bdf.c',
                './src/cff/cff.c',
                './src/base/ftbase.c',
                './src/base/ftbitmap.c',
                './src/cache/ftcache.c',
                './src/base/ftcid.c',
                './src/base/ftdebug.c',
                './src/base/ftfstype.c',
                './src/base/ftgasp.c',
                './src/base/ftglyph.c',
                './src/gzip/ftgzip.c',
                './src/base/ftinit.c',
                './src/lzw/ftlzw.c',
                './src/base/ftstroke.c',
                './src/base/ftsystem.c',
                './src/smooth/smooth.c',
                './include/freetype/config/ftconfig.h',
                './include/freetype/config/ftheader.h',
                './include/freetype/config/ftmodule.h',
                './include/freetype/config/ftoption.h',
                './include/freetype/config/ftstdlib.h',
                './include/ft2build.h'
            ]
        }
    ]        
}