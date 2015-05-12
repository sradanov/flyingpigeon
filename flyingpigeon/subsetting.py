# import ocgis

from .exceptions import CalculationException
from .utils import drs_filename, calc_grouping

from malleefowl import wpslogging as logging
#import logging

logger = logging.getLogger(__name__)

from os.path import dirname, join
DIR_MASKS = join(dirname(__file__), 'processes', 'masks')

def masking(resource , mask):
  """ possible masks: 
  'Europe'
  """
  
  from cdo import Cdo
  cdo = Cdo()
  from tempfile import mkstemp
  from os import system 
  
  masks = {'Europe':'/homel/nhempel/birdhouse/flyingpigeon/flyingpigeon/processes/masks/Europa.nc'}
  
  gnc, nc_remap= mkstemp(suffix='.nc')
  try:  
    call = "cdo div '%s' '%s' '%s'" % ( resource , masks[mask], nc_remap)
    system(call)
  except Exception as e:
    print 'direct masking failed %s' % (e)
  #else:
    try:
      gnc, mask_rm= mkstemp(suffix='.nc')    
      call = "cdo remapnn,%s %s %s" % (resource, masks[mask], mask_rm)
      masks[mask] = mask_rm
      call = "cdo div '%s' '%s' '%s'" % ( resource , masks[mask], nc_remap)
      system(call)
    except  Exception as e:
      print 'remaped masking failed %s' % (e)
  return nc_remap
  