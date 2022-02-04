import pandas as pd
import os, glob


def data_cleaning(file, save_local, file_name, month_name):

    # DataFrame Refactoring
    df = pd.read_csv(file, encoding='ISO=8859-1', sep=';')

    colunas = {
        'Data': 'Data',
        '24 - Captação líquida diária de depósitos de poupança - SBPE e rural - u.m.c. (mil)': 'Captação diária de poupança - mil'
        }

    df = df.rename(columns=colunas)
    
    # Deleting the last row
    df = df[:-1]

    # Refactoring the data values
    df['Captação diária de poupança - mil'] = df['Captação diária de poupança - mil'].str.replace(',', '')
    df['Captação diária de poupança - mil'] = df['Captação diária de poupança - mil'].str.replace(r'.', '')
    df['Captação diária de poupança - mil'] = pd.to_numeric(df['Captação diária de poupança - mil'])

    # Obtaining the sum of all values
    total = df['Captação diária de poupança - mil'].sum()
    df['Captação mensal acumulada - mil'] = total

    # Removing duplicated values
    df['Captação mensal acumulada - mil'] = df['Captação mensal acumulada - mil'].mask(df.duplicated(['Captação mensal acumulada - mil']))

    print('Tratamento realizado com sucesso!')
    return df.to_csv(f'{save_local}{file_name}{month_name}.csv', index=False, encoding='utf-8-sig', decimal=',', sep=';')