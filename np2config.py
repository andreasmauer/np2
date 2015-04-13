import sys


# reports are hardcoded in the controller too

variables = {
    
    'keyword_categories': ['brille', 'sonne', 'linsen', 'brands', 'others', 'brand'],
    'reports': ['single keyword', 'multiple keywords', 'full category', 'categories', 'regex'],
    'path': '',
    'kpis': ('clicks', 'impressions', 'ranking', 'ctr'),
    'os': '', 

}

# depending if windows or mac I define different paths
if sys.platform == 'darwin':
    variables['path'] = r'/Users/andres/Documents/python/np/np2.0/'
    variables['os'] = 'darwin'
else:

    variables['path'] = r'R:\Marketing\Channels\SEO\Ongoing\Regularly - Weekly reports\python' + '\\'
    variables['os'] = 'windows'
