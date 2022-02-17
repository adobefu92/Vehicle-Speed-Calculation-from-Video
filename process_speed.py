import pandas as pd
import numpy as np
import persepctiveTransform

def cal_distance(o,d):
    distance = np.sqrt((o[0]-d[0])**2 + (o[1]-d[1])**2)
    return(distance)


def cal_speed(trajectory,M):

    list_ID = trajectory['ID'].unique()
    list_ID

    i = 0
    for single_id in list_ID:
        single_veh = trajectory[trajectory['ID'] == single_id].sort_values(by='frame')
        single_veh = single_veh.reset_index(drop=True)
    #     print(single_veh)
        for idx, row in single_veh.iterrows():
        #     print(idx,row)
            ori_coord = np.float32([row['maxx'],row['maxy']])
            single_veh.loc[idx,['transformed_x','transformed_y']] = persepctiveTransform.transform_point(ori_coord,M)

            if idx > 0:
    #             print(idx-1)
                o = [single_veh.loc[idx-1,'transformed_x'], single_veh.loc[idx-1,'transformed_y']] 
                d = [single_veh.loc[idx,'transformed_x'], single_veh.loc[idx,'transformed_y']]
                single_veh.loc[idx,'distance'] = cal_distance(o, d)
                single_veh.loc[idx,'speed'] = single_veh.loc[idx,'distance']/(single_veh.loc[idx,'frame']-single_veh.loc[idx-1,'frame'])       
        if i == 0:
            df_speed = single_veh
        else: 
            df_speed = pd.concat([df_speed,single_veh], axis=0)
        i += 1
    return(df_speed)










