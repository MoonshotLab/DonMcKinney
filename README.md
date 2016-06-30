# Don McKinney

Don McKinney is a little [raspberry pi](https://www.raspberrypi.org/) computer which generates advertising related ideas using the [markov chain](https://en.wikipedia.org/wiki/Markov_chain). It both speaks it's ideas and prints them using a [thermal printer connected](https://www.amazon.com/Esky-High-speed-Receipt-Compatible-Commands/dp/B011KF6GW4/ref=sr_1_1?rps=1&ie=UTF8&qid=1466548398&sr=8-1&keywords=receipt+printer&refinements=p_85%3A2470955011#feature-bullets-btf).


## Installing a Thermal Printer
Every printer will probably have a slightly different installation sequence. The steps for the [E-Sky](https://www.amazon.com/Esky-High-speed-Receipt-Compatible-Commands/dp/B011KF6GW4/ref=sr_1_1?rps=1&ie=UTF8&qid=1466548398&sr=8-1&keywords=receipt+printer&refinements=p_85%3A2470955011#feature-bullets-btf) are as follows:

1. Install cups `sudo apt-get install cups`.  Optionally configure it to be administrated by different network devices by following [this guide](http://www.howtogeek.com/169679/how-to-add-a-printer-to-your-raspberry-pi-or-other-linux-computer/).
1. Install the cups development headers `sudo apt-get install libcups2-dev libcupsimage2-dev` so we can later build the ZJ-58 filter.
1. Clone the Zjiang ZJ-58 filter `git clone https://github.com/klirichek/zj-58.git`
1. Rebuild the rastertozj binary - `rm zj-58/rastertozj` and then `zj-58 make`
1. Install the zj-58 ppd and filter - `sudo zj-58/install`
1. Configure a new cups filter by visiting http://localhost:631
1. Download [escposf](http://www.tux.org/~bball/escposf/), make it, and drop it in /usr/bin



## Configuring Seed Text
I don't have a plan on how this will work yet.



## Dependencies
### Printer
* Cups Development Headers - `apt-get install libcups2-dev libcupsimage2-dev`
* [cups](https://wiki.archlinux.org/index.php/CUPS) - `apt-get install cups`
* [escposf](http://www.tux.org/~bball/escposf/)

### Talking
* [espeak](http://espeak.sourceforge.net/) - `apt-get install espeak`
* [alsa-tools](http://www.alsa-project.org/main/index.php/Main_Page) - `apt-get install alsa-tools`
* [alsa-utils](http://www.alsa-project.org/main/index.php/Main_Page) - `apt-get install alsa-utils`
* [pyttsx](https://github.com/parente/pyttsx) - `pip install pyttsx`

### Other
* [markovify](https://github.com/jsvine/markovify) - `pip install markfovify`
