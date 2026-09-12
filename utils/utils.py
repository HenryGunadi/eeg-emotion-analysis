# extract unique column names
def extract_unique_cols(prefix, columns: list[str]):
  cols = []

  for col in columns:
    text = col.split(prefix)[0]

    if text and text not in cols:
      cols.append(text)

  return cols