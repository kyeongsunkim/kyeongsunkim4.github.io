# Boilerplate
import numpy as np
from plxscripting.easy import *
import pandas as pd
import time

start_time = time.perf_counter()

def main(arg):
    print("START OF MAIN()")

    # Initialize Output server
    #s_o, g_o = new_server('localhost', 10000, password='Ntf$m5vs6U^x=a+!')
    #print("CONNECTED TO PLAXIS OUTPUT SERVER")

    # Define ResultTypes
    x_, y_, z_ = g_o.ResultTypes.RigidBody.XRef, g_o.ResultTypes.RigidBody.YRef, g_o.ResultTypes.RigidBody.ZRef
    Ux_, Uy_, Uz_ = g_o.ResultTypes.RigidBody.Ux, g_o.ResultTypes.RigidBody.Uy, g_o.ResultTypes.RigidBody.Uz
    Fx_, Fy_, Fz_ = g_o.ResultTypes.RigidBody.Fxreaction, g_o.ResultTypes.RigidBody.Fyreaction, g_o.ResultTypes.RigidBody.Fzreaction
    Rotx_, Roty_, Rotz_ = g_o.ResultTypes.RigidBody.phix, g_o.ResultTypes.RigidBody.phiy, g_o.ResultTypes.RigidBody.phiz
    Mx_, My_, Mz_ = g_o.ResultTypes.RigidBody.Mxreaction, g_o.ResultTypes.RigidBody.Myreaction, g_o.ResultTypes.RigidBody.Mzreaction

    # Define reference point of bucket1 at phase1
    bucket1 = g_o.RigidBodies[0][0]
    phase1 = g_o.Phases[2]
    step1 = g_o.Phases[2][arg]
    x_ref, y_ref, z_ref = g_o.getresults(bucket1, phase1, x_, "node"), g_o.getresults(bucket1, phase1, y_, "node"), g_o.getresults(bucket1, phase1, z_, "node")
    nparray = np.array([x_ref, y_ref, z_ref])
    ref_bucket1 = tuple(nparray.reshape(1, -1)[0])
    step_name = step1.Name
    phase_name = phase1.Name
    print(phase_name, step_name)
    print(f'bucket1 is located at : {ref_bucket1}')

    # get results of bucket 1
    Ux = g_o.getsingleresult(step1, Ux_, ref_bucket1)
    Uy = g_o.getsingleresult(step1, Uy_, ref_bucket1)
    Uz = g_o.getsingleresult(step1, Uz_, ref_bucket1)
    Fx = g_o.getsingleresult(step1, Fx_, ref_bucket1)
    Fy = g_o.getsingleresult(step1, Fy_, ref_bucket1)
    Fz = g_o.getsingleresult(step1, Fz_, ref_bucket1)
    Mx = g_o.getsingleresult(step1, Mx_, ref_bucket1)
    My = g_o.getsingleresult(step1, My_, ref_bucket1)
    Mz = g_o.getsingleresult(step1, Mz_, ref_bucket1)
    Rotx = g_o.getsingleresult(step1, Rotx_, ref_bucket1)
    Roty = g_o.getsingleresult(step1, Roty_, ref_bucket1)
    Rotz = g_o.getsingleresult(step1, Rotz_, ref_bucket1)

    print(f'Ux : {Ux}, Uy : {Uy}, Uz : {Uz}')
    print(f'Fx : {Fx}, Fy : {Fy}, Fz : {Fz}')
    print(f'Mx : {Mx}, My : {My}, Mz : {Mz}')
    print(f'Rotx : {Rotx}, Roty : {Roty}, Rotz : {Rotz}')

    # Loop over Dictionary
    mydict = {"Phase": 2, "Step": i, "Ux": Ux, "Uy": Uy, "Uz": Uz, "Fx": Fx, "Fy": Fy, "Fz": Fz, "Mx": Mx, "My": My, "Mz": Mz, "Rotx": Rotx,
            "Roty": Roty, "Rotz": Rotz}
    return mydict
    print("END OF MAIN()")

if __name__ == "__main__":
    s_o, g_o = new_server('localhost', 10000, password='Ntf$m5vs6U^x=a+!')
    print("CONNECTED TO PLAXIS OUTPUT SERVER")

    lst = g_o.Phases[2].ID
    print(f'Total number of steps : {len(lst)}')
    mydict = {}
    for i in range(len(lst)):
        print(f'i = {i}')
        ans = main(i)
        for key, val in ans.items():
            try:
                mydict[key].append(val)
            except KeyError:
                mydict[key] = [val]
        print(mydict)

    print("END OF IF NAME==MAIN")

    # Convert dictionary to dataframe
    df = pd.DataFrame.from_dict(mydict)
    print(df)
    filename = r'C:\Users\Admin\Desktop\pytools\kyeongsunkim.github.io\saved\saved.csv'
    df.to_csv(filename, index=False)

end_time = time.perf_counter()
print(f"Duration is {end_time-start_time} sec")