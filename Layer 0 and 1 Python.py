import pandas as pd
import numpy as np
np.random.seed(42)
agences = [f'AGENCE {i}' for i in range(1, 18)]

objectifs_conso = {'AGENCE 1': 1500000, 'AGENCE 2': 900000, 'AGENCE 3': 1550000, 'AGENCE 4': 1300000, 'AGENCE 5': 1300000,
                    'AGENCE 6': 1100000, 'AGENCE 7': 600000, 'AGENCE 8': 900000, 'AGENCE 9': 600000, 'AGENCE 10': 600000,
                      'AGENCE 11': 750000,'AGENCE 12': 700000, 'AGENCE 13': 750000, 'AGENCE 14': 800000, 'AGENCE 15': 600000,
                        'AGENCE 16': 700000, 'AGENCE 17': 800000}

objectifs_immo = {'AGENCE 1': 1000000, 'AGENCE 2': 150000, 'AGENCE 3': 1100000, 'AGENCE 4': 700000, 'AGENCE 5': 600000,
                   'AGENCE 6': 150000, 'AGENCE 7': 200000, 'AGENCE 8': 500000, 'AGENCE 9': 700000, 'AGENCE 10': 650000,
                     'AGENCE 11': 350000, 'AGENCE 12': 100000, 'AGENCE 13': 250000, 'AGENCE 14': 800000, 'AGENCE 15': 200000,
                       'AGENCE 16': 150000, 'AGENCE 17': 200000}

tro_annuel_conso = {'AGENCE 1': 78, 'AGENCE 2': 17, 'AGENCE 3': 45, 'AGENCE 4': 42, 'AGENCE 5': 38, 'AGENCE 6': 8, 'AGENCE 7': 60,
                     'AGENCE 8': 42, 'AGENCE 9': 115, 'AGENCE 10': 72, 'AGENCE 11': 36, 'AGENCE 12': 32, 'AGENCE 13': 26, 'AGENCE 14': 67,
                       'AGENCE 15': 48, 'AGENCE 16': 34, 'AGENCE 17': 28}

months = ['JANVIER', 'FEVRIER', 'MARS', 'AVRIL', 'MAI', 'JUIN']

month_nums = {'JANVIER': 1, 'FEVRIER': 2, 'MARS': 3, 'AVRIL': 4, 'MAI': 5, 'JUIN': 6}

def generate_credit_month(agence, objectif, tro_annual, month, credit_type='Conso'):
    perf_level = tro_annual / 100
    obj = int(objectif * np.random.uniform(0.8, 1.2))
    pipe_dossier = np.random.randint(2, 10)
    pipe_montant = int(pipe_dossier * np.random.uniform(80000, 300000))
    etude_dossier = np.random.randint(0, pipe_dossier)
    etude_montant = int(etude_dossier * np.random.uniform(80000, 200000))
    center = 1.0 + (perf_level - 0.5) * 0.4
    dbl_rate = max(0, np.random.uniform(center - 0.35, center + 0.35))
    dbl_montant = int(obj * dbl_rate)
    dbl_dossier = max(0, int(dbl_montant / np.random.uniform(80000, 200000)))
    tro_mensuel = round(dbl_montant / obj * 100 if obj > 0 else 0, 1)
    hit_objective = 'Yes' if dbl_montant >= obj else 'No'
    construction_dossier = np.random.randint(0, 3) if credit_type == 'Immo' else None
    construction_montant = int(construction_dossier * np.random.uniform(100000, 500000)) if credit_type == 'Immo' else None

    row = {'AGENCE': agence, 'Mois': month, 'Mois_Num': month_nums[month], 'Credit_Type': credit_type, 'PIPE_Dossier': pipe_dossier,
            'PIPE_Montant': pipe_montant, 'PIPE_ETUDE_Dossier': etude_dossier, 'PIPE_ETUDE_Montant': etude_montant, 
            'DBL_Dossier': dbl_dossier, 'DBL_Montant': dbl_montant, 'OBJECTIF_Mensuel': obj, 'TRO_Mensuel_%': tro_mensuel, 
            'TRO_Annuel_%': tro_annual, 'Hit_Objective': hit_objective, 'Ratio_DBL_Objectif': round(dbl_montant / obj, 3) if obj > 0 else 0,
              'Ratio_Pipe_Objectif': round(pipe_montant / obj, 3) if obj > 0 else 0}
    
    if credit_type == 'Immo':
        row['Construction_Dossier'] = construction_dossier
        row['Construction_Montant'] = construction_montant
    return row

all_rows = []
for month in months:
    for agence in agences:
        row_conso = generate_credit_month(agence, objectifs_conso[agence], tro_annuel_conso[agence], month, 'Conso')
        all_rows.append(row_conso)
        row_immo = generate_credit_month(agence, objectifs_immo[agence], tro_annuel_conso.get(agence, 50), month, 'Immo')
        all_rows.append(row_immo)
df = pd.DataFrame(all_rows)
print('=== CREDIT HISTORY DATASET ===')
print(f'Shape: {df.shape}')
print(f'Months: {df['Mois'].unique()}')
print(f'Hit rate: {(df['Hit_Objective'] == 'Yes').mean():.1%}')
print('\nSample:')
print(df[df['Credit_Type'] == 'Conso'].head(6)[['AGENCE', 'Mois', 'PIPE_Dossier', 'DBL_Dossier', 'OBJECTIF_Mensuel', 'TRO_Mensuel_%',
                                                 'Hit_Objective']].to_string())
df['DBL_Partiel_Dossier'] = (df['DBL_Dossier'] * np.random.uniform(0.4, 0.5, len(df))).astype(int)
df['DBL_Partiel_Montant'] = (df['DBL_Montant'] * np.random.uniform(0.4, 0.5, len(df))).astype(int)
df['TRO_Partiel_%'] = (df['DBL_Partiel_Montant'] / df['OBJECTIF_Mensuel'] * 100).round(1)
DAYS_ELAPSED = 10
DAYS_TOTAL = 22
df['DBL_Predit_FinMois'] = (df['DBL_Partiel_Montant'] / DAYS_ELAPSED * DAYS_TOTAL).astype(int)
df['TRO_Predit_%'] = (df['DBL_Predit_FinMois'] / df['OBJECTIF_Mensuel'] * 100).round(1)

def classify(row):
    tro = row['TRO_Predit_%']
    if tro >= 80:
        return 'On Track'
    elif tro >= 50:
        return 'At Risk'
    else:
        return 'Will Miss'
df['Statut_Predit'] = df.apply(classify, axis=1)
print('\n=== STATUS DISTRIBUTION ===')
print(df['Statut_Predit'].value_counts())
train_df = df[df['Mois_Num'] <= 5]
test_df = df[df['Mois_Num'] == 6]
print(f'\nTrain: {len(train_df)} rows, hit rate {(train_df['Hit_Objective'] == 'Yes').mean():.1%}')
print(f'Test: {len(test_df)} rows, hit rate {(test_df['Hit_Objective'] == 'Yes').mean():.1%}')
output = 'C:\\Users\\hp\\Desktop\\PFA\\6 Months\\Credit_ML_Dataset_v6.xlsx'
with pd.ExcelWriter(output, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Full_History', index=False)
    train_df.to_excel(writer, sheet_name='Train_JanMai', index=False)
    test_df.to_excel(writer, sheet_name='Test_Juin', index=False)
    
    feature_cols = ['AGENCE', 'Mois', 'Mois_Num', 'Credit_Type', 'PIPE_Dossier', 'PIPE_Montant', 'PIPE_ETUDE_Dossier',
                     'PIPE_ETUDE_Montant', 'DBL_Partiel_Dossier', 'DBL_Partiel_Montant', 'OBJECTIF_Mensuel', 'TRO_Annuel_%',
                       'TRO_Partiel_%', 'Ratio_Pipe_Objectif', 'DBL_Predit_FinMois', 'TRO_Predit_%', 'Hit_Objective', 'Statut_Predit']
    
    df[feature_cols].to_excel(writer, sheet_name='KNIME_Ready', index=False)
print(f'\nSaved to: {output}')
print('Sheets: Full_History, Train_JanMai, Test_Juin, KNIME_Ready')