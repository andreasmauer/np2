import np2user
import np2report
import np2config
import np2crawler

# I need a router as function that define which function should be shooted for each report


class Controller:

    def __init__(self):

        # instanciate all the objects
        self.User = np2user.Input()
        self.Report = np2report.Report()
        self.Crawler = np2crawler.Crawler()

        # then route the control to the reports
        self.router()

    def router(self):



        if self.User.get('reporttype') == 'single keyword':
            self.single_keyword_report()

        elif self.User.get('reporttype') == 'multiple keywords':
            self.multiple_keywords_report()

        elif self.User.get('reporttype') == 'full category':
            self.full_category_report()

        elif self.User.get('reporttype') == 'categories':
            self.categories_report()

        elif self.User.get('reporttype') == 'regex':
            self.regex_report()




    def single_keyword_report(self):

        # crawl the csvs
        self.Crawler.crawl(self.User.get('path'), self.User.get('weeks'),
            [self.User.get('single_keyword')], ['negative values here'], 'just', 'groupname')
        
        # print in report
        self.Report.restore(self.User.get('path'), self.User.get('filename_of_report'))

        self.Report.print_dictionary(self.User.get('reporttype'), np2config.variables['kpis'],
            self.User.get('weeks'), self.Crawler.kpis)

    def multiple_keywords_report(self):


        # crawl the csvs
        self.Crawler.crawl(self.User.get('path'), self.User.get('weeks'),
            self.User.get('multiple_keywords'), ['negative values here'], 'just', 'no-groupname')
        
        # print in report
        self.Report.restore(self.User.get('path'), self.User.get('filename_of_report'))

        self.Report.print_dictionary(self.User.get('reporttype'), np2config.variables['kpis'],
            self.User.get('weeks'), self.Crawler.kpis)

    def categories_report(self):



        # crawl the csvs
        self.Crawler.crawl(self.User.get('path'), self.User.get('weeks'),
            ['spex', 'mister'], ['negative values here'], 'consolidated_init', 'brand')

        self.Crawler.crawl(self.User.get('path'), self.User.get('weeks'),
            ['brille'], ['sonne'], 'consolidated_init', 'brille')
        
        # print in report
        self.Report.restore(self.User.get('path'), self.User.get('filename_of_report'))

        self.Report.print_dictionary(self.User.get('reporttype'), np2config.variables['kpis'],
            self.User.get('weeks'), self.Crawler.kpis)

    def full_category_report(self):


        # crawl the csvs
        self.Crawler.crawl(self.User.get('path'), self.User.get('weeks'),
            [self.User.get('category')], ['negative values here'], 'init', 'no-groupname')

        # print in report
        self.Report.restore(self.User.get('path'), self.User.get('filename_of_report'))

        self.Report.print_dictionary(self.User.get('reporttype'), np2config.variables['kpis'],
            self.User.get('weeks'), self.Crawler.kpis)

    def keyword_in_report(self):

        pass




    def regex_report(self):

        # crawl the csvs
        self.Crawler.crawl(self.User.get('path'), self.User.get('weeks'),
            self.User.get('regex'), ['negative values here'], 'regex', 'no-groupname')


        # print in report
        self.Report.restore(self.User.get('path'), self.User.get('filename_of_report'))

        self.Report.print_dictionary(self.User.get('reporttype'), np2config.variables['kpis'],
            self.User.get('weeks'), self.Crawler.kpis)


a = Controller()










