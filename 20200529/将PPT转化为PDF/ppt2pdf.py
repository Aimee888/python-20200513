#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> ppt2pdf.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/29 16:39
@Desc    :将PPT转换为PDF。
        参考链接：https://www.cnblogs.com/Ghost-bird/p/10530256.html
================================================="""
import comtypes.client
import os


def init_powerpoint():
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    return powerpoint


def ppt_to_pdf(powerpoint, inputFileName, outputFileName, formatType=32):
    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType)  # formatType = 32 for ppt to pdf
    deck.Close()


def convert_files_in_folder(powerpoint, folder):
    ppt_folder = folder + "\PPT"
    pdf_folder = folder + "\PDF"
    files = os.listdir(ppt_folder)
    pptfiles = [f for f in files if f.endswith((".ppt", ".pptx"))]
    for pptfile in pptfiles:
        ppt_fullpath = os.path.join(ppt_folder, pptfile)
        pdf_fullpath = os.path.join(pdf_folder, pptfile[:-4] + "pdf")
        ppt_to_pdf(powerpoint, ppt_fullpath, pdf_fullpath)


if __name__ == "__main__":
    powerpoint = init_powerpoint()
    cwd = os.getcwd()
    convert_files_in_folder(powerpoint, cwd)
    powerpoint.Quit()
