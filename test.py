import time
import os
import signal
import subprocess

folder_names = ['android','computer', 'defcon', 'cat', 'defcon9', 'defcon12', 'defcon13','defconlogo','cube','free','hacked','heart','loading','mario','meeseeks','mrrobot','nyancat','pacman','pepe','pika','pokemon','pop','rick','static','throwupp','titan','trump','wp']

pids = ""
def run_animation(name, timez):
    wd = '/home/pi/Desktop/{}/'.format(name)
    exe = wd + 'run.sh'
    p = subprocess.Popen(['bash', exe], cwd=wd)
    #p = subprocess.Popen('bash '+exe, stdout=subprocess.PIPE, shell=True)
    
    try:
        #pids=os.system("pgrep -f led-image-viewer")
        #print(pids)
        
        #p.wait(timeout=time)
        time.sleep(timez)
        os.system("kill $(pgrep -f -d \" \" led-image-viewer) -kill")
        #os.kill(os.getpgid(p.pid), signal.SIGTERM)
        p.kill()
        p.terminate()
        os.system("kill $(pgrep -f -d \" \" led-image-viewer) -kill")
    except:
        print('Terminating...')
        p.terminate()

        
while True:    
    for name in folder_names:
        run_animation(name, 15)
    
