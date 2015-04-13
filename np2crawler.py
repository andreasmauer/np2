import np2config
import sys
import csv
import re

class Crawler:


    def __init__(self):
        pass

        self.kpis = {}

        # store all the keywords and weeks that where crawled
        # self.keywords_crawled = [['kontaktlinsen', 21], ['kontaktlinsen', 22], ['sonnenbrillen', 21]]
        self.keywords_crawled = []




    def crawl(self, path, weeks, positives, negatives, how, group_name):

        for week in weeks:

            if np2config.variables['os'] == 'darwin':
                filepath = path + '/' + 'kw' + str(week) + '.csv'
            elif np2config.variables['os'] == 'windows':
                filepath = path + '\\' + 'kw' + str(week) + '.csv'
            
            with open(filepath, 'rb') as csvfile:
                
                csvfiletoread = csv.reader(csvfile, delimiter = ',')
                for row in csvfiletoread:

                    # the first row it is just bullshit from adwords, I have to jump it
                    if len(row) > 1 and row[0] != 'Search Result Type':


####################################################################################

                        # KEYWORD MAGIC
                            # 4 dif reports, init, consolidated_init, just, consolidated_just

####################################################################################



                        if how == 'init' and (any(element in row[1] for element in positives)) and (any(element not in row[1] for element in negatives)):
                            # print str(week) + ' ' + row[1]

                            self.keywords_crawled.append([row[1], week])

                            self.magic_crawl(row, week, how, group_name)

        

                        
                        elif how == 'consolidated_init' and (any(element in row[1] for element in positives)) and (any(element not in row[1] for element in negatives)):

                            self.magic_crawl(row, week, how, group_name)



                        elif how == 'just' and (any(element == row[1] for element in positives)):    
                            

                            self.magic_crawl(row, week, how, group_name)



                        elif how == 'consolidated_just' and (any(element == row[1] for element in positives)):

                            self.magic_crawl(row, week, how, group_name)



                        elif how == 'regex' and (re.search(positives, row[1])):

                            self.magic_crawl(row, week, how, group_name)


            print 'crawling for week ' + week + ' done'


        # print self.kpis





    def magic_crawl(self, row, week, how, group_name):


        # define keyword vs group_name
        if (how == 'init') or (how == 'just') or (how == 'regex'):

            keyword = row[1]

        elif (how == 'consolidated_init') or (how == 'consolidated_just'):

            keyword = group_name


        # check if keyword exists & update if not
        if keyword not in self.kpis:

        # the ctr is always tricky to set becaused x / 0
            try:     
                ctr = round(float(row[7].replace(",", ".")) / float(row[8].replace(",", ".")), 2)

            except:
                ctr = 0.0

        # update the self.kpis
            self.kpis.update({keyword: {
                'clicks': {week: float(row[7].replace(",", "."))},
                'impressions': {week: float(row[8].replace(",", "."))},
                'rankingbruto': {week: (float(row[8].replace(",", ".")) * float(row[11].replace(",", ".")))},
                'ranking': {week: float(row[11].replace(",", "."))},
                'ctr': {week: ctr}}})

        # check if week exists & pass values
        elif week in self.kpis[keyword]['clicks']:

            self.kpis[keyword]['clicks'][week] = self.kpis[keyword]['clicks'][week] + float(row[7].replace(",", "."))
            self.kpis[keyword]['impressions'][week] = self.kpis[keyword]['impressions'][week] + float(row[8].replace(",", "."))
            self.kpis[keyword]['rankingbruto'][week] = self.kpis[keyword]['rankingbruto'][week] + (float(row[8].replace(",", ".")) * float(row[11].replace(",", ".")))
            
            try:
                self.kpis[keyword]['ranking'][week] = float(self.kpis[keyword]['rankingbruto'][week] / self.kpis[keyword]['impressions'][week])
            except:
                self.kpis[keyword]['ranking'][week] = 0.0
            try:
                self.kpis[keyword]['ctr'][week] = float(self.kpis[keyword]['clicks'][week] / self.kpis[keyword]['impressions'][week])
            except:
                self.kpis[keyword]['ctr'][week] = 0.0


        # if not then I update
        else:

            try: 
                ctr = float(row[7].replace(",", ".")) / float(row[8].replace(",", "."))
            except:
                ctr = 0.0

            self.kpis[keyword]['clicks'].update({week: float(row[7].replace(",", "."))})
            self.kpis[keyword]['impressions'].update({week: float(row[8].replace(",", "."))})
            self.kpis[keyword]['rankingbruto'].update({week: float(row[8].replace(",", ".")) * float(row[11].replace(",", "."))})
            self.kpis[keyword]['ranking'].update({week: float(row[11].replace(",", "."))})
            self.kpis[keyword]['ctr'].update({week: ctr})













