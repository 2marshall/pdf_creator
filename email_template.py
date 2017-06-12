import sys
import os
import time
import datetime
from dateutil.relativedelta import *
from fpdf import FPDF
import glob

# Creating Up Front Variables

email_to = 'palger@crexendo.com'
prior_month = datetime.datetime.now() - relativedelta(months=1)
prior_month_name = prior_month.strftime("%B")
prior_month_year = prior_month.year
monthly_line_item_desc = ('{prior_month_name} {prior_month_year} Network Support Retainer'.format(prior_month_name=prior_month_name, prior_month_year=prior_month_year))
today = datetime.date.today()
today_month = today.month
today_day = today.day
today_year = today.year
today_month_name = today.strftime("%B")
date_of_invoice = ('{today_month}{today_day}{today_year}'.format(today_month=today_month, today_day=today_day, today_year=today_year))

# Generating the Invoice Number

invoice_file = glob.glob('inv*')
invoice_file_rename = invoice_file[0].replace('inv', '')
invoice_number_old_int = int(invoice_file_rename)
invoice_filename_old_str = str(invoice_file[0])
invoice_number_new_int = int(invoice_file_rename) + 1
invoice_number_new_str = str(invoice_number_new_int)
invoice_filename_new_str = ('inv{invoice_number_new_str}'.format(invoice_number_new_str=invoice_number_new_str))

# Removing Old invXXX File and Creating New

os.system('rm -f {invoice_filename_old_str}'.format(invoice_filename_old_str=invoice_filename_old_str))
os.system('touch {invoice_filename_new_str}'.format(invoice_filename_new_str=invoice_filename_new_str))


# Entering in PDF Filename

pdf_filename = ('crexendo-invoice-{invoice_number_new_str}-{date_of_invoice}.pdf'.format(invoice_number_new_str=invoice_number_new_str, date_of_invoice=date_of_invoice))


# Assigning Class to pdf object and Setting up Page Settings

pdf = FPDF()
pdf.set_margins(12.0, 30.0, 12.0)
pdf.add_page()

# Adding Invoice Specific Data . Date and Invoice #

pdf.set_font('Helvetica', 'B', 25)
pdf.cell(w = 0, h = 0, txt='INVOICE', border = 0, ln = 1, align = 'R', fill = False, link = '')
pdf.cell(w = 50, h = 15, txt='', border = 0, ln = 1, align = 'L', fill = False, link = '')

# Writing Date and Invoice# Sections

pdf.set_font('Helvetica', 'B', 15)
pdf.cell(w = 125, h = 12, txt='', border = 0, ln = 0, align = 'L', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt='Date', border = 1, ln = 0, align = 'C', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt='Invoice #', border = 1, ln = 1, align = 'C', fill = False, link = '')

# Input Date Variable function to calculate the current date this pdf is being created

invoice_date = ("{today_month}/{today_day}/{today_year}".format(today_month=today_month, today_day=today_day, today_year=today_year))
pdf.set_font('Courier', '', 8)
pdf.cell(w = 125, h = 12, txt='', border = 0, ln = 0, align = 'L', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt=invoice_date, border = 1, ln = 0, align = 'C', fill = False, link = '')

# Input Invoice number Here

pdf.cell(w = 30, h = 10, txt=invoice_number_new_str, border = 1, ln = 1, align = 'C', fill = False, link = '')
pdf.cell(w = 50, h = 15, txt='', border = 0, ln = 1, align = 'L', fill = False, link = '')

# Setting Company Address

pdf.set_font('Arial', '', 12)
pdf.cell(w = 50, h = 5, txt='The Computer Man LLC', border = 0, ln = 1, align = 'L', fill = False, link = '')
pdf.cell(w = 50, h = 5, txt='916 N Allen Circle', border = 0, ln = 1, align = 'L', fill = False, link = '')
pdf.cell(w = 50, h = 5, txt='Mesa AZ, 85203', border = 0, ln = 1, align = 'L', fill = False, link = '')
pdf.cell(w = 50, h = 5, txt='(480)862-5579', border = 0, ln = 1, align = 'L', fill = False, link = '')
pdf.cell(w = 50, h = 12, txt='', border = 0, ln = 1, align = 'L', fill = False, link = '')

# Setting Bill To: Address

pdf.set_font('Helvetica', 'B', 15)
pdf.cell(w = 50, h = 15, txt='Bill To:', border = 0, ln = 1, align = 'L', fill = False, link = '')
pdf.set_font('Arial', '', 12)
pdf.cell(w = 50, h = 5, txt='Crexendo Inc.', border = 0, ln = 1, align = 'L', fill = False, link = '')
pdf.cell(w = 50, h = 5, txt='1615 S. 52nd Street', border = 0, ln = 1, align = 'L', fill = False, link = '')
pdf.cell(w = 50, h = 5, txt='Tempe, AZ 85281', border = 0, ln = 1, align = 'L', fill = False, link = '')
pdf.cell(w = 50, h = 15, txt='', border = 0, ln = 1, align = 'L', fill = False, link = '')

# Entering in Line Item expenses

pdf.set_font('Helvetica', 'B', 15)
pdf.cell(w = 30, h = 10, txt='Date', border = 1, ln = 0, align = 'C', fill = False, link = '')
pdf.cell(w = 60, h = 10, txt='Description', border = 1, ln = 0, align = 'C', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt='Hours', border = 1, ln = 0, align = 'C', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt='Rate', border = 1, ln = 0, align = 'C', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt='Amount', border = 1, ln = 1, align = 'C', fill = False, link = '')

pdf.set_font('Courier', '', 8)
pdf.cell(w = 30, h = 10, txt=invoice_date, border = 0, ln = 0, align = 'L', fill = False, link = '')
pdf.cell(w = 60, h = 10, txt=monthly_line_item_desc, border = 0, ln = 0, align = 'L', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt='1.00', border = 0, ln = 0, align = 'R', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt='800.00', border = 0, ln = 0, align = 'R', fill = False, link = '')
pdf.cell(w = 30, h = 10, txt='800.00', border = 0, ln = 1, align = 'R', fill = False, link = '')
pdf.cell(w = 50, h = 20, txt='', border = 0, ln = 1, align = 'L', fill = False, link = '')

pdf.set_font('Helvetica', 'B', 15)
pdf.cell(w = 115, h = 10, txt='', border = 0, ln = 0, align = 'R', fill = False, link = '')
pdf.cell(w = 40, h = 10, txt='Total', border = 0, ln = 0, align = 'L', fill = False, link = '')
pdf.set_font('Courier', '', 8)
pdf.cell(w = 25, h = 10, txt='$800.00', border = 0, ln = 1, align = 'R', fill = False, link = '')
pdf.set_font('Helvetica', 'B', 15)
pdf.cell(w = 115, h = 10, txt='', border = 0, ln = 0, align = 'R', fill = False, link = '')
pdf.cell(w = 40, h = 10, txt='Balance Due', border = 0, ln = 0, align = 'L', fill = False, link = '')
pdf.set_font('Courier', '', 8)
pdf.cell(w = 25, h = 10, txt='$800.00', border = 0, ln = 1, align = 'R', fill = False, link = '')
pdf.cell(w = 30, h = 35, txt='', border = 0, ln = 1, align = 'L', fill = False, link = '')


pdf.set_font('Arial', '', 15)
pdf.cell(w = 175, h = 15, txt='Make check payable to The Computer Man LLC', border = 0, ln = 1, align = 'C', fill = False, link = '')


# Writing above formatting to pdf file and sending invoice

pdf.output(pdf_filename, 'F')

os.system('uuencode {pdf_filename} {pdf_filename} | mail -a "From: jesseshumaker@gmail.com" -s "Crexendo Network Support Invoice - {invoice_number_new_str} - {today_month}/{today_day}/{today_year}" {email_to}'.format(pdf_filename=pdf_filename, invoice_number_new_str=invoice_number_new_str, today_month=today_month, today_day=today_day, today_year=today_year, email_to=email_to))






