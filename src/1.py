import adata

df = adata.stock.info.all_code()

print(df.head(5))
print(df.shape)