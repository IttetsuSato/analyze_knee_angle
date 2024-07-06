import os
from get_knee_joint_min_max import get_knee_joint_min_max

# result.csvを初期化
with open('result.csv', 'w') as f:
    f.write('ファイルid,R膝関節の最大値,R膝関節の最小値,L膝関節の最大値,L膝関節の最小値\n')

# ./dataからファイル一覧を取得
files = os.listdir('./data')

# ファイルごとに処理
for file in files:
    # ファイル名にAngleが含まれていたら処理をスキップ
    if 'Angle' in file:
        continue
    
    # ファイル名からid部分を取得
    file_id = file.split('_')[0]
    print(file_id)

    marker_file_path = f'./data/{file_id}_Marker.csv'
    angle_file_path = f'./data/{file_id}_Angle.csv'

    max_r_angle, min_r_angle, max_l_angle, min_l_angle= get_knee_joint_min_max(marker_file_path, angle_file_path)

    # result.csvに出力
    with open('result.csv', 'a') as f:
        f.write(f'{file_id},{max_r_angle},{min_r_angle},{max_l_angle},{min_l_angle}\n')

print('処理が完了しました。result.csvを確認してください。')

