import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from openpyxl import load_workbook


def write_to_excel(x, y, path=''):
    writer = pd.ExcelWriter('ExcelFiles\y_naph_PRK_coethanol.xlsx', engine='openpyxl')
    wb = writer.book
    df = pd.DataFrame({'{}'.format(x): x},
                      {'{}'.format(y): y})
    df.to_excel(writer, index=False)
    wb.save('ExcelFiles\y_naph_PRK_coethanol.xlsx')

y_naph_eth = pd.read_excel('ExcelFiles\y_naph_PRK_coethanol.xlsx',)
print(y_naph_eth[1])

