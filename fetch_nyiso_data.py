from nyisotoolkit import NYISOData

df_prices = NYISOData(dataset="lbmp_rt_5m", year="2023").df
df_dam = NYISOData(dataset="lbmp_dam_h", year="2023").df
df_load = NYISOData(dataset="load_5m", year="2023").df
