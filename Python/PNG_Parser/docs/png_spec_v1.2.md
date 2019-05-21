# PNG (Portable Network Graphics) Specification

**Version 1.2**

## Table of contents

 - [Critical chunks](./png_spec_v1.2.md#critical-chunks)
   + [IHDR Image header](./png_spec_v1.2.md#ihdr-image-header)
   + [PLTE Palette](./png_spec_v1.2.md#plte-palette)
   + [IDAT Image data](./png_spec_v1.2.md#idat-image-data)
   + [IEND Image trailer](./png_spec_v1.2.md#iend-image-trailer)
 - [Ancillary chunks](./png_spec_v1.2.md#ancillary-chunks)
   + [Transparency information](./png_spec_v1.2.md#transparency-information)
      + [tRNS Transparency](./png_spec_v1.2.md#trns-transparency)
   + [Color space information](./png_spec_v1.2.md#color-space-information)
      + [gAMA Image gamma](./png_spec_v1.2.md#gama-image-gamma)
      + [cHRM Primary chromaticities](./png_spec_v1.2.md#chrm-primary-chromaticities)
      + [sRGB Standard RGB color space](./png_spec_v1.2.md#srgb-standard-rgb-color-space)
      + [iCCP Embedded ICC profile](./png_spec_v1.2.md#iccp-embedded-icc-profile)
   + [Textual information](./png_spec_v1.2.md#textual-information)
      + [tEXt Textual data](./png_spec_v1.2.md#text-textual-data)
      + [zTXt Compressed textual data](./png_spec_v1.2.md#ztxt-compressed-textual-data)
      + [TXt International textual data](./png_spec_v1.2.md#itxt-international-textual-data)
   + [Miscellaneous information](./png_spec_v1.2.md#miscellaneous-information)
      + [bKGD Background color](./png_spec_v1.2.md#bkgd-background-color)
      + [pHYs Physical pixel dimensions](./png_spec_v1.2.md#phys-physical-pixel-dimensions)
      + [sBIT Significant bits](./png_spec_v1.2.md#sbit-significant-bits)
      + [sPLT Suggested palette](./png_spec_v1.2.md#splt-suggested-palette)
      + [hIST Palette histogram](./png_spec_v1.2.md#hist-palette-histogram)
      + [tIME Image last-modification time](./png_spec_v1.2.md#time-image-last-modification-time)
- [Summary of standard chunks](./png_spec_v1.2.md#summary-of-standard-chunks)
- [Additional chunk types](./png_spec_v1.2.md#additional-chunk-types)
      
      

---

# Chunk Specifications

This chapter defines the standard types of PNG chunks.

## Critical chunks

All implementations must understand and successfully render the standard critical chunks. A valid PNG image must contain an IHDR chunk, one or more IDAT chunks, and an IEND chunk.

### IHDR Image header

The IHDR chunk must appear FIRST. It contains:

```
   Width:              4 bytes
   Height:             4 bytes
   Bit depth:          1 byte
   Color type:         1 byte
   Compression method: 1 byte
   Filter method:      1 byte
   Interlace method:   1 byte
```

Width and height give the image dimensions in pixels. They are 4-byte integers. Zero is an invalid value. The maximum for each is 231 in order to accommodate languages that have difficulty with unsigned 4-byte values.

Bit depth is a single-byte integer giving the number of bits per sample or per palette index (not per pixel). Valid values are 1, 2, 4, 8, and 16, although not all values are allowed for all color types.

Color type is a single-byte integer that describes the interpretation of the image data. Color type codes represent sums of the following values: 1 (palette used), 2 (color used), and 4 (alpha channel used). Valid values are 0, 2, 3, 4, and 6.

Bit depth restrictions for each color type are imposed to simplify implementations and to prohibit combinations that do not compress well. Decoders must support all valid combinations of bit depth and color type. The allowed combinations are:

```
   Color    Allowed    Interpretation
   Type    Bit Depths

   0       1,2,4,8,16  Each pixel is a grayscale sample.

   2       8,16        Each pixel is an R,G,B triple.

   3       1,2,4,8     Each pixel is a palette index;
                       a PLTE chunk must appear.

   4       8,16        Each pixel is a grayscale sample,
                       followed by an alpha sample.

   6       8,16        Each pixel is an R,G,B triple,
                       followed by an alpha sample.
```

The sample depth is the same as the bit depth except in the case of color type 3, in which the sample depth is always 8 bits.

Compression method is a single-byte integer that indicates the method used to compress the image data. At present, only compression method 0 (deflate/inflate compression with a sliding window of at most 32768 bytes) is defined. All standard PNG images must be compressed with this scheme. The compression method field is provided for possible future expansion or proprietary variants. Decoders must check this byte and report an error if it holds an unrecognized code. See Deflate/Inflate Compression for details.

Filter method is a single-byte integer that indicates the preprocessing method applied to the image data before compression. At present, only filter method 0 (adaptive filtering with five basic filter types) is defined. As with the compression method field, decoders must check this byte and report an error if it holds an unrecognized code. See Filter Algorithms for details.

Interlace method is a single-byte integer that indicates the transmission order of the image data. Two values are currently defined: 0 (no interlace) or 1 (Adam7 interlace). See Interlaced data order for details.

### PLTE Palette

The PLTE chunk contains from 1 to 256 palette entries, each a three-byte series of the form:

```
   Red:   1 byte (0 = black, 255 = red  )
   Green: 1 byte (0 = black, 255 = green)
   Blue:  1 byte (0 = black, 255 = blue )
```

The number of entries is determined from the chunk length. A chunk length not divisible by 3 is an error.

This chunk must appear for color type 3, and can appear for color types 2 and 6; it must not appear for color types 0 and 4. If this chunk does appear, it must precede the first IDAT chunk. There must not be more than one PLTE chunk.

For color type 3 (indexed color), the PLTE chunk is required. The first entry in PLTE is referenced by pixel value 0, the second by pixel value 1, etc. The number of palette entries must not exceed the range that can be represented in the image bit depth (for example, 24 = 16 for a bit depth of 4). It is permissible to have fewer entries than the bit depth would allow. In that case, any out-of-range pixel value found in the image data is an error.

For color types 2 and 6 (truecolor and truecolor with alpha), the PLTE chunk is optional. If present, it provides a suggested set of from 1 to 256 colors to which the truecolor image can be quantized if the viewer cannot display truecolor directly. If neither PLTE nor sPLT is present, such a viewer will need to select colors on its own, but it is often preferable for this to be done once by the encoder. (See Recommendations for Encoders: Suggested palettes.)

Note that the palette uses 8 bits (1 byte) per sample regardless of the image bit depth specification. In particular, the palette is 8 bits deep even when it is a suggested quantization of a 16-bit truecolor image.

There is no requirement that the palette entries all be used by the image, nor that they all be different.

### IDAT Image data

The IDAT chunk contains the actual image data. To create this data:

 - Begin with image scanlines represented as described in Image layout; the layout and total size of this raw data are determined by the fields of IHDR.

 - Filter the image data according to the filtering method specified by the IHDR chunk. (Note that with filter method 0, the only one currently defined, this implies prepending a filter-type byte to each scanline.)

 - Compress the filtered data using the compression method specified by the IHDR chunk.

The IDAT chunk contains the output datastream of the compression algorithm.

To read the image data, reverse this process.

There can be multiple IDAT chunks; if so, they must appear consecutively with no other intervening chunks. The compressed datastream is then the concatenation of the contents of all the IDAT chunks. The encoder can divide the compressed datastream into IDAT chunks however it wishes. (Multiple IDAT chunks are allowed so that encoders can work in a fixed amount of memory; typically the chunk size will correspond to the encoder's buffer size.) It is important to emphasize that IDAT chunk boundaries have no semantic significance and can occur at any point in the compressed datastream. A PNG file in which each IDAT chunk contains only one data byte is valid, though remarkably wasteful of space. (For that matter, zero-length IDAT chunks are valid, though even more wasteful.)

See Filter Algorithms and Deflate/Inflate Compression for details.

### IEND Image trailer

The IEND chunk must appear LAST. It marks the end of the PNG datastream. The chunk's data field is empty.

## Ancillary chunks

All ancillary chunks are optional, in the sense that encoders need not write them and decoders can ignore them. However, encoders are encouraged to write the standard ancillary chunks when the information is available, and decoders are encouraged to interpret these chunks when appropriate and feasible.

The standard ancillary chunks are described in the next four sections. This is not necessarily the order in which they would appear in a PNG datastream.

### Transparency information

This chunk conveys transparency information in datastreams that do not include a full alpha channel.

#### tRNS Transparency

The tRNS chunk specifies that the image uses simple transparency: either alpha values associated with palette entries (for indexed-color images) or a single transparent color (for grayscale and truecolor images). Although simple transparency is not as elegant as the full alpha channel, it requires less storage space and is sufficient for many common cases.

For color type 3 (indexed color), the tRNS chunk contains a series of one-byte alpha values, corresponding to entries in the PLTE chunk:

```
   Alpha for palette index 0:  1 byte
   Alpha for palette index 1:  1 byte
   ...etc...
```

Each entry indicates that pixels of the corresponding palette index must be treated as having the specified alpha value. Alpha values have the same interpretation as in an 8-bit full alpha channel: 0 is fully transparent, 255 is fully opaque, regardless of image bit depth. The tRNS chunk must not contain more alpha values than there are palette entries, but tRNS can contain fewer values than there are palette entries. In this case, the alpha value for all remaining palette entries is assumed to be 255. In the common case in which only palette index 0 need be made transparent, only a one-byte tRNS chunk is needed.

For color type 0 (grayscale), the tRNS chunk contains a single gray level value, stored in the format:

```
   Gray:  2 bytes, range 0 .. (2^bitdepth)-1
```

(If the image bit depth is less than 16, the least significant bits are used and the others are 0.) Pixels of the specified gray level are to be treated as transparent (equivalent to alpha value 0); all other pixels are to be treated as fully opaque (alpha value 2bitdepth).

For color type 2 (truecolor), the tRNS chunk contains a single RGB color value, stored in the format:

```
   Red:   2 bytes, range 0 .. (2^bitdepth)-1
   Green: 2 bytes, range 0 .. (2^bitdepth)-1
   Blue:  2 bytes, range 0 .. (2^bitdepth)-1
```

(If the image bit depth is less than 16, the least significant bits are used and the others are 0.) Pixels of the specified color value are to be treated as transparent (equivalent to alpha value 0); all other pixels are to be treated as fully opaque (alpha value 2bitdepth).

tRNS is prohibited for color types 4 and 6, since a full alpha channel is already present in those cases.

Note: when dealing with 16-bit grayscale or truecolor data, it is important to compare both bytes of the sample values to determine whether a pixel is transparent. Although decoders may drop the low-order byte of the samples for display, this must not occur until after the data has been tested for transparency. For example, if the grayscale level 0x0001 is specified to be transparent, it would be incorrect to compare only the high-order byte and decide that 0x0002 is also transparent.

When present, the tRNS chunk must precede the first IDAT chunk, and must follow the PLTE chunk, if any.

### Color space information

These chunks relate the image samples to the desired display intensity.

#### gAMA Image gamma

The gAMA chunk specifies the relationship between the image samples and the desired display output intensity as a power function:

```
   sample = light_out ^ gamma
```

Here sample and light_out are normalized to the range 0.0 (minimum intensity) to 1.0 (maximum intensity). Therefore:

```
   sample = integer_sample / (2^bitdepth - 1)
```

The gAMA chunk contains:

```
   Gamma: 4 bytes
```

The value is encoded as a 4-byte unsigned integer, representing gamma times 100000. For example, a gamma of 1/2.2 would be stored as 45455.

The gamma value has no effect on alpha samples, which are always a linear fraction of full opacity.

If the encoder does not know the image's gamma value, it should not write a gAMA chunk; the absence of a gAMA chunk indicates that the gamma is unknown.

Technically, "desired display output intensity" is not specific enough; one needs to specify the viewing conditions under which the output is desired. For gAMA these are the reference viewing conditions of the sRGB specification [sRGB], which are based on ISO standards [ISO-3664]. Adjusting for different viewing conditions is a complex process normally handled by a Color Management System (CMS). If this adjustment is not performed, the error is usually small. Applications desiring high color fidelity may wish to use an sRGB chunk (see the sRGB chunk specification) or an iCCP chunk (see the iCCP chunk specification).

If the gAMA chunk appears, it must precede the first IDAT chunk, and it must also precede the PLTE chunk if present. An sRGB chunk or iCCP chunk, when present and recognized, overrides the gAMA chunk.

See Gamma correction, Recommendations for Encoders: Encoder gamma handling, and Recommendations for Decoders: Decoder gamma handling.

#### cHRM Primary chromaticities

Applications that need device-independent specification of colors in a PNG file can use the cHRM chunk to specify the 1931 CIE x,y chromaticities of the red, green, and blue primaries used in the image, and the referenced white point. See Color Tutorial for more information.

The cHRM chunk contains:

```
   White Point x: 4 bytes
   White Point y: 4 bytes
   Red x:         4 bytes
   Red y:         4 bytes
   Green x:       4 bytes
   Green y:       4 bytes
   Blue x:        4 bytes
   Blue y:        4 bytes
```

Each value is encoded as a 4-byte unsigned integer, representing the x or y value times 100000. For example, a value of 0.3127 would be stored as the integer 31270.

cHRM is allowed in all PNG files, although it is of little value for grayscale images.

If the encoder does not know the chromaticity values, it should not write a cHRM chunk; the absence of a cHRM chunk indicates that the image's primary colors are device-dependent.

If the cHRM chunk appears, it must precede the first IDAT chunk, and it must also precede the PLTE chunk if present.

An sRGB chunk or iCCP chunk, when present and recognized, overrides the cHRM chunk.

See the sRGB chunk specification, the iCCP chunk specification, Recommendations for Encoders: Encoder color handling, and Recommendations for Decoders: Decoder color handling.

#### sRGB Standard RGB color space

If the sRGB chunk is present, the image samples conform to the sRGB color space [sRGB], and should be displayed using the specified rendering intent as defined by the International Color Consortium [ICC].

The sRGB chunk contains:

```
   Rendering intent: 1 byte
```

The following values are defined for the rendering intent:

```
   0: Perceptual
   1: Relative colorimetric
   2: Saturation
   3: Absolute colorimetric
```

Perceptual intent is for images preferring good adaptation to the output device gamut at the expense of colorimetric accuracy, like photographs.

Relative colorimetric intent is for images requiring color appearance matching (relative to the output device white point), like logos.

Saturation intent is for images preferring preservation of saturation at the expense of hue and lightness, like charts and graphs.

Absolute colorimetric intent is for images requiring preservation of absolute colorimetry, like proofs (previews of images destined for a different output device).

An application that writes the sRGB chunk should also write a gAMA chunk (and perhaps a cHRM chunk) for compatibility with applications that do not use the sRGB chunk. In this situation, only the following values may be used:

```
   gAMA:
   Gamma:         45455

   cHRM:
   White Point x: 31270
   White Point y: 32900
   Red x:         64000
   Red y:         33000
   Green x:       30000
   Green y:       60000
   Blue x:        15000
   Blue y:         6000
```

When the sRGB chunk is present, applications that recognize it and are capable of color management [ICC] must ignore the gAMA and cHRM chunks and use the sRGB chunk instead.

Applications that recognize the sRGB chunk but are not capable of full-fledged color management must also ignore the gAMA and cHRM chunks, because the applications already know what values those chunks should contain. The applications must therefore use the values of gAMA and cHRM given above as if they had appeared in gAMA and cHRM chunks.

If the sRGB chunk appears, it must precede the first IDAT chunk, and it must also precede the PLTE chunk if present. The sRGB and iCCP chunks should not both appear.

#### iCCP Embedded ICC profile

If the iCCP chunk is present, the image samples conform to the color space represented by the embedded ICC profile as defined by the International Color Consortium [ICC]. The color space of the ICC profile must be an RGB color space for color images (PNG color types 2, 3, and 6), or a monochrome grayscale color space for grayscale images (PNG color types 0 and 4).

The iCCP chunk contains:

```
   Profile name:       1-79 bytes (character string)
   Null separator:     1 byte
   Compression method: 1 byte
   Compressed profile: n bytes
```

The format is like the zTXt chunk. (see the zTXt chunk specification). The profile name can be any convenient name for referring to the profile. It is case-sensitive and subject to the same restrictions as the keyword in a text chunk: it must contain only printable Latin-1 [ISO/IEC-8859-1] characters (33-126 and 161-255) and spaces (32), but no leading, trailing, or consecutive spaces. The only value presently defined for the compression method byte is 0, meaning zlib datastream with deflate compression (see Deflate/Inflate Compression). Decompression of the remainder of the chunk yields the ICC profile.

An application that writes the iCCP chunk should also write gAMA and cHRM chunks that approximate the ICC profile's transfer function, for compatibility with applications that do not use the iCCP chunk.

When the iCCP chunk is present, applications that recognize it and are capable of color management [ICC] should ignore the gAMA and cHRM chunks and use the iCCP chunk instead, but applications incapable of full-fledged color management should use the gAMA and cHRM chunks if present.

A file should contain at most one embedded profile, whether explicit like iCCP or implicit like sRGB.

If the iCCP chunk appears, it must precede the first IDAT chunk, and it must also precede the PLTE chunk if present.

### Textual information

The iTXt, tEXt, and zTXt chunks are used for conveying textual information associated with the image. This specification refers to them generically as "text chunks".

Each of the text chunks contains as its first field a keyword that indicates the type of information represented by the text string. The following keywords are predefined and should be used where appropriate:

```
   Title            Short (one line) title or caption for image
   Author           Name of image's creator
   Description      Description of image (possibly long)
   Copyright        Copyright notice
   Creation Time    Time of original image creation
   Software         Software used to create the image
   Disclaimer       Legal disclaimer
   Warning          Warning of nature of content
   Source           Device used to create the image
   Comment          Miscellaneous comment; conversion from
                    GIF comment
```

For the Creation Time keyword, the date format defined in section 5.2.14 of RFC 1123 is suggested, but not required [RFC-1123]. Decoders should allow for free-format text associated with this or any other keyword.

Other keywords may be invented for other purposes. Keywords of general interest can be registered with the maintainers of the PNG specification. However, it is also permitted to use private unregistered keywords. (Private keywords should be reasonably self-explanatory, in order to minimize the chance that the same keyword will be used for incompatible purposes by different people.)

The keyword must be at least one character and less than 80 characters long. Keywords are always interpreted according to the ISO/IEC 8859-1 (Latin-1) character set [ISO/IEC-8859-1]. They must contain only printable Latin-1 characters and spaces; that is, only character codes 32-126 and 161-255 decimal are allowed. To reduce the chances for human misreading of a keyword, leading and trailing spaces are forbidden, as are consecutive spaces. Note also that the non-breaking space (code 160) is not permitted in keywords, since it is visually indistinguishable from an ordinary space.

Keywords must be spelled exactly as registered, so that decoders can use simple literal comparisons when looking for particular keywords. In particular, keywords are considered case-sensitive.

Any number of text chunks can appear, and more than one with the same keyword is permissible.

See Recommendations for Encoders: Text chunk processing and Recommendations for Decoders: Text chunk processing.

#### tEXt Textual data

Textual information that the encoder wishes to record with the image can be stored in tEXt chunks. Each tEXt chunk contains a keyword (see above) and a text string, in the format:

```
   Keyword:        1-79 bytes (character string)
   Null separator: 1 byte
   Text:           n bytes (character string)
```

The keyword and text string are separated by a zero byte (null character). Neither the keyword nor the text string can contain a null character. Note that the text string is not null-terminated (the length of the chunk is sufficient information to locate the ending). The text string can be of any length from zero bytes up to the maximum permissible chunk size less the length of the keyword and separator.

The text is interpreted according to the ISO/IEC 8859-1 (Latin-1) character set [ISO/IEC-8859-1]. The text string can contain any Latin-1 character. Newlines in the text string should be represented by a single linefeed character (decimal 10); use of other control characters in the text is discouraged.

#### zTXt Compressed textual data

The zTXt chunk contains textual data, just as tEXt does; however, zTXt takes advantage of compression. The zTXt and tEXt chunks are semantically equivalent, but zTXt is recommended for storing large blocks of text.

A zTXt chunk contains:

```
   Keyword:            1-79 bytes (character string)
   Null separator:     1 byte
   Compression method: 1 byte
   Compressed text:    n bytes
```

The keyword and null separator are exactly the same as in the tEXt chunk. Note that the keyword is not compressed. The compression method byte identifies the compression method used in this zTXt chunk. The only value presently defined for it is 0 (deflate/inflate compression). The compression method byte is followed by a compressed datastream that makes up the remainder of the chunk. For compression method 0, this datastream adheres to the zlib datastream format (see Deflate/Inflate Compression). Decompression of this datastream yields Latin-1 text that is identical to the text that would be stored in an equivalent tEXt chunk.

#### iTXt International textual data

This chunk is semantically equivalent to the tEXt and zTXt chunks, but the textual data is in the UTF-8 encoding of the Unicode character set instead of Latin-1. This chunk contains:

```
   Keyword:             1-79 bytes (character string)
   Null separator:      1 byte
   Compression flag:    1 byte
   Compression method:  1 byte
   Language tag:        0 or more bytes (character string)
   Null separator:      1 byte
   Translated keyword:  0 or more bytes
   Null separator:      1 byte
   Text:                0 or more bytes
```

The keyword is described above.

The compression flag is 0 for uncompressed text, 1 for compressed text. Only the text field may be compressed. The only value presently defined for the compression method byte is 0, meaning zlib datastream with deflate compression. For uncompressed text, encoders should set the compression method to 0 and decoders should ignore it.

The language tag [RFC-1766] indicates the human language used by the translated keyword and the text. Unlike the keyword, the language tag is case-insensitive. It is an ASCII [ISO-646] string consisting of hyphen-separated words of 1-8 letters each (for example: cn, en-uk, no-bok, x-klingon). If the first word is two letters long, it is an ISO language code [ISO-639]. If the language tag is empty, the language is unspecified.

The translated keyword and text both use the UTF-8 encoding of the Unicode character set [ISO/IEC-10646-1], and neither may contain a zero byte (null character). The text, unlike the other strings, is not null-terminated; its length is implied by the chunk length.

Line breaks should not appear in the translated keyword. In the text, a newline should be represented by a single line feed character (decimal 10). The remaining control characters (1-9, 11-31, and 127-159) are discouraged in both the translated keyword and the text. Note that in UTF-8 there is a difference between the characters 128-159 (which are discouraged) and the bytes 128-159 (which are often necessary).

The translated keyword, if not empty, should contain a translation of the keyword into the language indicated by the language tag, and applications displaying the keyword should display the translated keyword in addition.

### Miscellaneous information

These chunks are used for conveying other information associated with the image.

#### bKGD Background color

The bKGD chunk specifies a default background color to present the image against. Note that viewers are not bound to honor this chunk; a viewer can choose to use a different background.

For color type 3 (indexed color), the bKGD chunk contains:

```
   Palette index:  1 byte
```

The value is the palette index of the color to be used as background.

For color types 0 and 4 (grayscale, with or without alpha), bKGD contains:

```
   Gray:  2 bytes, range 0 .. (2^bitdepth)-1
```

(If the image bit depth is less than 16, the least significant bits are used and the others are 0.) The value is the gray level to be used as background.

For color types 2 and 6 (truecolor, with or without alpha), bKGD contains:

```
   Red:   2 bytes, range 0 .. (2^bitdepth)-1
   Green: 2 bytes, range 0 .. (2^bitdepth)-1
   Blue:  2 bytes, range 0 .. (2^bitdepth)-1
```

(If the image bit depth is less than 16, the least significant bits are used and the others are 0.) This is the RGB color to be used as background.

When present, the bKGD chunk must precede the first IDAT chunk, and must follow the PLTE chunk, if any.

See Recommendations for Decoders: Background color.

#### pHYs Physical pixel dimensions

The pHYs chunk specifies the intended pixel size or aspect ratio for display of the image. It contains:

```
   Pixels per unit, X axis: 4 bytes (unsigned integer)
   Pixels per unit, Y axis: 4 bytes (unsigned integer)
   Unit specifier:          1 byte
```

The following values are defined for the unit specifier:

```
   0: unit is unknown
   1: unit is the meter
```

When the unit specifier is 0, the pHYs chunk defines pixel aspect ratio only; the actual size of the pixels remains unspecified.

Conversion note: one inch is equal to exactly 0.0254 meters.

If this ancillary chunk is not present, pixels are assumed to be square, and the physical size of each pixel is unknown.

If present, this chunk must precede the first IDAT chunk.

See Recommendations for Decoders: Pixel dimensions.
#### sBIT Significant bits

To simplify decoders, PNG specifies that only certain sample depths can be used, and further specifies that sample values should be scaled to the full range of possible values at the sample depth. However, the sBIT chunk is provided in order to store the original number of significant bits. This allows decoders to recover the original data losslessly even if the data had a sample depth not directly supported by PNG. We recommend that an encoder emit an sBIT chunk if it has converted the data from a lower sample depth.

For color type 0 (grayscale), the sBIT chunk contains a single byte, indicating the number of bits that were significant in the source data.

For color type 2 (truecolor), the sBIT chunk contains three bytes, indicating the number of bits that were significant in the source data for the red, green, and blue channels, respectively.

For color type 3 (indexed color), the sBIT chunk contains three bytes, indicating the number of bits that were significant in the source data for the red, green, and blue components of the palette entries, respectively.

For color type 4 (grayscale with alpha channel), the sBIT chunk contains two bytes, indicating the number of bits that were significant in the source grayscale data and the source alpha data, respectively.

For color type 6 (truecolor with alpha channel), the sBIT chunk contains four bytes, indicating the number of bits that were significant in the source data for the red, green, blue, and alpha channels, respectively.

Each depth specified in sBIT must be greater than zero and less than or equal to the sample depth (which is 8 for indexed-color images, and the bit depth given in IHDR for other color types).

A decoder need not pay attention to sBIT: the stored image is a valid PNG file of the sample depth indicated by IHDR. However, if the decoder wishes to recover the original data at its original precision, this can be done by right-shifting the stored samples (the stored palette entries, for an indexed-color image). The encoder must scale the data in such a way that the high-order bits match the original data.

If the sBIT chunk appears, it must precede the first IDAT chunk, and it must also precede the PLTE chunk if present.

See Recommendations for Encoders: Sample depth scaling and Recommendations for Decoders: Sample depth rescaling.

#### sPLT Suggested palette

This chunk can be used to suggest a reduced palette to be used when the display device is not capable of displaying the full range of colors present in the image. If present, it provides a recommended set of colors, with alpha and frequency information, that can be used to construct a reduced palette to which the PNG image can be quantized.

This chunk contains a null-terminated text string that names the palette and a one-byte sample depth, followed by a series of palette entries, each a six-byte or ten-byte series containing five unsigned integers:

```
   Palette name:    1-79 bytes (character string)
   Null terminator: 1 byte
   Sample depth:    1 byte
   Red:             1 or 2 bytes
   Green:           1 or 2 bytes
   Blue:            1 or 2 bytes
   Alpha:           1 or 2 bytes
   Frequency:       2 bytes
   ...etc...
```

There can be any number of entries; a decoder determines the number of entries from the remaining chunk length after the sample depth byte. It is an error if this remaining length is not divisible by 6 (if the sPLT sample depth is 8) or by 10 (if the sPLT sample depth is 16). Entries must appear in decreasing order of frequency. There is no requirement that the entries all be used by the image, nor that they all be different.

The palette name can be any convenient name for referring to the palette (for example, "256 color including Macintosh default", "256 color including Windows-3.1 default", "Optimal 512"). It may help applications or people to choose the appropriate suggested palette when more than one appears in a PNG file. The palette name is case-sensitive and subject to the same restrictions as a text keyword: it must contain only printable Latin-1 [ISO/IEC-8859-1] characters (33-126 and 161-255) and spaces (32), but no leading, trailing, or consecutive spaces.

The sPLT sample depth must be 8 or 16.

The red, green, blue, and alpha samples are either one or two bytes each, depending on the sPLT sample depth, regardless of the image bit depth. The color samples are not premultiplied by alpha, nor are they precomposited against any background. An alpha value of 0 means fully transparent, while an alpha value of 255 (when the sPLT sample depth is 8) or 65535 (when the sPLT sample depth is 16) means fully opaque. The palette samples have the same gamma and chromaticity values as those of the PNG image.

Each frequency value is proportional to the fraction of pixels in the image that are closest to that palette entry in RGBA space, before the image has been composited against any background. The exact scale factor is chosen by the encoder, but should be chosen so that the range of individual values reasonably fills the range 0 to 65535. It is acceptable to artificially inflate the frequencies for "important" colors such as those in a company logo or in the facial features of a portrait. Zero is a valid frequency meaning the color is "least important" or that it is rarely if ever used. But when all of the frequencies are zero, they are meaningless (nothing may be inferred about the actual frequencies of the colors).

The sPLT chunk can appear for any PNG color type. Note that entries in sPLT can fall outside the color space of the PNG image; for example, in a grayscale PNG, sPLT entries would typically satisfy R=G=B, but this is not required. Similarly, sPLT entries can have nonopaque alpha values even when the PNG image does not use transparency.

If sPLT appears, it must precede the first IDAT chunk. There can be multiple sPLT chunks, but if so they must have different palette names.

See Recommendations for Encoders: Suggested palettes and Recommendations for Decoders: Suggested-palette and histogram usage

#### hIST Palette histogram

The hIST chunk gives the approximate usage frequency of each color in the color palette. A hIST chunk can appear only when a PLTE chunk appears. If a viewer is unable to provide all the colors listed in the palette, the histogram may help it decide how to choose a subset of the colors for display.

The hIST chunk contains a series of 2-byte (16 bit) unsigned integers. There must be exactly one entry for each entry in the PLTE chunk. Each entry is proportional to the fraction of pixels in the image that have that palette index; the exact scale factor is chosen by the encoder.

Histogram entries are approximate, with the exception that a zero entry specifies that the corresponding palette entry is not used at all in the image. It is required that a histogram entry be nonzero if there are any pixels of that color.

When the palette is a suggested quantization of a truecolor image, the histogram is necessarily approximate, since a decoder may map pixels to palette entries differently than the encoder did. In this situation, zero entries should not appear.

The hIST chunk, if it appears, must follow the PLTE chunk, and must precede the first IDAT chunk.

See Rationale: Palette histograms and Recommendations for Decoders: Suggested-palette and histogram usage.

#### tIME Image last-modification time

The tIME chunk gives the time of the last image modification (not the time of initial image creation). It contains:

```
   Year:   2 bytes (complete; for example, 1995, not 95)
   Month:  1 byte (1-12)
   Day:    1 byte (1-31)
   Hour:   1 byte (0-23)
   Minute: 1 byte (0-59)
   Second: 1 byte (0-60)    (yes, 60, for leap seconds; not 61,
                             a common error)
```

Universal Time (UTC, also called GMT) should be specified rather than local time.

The tIME chunk is intended for use as an automatically-applied time stamp that is updated whenever the image data is changed. It is recommended that tIME not be changed by PNG editors that do not change the image data. The Creation Time text keyword can be used for a user-supplied time (see the text chunk specification).

## Summary of standard chunks

This table summarizes some properties of the standard chunk types.

   Critical chunks (must appear in this order, except PLTE
                    is optional):

```
 |======|==========|=====================================|
 | Name | Multiple | Ordering constraints                |
 |      |   OK?    |                                     |
 |======|==========|=====================================|
 | IHDR |    No    | Must be first                       |
 | PLTE |    No    | Before IDAT                         |
 | IDAT |    Yes   | Multiple IDATs must be consecutive  |
 | IEND |    No    | Must be last                        |
 |======|==========|=====================================|
```

   Ancillary chunks (need not appear in this order):

```
 |======|==========|=========================|
 | Name | Multiple | Ordering constraints    |
 |      |   OK?    |                         |
 |======|==========|=========================|
 | cHRM |    No    | Before PLTE and IDAT    |
 | gAMA |    No    | Before PLTE and IDAT    |
 | iCCP |    No    | Before PLTE and IDAT    |
 | sBIT |    No    | Before PLTE and IDAT    |
 | sRGB |    No    | Before PLTE and IDAT    |
 | bKGD |    No    | After PLTE; before IDAT |
 | hIST |    No    | After PLTE; before IDAT |
 | tRNS |    No    | After PLTE; before IDAT |
 | pHYs |    No    | Before IDAT             |
 | sPLT |    Yes   | Before IDAT             |
 | tIME |    No    | None                    |
 | iTXt |    Yes   | None                    |
 | tEXt |    Yes   | None                    |
 | zTXt |    Yes   | None                    |
 |======|==========|=========================|
```

Standard keywords for text chunks:

```
 |================|==============================================|
 |  Title         |  Short (one line) title or caption for image |
 |  Author        |  Name of image's creator                     |
 |  Description   |  Description of image (possibly long)        |
 |  Copyright     |  Copyright notice                            |
 |  Creation Time |  Time of original image creation             |
 |  Software      |  Software used to create the image           |
 |  Disclaimer    |  Legal disclaimer                            |
 |  Warning       |  Warning of nature of content                |
 |  Source        |  Device used to create the image             |
 |  Comment       |  Miscellaneous comment; conversion from      |
 |                |  GIF comment                                 |
 |================|==============================================|
```

## Additional chunk types

Additional public PNG chunk types are defined in the document "Extensions to the PNG 1.2 Specification, Version 1.2.0" [PNG-EXTENSIONS]. Chunks described there are expected to be less widely supported than those defined in this specification. However, application authors are encouraged to use those chunk types whenever appropriate for their applications. Additional chunk types can be proposed for inclusion in that list by contacting the PNG specification maintainers at png-info@uunet.uu.net or at png-group@w3.org.

New public chunks will be registered only if they are of use to others and do not violate the design philosophy of PNG. Chunk registration is not automatic, although it is the intent of the authors that it be straightforward when a new chunk of potentially wide application is needed. Note that the creation of new critical chunk types is discouraged unless absolutely necessary.

Applications can also use private chunk types to carry data that is not of interest to other applications. See Recommendations for Encoders: Use of private chunks.

Decoders must be prepared to encounter unrecognized public or private chunk type codes. Unrecognized chunk types must be handled as described in Chunk naming conventions.
