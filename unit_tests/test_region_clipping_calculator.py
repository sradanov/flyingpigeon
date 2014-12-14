import nose.tools
from unittest import TestCase
from nose import SkipTest
from nose.plugins.attrib import attr

from __init__ import TESTDATA, SERVICE

import tempfile
from netCDF4 import Dataset

from flyingpigeon import region_clipping_calculator

class RegionClippingCalculatorTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # TODO: ocgis does not like file:// urls
        from urllib2 import urlparse
        # tas
        url_parts = urlparse.urlparse(
            TESTDATA["tas_EUR-11_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22E_v1_mon_200101-200512.nc"])
        cls.tas_historical_2001_nc = url_parts.path
        url_parts = urlparse.urlparse(
            TESTDATA['tas_EUR-11_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22E_v1_mon_200601-201012.nc'])
        cls.tas_rcp45_2006_nc = url_parts.path
        # cmip5 ...
        url_parts = urlparse.urlparse(
            TESTDATA['cct_Amon_MPI-ESM-LR_historical_r1i1p1_185001-200512.nc'])
        cls.cmip5_historical_1850_nc = url_parts.path

    def test_select_ugid(self):
        from flyingpigeon.region_clipping_calculator import select_ugid
        nose.tools.ok_(select_ugid('AUT') == [17], select_ugid('AUT'))
        nose.tools.ok_(select_ugid('FIN') == [70], select_ugid('FIN'))
        nose.tools.ok_(select_ugid('ITA') == [107], select_ugid('ITA'))
        nose.tools.ok_(select_ugid('unknown') == [], select_ugid('unknown'))

    @attr('testdata')
    def test_calc_region_clipping_cmip5(self):
        #raise SkipTest
        out_dir = tempfile.mkdtemp()

        result = region_clipping_calculator.calc_region_clipping(
            [self.cmip5_historical_1850_nc], variable='cct', region='ITA', output_format='nc', out_dir=out_dir)

        nose.tools.ok_(
            result['drs_filename'] == 'cct_MPI-ESM-LR_historical_r1i1p1_19491216-21051115.nc',
            result)
        
        ds = Dataset(result['output'])
        nose.tools.ok_('cct' in ds.variables, ds.variables.keys())





        
    
