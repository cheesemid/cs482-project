# Quick installation guide

Before you can use CVAT, you’ll need to get it installed. The document below
contains instructions for the most popular operating systems. If your system is
not covered by the document it should be relatively straight forward to adapt
the instructions below for other systems.

Probably you need to modify the instructions below in case you are behind a proxy
server. Proxy is an advanced topic and it is not covered by the guide.

For access from China, read [sources for users from China](#sources-for-users-from-china) section.

## Ubuntu 18.04 (x86_64/amd64)

- Open a terminal window. If you don't know how to open a terminal window on
  Ubuntu please read [the answer](https://askubuntu.com/questions/183775/how-do-i-open-a-terminal).

- Type commands below into the terminal window to install `docker`. More
  instructions can be found [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

  ```shell
  sudo apt-get update
  sudo apt-get --no-install-recommends install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
  sudo apt-get update
  sudo apt-get --no-install-recommends install -y docker-ce docker-ce-cli containerd.io
  ```

- Perform [post-installation steps](https://docs.docker.com/install/linux/linux-postinstall/)
  to run docker without root permissions.

  ```shell
  sudo groupadd docker
  sudo usermod -aG docker $USER
  ```

  Log out and log back in (or reboot) so that your group membership is
  re-evaluated. You can type `groups` command in a terminal window after
  that and check if `docker` group is in its output.

- Install docker-compose (1.19.0 or newer). Compose is a tool for
  defining and running multi-container docker applications.

  ```shell
  sudo apt-get --no-install-recommends install -y python3-pip python3-setuptools
  sudo python3 -m pip install setuptools docker-compose
  ```

- Clone _CVAT_ source code from the
  [GitHub repository](https://github.com/opencv/cvat) with Git.

  Following command will clone latest develop branch:
  ```shell
  git clone https://github.com/opencv/cvat
  cd cvat
  ```

  See [alternatives](#how-to-get-cvat-source-code) if you want to download one of the release
  versions or use the `wget` or `curl` tools.

- To access CVAT over a network or through a different system, export `CVAT_HOST` environment variable

  ```shell
  export CVAT_HOST=your-ip-address
  ```

- Run docker containers. It will take some time to download the latest CVAT
  release and other required images like postgres, redis, etc. from DockerHub and create containers.

  ```shell
  docker-compose up -d
  ```

- (Optional) Use `CVAT_VERSION` environment variable to specify the version of CVAT you want to
  install specific version (e.g `v2.1.0`, `dev`).
  Default behavior: `dev` images will be pulled for develop branch,
  and corresponding release images for release versions.
  ```shell
  CVAT_VERSION=dev docker-compose up -d
  ```

- Alternative: if you want to build the images locally with unreleased changes
  see [How to pull/build/update CVAT images section](#how-to-pullbuildupdate-cvat-images)

- You can register a user but by default it will not have rights even to view
  list of tasks. Thus you should create a superuser. A superuser can use an
  admin panel to assign correct groups to the user. Please use the command
  below:

  ```shell
  docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
  ```

  Choose a username and a password for your admin account. For more information
  please read [Django documentation](https://docs.djangoproject.com/en/2.2/ref/django-admin/#createsuperuser).

- Google Chrome is the only browser which is supported by CVAT. You need to
  install it as well. Type commands below in a terminal window:

  ```shell
  curl https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
  sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
  sudo apt-get update
  sudo apt-get --no-install-recommends install -y google-chrome-stable
  ```

- Open the installed Google Chrome browser and go to [localhost:8080](http://localhost:8080).
  Type your login/password for the superuser on the login page and press the _Login_
  button. Now you should be able to create a new annotation task. Please read the
  [CVAT manual](/docs/manual/) for more details.