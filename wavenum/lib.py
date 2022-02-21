def wavenum_convert(wavenumber):
    """
    Return a wavenumber to a wavelength, backwards compatible
    wavenumber in cm-1
    wavelength in nm
    """
    wavelength = (1/wavenumber) * 10**(7)

    return wavelength

def try_me():
    wavenumber = 20_000
    wavelength = wavenum_convert(20000)
    result = f"Wavenumber {wavenumber} cm-1 converted to Wavelength {wavelength} nm"
    return result
