from selenium import webdriver
import unittest
from cStringIO import StringIO

class Report(object):
    _report_string=None

    def __init__(self):
        self._report_string=""
    def WriteReportHeader(self):
        self._report_string+="<html><header><title>Test result report</title></header></body>"
        self._report_string +="<table borde=\"2\">"
        self._report_string +="<tr>"
        self._report_string +="<td>TestID</td>"
        self._report_string += "<td>Title</td>"
        self._report_string += "<td>Steps</td>"
        self._report_string += "<td>ER</td>"
        self._report_string += "<td>AR</td>"
        self._report_string += "<td>PASS/FAIL</td>"
        self._report_string += "<td>Notes</td>"
        self._report_string += "</tr>"
    def AppentToReport(self,test_id,title,steps,er,ar,pass_fail,notes):
        if(pass_fail.lower()=="pass"):
            self._report_string+="<tr style=\"background-color:#33CC33\">"
        else:
            self._report_string += "<tr style=\"background-color:#FFFF00\">"
        self._report_string += "<td>"+ test_id + "</td>"
        self._report_string += "<td>" + title + "</td>"
        self._report_string += "<td>" + steps + "</td>"
        self._report_string += "<td>" + er + "</td>"
        self._report_string += "<td>" + ar + "</td>"
        self._report_string += "<td>" + pass_fail + "</td>"
        self._report_string += "<td>" + notes + "</td>"
        self._report_string += "</tr>"
    def WriteReportFooter(self):
        self._report_string+="</table></body></html>"
    def WriteToFile(self,filename):
        final_string=self._report_string
        print final_string
        report_file=open(filename,"w")
        report_file.write(final_string)
        report_file.close()

