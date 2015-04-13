import csv

class Report:

    def restore(self, path, filename_of_report):
        self.where = path + '/' + filename_of_report

    def append_new_row(self, row_to_write):
        
        with open(self.where, 'a') as f:
            mycsv = csv.writer(f, delimiter=',', lineterminator='\n')
            mycsv.writerow(row_to_write)

    def print_general_headers_in_csv(self, reporttype):

        self.append_new_row([reporttype])
        self.append_new_row('')
        self.append_new_row('')

    def print_weeks_line(self, weeks):

        weeks_line = list(weeks)
        weeks_line.insert(0, 'week')
        self.append_new_row(weeks_line)


    def print_kpi_line(self, kpis_per_week, first_column_str):

        # this is wrong I shouldnt manipulate the object, same as the print_weeks_line
        
        kpis_per_week_line = list(kpis_per_week)
        kpis_per_week_line.insert(0, first_column_str)
        self.append_new_row(kpis_per_week_line)

    def print_dictionary(self, reporttype, kpi_names_tuple, weeks, dictionary):

        # check which kpis do I have to print
        self.print_general_headers_in_csv(reporttype)
        

        # for each kpi we create a block 
        i = 0
        for kpi_name in kpi_names_tuple:
            
            self.append_new_row([kpi_names_tuple[i]])
            self.print_weeks_line(weeks)

            # I print the kpis
            for keyword in dictionary:
                weekly_line_to_print = []

                # for each week I take the value needed and pass it to the print_kpi_line function
                # there are cases where I dont have values for that week, therefore I print 0
                for week in weeks:
                    try:
                        weekly_line_to_print.append(dictionary[keyword][kpi_name][week])
                    except:
                        weekly_line_to_print.append(0.0)

                self.print_kpi_line(weekly_line_to_print, keyword)


            i = i + 1

            # print an empty line to separate:
            self.append_new_row('')

        print 'the report is done on the path' + self.where