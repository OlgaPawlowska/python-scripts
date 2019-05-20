last_start = None
region_start = None
for _, row in pirna_lps5[pirna_lps5['scf'] == 'Scf_X_assembled'][['start', 'stop']].iterrows():
    if last_start == None:
        last_start = row['start']
        region_start = last_start
    if row['start'] - last_start > 1000 :
        print(region_start, last_start+5000)
        region_start = row['start']
    last_start = row['start']
    