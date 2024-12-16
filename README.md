# Smart-Home-Escape-Room-Workshop

Companies in Germany are facing the problem of a shortage of skilled workers, particularly in the IT sector. This is influenced by a variety of factors, such as the rapid development of technology, from which an increasing demand for qualified IT specialists can be derived. According to statistics, the number of computer science students is steadily increasing, but there are large differences between the sexes and, despite the increase, it is currently not possible to meet the demand for specialists. Furtwangen University has been cooperating with several schools in the area for years and offers interactive workshops for pupils to counteract this problem. In order to offer pupils an insight into teaching at Furtwangen University and to arouse their interest in current IT topics, especially with regard to SmartHome technologies, the project group has been working on the conception of a workshop, which is to serve as the first building block of a scalable workshop concept of the Faculty of Computer Science. The topic of SmartHome is closely linked to a fundamental understanding of IoT applications and the technological progress that is often required in the IT industry. The research project deals in particular with the research question of what influence design thinking principles and gamification have on the effectiveness and implementation of innovative solutions for smart home challenges.

---

## Pre-Installation

### Selenium standalone server

You need `Selenium` as standalone server. At first you have to install `Java`:

```
sudo apt update
sudo apt install openjdk-11-jdk
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> ~/.bashrc
source ~/.bashrc
```

Then you have to download and install the `Selenium Server` (`Selenium Grid`):

```
wget https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.27.0/selenium-server-4.27.0.jar
mv selenium-server-4.27.0.jar /usr/local/bin
```

You can start and run it with:

```
java -jar /usr/local/bin/selenium-server-4.27.0.jar standalone
```

### Chrome and chromedriver

For `Chrome` you need a compatible `chromedriver`, otherwise it is not possible to control the browser remotely. First of all, I will show you how to install `Chrome` manually:

```
wget https://mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.90-1_amd64.deb
sudo dpkg -i google-chrome-stable_114.0.5735.90-1_amd64.deb
sudo apt-mark hold google-chrome-stable
```

Then you have to download and install the `chromedriver`:

```
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/local/bin
```

---

### PyChromeController

The [PyChromeController](https://github.com/Michdo93/PyChromeController) will controll `Chrome` at least via `Python3`. You can install it with:

```
pip install PyChromeController
```

### NotipyDesktop

[NotipyDesktop]() is a simple Python library for sending desktop notifications using [libnotify](https://developer.gnome.org/libnotify/). It is used to signal on the tablet that a level has been completed. You can install it with:

```
pip install NotipyDesktop
```

You can make the program system wide executable with:

```bash
chmod +x /path/to/NotipyDesktop/NotipyDesktop
```

After that you have to add the path to `$PATH`:

```bash
export PATH=$PATH:/path/to/NotipyDesktop
```

Then you can run it with:

```bash
NotipyDesktop MyApp "Test Notification" "This is a test message."
```

### NVM and Node.js

```bash
sudo apt install gcc g++ make -y
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

source ~/.bashrc

nvm install 16.13.2
nvm use 16.13.2
nvm alias default 16.13.2

echo 'PATH=$PATH:/home/$USER/.nvm/versions/node/v16.13.2/bin' | sudo tee -a /etc/environment

sudo ln -s /home/$USER/.nvm/versions/node/v16.13.2/bin/node /usr/bin/node
sudo ln -s /home/$USER/.nvm/versions/node/v16.13.2/bin/npm /usr/bin/npm
```

### Node-RED

```bash
sudo npm install -g --unsafe-perm node-red
```

### PM2

```bash
sudo npm install -g pm2
pm2 startup systemd
echo 'PM2_HOME="/root/.pm2"' >> /etc/environment
sudo reboot
```

---

## Installation

```bash
cd ~
git clone https://github.com/Michdo93/Smart-Home-Escape-Room-Workshop
cd Smart-Home-Escape-Room-Workshop
./install.sh
```

---

## Execution

to be continued ...

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

###
