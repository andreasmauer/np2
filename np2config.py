import sys


# reports are hardcoded in the controller too

variables = {
    
    'keyword_categories': ['brille', 'sonne', 'linsen', 'brands', 'others', 'brand'],
    'brands': ['adidas', 'arnette', 'blue bay', 'boss', 'brendel', 'burberry', 'carrera', 'chiemsee', 'ck', 'calvin', 'diesel', 'dkny', 'dolce', 'gabanna', 'd&g', 'dsquared', 'emporio', 'armani', 'escada', 'esprit', 'fossil', 'furla', 'gant', 'gucci', 'guess', 'hackett', 'humphreys', 'italia', 'jaguar', 'jee vice', 'jette joop', 'jil sander', 'joop', 'cavalli', 'karen', 'lacoste', 'le specs', 'loveyewear', 'lozza', 'jacobs', 'polo', 'mara', 'mexx', 'kors', 'michalsky', 'nike', 'nozomi', 'oakley', 'oxydo', 'persol', 'police', 'ralph', 'lauren', 'porsche', 'prada', 'puma', 'quicksilver', 'ray', 'ban', 'replay', 'rosy', 'belluni', 'scott', 'superdry', 'timberland', 'titanflex', 'ford', 'hilfiger', 'uvex', 'vogue', 'wood fellas', 'xray'],
    'reports': ['single keyword', 'multiple keywords', 'full category', 'categories', 'regex', 'test'],
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

