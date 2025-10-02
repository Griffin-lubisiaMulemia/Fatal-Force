import nbformat as nbf

nb = nbf.read('Fatal_Force_(start).ipynb', nbf.NO_CONVERT)

# Find the index of the cell with plt.show() in the line chart
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and 'plt.show()' in ''.join(cell.source):
        break

# Insert after i
new_cell = nbf.v4.new_code_cell("""# Visualise the relationship using jointplot
df_relationship = pd.DataFrame({
    'Geographic Area': state_poverty.index,
    'poverty_rate': state_poverty.values,
    'hs_completion': state_hs_completion.values
})
sns.jointplot(data=df_relationship, x='poverty_rate', y='hs_completion', kind='scatter', marginal_kws={'kind': 'kde'})
plt.show()""")

nb.cells.insert(i+1, new_cell)

nbf.write(nb, 'Fatal_Force_(start).ipynb')
