import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from openpyxl import load_workbook


def write_to_excel(x, y, path='', x_head= 'x', y_head='y'):
    """ x: data,
        y: data,
        path: path/to/excelfile.xlsx
        x_head: name of the x header
        y_head: name of the y header
    """
    writer = pd.ExcelWriter(path, engine='openpyxl')
    wb = writer.book
    df = pd.DataFrame({'{}'.format(x_head): x,
                      '{}'.format(y_head): y})
    df.to_excel(writer, index=False)
    wb.save(path)



