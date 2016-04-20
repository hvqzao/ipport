Setup assumes https://github.com/hvqzao/x is set up in /root/x directory.

Usage:

Install docker:

```sh
sudo aptitude install docker.io
```

Build kali-linux docker image and dependent ipport image:

```sh
cd ~/x/p/ipport
git submodule update --init --recursive
./kali-linux-docker/build.sh
./build.sh
```

Start container:

```sh
~/x/p/ipport/docker/run some-temporary-container-name
```

(container will be automatically removed once shell will be closed, but /root folder is shared between host and container)
