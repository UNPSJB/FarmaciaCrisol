###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2015, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):
        self.maxDiff = None

        filename = 'excel2003_style08.xlsx'

        test_dir = 'xlsxwriter/test/comparison/'
        self.got_filename = test_dir + '_test_' + filename
        self.exp_filename = test_dir + 'xlsx_files/' + filename

        self.ignore_files = []
        self.ignore_elements = {}

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file."""

        workbook = Workbook(self.got_filename, {'excel2003_style': True})

        worksheet = workbook.add_worksheet()

        courier = workbook.add_format({'font_name': 'Courier',
                                       'font_size': 8,
                                       'font_family': 3})

        worksheet.write('A1', 'Foo')
        worksheet.write('A2', 'Bar', courier)

        workbook.close()

        self.assertExcelEqual()
