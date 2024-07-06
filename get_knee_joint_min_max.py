import pandas as pd

def get_knee_joint_min_max(marker_file_path, angle_file_path):
    header_row = 7 # ヘッダー行(シートの番号-1)
    cog_z_column_name = 'COG(全身)(z)'

    r_knee_joint_angle_column_name = 'R 膝関節 外反(＋)⇔内反(−)' # シートからコピペすると-の文字コードが違うので注意
    l_knee_joint_angle_column_name = 'L 膝関節 外反(＋)⇔内反(−)'

    marker_df = pd.read_csv(marker_file_path, encoding="shift-jis", header=header_row)
    angle_df = pd.read_csv(angle_file_path, encoding="shift-jis", header=header_row)

    cog_z_column = marker_df[cog_z_column_name]
    print('cog(z)の列を取得==>\n', cog_z_column)

    min_cog_z = cog_z_column.min()
    print('COGの最小値==>\n', min_cog_z)

    min_cog_z_index = marker_df[cog_z_column == min_cog_z].index[0]
    print('COGの最小の行==>\n', min_cog_z_index)

    angle_df_to_min_cog_z = angle_df.loc[:min_cog_z_index]
    print('COGが最小になるまでの角度の表==>\n', angle_df_to_min_cog_z)

    r_knee_joint_angle_column = angle_df_to_min_cog_z[r_knee_joint_angle_column_name]
    print('R膝関節の列を取得==>\n', r_knee_joint_angle_column)

    l_knee_joint_angle_column = angle_df_to_min_cog_z[l_knee_joint_angle_column_name]
    print('L膝関節の列を取得==>\n', l_knee_joint_angle_column)

    max_r_knee_joint_angle = r_knee_joint_angle_column.max()
    print('R膝関節の最大値==>\n', max_r_knee_joint_angle)

    min_r_knee_joint_angle = r_knee_joint_angle_column.min()
    print('R膝関節の最小値==>\n', min_r_knee_joint_angle)

    max_l_knee_joint_angle = l_knee_joint_angle_column.max()
    print('L膝関節の最大値==>\n', max_l_knee_joint_angle)

    min_l_knee_joint_angle = l_knee_joint_angle_column.min()
    print('L膝関節の最小値==>\n', min_l_knee_joint_angle)

    return max_r_knee_joint_angle, min_r_knee_joint_angle, max_l_knee_joint_angle, min_l_knee_joint_angle
