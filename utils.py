from disjoint_set import DisjointSet

def get_correlated_columns(corr_mat, thresh=0.8):
    corr_abs = corr_mat.abs()
    corr_vals = corr_abs.values
    col_names = corr_mat.columns

    # get correlated pairs
    corr_pairs = []

    for i in range(len(corr_vals) - 1):
        for j in range(i + 1, len(corr_vals)):
            if corr_vals[i][j] >= thresh:
                corr_pairs.append((i, j))

    # get the DisjointSet of the correlated columns
    ds = DisjointSet()

    for x, y in corr_pairs:
        ds.union(x, y)

    # for each disjoint set, get the first column as a representative
    # should replicate the behavior of drop_duplicate(keep="first") in a DataFrame
    keep_cols_idx = []
    remove_cols_idx = []
    for dis_set in ds.itersets():
        min_col_index = min(dis_set)
        dis_set.remove(min_col_index)

        keep_cols_idx.append(min_col_index)
        remove_cols_idx.extend(list(dis_set))

    keep_cols = col_names[keep_cols_idx]
    remove_cols = col_names[remove_cols_idx]

    return keep_cols, remove_cols



