import subprocess

def output(idea):
    # create a file and prepare it for writing
    subprocess.call('escposf --i > ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('escposf --a 1 > ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('escposf --r 1 >> ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('escposf --t 3 >> ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('echo "    NEW IDEA    " >> ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('escposf --t 0 >> ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('escposf --r 0 >> ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('escposf --a 0 >> ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('echo "\n" >> ./idea.txt', shell=True, stdout=subprocess.PIPE)

    # append the idea to the document and add a few line breaks
    subprocess.call('echo ' + idea + ' >> ./idea.txt', shell=True, stdout=subprocess.PIPE)
    subprocess.call('echo "\n\n\n" >> ./idea.txt', shell=True, stdout=subprocess.PIPE)

    # print it
    subprocess.call('lpr -P zj58 -o raw ./idea.txt', shell=True, stdout=subprocess.PIPE)

    # clean up
    subprocess.call(['rm', './idea.txt'])
