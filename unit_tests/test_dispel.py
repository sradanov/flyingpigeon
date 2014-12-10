import nose.tools
from unittest import TestCase
from nose import SkipTest
from nose.plugins.attrib import attr

from __init__ import TESTDATA, SERVICE

from flyingpigeon.dispel import climate_indice_workflow

# TODO: set GDAL_DATA in a save way
import os
from os.path import join
os.environ['GDAL_DATA'] = join(os.environ['HOME'], 'anaconda', 'share', 'gdal')

def my_monitor(execution):
    print execution.status
    print execution.percentCompleted
    print execution.statusMessage

class WorkflowTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.nc_files = []
        cls.nc_files.append( TESTDATA["tas_EUR-11_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22E_v1_mon_200101-200512.nc"] )
        cls.nc_files.append( TESTDATA['tas_EUR-11_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22E_v1_mon_200601-201012.nc'] )
        cls.nc_files.append( TESTDATA['tasmax_WAS-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_20010101-20051231.nc'] )
        cls.nc_files.append( TESTDATA['tasmax_WAS-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19960101-20001231.nc'] )
        cls.nc_files.append( TESTDATA['tasmax_WAS-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19910101-19951231.nc'] )

    def test_indice_workflow(self):
        result = climate_indice_workflow(
            url=SERVICE,
            resources=self.nc_files,
            indices=['SU', 'TG'],
            grouping='year',
            monitor=my_monitor)

        #nose.tools.ok_(False, result)
        
        
        
    
